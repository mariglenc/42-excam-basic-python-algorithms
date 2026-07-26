"""Command-line interface: list / ask / exam / grade / stats / solution.

Run it from the repo root via the launcher::

    python study.py list
    python study.py ask                 # weighted pick; every exercise once per round
    python study.py ask ex2-1           # a specific exercise
    python study.py ask ex1-*           # weighted pick within a group
    python study.py exam                # exam shell: one random exercise per level
    python study.py grade ex2-1         # grade the latest try<N>.py
    python study.py grade ex2-1 --try 1 # grade a specific attempt
    python study.py stats
    python study.py solution ex2-1      # explicit: reveal the reference solution
"""
from __future__ import annotations

import argparse
import os
import random
import re
import sys

from . import attempts, discovery, progress
from .grader import GradeResult, grade_file

_TRY_RE = re.compile(r"^try\d+\.py$", re.IGNORECASE)


# --------------------------------------------------------------------------- #
# tiny ANSI colour helper (best-effort; silently plain if unsupported)
# --------------------------------------------------------------------------- #
def _enable_color() -> bool:
    if os.environ.get("NO_COLOR") is not None or not sys.stdout.isatty():
        return False
    if os.name == "nt":
        try:  # turn on virtual-terminal processing so ANSI codes render
            import ctypes

            k = ctypes.windll.kernel32
            k.SetConsoleMode(k.GetStdHandle(-11), 7)
        except Exception:  # noqa: BLE001
            return False
    return True


_COLOR = _enable_color()
_C = {
    "PASS": "\033[32m", "FAIL": "\033[31m", "ERROR": "\033[35m",
    "SKIP": "\033[33m", "dim": "\033[2m", "bold": "\033[1m", "reset": "\033[0m",
}


def c(text: str, key: str) -> str:
    return f"{_C[key]}{text}{_C['reset']}" if _COLOR else text


def repo_root() -> str:
    """Repo root: ``$STUDYTOOL_ROOT`` if set, else the folder holding this package."""
    override = os.environ.get("STUDYTOOL_ROOT")
    if override:
        return os.path.abspath(override)
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# --------------------------------------------------------------------------- #
# commands
# --------------------------------------------------------------------------- #
def cmd_list(args) -> int:
    root = repo_root()
    exs = discovery.resolve(discovery.discover(root), args.filter)
    if not exs:
        print(f"No exercises match {args.filter!r}.")
        return 1
    data = progress.load(root)
    print(c(f"{'id':<8} {'function':<28} {'cases':>5}  {'tries':>5}  latest", "bold"))
    for ex in exs:
        s = progress.stats_for(data, ex.id)
        n_tries = len(attempts.list_attempts(ex.dir))
        latest = "-" if s["latest_score"] is None else f"{s['latest_score'] * 100:.0f}%"
        func = ex.func_name or "(unparsed)"
        print(f"{ex.id:<8} {func:<28} {len(ex.parsed.examples):>5}  {n_tries:>5}  {latest}")
    return 0


def cmd_ask(args) -> int:
    root = repo_root()
    all_exs = discovery.discover(root)
    pool = discovery.resolve(all_exs, args.filter)
    if not pool:
        print(f"No exercises match {args.filter!r}.")
        return 1

    data = progress.load(root)
    rng = random.Random(args.seed) if args.seed is not None else random.Random()
    chosen_id, weights = progress.select_for_ask(
        data, [e.id for e in all_exs], [e.id for e in pool], rng)
    ex = next(e for e in pool if e.id == chosen_id)
    progress.save(root, data)  # the pick now counts toward the round; persist it

    # --- print the question (straight from the .en; never the solution) ---
    with open(ex.en_path, encoding="utf-8") as fh:
        question = fh.read().rstrip()
    print(c(f"=== {ex.id}  ({os.path.basename(ex.en_path)}) ===", "bold"))
    if len(weights) > 1:
        w = weights[ex.id]
        print(c(f"(picked by weight {w:.2f} of {sum(weights.values()):.2f} over the "
                f"{len(weights)} exercises not yet asked this round)", "dim"))
    asked = data["round"]["asked"]
    note = " - round complete! next ask starts a new round" if len(asked) >= len(all_exs) else ""
    print(c(f"(round progress: {len(asked)}/{len(all_exs)} exercises asked{note})", "dim"))
    print()
    print(question)
    print()

    # --- create the next attempt file (pre-filled, never overwritten) ---
    n, path = attempts.create_attempt(ex.dir, ex.parsed, ex.id)
    rel = os.path.relpath(path, root)
    print(c(f"created {rel}", "PASS") + f"  (pre-filled with: {ex.parsed.signature})")
    print(f"Edit it, then grade with:  python study.py grade {ex.id}")
    return 0


_LEVEL_RE = re.compile(r"^ex(\d+)")


