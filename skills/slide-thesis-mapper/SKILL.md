---
name: slide-thesis-mapper
description: Use when an approved argument spine must become slide-level audience questions, answer theses, sections, backup topics, and time-fit decisions before any design, rendering, or deck compilation.
---

# Slide Thesis Mapper

Convert an argument spine into slide-level audience questions and answer theses. This is a hard gate before design, rendering, or deck compilation.

Do not create visual layouts, speaker notes, or finished slides until the thesis map is approved.

## Inputs

- Approved intent brief.
- Approved insight artifact.
- Approved argument spine with evidence needs and rebuttals.
- Presentation format, duration, audience setting, and any slide count constraints.
- Required sections, mandated content, or existing deck structure if applicable.

## Outputs

Return a `Slide Thesis Map` with:

- `slide_thesis_map`: each slide or segment with audience question, answer thesis, proof job, and source/evidence need.
- `section_roadmap`: section sequence, purpose, transition logic, and approximate time allocation.
- `backup_slide_topics`: optional detail, evidence, appendix, or rebuttal slides.
- `time_fit_notes`: pacing risks, compression options, expansion options, and likely cuts.

Use this compact format:

```markdown
## Slide Thesis Map
- Section roadmap:
- Slide thesis map:
- Backup slide topics:
- Time fit notes:
- Approval questions:
```

## Workflow

1. Translate each argument branch into the audience question it must answer.
2. Write one answer thesis per slide or segment. Each thesis must be a complete sentence with a claim.
3. Assign a proof job to each slide: establish context, prove branch, compare options, resolve objection, show implication, or drive action.
4. Group slides into sections that match audience logic and the argument spine.
5. Add transitions that explain why the next question follows from the previous answer.
6. Move deep detail, edge cases, and defensive proof into backup slide topics.
7. Check time fit against duration, complexity, and expected discussion.
8. Mark unresolved evidence needs or unclear theses before allowing design or compilation.
9. Ask for approval and treat changes to the spine as upstream revisions.

## Evaluation Checks

- Every slide has one controlling answer thesis.
- Each thesis answers an audience question, not a speaker filing category.
- The section roadmap preserves the argument spine's logic.
- Backup topics protect the main flow from overload.
- Time fit notes identify what to cut or expand.
- No slide exists only because there is data available.
- The map is ready for design without inventing new claims.

## Failure Modes

- Turning support branches into vague section headers.
- Creating slide titles before deciding the thesis.
- Letting source material dictate slide order.
- Packing multiple claims into one slide.
- Designing layouts, choosing visuals, or compiling a deck before approval.
- Hiding controversial claims in backup instead of addressing them in the main flow.

## Next Route

- If slide theses, audience questions, proof jobs, section sequence, or time fit are unresolved: stay in `slide-thesis-mapper`.
- If the `Slide Thesis Map` is approved and claims need proof: load `evidence-curator`.
- If the map is approved and slide comprehension or accessibility needs shaping: load `cognitive-designer`.
- If the map is approved and visual form choices are needed: load `visual-reasoner`.
- If the map is approved and content density is already a risk: load `content-distiller`.
- If all hard gates and relevant Phase 2 artifacts are approved: load `deck-compiler`.
- If the map changes the argument: return to `argument-spine-builder`; if it changes insight or intent, return to the earliest affected upstream skill.
- This artifact feeds the whole presentation by assigning one audience question, one answer thesis, and one proof job to each slide or segment before layout begins.

## Handoff

Handoff an approved `Slide Thesis Map` to design, evidence curation, or deck compilation. Treat this artifact as the required gate: no rendering, layout design, or deck assembly should begin until it is approved and consistent with the intent, insight, and argument spine.
