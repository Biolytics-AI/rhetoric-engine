---
name: argument-spine-builder
description: Use when a presentation has an approved intent and insight but lacks a clear answer-first persuasive logic, core claim, support structure, warrants, evidence needs, or rebuttals.
---

# Argument Spine Builder

Build a claim-evidence-warrant spine that makes the presentation answer-first. Prevent piles of facts, chronology, or topic lists that never make a claim.

Use after intent and insight are approved, and before slide thesis mapping.

## Inputs

- Approved intent brief.
- Approved insight artifact, including labeled facts, inferences, assumptions, and open questions.
- Available evidence, source constraints, and required claims.
- Audience objections, decision criteria, and success test.

## Outputs

Return an `Argument Spine` with:

- `core_claim`: the answer the presentation asks the audience to accept.
- `support_branches`: main reasons that make the core claim believable and useful.
- `warrants`: why each support branch proves or advances the claim.
- `evidence_needs`: proof required, available evidence, gaps, and source priority.
- `rebuttals`: likely objections and the response strategy for each.

Use this compact format:

```markdown
## Argument Spine
- Core claim:
- Support branches:
- Warrants:
- Evidence needs:
- Rebuttals:
- Approval questions:
```

## Workflow

1. State the answer first as a complete claim, not a topic or theme.
2. Test the core claim against the intent brief: it must move the primary audience toward the desired change.
3. Create three to five support branches, each phrased as a reason the claim is true, necessary, or preferable.
4. For each branch, write the warrant: the reasoning bridge between evidence and claim.
5. Attach available evidence only where it serves a branch. Do not dump facts without a claim job.
6. Mark evidence needs as `available`, `needs source`, `needs user confirmation`, or `optional backup`.
7. Add rebuttals for objections that could block acceptance, action, trust, or timing.
8. Order the spine by audience logic: what they need to accept first, not the order the user discovered it.
9. Ask for approval before mapping slides.

## Evaluation Checks

- The core claim answers the audience's implicit question.
- Each support branch is a claim-bearing reason, not a category label.
- Every evidence item has a job in the argument.
- Warrants are explicit enough to reveal weak logic.
- Rebuttals address real audience resistance, not straw objections.
- The spine can be summarized aloud in under one minute.

## Failure Modes

- Starting with background, chronology, or data before the answer.
- Mistaking "here are facts" for persuasion.
- Using evidence as decoration instead of proof.
- Leaving warrants implicit because the logic feels obvious to the speaker.
- Adding too many branches for the audience's time and attention.
- Ignoring objections that the audience will raise privately.

## Next Route

- If the core claim, warrants, support branches, or rebuttals are still unresolved: stay in `argument-spine-builder`.
- If the `Argument Spine` is approved: load `slide-thesis-mapper`.
- If the spine exposes a weak or unowned insight: return to `insight-externalizer`.
- If the spine changes the intended audience movement, stakes, or success test: return to `intent-framer` and mark downstream artifacts stale.
- This artifact feeds the whole presentation by defining the persuasive logic every slide must serve: claim, reasons, warrants, evidence needs, and objection strategy.

## Handoff

Handoff an approved `Argument Spine` to `slide-thesis-mapper`. Include evidence gaps and rebuttal needs so slide-level theses can reserve space for proof, qualification, and backup material.
