---
name: content-distiller
description: Use after slide theses are known to improve deck signal by cutting, moving, splitting, and risk-checking content while preserving argument integrity and one idea per slide.
---

# Content Distiller

Optimize signal, not mere length. Distill content so each slide carries one clear idea, protects the approved argument, and keeps useful overflow available in notes or backup.

## Inputs

- Approved intent, insight, argument spine, and slide thesis map when available.
- Draft deck spec, slide copy, notes, source material, evidence dossier, or existing deck content.
- Audience, duration, medium, required inclusions, and constraints.
- Cognitive design, visual reasoning, or compilation feedback when available.

## Outputs

- `distilled_deck_spec`: revised slide-by-slide content with one controlling idea per slide.
- `moved_to_notes_list`: detail, caveats, backup proof, examples, and delivery support moved out of slides.
- `cut_list`: removed content with rationale.
- `split_recommendations`: slides that need separation because they carry multiple ideas or proof jobs.
- `risk_notes`: warnings for over-cut content that may weaken logic, evidence, trust, nuance, or objections handling.

## Workflow

1. Confirm the controlling thesis and proof job for each slide before cutting.
2. Preserve the argument spine, slide theses, and audience decision path.
3. Remove duplication, throat-clearing, decorative facts, weak examples, and unsupported tangents.
4. Move useful but nonessential detail to speaker notes or backup instead of deleting it.
5. Split slides that contain multiple claims, audiences questions, proof jobs, or visual reasoning tasks.
6. Keep evidence that is necessary for belief; cut evidence that only adds volume or prestige.
7. Record every meaningful cut, move, split, and risk so downstream compilation can stay faithful.
8. Stop and route upstream if distillation exposes a broken thesis, missing proof, or contradicted argument.

## Evaluation Checks

- Each slide has one idea and one controlling thesis.
- The distilled spec preserves argument integrity and audience logic.
- Cuts improve signal rather than simply reducing word count.
- Notes retain necessary caveats, proof, and delivery context.
- Split recommendations identify slides that cannot be fixed by trimming.
- Risk notes warn where compression may damage persuasion, accuracy, or trust.

## Failure Modes

- Shortening copy while leaving multiple ideas on a slide.
- Cutting evidence or caveats required for audience belief.
- Removing objections that the argument must answer.
- Rewriting the approved thesis without routing upstream.
- Treating speaker notes as a trash bin instead of a useful overflow layer.
- Producing a prettier deck spec that no longer follows the argument spine.

## Handoff

Handoff the distilled deck spec, moved-to-notes list, cut list, split recommendations, and risk notes to `cognitive-designer`, `visual-reasoner`, `evidence-curator`, or `deck-compiler`. Mark unresolved thesis or proof problems as upstream issues, not compilation tasks.
