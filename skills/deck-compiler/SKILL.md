---
name: deck-compiler
description: Use only after approved intent, insight, argument spine, slide thesis map, and relevant Phase 2 artifacts to compile editable presentation output through any available deck backend.
---

# Deck Compiler

Compile approved rhetorical artifacts into an editable deck spec or actual deck. Use the available backend or artifact pipeline: PPTX, Google Slides, HTML slides, Markdown slides, or another editable format.

Never compile before the approved intent, approved insight, approved argument spine, approved slide thesis map, and relevant Phase 2 artifacts are present.

## Inputs

- Approved intent brief, insight artifact, argument spine, and slide thesis map.
- Relevant Phase 2 design, visual, and evidence artifacts: cognitive design QC, visual reasoning plan, evidence dossier, or approved equivalents.
- Content distillation outputs only if already produced or explicitly provided as a Phase 3 companion input: distilled deck spec, moved-to-notes list, cut list, split recommendations, and risk notes.
- Source materials, brand or format constraints, target medium, duration, and backend availability.
- Existing deck or template when the user asks to revise or conform to one.

## Outputs

- Editable deck spec or editable deck in the best available backend.
- Speaker notes containing overflow, caveats, backup proof, and delivery guidance.
- Compilation notes covering backend used, assumptions, unresolved gaps, and manual follow-ups.
- Inspection report for thesis drift, layout issues, overflow, accessibility risks, and editability.

## Workflow

1. Verify all hard-gate artifacts are present and approved; stop and route upstream if any are missing, stale, or contradicted.
2. Choose the most suitable available editable output pipeline without imposing renderer-specific requirements.
3. Preserve each slide thesis as the controlling claim for its slide.
4. Translate approved evidence, visual reasoning, cognitive design guidance, and any provided content distillation outputs into editable slide content.
5. Keep one idea per slide; move supporting detail, defensive proof, caveats, and overflow into speaker notes.
6. Preserve citations, provenance, and backup evidence where provided.
7. Generate or update the deck artifact without flattening editable text, shapes, charts, or notes unless no editable alternative exists.
8. Inspect generated slides for thesis drift, overloaded layouts, missing notes, broken reading order, inaccessible contrast, and backend conversion issues.
9. Return the deck or deck spec with the inspection report and any required handoff notes.

## Evaluation Checks

- Every slide still expresses its approved thesis.
- The output remains editable in the selected backend or format.
- Overflow appears in speaker notes instead of crowding slides.
- Layout, hierarchy, reading order, and accessibility match approved Phase 2 guidance.
- Evidence and citations do not create unsupported new claims.
- The compilation report identifies thesis drift and layout issues found during inspection.

## Failure Modes

- Compiling before intent, insight, spine, thesis map, or relevant Phase 2 artifacts are approved.
- Treating a renderer as mandatory when another editable backend is available.
- Flattening content into screenshots or images without need.
- Rewriting theses during production.
- Hiding overflow on slides instead of moving it to notes.
- Skipping post-generation inspection for drift, layout, or editability problems.

## Handoff

Handoff the editable deck spec or deck, speaker notes, and inspection report to critique, rehearsal, user review, or downstream production. Flag any slide that needs upstream revision rather than silently changing its thesis during compilation.