def cmd_exam(args) -> int:
    """Exam-shell simulation: one uniformly-random exercise from each level.

    The level is the number in the folder name (ex1-3 -> level 1, ex4 -> level
    4). Picks are uniform per level and independent of the `ask` round, so an
    exam never disturbs your drill rotation.
    """
    root = repo_root()
    all_exs = discovery.discover(root)
    if not all_exs:
        print("No exercises found.")
        return 1

    levels: dict[int, list] = {}
    unlevelled = []
    for e in all_exs:
        m = _LEVEL_RE.match(e.id)
        if m:
            levels.setdefault(int(m.group(1)), []).append(e)
        else:
            unlevelled.append(e.id)

    rng = random.Random(args.seed) if args.seed is not None else random.Random()
    picks = [(lvl, rng.choice(levels[lvl])) for lvl in sorted(levels)]

    print(c(f"=== EXAM SHELL: {len(picks)} exercises, one per level ===", "bold"))
    if unlevelled:
        print(c(f"(skipped, id has no level number: {', '.join(unlevelled)})", "dim"))

    sheet = []
    for lvl, ex in picks:
        with open(ex.en_path, encoding="utf-8") as fh:
            question = fh.read().rstrip()
        print()
        print(c(f"--- Level {lvl}: {ex.id}  ({os.path.basename(ex.en_path)}) ---", "bold"))
        print(question)
        print()
        n, path = attempts.create_attempt(ex.dir, ex.parsed, ex.id)
        rel = os.path.relpath(path, root)
        sheet.append((lvl, ex, rel))
        print(c(f"created {rel}", "PASS") + f"  (pre-filled with: {ex.parsed.signature})")

    print()
    print(c("=== Your exam sheet ===", "bold"))
    for lvl, ex, rel in sheet:
        print(f"  Level {lvl}: edit {rel:<20} then:  python study.py grade {ex.id}")
    print(c("(picked uniformly at random per level; does not affect the ask round)", "dim"))
    return 0


def _print_grade(res: GradeResult) -> None:
    header = f"{res.ex_id}  ({res.try_file})"
    print(c(f"--- {header} ---", "bold"))
    if res.load_error:
        print(c("  LOAD ERROR ", "ERROR") + res.load_error)
        print(c("  Score: 0 (attempt could not be imported)", "FAIL"))
        return
    for r in res.results:
        tag = c(f"{r.status:<5}", r.status)
        call = " ".join(r.call.split()) if r.call else "(unparsed example)"  # collapse multi-line
        print(f"  {tag} {call}")
        if r.status == "FAIL":
            print(f"        expected {r.expected!r}, got {r.got!r}")
        elif r.status == "ERROR":
            print(f"        raised {r.detail}")
        elif r.status == "SKIP":
            print(f"        {r.detail}")
    pct = f"{res.score * 100:.0f}%"
    tail = f"  [{res.skipped} skipped]" if res.skipped else ""
    line = f"  Score: {res.passed}/{res.gradeable} gradeable passed ({pct}){tail}"
    print(c(line, "PASS" if res.all_passed else "FAIL"))


def cmd_grade(args) -> int:
    root = repo_root()
    exs = discovery.resolve(discovery.discover(root), args.filter)
    if not exs:
        print(f"No exercises match {args.filter!r}.")
        return 1
    if args.try_num is not None and len(exs) != 1:
        print("--try only works when the filter selects a single exercise.")
        return 1

    data = progress.load(root)
    graded_any = False
    exit_code = 0

    for ex in exs:
        if args.try_num is not None:
            path = attempts.find_by_number(ex.dir, args.try_num)
            if not path:
                print(f"{ex.id}: no try{args.try_num}.py")
                exit_code = 1
                continue
        else:
            latest = attempts.latest_attempt(ex.dir)
            if not latest:
                if len(exs) == 1:
                    print(f"{ex.id}: no attempts yet - run `python study.py ask {ex.id}`")
                    return 1
                continue
            path = latest[1]

        res = grade_file(ex.parsed, path, ex.id)
        _print_grade(res)
        progress.record(data, res)
        graded_any = True
        if not res.all_passed:
            exit_code = 1

    if graded_any:
        progress.save(root, data)
    elif args.try_num is None:
        print("Nothing to grade (no attempts found). Run `ask` first.")
        exit_code = 1
    return exit_code


