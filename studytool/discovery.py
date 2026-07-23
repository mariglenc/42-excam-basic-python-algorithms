"""Find exercises in the repo and resolve command-line filters.

An *exercise* is any immediate sub-folder of the repo root that contains an
`.en` file (e.g. ``ex2-1/echo_validator.en``). The folder name (``ex2-1``) is
the exercise id used everywhere else.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from fnmatch import fnmatch

from . import enparser
from .enparser import ParsedEn

# Folders that are never exercises even if they somehow contain an .en file.
_SKIP_DIRS = {".git", "__pycache__", "studytool", ".idea", ".vscode"}


@dataclass
class Exercise:
    id: str                 # folder name, e.g. 'ex2-1'
    dir: str                # absolute path to the folder
    en_path: str            # absolute path to the .en file
    parsed: ParsedEn = field(default=None)  # type: ignore[assignment]

    @property
    def func_name(self) -> str | None:
        return self.parsed.func_name if self.parsed else None

    @property
    def title(self) -> str | None:
        return self.parsed.title if self.parsed else None


def discover(repo_root: str) -> list[Exercise]:
    """Return every exercise under ``repo_root``, sorted by id.

    Each exercise's `.en` is parsed eagerly (the files are tiny). A folder with
    more than one `.en` uses the first alphabetically; a folder with none is
    skipped.
    """
    exercises: list[Exercise] = []
    for name in sorted(os.listdir(repo_root)):
        path = os.path.join(repo_root, name)
        if not os.path.isdir(path) or name in _SKIP_DIRS:
            continue
        ens = sorted(f for f in os.listdir(path) if f.endswith(".en"))
        if not ens:
            continue
        en_path = os.path.join(path, ens[0])
        exercises.append(
            Exercise(id=name, dir=path, en_path=en_path, parsed=enparser.parse_en_file(en_path))
        )
    return exercises


def resolve(exercises: list[Exercise], filt: str | None) -> list[Exercise]:
    """Resolve a filter string to a list of exercises.

    Accepted forms:
      * ``None`` / ``"all"``   -> every exercise
      * an exact id            -> just that one          (``ex2-1``, ``ex4``)
      * a glob                 -> fnmatch on ids          (``ex1-*``, ``ex?-1``)
      * a prefix "group"       -> ids that start with it  (``ex1`` -> ex1-1, ex1-2, ...)
    Exact id is tried first so a real folder like ``ex4`` wins over the group
    interpretation.
    """
    if not filt or filt.lower() == "all":
        return list(exercises)

    by_id = {e.id: e for e in exercises}
    if filt in by_id:                                   # exact id
        return [by_id[filt]]

    if any(ch in filt for ch in "*?["):                 # glob
        return [e for e in exercises if fnmatch(e.id, filt)]

    # prefix group: 'ex1' matches 'ex1-1', 'ex1-2', ... (but also exact 'ex1')
    return [e for e in exercises if e.id == filt or e.id.startswith(filt + "-")]
