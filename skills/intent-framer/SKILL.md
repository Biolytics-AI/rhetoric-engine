---
name: intent-framer
description: Use when a presentation, talk, memo-to-deck, or slide request has unclear intent, audience, outcome, stakes, constraints, or success criteria, before argument construction or deck work begins.
---

# Intent Framer

Transform a rough presentation topic into an intent brief. Use this before argument, outline, design, rendering, or deck compilation whenever the audience, desired change, or success test is unclear.

Keep the user's purpose primary. Do not make a generic communication plan when the user needs a specific audience outcome.

## Inputs

- Rough topic, prompt, notes, meeting context, or existing deck request.
- Known audience, venue, format, timing, and decision context.
- User constraints such as duration, politics, brand rules, required content, source limits, or tone.
- Any stated fears, objections, desired reactions, or non-goals.

## Outputs

Return an `Intent Brief` with:

- `primary_audience`: the real decision-maker or learner, not a vague demographic.
- `current_state`: what the audience currently believes, knows, feels, or does.
- `desired_change`: what should be different after the presentation.
- `stakes`: why the change matters now.
- `success_test`: observable evidence that the presentation worked.
- `constraints`: time, medium, politics, brand, data, compliance, or production limits.
- `objections`: likely resistance, doubts, risks, or hidden agendas.
- `non_goals`: what the presentation must not try to do.

Use this compact format:

```markdown
## Intent Brief
- Primary audience:
- Current state:
- Desired change:
- Stakes:
- Success test:
- Constraints:
- Objections:
- Non-goals:
```

## Workflow

1. Restate the topic as a communication situation: speaker, audience, moment, and desired movement.
2. Identify missing intent fields. Ask the fewest questions needed to avoid guessing; if the user wants speed, mark assumptions explicitly.
3. Separate audience roles: primary audience, secondary audience, approvers, and bystanders.
4. Convert vague goals into a desired change using this form: `from [current state] to [desired state]`.
5. Define stakes in concrete terms: decision, risk, opportunity, cost, trust, alignment, or action.
6. Draft a success test that can be observed after the talk.
7. Name constraints, objections, and non-goals that should shape downstream argument choices.
8. Present the brief for approval before routing to insight or argument work.

## Evaluation Checks

- The audience is specific enough to predict questions and resistance.
- The desired change is behavioral, cognitive, emotional, or decisional, not just "inform."
- The success test is observable and not merely "they liked it."
- Constraints and non-goals prevent scope creep.
- Objections are plausible from the audience's point of view.
- Downstream work could use the brief without asking what the deck is for.

## Failure Modes

- Treating the topic as the intent.
- Naming "everyone" or "stakeholders" as the primary audience.
- Jumping to slide titles, visuals, or narrative structure too early.
- Inventing audience beliefs when the user has not supplied them.
- Optimizing for polish instead of the desired audience change.
- Ignoring political, time, source, or approval constraints.

## Handoff

Handoff an approved `Intent Brief` to `insight-externalizer` as the normal next step. Proceed beyond `insight-externalizer` only when the user has explicitly supplied an already-approved insight artifact equivalent to the required insight outputs. Do not skip the insight gate merely because the idea seems clear. Mark downstream artifacts stale if the audience, desired change, stakes, constraints, or insight changes.
