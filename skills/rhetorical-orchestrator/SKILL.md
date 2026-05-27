---
name: rhetorical-orchestrator
description: Master bootstrap gatekeeper for the Rhetoric Engine presentation pipeline. Use when a user wants to create, improve, critique, rehearse, or compile a presentation or slide deck, especially when the agent must decide which rhetorical stage skill to invoke and prevent premature slide generation.
---

# Rhetorical Orchestrator

Use this as the entry gate for the Rhetoric Engine. Keep the user's view primary: optimize for their intent, audience, constraints, and decision needs before optimizing for slide count, visual polish, or production speed.

## Operating Model

Run one plugin with many stage skills. You are the orchestrator, not the whole pipeline. Diagnose the user's current rhetorical state, route to the smallest applicable phase, update the artifact ledger, and stop at the next required approval gate. If a named stage skill is unavailable in the current install, execute the phase instructions yourself and record that the route was handled by `rhetorical-orchestrator`.

Do not compile, draft, or render a deck just because the user mentions slides. First make sure the rhetorical artifacts exist and are approved.

## Phase Order

| Phase | Intended stage skill ID | Purpose | Route when |
| --- | --- | --- |
| 1. Intent | `intent-framer` when available; otherwise this skill. | Define objective, audience, stakes, constraints, and success criteria. | The ask is broad, ambiguous, new, or missing audience/outcome. |
| 2. Insight | `insight-externalizer` when available; otherwise this skill. | Find the core audience-relevant idea, tension, or useful shift in perspective. | The user has facts but no clear point of view or audience insight. |
| 3. Argument spine | `argument-spine-builder` when available; otherwise this skill. | Build the persuasive sequence: claim, reasons, evidence, objections, and resolution. | The thesis exists but the logic, sequence, or persuasion path is weak. |
| 4. Slide thesis map | `slide-thesis-mapper` when available; otherwise this skill. | Assign one controlling thesis to each slide or section before layout. | The argument exists but slide-level jobs are not mapped. |
| 5. Cognitive design | `cognitive-designer` when available; otherwise this skill. | Resolve attention, hierarchy, accessibility, reading order, slide grammar, and cognitive risk before production. | Slide theses are approved and the deck needs design decisions, cognitive load reduction, accessibility checks, or slide grammar guidance. |
| 6. Visual reasoning | `visual-reasoner` when available; otherwise this skill. | Create the visual plan, chart or diagram recommendations, and annotation plan. | Slide theses are approved and the deck needs visual strategy, data display choices, diagrams, visual hierarchy, or annotation decisions; run after or alongside cognitive design. |
| 7. Evidence curation | `evidence-curator` when available; otherwise this skill. | Build the claim-evidence matrix, choose evidence, track provenance, identify backup evidence, and flag evidence gaps. | Claims, source materials, or proof burden matter before compilation; run before deck compilation whenever evidence/design/visual reasoning is relevant. |
| 8. Content distillation | `content-distiller` when available; otherwise this skill. | Tighten, cut, compress, fit to time or attention budget, move overflow to notes, recommend splits, and preserve argument integrity before or during production. | Slide theses are known and content needs signal improvement, compression, moved-to-notes decisions, split recommendations, or risk checks before compilation. |
| 9. Deck compilation | `deck-compiler` when available; otherwise this skill only after gates pass. | Produce or revise slides from approved slide theses plus Phase 2 artifacts and any existing content distillation outputs when available or needed. | Intent, insight, spine, and thesis map are approved, and relevant evidence, cognitive design, visual reasoning, and content distillation work has not been bypassed. |
| 10. Critique/rehearsal | `critique-iterator` for feedback, rubric review, severity-ranked revision backlog, root causes, fixes, retest plan, and delta report; `delivery-coach` for timing, transitions, pacing, written/visual/verbal delivery, Q&A, and rehearsal guidance; otherwise this skill. | Stress-test clarity, pacing, delivery, objections, and audience reception. | A draft, outline, or talk track exists and the user asks to improve or practice. |

## Hard Gates

Never compile a deck before all four upstream artifacts are present and approved:

- Approved intent.
- Approved insight.
- Approved argument spine.
- Approved slide thesis map.

Deck compilation should use the approved slide thesis map plus Phase 2 artifacts when available or needed: cognitive design guidance, visual reasoning plans, and evidence curation outputs. Route through `content-distiller` before compilation when tightening, cutting, compression, fit-to-time or attention-budget, moved-to-notes decisions, split recommendations, or argument-integrity checks are needed. Do not bypass evidence, design, visual reasoning, or needed content distillation when claims need support, visual choices affect comprehension, slide grammar/accessibility/cognitive load risks are relevant, or density threatens the argument.

If any artifact is missing, stale, or contradicted by new user input, pause compilation and route to the earliest affected phase. Ask only the minimum questions needed to unblock that phase.

## Artifact Ledger

Maintain a compact ledger in working notes or the project artifact when available:

- `user_goal`: what the user is trying to make happen.
- `audience`: who must be moved, informed, reassured, challenged, or equipped.
- `context`: venue, format, duration, medium, deadline, and constraints.
- `success_criteria`: how the user will judge the presentation worked.
- `approved_intent`: current approved intent statement, or `missing`.
- `approved_insight`: current approved insight, or `missing`.
- `approved_argument_spine`: current approved sequence, or `missing`.
- `approved_slide_thesis_map`: current approved slide or section thesis list, or `missing`.
- `phase_2_artifacts`: cognitive design guidance, visual reasoning plan, evidence matrix, provenance, backup evidence, and gaps, or `missing`.
- `content_distillation_outputs`: distilled deck spec, moved-to-notes list, cut list, split recommendations, and risk notes, or `missing`.
- `source_materials`: files, notes, data, links, and user-provided claims being used.
- `open_questions`: unresolved decisions blocking the next phase.
- `stage_status`: `draft`, `awaiting_user_approval`, `approved`, or `stale`.

## Skip Rules

For narrow user requests, do not force the full pipeline. Answer directly when the user asks for a bounded surface or text edit such as fixing grammar, tightening one title, changing tone within existing copy, formatting already-existing content, or extracting a short summary.

Skipped work must not create new slide structure, add or change claims, invent evidence, expand a one-slide edit into a sequence, or compile/render deck output. If the user asks to rewrite a single slide, limit the response to that slide's existing text and stated claim. If the user asks to format an existing deck, limit the work to presentation of existing content unless the hard gates are approved.

Even when skipping, preserve the user's stated intent and do not introduce new claims, strategy, or structure that would require upstream approval. If the narrow request reveals a serious rhetorical contradiction, flag it briefly and ask whether to route back to the relevant phase.

## Routing Discipline

Start every substantial presentation task by checking the ledger and naming the current phase. Prefer the earliest phase that is not approved. When the user explicitly approves an artifact, record it and move forward one phase. When the user revises goals, audience, constraints, or evidence, mark downstream artifacts stale and rebuild from the earliest affected point.
