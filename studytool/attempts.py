"""Manage `try<N>.py` attempt files inside an exercise folder.

Rules:
  * An attempt is exactly ``try<N>.py`` (N = 1, 2, 3, ...). Nothing else in the
    folder is treated as an attempt.
  * New attempts are numbered ``max(existing) + 1``.
  * We NEVER overwrite, rename, move, or delete an existing file — only create
    new ones. (If the computed target somehow already exists we bump N again.)
"""
from __future__ import annotations

import os
import re

from .enparser import ParsedEn

# Windows filesystems are case-insensitive, so match 'try'/'TRY' but always
# create lowercase 'tryN.py'.
_TRY_RE = re.compile(r"^try(\d+)\.py$", re.IGNORECASE)


def list_attempts(ex_dir: str) -> list[tuple[int, str]]:
    """Return ``[(n, abspath), ...]`` for every try<N>.py, sorted by N."""
    found: list[tuple[int, str]] = []
    for fname in os.listdir(ex_dir):
        m = _TRY_RE.match(fname)
        if m:
            found.append((int(m.group(1)), os.path.join(ex_dir, fname)))
    found.sort(key=lambda t: t[0])
    return found


def latest_attempt(ex_dir: str) -> tuple[int, str] | None:
    """The highest-numbered attempt, or None if there are none yet."""
    attempts = list_attempts(ex_dir)
    return attempts[-1] if attempts else None


def next_number(ex_dir: str) -> int:
    """The N to use for the next new attempt."""
    attempts = list_attempts(ex_dir)
    return attempts[-1][0] + 1 if attempts else 1


def find_by_number(ex_dir: str, n: int) -> str | None:
    """Absolute path of try<n>.py if it exists."""
    for num, path in list_attempts(ex_dir):
        if num == n:
            return path
    return None


def _prefill(parsed: ParsedEn, ex_id: str, filename: str) -> str:
    """Body for a fresh attempt file: a small header + the signature stub."""
    header = parsed.signature_with_colon or f"def {parsed.func_name}():"
    return (
        f"# {ex_id} - {parsed.func_name}\n"
        f"# attempt: {filename}\n"
        f"# (signature pre-filled from the .en; write your solution below)\n"
        f"\n"
        f"{header}\n"
        f"    # TODO: implement\n"
        f"    pass\n"
    )


def create_attempt(ex_dir: str, parsed: ParsedEn, ex_id: str) -> tuple[int, str]:
    """Create the next try<N>.py, pre-filled with the signature. Never clobbers.

    Returns ``(n, abspath)``. Uses ``x`` mode so a race can't overwrite an
    existing file; if that ever fires we simply try the next number.
    """
    n = next_number(ex_dir)
    while True:
        filename = f"try{n}.py"
        path = os.path.join(ex_dir, filename)
        try:
            with open(path, "x", encoding="utf-8") as fh:   # 'x' = create, fail if exists
                fh.write(_prefill(parsed, ex_id, filename))
            return n, path
        except FileExistsError:
            n += 1
