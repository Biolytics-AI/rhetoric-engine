#!/usr/bin/env python3
"""Fail if canonical skills depend on one harness-specific runtime."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

FORBIDDEN = [
    (re.compile(r"\bsubagent(s)?\b", re.I), "subagent orchestration belongs in a harness adapter"),
    (re.compile(r"\bspawn[_ -]?agent\b", re.I), "agent spawning is not portable"),
    (re.compile(r"\bSessionStart\b", re.I), "session-start hooks are not portable"),
    (re.compile(r"/brainstorm\b", re.I), "slash commands are not portable skill instructions"),
    (re.compile(r"\bClaude Code\b", re.I), "product-specific instructions belong in install docs or adapters"),
    (re.compile(r"\bCodex\b", re.I), "product-specific instructions belong in install docs or adapters"),
    (re.compile(r"\bChatGPT\b", re.I), "product-specific instructions belong in install docs or adapters"),
    (re.compile(r"\bGemini CLI\b", re.I), "product-specific instructions belong in install docs or adapters"),
    (re.compile(r"\bMCP\b", re.I), "MCP serving is optional infrastructure, not portable core"),
]


def main() -> int:
    errors: list[str] = []
    for path in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        for idx, line in enumerate(text.splitlines(), start=1):
            for pattern, reason in FORBIDDEN:
                if pattern.search(line):
                    errors.append(f"{path.relative_to(ROOT)}:{idx}: {reason}: {line.strip()}")

    if errors:
        print("Portability lint failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("portability-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
