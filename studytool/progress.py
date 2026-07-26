"""Persistent progress store (``.progress.json`` at the repo root) + weighting.

Shape of the JSON::

    {
      "version": 1,
      "round": {"asked": ["ex1-3", "ex2-1"]},
      "exercises": {
        "ex2-1": {
          "attempts": [
            {"try": "try1.py", "timestamp": "2026-07-23T14:03:11",
             "passed": 3, "gradeable": 4, "skipped": 0,
             "score": 0.75, "all_passed": false, "load_error": null}
          ]
        }
      }
    }

``round`` tracks the current *ask-round* (see :func:`select_for_ask`): every
exercise is asked once per round before any exercise is asked a second time.

Every graded run appends one entry. Nothing is ever removed. Aggregates
(attempt count, fail count, pass rate, latest/best score) are computed on read.
"""
from __future__ import annotations

import json
import os
import random
from datetime import datetime
from typing import Any

from .grader import GradeResult

STORE_VERSION = 1


def store_path(repo_root: str) -> str:
    return os.path.join(repo_root, ".progress.json")


def load(repo_root: str) -> dict[str, Any]:
    """Load the store, returning a fresh skeleton if it doesn't exist yet."""
    path = store_path(repo_root)
    if not os.path.exists(path):
        return {"version": STORE_VERSION, "exercises": {}, "round": {"asked": []}}
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError):
        # Corrupt/unreadable store shouldn't wipe a practice session; start clean.
        return {"version": STORE_VERSION, "exercises": {}, "round": {"asked": []}}
    data.setdefault("version", STORE_VERSION)
    data.setdefault("exercises", {})
    data.setdefault("round", {"asked": []})
    return data


def save(repo_root: str, data: dict[str, Any]) -> None:
    """Write the store atomically (temp file + replace)."""
    path = store_path(repo_root)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, sort_keys=True)
    os.replace(tmp, path)


def record(data: dict[str, Any], result: GradeResult, when: str | None = None) -> None:
    """Append one graded attempt to the store (in memory; caller saves)."""
    entry = {
        "try": result.try_file,
        "timestamp": when or datetime.now().isoformat(timespec="seconds"),
        "passed": result.passed,
        "gradeable": result.gradeable,
        "skipped": result.skipped,
        "score": round(result.score, 4),
        "all_passed": result.all_passed,
        "load_error": result.load_error,
    }
    ex = data["exercises"].setdefault(result.ex_id, {"attempts": []})
    ex["attempts"].append(entry)


RECENT_WINDOW = 5  # how many of the latest graded attempts drive the weight


def stats_for(data: dict[str, Any], ex_id: str) -> dict[str, Any]:
    """Aggregate stats for one exercise (safe for never-attempted ids)."""
    attempts = data.get("exercises", {}).get(ex_id, {}).get("attempts", [])
    total = len(attempts)
    # A "fail" = a graded attempt that did not pass every gradeable example.
    fails = sum(1 for a in attempts if not a.get("all_passed"))
    passes = total - fails
    scored = [a["score"] for a in attempts if a.get("gradeable", 0) > 0 or a.get("all_passed")]
    recent = attempts[-RECENT_WINDOW:]
    recent_fails = sum(1 for a in recent if not a.get("all_passed"))
    return {
        "attempts": total,
        "fails": fails,
        "passes": passes,
        "pass_rate": (passes / total) if total else 0.0,
        "recent_n": len(recent),
        "recent_fails": recent_fails,
        "recent_fail_rate": (recent_fails / len(recent)) if recent else 0.0,
        "latest_score": attempts[-1]["score"] if attempts else None,
        "latest_all_passed": bool(attempts[-1]["all_passed"]) if attempts else False,
        "best_score": max(scored) if scored else None,
    }


