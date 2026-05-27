# Rhetoric Engine Implementation Plan

> **For Codex:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task.

**Goal:** Scaffold `rhetoric-engine` as one installable plugin containing the renamed presentation cognition skills.

**Architecture:** Use a Superpowers-style plugin layout: a root `.codex-plugin/plugin.json`, a `.claude-plugin/plugin.json`, and modular `skills/*/SKILL.md` folders. The `rhetorical-orchestrator` skill is the bootstrap gatekeeper and each phase skill owns one stage artifact.

**Tech Stack:** Markdown skills, JSON plugin manifests, shell validation with `python3`/`json.tool`, optional Codex `quick_validate.py` for each skill.

---

### Task 1: Create Plugin Manifests

**Files:**
- Create: `.codex-plugin/plugin.json`
- Create: `.claude-plugin/plugin.json`

**Step 1: Add Codex manifest**

Create `.codex-plugin/plugin.json` with:

```json
{
  "name": "rhetoric-engine",
  "version": "0.1.0",
  "description": "A staged presentation cognition pipeline for turning user intent, insight, argument, evidence, and delivery constraints into effective slide decks.",
  "author": {
    "name": "Hugo Evers"
  },
  "homepage": "https://github.com/hugoevers/rhetoric-engine",
  "repository": "https://github.com/hugoevers/rhetoric-engine",
  "license": "MIT",
  "keywords": [
    "presentations",
    "slides",
    "rhetoric",
    "argument",
    "storytelling",
    "skills"
  ],
  "skills": "./skills/",
  "interface": {
    "displayName": "Rhetoric Engine",
    "shortDescription": "A staged cognition pipeline for user-led presentation creation",
    "longDescription": "Use Rhetoric Engine to guide agents through intent framing, insight externalization, argument construction, slide thesis mapping, visual reasoning, evidence curation, deck compilation, critique, distillation, and delivery coaching.",
    "developerName": "Hugo Evers",
    "category": "Productivity",
    "capabilities": [
      "Interactive",
      "Read",
      "Write"
    ],
    "defaultPrompt": [
      "Help me turn this rough presentation idea into a clear deck.",
      "Help me build a presentation that communicates my view, not a generic AI summary."
    ],
    "websiteURL": "https://github.com/hugoevers/rhetoric-engine",
    "privacyPolicyURL": "https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement",
    "termsOfServiceURL": "https://docs.github.com/en/site-policy/github-terms/github-terms-of-service",
    "brandColor": "#7C3AED",
    "screenshots": []
  }
}
```

**Step 2: Add Claude manifest**

Create `.claude-plugin/plugin.json` with a minimal local plugin manifest:

```json
{
  "name": "rhetoric-engine",
  "description": "A staged presentation cognition pipeline for user-led slide creation.",
  "version": "0.1.0"
}
```

**Step 3: Validate JSON**

Run:

```bash
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
python3 -m json.tool .claude-plugin/plugin.json >/dev/null
```

Expected: both commands exit with status 0.

### Task 2: Create Skill Directories

**Files:**
- Create directories under `skills/`

**Step 1: Create stage folders**

Create these folders:

```text
skills/rhetorical-orchestrator/
skills/intent-framer/
skills/insight-externalizer/
skills/argument-spine-builder/
skills/slide-thesis-mapper/
skills/cognitive-designer/
skills/visual-reasoner/
skills/evidence-curator/
skills/deck-compiler/
skills/content-distiller/
skills/critique-iterator/
skills/delivery-coach/
```

**Step 2: Check directory list**

Run:

```bash
find skills -mindepth 1 -maxdepth 1 -type d | sort
```

Expected: exactly the 12 skill directories above.

### Task 3: Implement The Orchestrator Skill

**Files:**
- Create: `skills/rhetorical-orchestrator/SKILL.md`

**Step 1: Write frontmatter**

Use:

```yaml
---
name: rhetorical-orchestrator
description: Master bootstrap gatekeeper for the Rhetoric Engine presentation pipeline. Use when a user wants to create, improve, critique, rehearse, or compile a presentation or slide deck, especially when the agent must decide which rhetorical stage skill to invoke and prevent premature slide generation.
---
```

**Step 2: Write body**

Include:

- One-plugin/many-skills operating model.
- Phase order and routing table.
- Hard gates: no deck compilation before approved intent, insight, argument spine, and slide thesis map.
- Artifact ledger fields.
- Skip rules for narrow user requests.
- Instruction to keep the user's view primary.

**Step 3: Validate frontmatter**

Run:

```bash
python3 /Users/hugoevers/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/rhetorical-orchestrator
```

Expected: validation passes.

### Task 4: Implement Phase 1 Skills

**Files:**
- Create: `skills/intent-framer/SKILL.md`
- Create: `skills/insight-externalizer/SKILL.md`
- Create: `skills/argument-spine-builder/SKILL.md`
- Create: `skills/slide-thesis-mapper/SKILL.md`

