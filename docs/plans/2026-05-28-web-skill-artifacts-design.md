# Web Skill Artifacts Design

## Goal

Make Biolytics Rhetoric Engine installable by both coding agents and mainstream web/chat agents without duplicating skill content.

## Verified Entry Points

Claude web custom skills are uploaded as a zip file containing one skill folder at the zip root. Anthropic's current help article describes the required entry file as `skill.md`, with required `name` and `description` frontmatter, and says the folder name should match the skill name.

ChatGPT web skills and ChatGPT Agent Studio expose upload flows for skill files. The current UI accepts `.zip`, `.skill`, or `SKILL.md` uploads. There is no public one-click install URL for either Claude web or ChatGPT web; users must download an artifact and upload it through the product UI.

Coding agents should continue to use native marketplace/repo installation from this repository.

## DRY Strategy

Keep `skills/*/SKILL.md` as the canonical source for coding agents.

Generate web artifacts from that source:

- Claude web: `dist/web/claude/rhetoric-engine.zip`, containing `rhetoric-engine/skill.md` and `rhetoric-engine/references/*.md`.
- ChatGPT web and ChatGPT Agent Studio: `dist/web/chatgpt/rhetoric-engine.skill` and `dist/web/chatgpt/rhetoric-engine.zip`, containing `rhetoric-engine/SKILL.md` and `rhetoric-engine/references/*.md`.
- Optional per-stage artifacts for power users: one zip per source skill.

The generated umbrella skill contains one entrypoint skill that routes through stage reference files. The stage reference files are generated from the canonical `skills/*/SKILL.md` bodies, so updates happen in one place.

## Build Contract

Add `scripts/build_web_artifacts.py`.

The script should:

1. Remove and recreate `dist/web/`.
2. Read each `skills/*/SKILL.md`.
3. Create an umbrella `rhetoric-engine` skill folder for each target.
4. Write target-appropriate entry filenames:
   - Claude: `skill.md`
   - ChatGPT: `SKILL.md`
5. Copy stage skills into `references/<skill-name>.md`.
6. Zip each artifact so the skill folder is the root entry inside the archive.
7. Write `dist/web/manifest.json` with artifact paths and SHA-256 checksums.

Generated artifacts are not committed by default. GitHub Actions should build them and attach them to releases.

## Lint Contract

Add `scripts/lint_portability.py`.

The linter should fail on obvious harness-only leakage inside canonical `skills/*/SKILL.md`, including references to subagents, session-start hooks, slash-command-only workflows, or product-specific install instructions. Platform-specific install instructions belong in `INSTALL.md`, not in portable skills.

## Documentation Contract

README and INSTALL should include direct latest-release links:

- `https://github.com/Biolytics-AI/rhetoric-engine/releases/latest/download/rhetoric-engine.skill`
- `https://github.com/Biolytics-AI/rhetoric-engine/releases/latest/download/rhetoric-engine-chatgpt.zip`
- `https://github.com/Biolytics-AI/rhetoric-engine/releases/latest/download/rhetoric-engine-claude.zip`

Screenshots should live under `docs/assets/screenshots/`. The README can reference stable paths immediately; the actual screenshots can be added when available as files.