def cmd_stats(args) -> int:
    root = repo_root()
    all_exs = discovery.discover(root)
    exs = discovery.resolve(all_exs, args.filter)
    if not exs:
        print(f"No exercises match {args.filter!r}.")
        return 1
    data = progress.load(root)

    print(c(f"{'id':<8} {'attempts':>8} {'fails':>6} {'pass%':>6} {'last5':>6} "
            f"{'latest':>7} {'best':>6} {'weight':>7}", "bold"))
    rows = []
    for ex in exs:
        s = progress.stats_for(data, ex.id)
        w = progress.compute_weight(data, ex.id)
        rows.append((ex.id, s, w))
        latest = "-" if s["latest_score"] is None else f"{s['latest_score'] * 100:.0f}%"
        best = "-" if s["best_score"] is None else f"{s['best_score'] * 100:.0f}%"
        pr = f"{s['pass_rate'] * 100:.0f}%" if s["attempts"] else "-"
        last5 = f"{s['recent_fails']}F/{s['recent_n']}" if s["attempts"] else "-"
        print(f"{ex.id:<8} {s['attempts']:>8} {s['fails']:>6} {pr:>6} {last5:>6} "
              f"{latest:>7} {best:>6} {w:>7.2f}")

    # most-failed leaderboard
    failed = sorted([r for r in rows if r[1]["fails"] > 0],
                    key=lambda r: r[1]["fails"], reverse=True)
    print()
    if failed:
        board = ", ".join(f"{r[0]} ({r[1]['fails']})" for r in failed[:5])
        print(c("Most-failed: ", "bold") + board)
    never = [r[0] for r in rows if r[1]["attempts"] == 0]
    if never:
        print(c("Never attempted: ", "bold") + ", ".join(never))

    asked = progress.round_state(data, [e.id for e in all_exs])
    remaining = [e.id for e in all_exs if e.id not in asked]
    print(c("Ask-round: ", "bold") + f"{len(asked)}/{len(all_exs)} asked"
          + (f"; still to come: {', '.join(remaining)}" if remaining else " (complete)"))
    print(c("Weighting: ", "dim")
          + c("never-tried=3.0; tried=1+4*fail_rate over the last 5 grades (last5 column); "
              "just-passed *0.4; floor 0.2. `ask` asks every exercise once per round; "
              "higher weight just comes up earlier.", "dim"))
    return 0


def cmd_solution(args) -> int:
    """Explicit, opt-in reveal of the reference solution(s). Never automatic."""
    root = repo_root()
    exs = discovery.resolve(discovery.discover(root), args.exid)
    if not exs:
        print(f"No exercises match {args.exid!r}.")
        return 1
    if len(exs) != 1:
        print(f"{args.exid!r} matches {len(exs)} exercises; name a single one.")
        return 1
    ex = exs[0]

    # reference = any .py in the folder that is NOT a try<N>.py attempt
    refs = sorted(
        f for f in os.listdir(ex.dir)
        if f.endswith(".py") and not _TRY_RE.match(f)
    )
    if not refs:
        print(f"{ex.id}: no reference solution file found.")
        return 1

    print(c(f"Reference solution(s) for {ex.id} (you asked):", "bold"))
    for fname in refs:
        print(c(f"\n----- {fname} -----", "dim"))
        with open(os.path.join(ex.dir, fname), encoding="utf-8") as fh:
            print(fh.read().rstrip())
    return 0


# --------------------------------------------------------------------------- #
# argument parsing
# --------------------------------------------------------------------------- #
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="study", description="Practice/drill tool for the exercise repo.")
    sub = p.add_subparsers(dest="command", required=True)

    lp = sub.add_parser("list", help="list exercises and your progress")
    lp.add_argument("filter", nargs="?", default=None, help="id / group / glob (default: all)")
    lp.set_defaults(func=cmd_list)

    ap = sub.add_parser("ask", help="show a question and create the next attempt file "
                                    "(weighted; every exercise once per round)")
    ap.add_argument("filter", nargs="?", default=None, help="id / group / glob (default: weighted pick over all)")
    ap.add_argument("--seed", type=int, default=None, help="seed the random pick (reproducible)")
    ap.set_defaults(func=cmd_ask)

    xp = sub.add_parser("exam", aliases=["examshell"],
                        help="exam-shell drill: one random exercise from each level")
    xp.add_argument("--seed", type=int, default=None, help="seed the random picks (reproducible)")
    xp.set_defaults(func=cmd_exam)

    gp = sub.add_parser("grade", help="grade an attempt against the .en examples")
    gp.add_argument("filter", nargs="?", default=None, help="id / group / glob (default: all with attempts)")
    gp.add_argument("--try", dest="try_num", type=int, default=None, help="grade try<N>.py (single exercise only)")
    gp.set_defaults(func=cmd_grade)

    sp = sub.add_parser("stats", help="attempt counts, fails, pass rates, scores, weights")
    sp.add_argument("filter", nargs="?", default=None, help="id / group / glob (default: all)")
    sp.set_defaults(func=cmd_stats)

    op = sub.add_parser("solution", help="EXPLICITLY reveal the reference solution")
    op.add_argument("exid", help="a single exercise id, e.g. ex2-1")
    op.set_defaults(func=cmd_solution)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)
