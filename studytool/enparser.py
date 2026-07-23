"""Parser for `.en` exercise files.

Format (verified against every .en in this repo)::

    <title>
    ==========            <- underline of '=' characters
                          <- (blank)
    Write a function:
                          <- (blank)
        def <name>(<params>) -> <ret>      <- indented signature, NO trailing ':'
                          <- (blank)
    <free-text description...>

    Examples:
        <name>(<args>)   -> <expected>     # optional inline comment
        ...

Two pieces of the algorithm are worth understanding (they exist because the
real files are messier than the happy path):

1. SPLITTING EXAMPLES.  We do not split on newlines, because a single example
   can span several physical lines (see ex2-2/mirror_matrix.en, where both the
   call *and* the expected value are pretty-printed across multiple lines).
   Instead we use the *function name* as the delimiter: every example begins
   with ``name(``. Each example therefore runs from one ``name(`` up to the
   next one (or end of block). Anything trailing after the final example — e.g.
   the markdown tables in ex1-1/bracket_validator.en — is naturally discarded
   because it never terminates in a valid literal (or is cut at the first blank
   line). The call itself is bounded by BALANCED-PAREN scanning that skips over
   quotes, so commas/parens inside string args don't fool us.

2. TYPING THE VALUES.  Both the arguments and the expected value are turned
   into real Python objects with ``ast.literal_eval`` — never ``eval`` — so
   ``True``/``False``/``None``, ints, negative ints, quoted strings, lists and
   nested lists all come back as the correct type. If an example line is
   truncated or otherwise not a valid literal, that example is flagged
   (``call_ok`` / ``expected_ok`` = False) and carries a human-readable
   ``note`` instead of crashing the whole parse.
"""
from __future__ import annotations

import ast
import re
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Example:
    """One parsed `name(args) -> expected` line (possibly multi-line)."""
    call: str                       # the raw call text, e.g. 'mirror_matrix([[1,2]])'
    args: list = field(default_factory=list)      # positional arg *values*
    kwargs: dict = field(default_factory=dict)     # keyword arg values (rare)
    expected: Any = None            # the expected return *value*
    expected_raw: str = ""          # raw text after '->', before literal_eval
    call_ok: bool = False           # were the args parseable as literals?
    expected_ok: bool = False       # was the expected value a valid literal?
    note: str = ""                  # why something failed, if it did

    @property
    def gradeable(self) -> bool:
        """True only when we have real values on both sides to compare."""
        return self.call_ok and self.expected_ok


@dataclass
class ParsedEn:
    """Everything the tool needs out of one `.en` file."""
    title: str | None = None
    func_name: str | None = None
    signature: str | None = None    # e.g. 'def echo_validator(text: str) -> bool'
    description: str = ""
    examples: list[Example] = field(default_factory=list)

    @property
    def signature_with_colon(self) -> str | None:
        """The signature as a valid `def` header (the .en omits the ':')."""
        if not self.signature:
            return None
        return self.signature if self.signature.rstrip().endswith(":") else self.signature + ":"


# --------------------------------------------------------------------------- #
# low-level scanners
# --------------------------------------------------------------------------- #
def _scan_balanced_paren(s: str, open_idx: int) -> int:
    """Index of the ')' that matches the '(' at ``open_idx``, honoring quotes.

    Returns -1 if the parentheses never balance (e.g. a line was cut off).
    Quote-awareness matters so that a ``)`` or ``,`` *inside* a string argument
    is not mistaken for structure.
    """
    depth = 0
    i = open_idx
    quote: str | None = None
    while i < len(s):
        c = s[i]
        if quote:
            if c == "\\":            # backslash escape inside a string literal
                i += 2
                continue
            if c == quote:
                quote = None
        elif c in "\"'":
            quote = c
        elif c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def _strip_inline_comment(s: str) -> str:
    """Drop a trailing ``# ...`` comment, ignoring '#' inside string literals."""
    quote: str | None = None
    i = 0
    while i < len(s):
        c = s[i]
        if quote:
            if c == "\\":
                i += 2
                continue
            if c == quote:
                quote = None
        elif c in "\"'":
            quote = c
        elif c == "#":
            return s[:i]
        i += 1
    return s


