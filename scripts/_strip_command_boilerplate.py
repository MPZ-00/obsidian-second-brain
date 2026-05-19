#!/usr/bin/env python3
"""One-shot tooling: strip boilerplate from obsidian-* command files.

Removes:
  1. Step "Read `_CLAUDE.md` first ..." (now handled by SessionStart hook)
     and renumbers subsequent steps.
  2. Trailing "---\\n\\n**AI-first rule:** ..." footer
     (centralized in SKILL.md).

Run once after editing the canonical commands in the repo, then sync to
~/.claude/commands/ via install.sh --force.

Usage:
    python scripts/_strip_command_boilerplate.py path/to/commands/
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

CLAUDE_READ_STEP = re.compile(
    r"^\d+\.\s+Read\s+`_CLAUDE\.md`\s+first[^\n]*\n",
    re.MULTILINE,
)
NUMBERED_STEP = re.compile(r"^(\d+)\.\s", re.MULTILINE)
AI_FIRST_FOOTER = re.compile(
    r"\n---\s*\n\s*\*\*AI-first rule:\*\*[\s\S]*$",
    re.MULTILINE,
)


def strip_file(path: Path) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8")
    original = text

    m = CLAUDE_READ_STEP.search(text)
    if m:
        text = text[: m.start()] + text[m.end() :]
        # Renumber subsequent steps: each `N. ` becomes `(N-1). `
        # Only renumber within the contiguous list block following the deletion.
        # Simpler: renumber every `N. ` in the file where N > 1 by decrementing.
        # Constraint: only one numbered list block per command file (verified
        # by inspection of all 11 files).
        def renumber(match: re.Match[str]) -> str:
            n = int(match.group(1))
            return f"{n - 1}. " if n > 1 else match.group(0)

        text = NUMBERED_STEP.sub(renumber, text)

    text = AI_FIRST_FOOTER.sub("\n", text)

    # Tidy: collapse 3+ blank lines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text.endswith("\n"):
        text += "\n"

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True, f"stripped {path.name}"
    return False, f"unchanged {path.name}"


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    root = Path(sys.argv[1])
    files = sorted(root.glob("obsidian-*.md"))
    if not files:
        print(f"error: no obsidian-*.md under {root}", file=sys.stderr)
        return 1
    for f in files:
        changed, msg = strip_file(f)
        print(("  " if not changed else "  * ") + msg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