**Step 1: Write `intent-framer`**

Purpose: transform rough topic into intent brief. Required outputs: primary audience, current state, desired change, stakes, success test, constraints, objections, non-goals.

**Step 2: Write `insight-externalizer`**

Purpose: turn tacit user understanding into inspectable artifacts. Required outputs: plain-language explanation, concept map, assumptions ledger, fact/inference/assumption labels, open questions.

**Step 3: Write `argument-spine-builder`**

Purpose: build claim-evidence-warrant spine. Required outputs: core claim, support branches, warrants, evidence needs, rebuttals.

**Step 4: Write `slide-thesis-mapper`**

Purpose: convert argument spine into slide-level questions and answer theses. Required outputs: slide thesis map, section roadmap, backup slide topics, time fit notes.

**Step 5: Validate each skill**

Run:

```bash
for skill in intent-framer insight-externalizer argument-spine-builder slide-thesis-mapper; do
  python3 /Users/hugoevers/.codex/skills/.system/skill-creator/scripts/quick_validate.py "skills/$skill"
done
```

Expected: all validations pass.

### Task 5: Implement Phase 2 Skills

**Files:**
- Create: `skills/cognitive-designer/SKILL.md`
- Create: `skills/visual-reasoner/SKILL.md`
- Create: `skills/evidence-curator/SKILL.md`

**Step 1: Write `cognitive-designer`**

Purpose: apply attention, multimedia learning, accessibility, hierarchy, contrast, reading order, and slide grammar.

**Step 2: Write `visual-reasoner`**

Purpose: choose the visual reasoning pattern that makes each slide thesis understandable and believable.

**Step 3: Write `evidence-curator`**

Purpose: build claim-evidence matrix, rank evidence, choose primary and backup evidence.

**Step 4: Validate each skill**

Run:

```bash
for skill in cognitive-designer visual-reasoner evidence-curator; do
  python3 /Users/hugoevers/.codex/skills/.system/skill-creator/scripts/quick_validate.py "skills/$skill"
done
```

Expected: all validations pass.

### Task 6: Implement Phase 3 Skills

**Files:**
- Create: `skills/deck-compiler/SKILL.md`
- Create: `skills/content-distiller/SKILL.md`

**Step 1: Write `deck-compiler`**

Purpose: compile approved artifacts into an editable deck spec or actual deck using whatever backend is available.

Required behavior: preserve slide theses, keep output editable, put overflow in speaker notes, inspect generated slides for thesis drift and layout issues.

**Step 2: Write `content-distiller`**

Purpose: optimize signal, not merely shorten. Required outputs: distilled deck spec, moved-to-notes list, cut list, split recommendations, risk notes for over-cut content.

**Step 3: Validate each skill**

Run:

```bash
for skill in deck-compiler content-distiller; do
  python3 /Users/hugoevers/.codex/skills/.system/skill-creator/scripts/quick_validate.py "skills/$skill"
done
```

Expected: all validations pass.

### Task 7: Implement Phase 4 Skills

**Files:**
- Create: `skills/critique-iterator/SKILL.md`
- Create: `skills/delivery-coach/SKILL.md`

**Step 1: Write `critique-iterator`**

Purpose: convert feedback into a ranked revision backlog. Required outputs: severity-ranked issues, root causes, concrete fixes, retest plan, delta report.

**Step 2: Write `delivery-coach`**

Purpose: create timing, transition, pacing, written delivery, visual delivery, verbal delivery, Q&A, and rehearsal guidance.

**Step 3: Validate each skill**

Run:

```bash
for skill in critique-iterator delivery-coach; do
  python3 /Users/hugoevers/.codex/skills/.system/skill-creator/scripts/quick_validate.py "skills/$skill"
done
```

Expected: all validations pass.

### Task 8: Add Minimal Repository Metadata

**Files:**
- Create: `README.md`
- Create: `LICENSE`

**Step 1: Write README**

Include:

- What Rhetoric Engine does.
- Why it is not a one-shot deck generator.
- Install shape: one plugin, many skills.
- Skill list grouped by phase.
- Basic local install instructions for Codex/Claude-style skill consumers.

**Step 2: Add MIT license**

Use standard MIT text with current year and owner.

### Task 9: Final Validation

**Files:**
- Inspect all created files.

**Step 1: Validate JSON manifests**

Run:

```bash
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
python3 -m json.tool .claude-plugin/plugin.json >/dev/null
```

Expected: status 0.

**Step 2: Validate all skills**

Run:

```bash
for skill in skills/*; do
  python3 /Users/hugoevers/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill"
done
```

Expected: every skill passes.

**Step 3: Check tree**

Run:

```bash
find . -maxdepth 3 -type f | sort
```

Expected: plugin manifests, README, LICENSE, research report, design plan, implementation plan, and 12 `SKILL.md` files are present.