def _clean_expected(raw: str) -> str:
    """Reduce the text after '->' to just the literal.

    An expected value ends at the first blank line — that blank line is the
    boundary before the next example or a trailing prose/markdown block. Inline
    ``# ...`` comments (present in ex1-3 and ex3-1) are removed.
    """
    lines: list[str] = []
    for line in raw.splitlines():
        if line.strip() == "":       # blank line == end of this logical block
            break
        lines.append(line)
    return _strip_inline_comment("\n".join(lines)).strip()


# --------------------------------------------------------------------------- #
# public API
# --------------------------------------------------------------------------- #
def parse_en(text: str) -> ParsedEn:
    """Parse the full text of an `.en` file into a :class:`ParsedEn`."""
    parsed = ParsedEn()
    lines = text.splitlines()

    # --- title: first non-empty line that is underlined by '=' characters ---
    for i, line in enumerate(lines):
        if line.strip():
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
            if nxt and set(nxt) <= {"="}:
                parsed.title = line.strip()
            break

    # --- signature: the indented `def NAME(...) -> ret` line ---------------- #
    # Use [ \t] (not \s) for the indent so the match cannot span the blank line
    # above `def` and accidentally swallow the whole line.
    m = re.search(r"^[ \t]*def[ \t]+(\w+)[ \t]*\(", text, re.MULTILINE)
    if m:
        parsed.func_name = m.group(1)
        line_start = text.rfind("\n", 0, m.start()) + 1
        line_end = text.find("\n", m.start())
        line_end = len(text) if line_end == -1 else line_end
        parsed.signature = text[line_start:line_end].strip()

    if not parsed.func_name:
        return parsed

    # --- description: text between the signature line and 'Examples:' ------- #
    ex_idx = text.find("Examples:")
    if parsed.signature is not None:
        desc_start = text.find("\n", m.end())
        desc_end = ex_idx if ex_idx != -1 else len(text)
        if desc_start != -1 and desc_start < desc_end:
            parsed.description = text[desc_start:desc_end].strip()

    # --- examples ----------------------------------------------------------- #
    if ex_idx == -1:
        return parsed
    block = text[ex_idx + len("Examples:"):]
    parsed.examples = _parse_examples(block, parsed.func_name)
    return parsed


def parse_en_file(path: str) -> ParsedEn:
    """Read ``path`` (utf-8) and parse it."""
    with open(path, encoding="utf-8") as fh:
        return parse_en(fh.read())


def _parse_examples(block: str, func: str) -> list[Example]:
    """Split the Examples block on ``func(`` and parse each chunk."""
    call_re = re.compile(r"\b" + re.escape(func) + r"\s*\(")
    starts = [mm.start() for mm in call_re.finditer(block)]
    out: list[Example] = []

    for n, start in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(block)
        chunk = block[start:end]
        ex = Example(call="")

        paren = chunk.find("(")
        close = _scan_balanced_paren(chunk, paren)
        if close == -1:
            ex.call = chunk.strip()
            ex.note = "call parentheses not balanced (line cut off?)"
            out.append(ex)
            continue

        ex.call = chunk[: close + 1].strip()

        # argument VALUES via AST — literal_eval each arg node (no eval())
        try:
            node = ast.parse(ex.call, mode="eval").body
            ex.args = [ast.literal_eval(a) for a in node.args]           # type: ignore[attr-defined]
            ex.kwargs = {kw.arg: ast.literal_eval(kw.value) for kw in node.keywords}  # type: ignore[attr-defined]
            ex.call_ok = True
        except (SyntaxError, ValueError) as exc:
            ex.note = f"could not parse call args: {exc}"

        rest = chunk[close + 1:]
        arrow = rest.find("->")
        if arrow == -1:
            ex.note = (ex.note + "; " if ex.note else "") + 'no "->" (expected cut off?)'
            out.append(ex)
            continue

        ex.expected_raw = _clean_expected(rest[arrow + 2:])
        try:
            ex.expected = ast.literal_eval(ex.expected_raw)
            ex.expected_ok = True
        except (SyntaxError, ValueError) as exc:
            ex.note = (ex.note + "; " if ex.note else "") + f"expected not a literal: {exc}"

        out.append(ex)

    return out
