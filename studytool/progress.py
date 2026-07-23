"""Persistent progress store (``.progress.json`` at the repo root) + weighting.

Shape of the JSON::

    {
      "version": 1,
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
        return {"version": STORE_VERSION, "exercises": {}}
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError):
        # Corrupt/unreadable store shouldn't wipe a practice session; start clean.
        return {"version": STORE_VERSION, "exercises": {}}
    data.setdefault("version", STORE_VERSION)
    data.setdefault("exercises", {})
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


def stats_for(data: dict[str, Any], ex_id: str) -> dict[str, Any]:
    """Aggregate stats for one exercise (safe for never-attempted ids)."""
    attempts = data.get("exercises", {}).get(ex_id, {}).get("attempts", [])
    total = len(attempts)
    # A "fail" = a graded attempt that did not pass every gradeable example.
    fails = sum(1 for a in attempts if not a.get("all_passed"))
    passes = total - fails
    scored = [a["score"] for a in attempts if a.get("gradeable", 0) > 0 or a.get("all_passed")]
    return {
        "attempts": total,
        "fails": fails,
        "passes": passes,
        "pass_rate": (passes / total) if total else 0.0,
        "latest_score": attempts[-1]["score"] if attempts else None,
        "latest_all_passed": bool(attempts[-1]["all_passed"]) if attempts else False,
        "best_score": max(scored) if scored else None,
    }


# --------------------------------------------------------------------------- #
# weighting  (spaced-repetition-style selection)
# --------------------------------------------------------------------------- #
def compute_weight(data: dict[str, Any], ex_id: str) -> float:
    """Selection weight for one exercise. Higher weight = more likely to be asked.

    The intent (from the spec): favour what you fail most, keep never-attempted
    exercises at a healthy priority, and back off from things you just passed.

    Formula
    -------
    * Never attempted        -> 3.0
        A solid default: above a mastered exercise, below one you keep failing,
        so new material surfaces regularly but doesn't crowd out your weak spots.
    * Attempted              -> 1.0 + 4.0 * fail_rate      (fail_rate = fails/attempts)
        Ranges from 1.0 (you've never failed it) up to 5.0 (you fail every time),
        so the more often you fail an exercise the more often it comes back.
    * Just passed last time  -> the above is multiplied by 0.4
        Spaced repetition: a fresh success pushes it down the queue for a while.
    * Floor of 0.2
        Even a mastered exercise keeps a small chance of resurfacing, so nothing
        is ever permanently retired.
    """
    s = stats_for(data, ex_id)
    if s["attempts"] == 0:
        return 3.0

    fail_rate = s["fails"] / s["attempts"]
    weight = 1.0 + 4.0 * fail_rate
    if s["latest_all_passed"]:
        weight *= 0.4
    return max(weight, 0.2)


def weights_for(data: dict[str, Any], ex_ids: list[str]) -> dict[str, float]:
    """Weight for each id (handy for `stats` and for explaining a pick)."""
    return {eid: compute_weight(data, eid) for eid in ex_ids}


def select_weighted(data: dict[str, Any], ex_ids: list[str],
                    rng: random.Random | None = None) -> tuple[str, dict[str, float]]:
    """Pick one id via weighted random choice. Returns ``(chosen_id, weights)``."""
    if not ex_ids:
        raise ValueError("no exercises to choose from")
    rng = rng or random.Random()
    weights = weights_for(data, ex_ids)
    chosen = rng.choices(ex_ids, weights=[weights[e] for e in ex_ids], k=1)[0]
    return chosen, weights
