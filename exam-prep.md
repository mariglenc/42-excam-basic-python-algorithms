# Exam Prep — 2026-07-28, 10:00

4 random questions, one per level. Latest attempt on every exercise: 100%. You're ready.

## Tomorrow morning (~8:30)

```bash
python study.py exam        # one warm-up round, one exercise per level
python study.py grade ex…   # grade each answer
```

Then STOP. No cramming past the warm-up.

## Before EVERY submission — say it out loud

1. `isalnum()` — not `.alnum()`
2. `i += 1` — not `i =+ 1`
3. `ord('a')` — not `char('a')`
4. `int(text[i])` before doing math on a digit character
5. **Delete all `print()` lines**

## Concepts to have fresh

- **Look-ahead loop** (ex1-3): `for i in range(len(text) - 1)` — the `-1` is because you access `text[i+1]`
- **Caesar cipher** (ex1-5): rebuild it from the story, don't memorize:
  letter → position 0–25 (`ord(c) - ord('a')`) → `+ shift` → wrap `% 26` → back to letter (`+ ord('a')`, `chr(...)`)
  Handle `a-z` and `A-Z` in separate branches; non-letters pass through unchanged
- **Palindrome cleanup** (ex2-1): keep `isalnum()` chars, `.lower()` them, compare with `[::-1]`
- **Reverse a list/string**: `[::-1]`
- **Interleave two lists** (ex2-3): loop `range(max(len(a), len(b)))`, guard each append with `if i < len(...)`
- **Permutation check** (ex3-2): `.replace(" ", "").lower()` both, then `sorted(a) == sorted(b)`
- **Sort by multiple criteria** (ex4): `sorted(items, key=fn)` where `fn` returns a tuple `(len, word.lower(), vowels)` — compared left to right, first difference wins

## If a grade run fails

Don't panic — your pattern is fail-first, fix-in-minutes. Read the error/expected-vs-got, find the typo, resubmit.

## Debugging by error message

- `'str' object is not callable` → you put `(...)` after a string variable (e.g. `char('a')`)
- `can only concatenate str (not "int") to str` → missing `str(...)` or `int(...)` conversion
- `'str' object has no attribute ...` → misspelled method (`.alnum` → `.isalnum`)
