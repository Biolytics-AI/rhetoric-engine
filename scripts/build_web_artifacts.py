#!/usr/bin/env python3
"""Build Claude web and ChatGPT upload artifacts from canonical skills."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist" / "web"

PHASES = [
    ("Bootstrap", ["rhetorical-orchestrator"]),
    (
        "Phase 1: Intent, Insight, Argument",
        [
            "intent-framer",
            "insight-externalizer",
            "argument-spine-builder",
            "slide-thesis-mapper",
        ],
    ),
    (
        "Phase 2: Cognition, Visuals, Evidence",
        ["cognitive-designer", "visual-reasoner", "evidence-curator"],
    ),
    ("Phase 3: Distillation and Compilation", ["content-distiller", "deck-compiler"]),
    ("Phase 4: Critique and Delivery", ["critique-iterator", "delivery-coach"]),
]


FRONTMATTER_RE = re.compile(r"\A---\n(?P<yaml>.*?)\n---\n(?P<body>.*)\Z", re.S)


def parse_skill(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"{path} missing YAML frontmatter")

    meta: dict[str, str] = {}
    for line in match.group("yaml").splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"{path} has invalid frontmatter line: {line}")
        meta[key.strip()] = value.strip().strip('"')

    if "name" not in meta or "description" not in meta:
        raise ValueError(f"{path} must contain name and description")
    return meta, match.group("body").strip() + "\n"


def load_skills() -> dict[str, tuple[dict[str, str], str, str]]:
    skills: dict[str, tuple[dict[str, str], str, str]] = {}
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_path = skill_dir / "SKILL.md"
        if not skill_path.exists():
            raise FileNotFoundError(skill_path)
        meta, body = parse_skill(skill_path)
        name = meta["name"]
        if name != skill_dir.name:
            raise ValueError(f"{skill_path} name {name!r} does not match folder {skill_dir.name!r}")
        skills[name] = (meta, body, skill_path.read_text(encoding="utf-8"))
    return skills


def umbrella_skill(entry_filename: str) -> str:
    skill_ref = "skill.md" if entry_filename == "skill.md" else "SKILL.md"
    return f"""---
name: rhetoric-engine
description: Biolytics staged presentation cognition pipeline for user-led slide decks. Use for creating, improving, critiquing, rehearsing, or compiling presentations.
---

# Biolytics Rhetoric Engine

Use this skill when the user wants to create, improve, critique, rehearse, or compile a presentation, talk, slide deck, or slide-based argument.

Preserve the user's point of view. Do not replace it with a generic model-generated deck.

## First Move

Read `references/rhetorical-orchestrator.md` and follow it as the routing gate. The orchestrator explains when to use each stage reference and when to stop for user approval.

## Hard Gate

Do not draft, compile, or render slides until these four artifacts are explicit and approved:

- approved intent
- approved insight
- approved argument spine
- approved slide thesis map

## Stage References

{stage_list()}

## Web Package Note

This web upload package is generated from the same source skills used by coding agents. The canonical source repository is:

https://github.com/Biolytics-AI/rhetoric-engine

If your platform asks for a single file, upload the generated archive that contains this `{skill_ref}` file and the `references/` directory.
"""


def stage_list() -> str:
    lines: list[str] = []
    for title, names in PHASES:
        lines.append(f"### {title}\n")
        for name in names:
            lines.append(f"- `references/{name}.md`")
        lines.append("")
    return "\n".join(lines).strip()


def write_web_tree(target_dir: Path, entry_filename: str, skills: dict[str, tuple[dict[str, str], str, str]]) -> None:
    skill_dir = target_dir / "rhetoric-engine"
    references_dir = skill_dir / "references"
    references_dir.mkdir(parents=True, exist_ok=True)

    (skill_dir / entry_filename).write_text(umbrella_skill(entry_filename), encoding="utf-8")
    for name in sorted(skills):
        _meta, _body, full_text = skills[name]
        (references_dir / f"{name}.md").write_text(full_text, encoding="utf-8")


def zip_dir(source_dir: Path, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source_dir.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(source_dir.parent))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_per_skill_zips(skills: dict[str, tuple[dict[str, str], str, str]]) -> list[Path]:
    output_paths: list[Path] = []
    per_skill_dir = DIST_DIR / "per-skill"
    for name in sorted(skills):
        source_dir = SKILLS_DIR / name
        output_path = per_skill_dir / f"{name}.zip"
        zip_dir(source_dir, output_path)
        output_paths.append(output_path)
    return output_paths


def build() -> None:
    skills = load_skills()
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    claude_dir = DIST_DIR / "claude"
    chatgpt_dir = DIST_DIR / "chatgpt"
    write_web_tree(claude_dir, "skill.md", skills)
    write_web_tree(chatgpt_dir, "SKILL.md", skills)

    artifacts = [
        DIST_DIR / "rhetoric-engine-claude.zip",
        DIST_DIR / "rhetoric-engine-chatgpt.zip",
        DIST_DIR / "rhetoric-engine.skill",
    ]
    zip_dir(claude_dir / "rhetoric-engine", artifacts[0])
    zip_dir(chatgpt_dir / "rhetoric-engine", artifacts[1])
    shutil.copyfile(artifacts[1], artifacts[2])
    artifacts.extend(build_per_skill_zips(skills))

    manifest = {
        "version": "0.2.0",
        "source": "https://github.com/Biolytics-AI/rhetoric-engine",
        "artifacts": [
            {
                "path": str(path.relative_to(ROOT)),
                "sha256": sha256(path),
                "bytes": path.stat().st_size,
            }
            for path in artifacts
        ],
    }
    (DIST_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    build()


if __name__ == "__main__":
    main()
