---
name: insight-externalizer
description: Use when the user has tacit expertise, scattered notes, strong opinions, domain intuition, or source material but the presentation's core insight and assumptions are not yet inspectable.
---

# Insight Externalizer

Turn tacit user understanding into artifacts that can be inspected, corrected, and used. Protect the user's view: do not substitute the model's understanding for the user's understanding.

Use after intent framing and before argument spine work when the point of view, causal model, assumptions, or key distinction is still implicit.

## Inputs

- Approved intent brief or enough context to preserve audience and desired change.
- User notes, transcripts, source excerpts, examples, anecdotes, data, or rough claims.
- The user's own explanation of what matters, what is misunderstood, and what they believe others miss.
- Any known disputes, uncertainties, or missing evidence.

## Outputs

Return an `Insight Artifact` with:

- `plain_language_explanation`: the user's idea in direct, non-jargony language.
- `concept_map`: key concepts and relationships, including cause, contrast, dependency, sequence, and tradeoff.
- `assumptions_ledger`: assumptions, why they matter, confidence, and how to verify them.
- `fact_inference_assumption_labels`: labeled statements so claims are not blurred together.
- `open_questions`: questions that must be answered before argument or slide work can proceed confidently.

Use this compact format:

```markdown
## Insight Artifact
- Plain-language explanation:
- Concept map:
- Assumptions ledger:
- Fact / inference / assumption labels:
- Open questions:
- User confirmation needed:
```

## Workflow

1. Restate the user's view using their terms first, then simplify only after preserving meaning.
2. Extract key concepts, actors, forces, metrics, tradeoffs, and tensions.
3. Build a compact concept map in text using arrows or grouped bullets.
4. Label each important statement as `fact`, `inference`, or `assumption`.
5. Create an assumptions ledger for claims that carry persuasive or factual risk.
6. Compare the emerging insight against the intent brief: ask whether it helps move the primary audience from current state to desired change.
7. Ask targeted questions where the user's view is missing, not where the model merely wants more detail.
8. Return the artifact and ask the user to correct it before argument spine work.

## Evaluation Checks

- The explanation sounds like the user's view, not a generic industry summary.
- The concept map shows relationships, not just a list of topics.
- Facts, inferences, and assumptions are visibly separated.
- Risky assumptions are named before they become unsupported claims.
- Open questions are few, consequential, and tied to the presentation outcome.
- The artifact gives the user something concrete to agree with, reject, or refine.

## Failure Modes

- Filling gaps with plausible model knowledge instead of asking or labeling assumptions.
- Flattening a nuanced view into a slogan.
- Treating all source material as equally true, relevant, or audience-ready.
- Hiding uncertainty inside polished prose.
- Creating a concept map that is only a table of contents.
- Moving to argument structure before the user has approved the underlying view.

## Handoff

Handoff an approved `Insight Artifact` to `argument-spine-builder`. Include the labeled facts, inferences, assumptions, and open questions so the argument spine can distinguish claims that are ready from claims that need evidence or user confirmation.