# --------------------------------------------------------------------------- #
# weighting  (spaced-repetition-style selection)
# --------------------------------------------------------------------------- #
def compute_weight(data: dict[str, Any], ex_id: str) -> float:
    """Selection weight for one exercise. Higher weight = asked sooner in a round.

    The intent (from the spec): favour what you fail most *now*, keep
    never-attempted exercises at a healthy priority, and back off from things
    you just passed.

    Formula
    -------
    * Never attempted        -> 3.0
        A solid default: above a mastered exercise, below one you keep failing,
        so new material surfaces regularly but doesn't crowd out your weak spots.
    * Attempted              -> 1.0 + 4.0 * recent_fail_rate
        ``recent_fail_rate`` looks at only the last ``RECENT_WINDOW`` (5) graded
        attempts, so the weight reflects how you do *today*. (It used to use
        all-time history, which made an exercise you bombed early on haunt you
        forever even after you had clearly mastered it.)
    * Just passed last time  -> the above is multiplied by 0.4
        Spaced repetition: a fresh success pushes it down the queue for a while.
    * Floor of 0.2
        Even a mastered exercise keeps a small chance of resurfacing, so nothing
        is ever permanently retired.

    Coverage itself is NOT the weight's job: :func:`select_for_ask` guarantees
    every exercise is asked once per round; the weight only orders the round.
    """
    s = stats_for(data, ex_id)
    if s["attempts"] == 0:
        return 3.0

    weight = 1.0 + 4.0 * s["recent_fail_rate"]
    if s["latest_all_passed"]:
        weight *= 0.4
    return max(weight, 0.2)


def weights_for(data: dict[str, Any], ex_ids: list[str]) -> dict[str, float]:
    """Weight for each id (handy for `stats` and for explaining a pick)."""
    return {eid: compute_weight(data, eid) for eid in ex_ids}


def round_state(data: dict[str, Any], all_ids: list[str]) -> list[str]:
    """Ids already asked in the current round, pruned to exercises that still
    exist. A completed round (every exercise asked) resets to empty. Mutates
    ``data`` in place; the caller decides whether to save."""
    existing = set(all_ids)
    rnd = data.get("round", {})
    asked = [i for i in rnd.get("asked", []) if i in existing]
    if all_ids and existing <= set(asked):
        asked = []
    last = rnd.get("last")
    data["round"] = {"asked": asked, "last": last if last in existing else None}
    return asked


def select_for_ask(data: dict[str, Any], all_ids: list[str], pool_ids: list[str],
                   rng: random.Random | None = None) -> tuple[str, dict[str, float]]:
    """Pick the next exercise to ask: weighted, but with guaranteed coverage.

    Selection runs in *rounds*: an exercise asked once in the current round is
    not asked again until every other exercise has had its turn, so `ask` can
    no longer hand you the same exercise five times in an afternoon while
    others starve. Within a round the weights still apply, so current weak
    spots surface early. If a *filtered* pool (e.g. ``ask ex1-*``) is already
    fully asked this round, just that pool is recycled, so drilling one group
    keeps cycling through the whole group.

    Returns ``(chosen_id, weights_of_candidates)`` and records the pick in
    ``data`` (caller saves).
    """
    if not pool_ids:
        raise ValueError("no exercises to choose from")
    rng = rng or random.Random()

    asked = round_state(data, all_ids)
    candidates = [i for i in pool_ids if i not in asked]
    if not candidates:                      # filtered pool exhausted this round:
        pool = set(pool_ids)                # recycle just the pool, keep the
        asked = [i for i in asked if i not in pool]      # rest of the round
        candidates = list(pool_ids)

    # After a reset/recycle the previous pick is available again - avoid asking
    # the exact same exercise twice in a row whenever there is an alternative.
    last = data["round"].get("last")
    if len(candidates) > 1 and last in candidates:
        candidates = [i for i in candidates if i != last]

    weights = weights_for(data, candidates)
    chosen = rng.choices(candidates, weights=[weights[c] for c in candidates], k=1)[0]
    if chosen not in asked:
        asked.append(chosen)
    data["round"] = {"asked": asked, "last": chosen}
    return chosen, weights
