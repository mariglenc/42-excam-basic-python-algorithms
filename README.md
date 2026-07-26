# study tool

A small, dependency-free CLI for drilling the exercises in this repo. It reads
each exercise's `.en` file, quizzes you, creates your next attempt file,
auto-grades it against the `Examples:` in the `.en`, and tracks which exercises
you fail most so it can bring them back more often.

Pure standard library. **Python 3.8+.** Run everything from the repo root.

## Commands

```bash
python study.py list                 # every exercise + your attempt count / latest score
python study.py list ex1-*           # just a group

python study.py ask                  # pick one (weighted, see below), print the question,
                                     #   and create the next try<N>.py (pre-filled, never overwritten)
python study.py ask ex2-1            # ask a specific exercise
python study.py ask ex1-*            # weighted pick within a group
python study.py ask --seed 42        # reproducible pick

python study.py exam                 # exam-shell drill: one random exercise from each level
python study.py exam --seed 42       # reproducible exam (retake the same one)

python study.py grade ex2-1          # grade the latest try<N>.py in ex2-1
python study.py grade ex2-1 --try 1  # grade a specific attempt
python study.py grade ex1-*          # grade the latest attempt of each match

python study.py stats                # attempts, fails, pass rate, latest/best score, weight
python study.py solution ex2-1       # EXPLICITLY reveal the reference solution (only when you ask)
```

### Filters
`all` (or nothing) · an exact id (`ex2-1`, `ex4`) · a glob (`ex1-*`, `ex?-1`) ·
or a prefix group (`ex1` → `ex1-1`, `ex1-2`, …). Exact ids win over the group
reading, so `ex4` selects the `ex4` exercise.

## Workflow

1. `python study.py ask ex2-1` — prints the question and creates `ex2-1/try<N>.py`
   pre-filled with the function signature from the `.en`.
2. Open that file in your editor and write your solution. *(The tool does not
   open an editor for you — it just prints the path.)*
3. `python study.py grade ex2-1` — runs your function against every example and
   prints `PASS` / `FAIL` (expected vs. got) / `ERROR` (exception) / `SKIP`,
   plus a score. The result is saved to `.progress.json`.

## How grading works

Your `try<N>.py` is imported from its path, the target function is found by name
(falling back to the sole function defined in the file), and it's called with the
arguments parsed from each example. Comparison is `==`, with one deliberate
twist: **`bool` is kept distinct from `int`**, so returning `1` when `True` is
expected is a FAIL. Arguments and expected values come from `ast.literal_eval`
(never `eval`); an example whose value is cut off / not a literal is reported as
`SKIP` rather than crashing the run.

## Weighted selection (spaced repetition)

`ask` favours exercises you get wrong, keeps new material in rotation, and eases
off things you just nailed. Each exercise gets a weight; `ask` picks in
proportion to it (and prints the weight it used).

| Situation | Weight |
|---|---|
| Never attempted | `3.0` — solid priority so new material surfaces |
| Attempted | `1.0 + 4.0 × fail_rate` → `1.0` (never fail) … `5.0` (always fail) |
| Last attempt passed everything | the above `× 0.4` (back off for a while) |
| Floor | `0.2` — even mastered exercises can resurface |

`fail_rate = fails / attempts`, where a "fail" is any graded attempt that didn't
pass every gradeable example. See `stats` for the current weights.

## Exam mode

`exam` simulates the exam shell: it picks **one exercise per level**, uniformly
at random (the level is the number in the folder name, so `ex1-3` is level 1
and `ex4` is level 4). It prints every question, creates a fresh `try<N>.py`
for each pick, and ends with an "exam sheet" recap of which file belongs to
which level. Grade each answer as usual with `python study.py grade <id>`.

Exam picks are independent of the `ask` round — taking an exam never disturbs
the weighted drill rotation above. `--seed <n>` makes the picks reproducible,
so you can retake the same exam.

## What it will and won't touch

- **Creates** only new `try<N>.py` files (numbered `max(existing)+1`) and
  `.progress.json` at the repo root.
- **Never** overwrites, renames, moves, or deletes any existing file.
- Reference solutions are shown **only** via the explicit `solution` command.

`.progress.json` is per-machine practice data and is git-ignored. Set
`STUDYTOOL_ROOT` to point the tool at a different repo copy (used by the tests).

## Layout

```
study.py               # entry point
studytool/
  discovery.py         # find exercises, resolve filters
  enparser.py          # parse .en -> function name, signature, typed examples
  attempts.py          # find/create try<N>.py (never overwrites)
  grader.py            # import an attempt, run it against examples, score
  progress.py          # .progress.json store + weighting
  cli.py               # argparse command line
```
