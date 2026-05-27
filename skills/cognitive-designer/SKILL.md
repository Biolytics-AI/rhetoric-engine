---
name: cognitive-designer
description: Use after an approved slide thesis map to apply attention, multimedia learning, accessibility, hierarchy, contrast, reading order, and slide grammar before or alongside visual reasoning.
---

# Cognitive Designer

Design slide cognition so the audience can perceive, understand, and remember each thesis. Run after `slide-thesis-mapper` and before or alongside `visual-reasoner`.

## Inputs

- Approved intent brief, insight artifact, argument spine, and slide thesis map.
- Audience accessibility needs, medium, room, screen, and time constraints.
- Draft slide content, visual plan, evidence choices, or existing deck when available.
- Brand, style, or format constraints that affect legibility and emphasis.

## Outputs

Return a `Cognitive Design QC` with:

- `design_qc_report`: per-slide attention, load, reading order, contrast, and slide grammar notes.
- `accessibility_fixes`: required fixes for contrast, text size, alt text needs, color dependence, and reading sequence.
- `hierarchy_decisions`: primary focal point, secondary support, grouping, and progressive reveal decisions.
- `cognitive_risk_notes`: overload, ambiguity, split attention, weak signal, or memorability risks.

## Workflow

1. Confirm every reviewed slide has a clear thesis from the approved slide thesis map.
2. Assign one primary attention target per slide and subordinate all other elements to it.
3. Apply multimedia learning: pair words and visuals deliberately, remove redundancy, and keep related elements close.
4. Reduce cognitive load by chunking, sequencing, and removing nonessential marks or copy.
5. Check reading order across titles, labels, visuals, evidence, annotations, and speaker flow.
6. Strengthen hierarchy with size, position, grouping, contrast, whitespace, and emphasis.
7. Check accessibility for contrast, color-only meaning, text density, legibility, alt text needs, and keyboard or screen-reader order when relevant.
8. Record risks and fixes without inventing new claims, evidence, or renderer-specific implementation requirements.

## Evaluation Checks

- Each slide communicates one thesis before details compete for attention.
- Visual and verbal channels reinforce the same idea instead of duplicating noise.
- Reading order matches the audience's reasoning path.
- Contrast, scale, and grouping make hierarchy obvious.
- Accessibility fixes are explicit and actionable.
- Slide grammar supports the argument spine and does not create new claims.

## Failure Modes

- Polishing style while the thesis remains unclear.
- Adding emphasis everywhere and destroying hierarchy.
- Treating accessibility as optional or cosmetic.
- Creating decorative complexity that increases cognitive load.
- Reordering information against the argument logic.
- Making renderer-specific production demands.

## Handoff

Handoff `Cognitive Design QC` to `visual-reasoner`, evidence curation, or deck compilation. Include unresolved cognitive risks and accessibility fixes so downstream work preserves hierarchy, contrast, reading order, and slide grammar.
