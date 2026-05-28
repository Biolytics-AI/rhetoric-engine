---
name: visual-reasoner
description: Use after a slide thesis is clear to choose the visual reasoning pattern that makes each slide thesis understandable and believable through charts, diagrams, annotations, or other nondecorative visual forms.
---

# Visual Reasoner

Choose visual forms that help the audience reason from thesis to belief. Do not choose visuals before the slide thesis is clear.

## Inputs

- Approved slide thesis map with audience question, answer thesis, and proof job per slide.
- Argument spine, evidence needs, and known objections.
- Available data, examples, images, diagrams, source material, and constraints.
- Cognitive design notes, accessibility requirements, and medium constraints when available.

## Outputs

Return a `Visual Reasoning Plan` with:

- `visual_plan_per_slide`: selected reasoning pattern, visual role, key encodings, and audience takeaway.
- `chart_diagram_recommendations`: chart, diagram, table, map, timeline, process, hierarchy, comparison, or annotated figure choices.
- `annotation_plan`: labels, callouts, emphasis, sequencing, and explanation needed to make the visual believable.
- `rejected_visuals`: decorative, weak, misleading, or thesis-mismatched visuals and why they were rejected.

## Workflow

1. Confirm the slide thesis, audience question, and proof job are explicit.
2. Select a visual reasoning pattern that matches the thinking task: compare, sequence, locate, quantify, classify, explain causality, show structure, reveal change, or decide.
3. Map evidence to visual elements only where it proves, clarifies, or qualifies the thesis.
4. Recommend the simplest chart or diagram that makes the relationship legible and credible.
5. Plan annotations that direct attention to the claim-relevant signal, not every available detail.
6. Reject visuals that decorate, imply unsupported causality, hide uncertainty, or compete with the thesis.
7. Flag slides that need stronger evidence, a clearer thesis, or cognitive design review before visual selection can proceed.

## Evaluation Checks

- Every visual has a reasoning job tied to the slide thesis.
- The recommended form fits the data relationship and audience task.
- Annotations make the belief path visible.
- Decorative or weak visuals are explicitly rejected.
- Uncertainty, caveats, and comparisons are not visually distorted.
- No visual choice depends on a specific renderer or slide backend.

## Failure Modes

- Choosing a chart because data exists instead of because it proves the thesis.
- Selecting visual style before the thesis is stable.
- Using illustrations, icons, or photos as decoration.
- Encoding too many variables for the audience's decision need.
- Hiding caveats or uncertainty to make the visual cleaner.
- Creating visuals that contradict cognitive design or accessibility constraints.

## Next Route

- If visual reasoning is blocked by unclear theses: return to `slide-thesis-mapper`.
- If visual reasoning is blocked by weak or missing proof: load `evidence-curator`.
- If visual choices create hierarchy, density, or accessibility risks: load `cognitive-designer`.
- If the `Visual Reasoning Plan` is complete and content is too dense: load `content-distiller`.
- If visual reasoning, cognitive design, evidence, and content fit are sufficient: load `deck-compiler`.
- This artifact feeds the whole presentation by making every chart, diagram, image, annotation, or table serve the approved slide thesis rather than decoration.

## Handoff

Handoff the `Visual Reasoning Plan` to `cognitive-designer`, `evidence-curator`, or deck compilation. Include rejected visuals and unresolved evidence or thesis issues so downstream work does not substitute decoration for reasoning.
