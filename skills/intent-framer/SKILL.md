---
name: intent-framer
description: Use when a presentation, talk, memo-to-deck, or slide request has unclear intent, audience, outcome, stakes, constraints, or success criteria, before argument construction or deck work begins.
---

# Intent Framer

Transform a rough presentation topic into a user-owned intent brief. Use this before argument, outline, design, rendering, or deck compilation whenever the audience, desired change, or success test is unclear.

Keep the user's purpose primary. Do not make a generic communication plan when the user needs a specific audience outcome.

Default to elicitation, not drafting. The goal is to help the user discover and sharpen their view, not to get them to approve the agent's inferred view.

## Inputs

- Rough topic, prompt, notes, meeting context, or existing deck request.
- Known audience, venue, format, timing, and decision context.
- User constraints such as duration, politics, brand rules, required content, source limits, or tone.
- Any stated fears, objections, desired reactions, or non-goals.

## Outputs

Default output is an `Intent Exploration` until the readiness checks pass.

Return an `Intent Exploration` with:

- `what_user_has_said`: only the intent facts the user supplied or selected.
- `candidate_frames`: 2-4 abstract hypotheses the user can react to, not concrete claims disguised as assumptions.
- `activating_questions`: the next 1-3 questions that would most improve the user's own thinking.
- `zoom_out_option`: a way to step back if the candidate frames feel wrong.
- `next_decision`: the smallest decision needed before drafting a brief.

Use this compact format:

```markdown
## Intent Exploration
- What you have said:
- Candidate frames:
- Activating questions:
- Zoom-out option:
- Next decision:
```

Return an `Intent Brief` only when the user has supplied, selected, or explicitly accepted enough substance for the fields below:

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

1. Reflect only what the user actually said. Distinguish supplied facts from possible interpretations.
2. Ask 1-3 activating questions that help the user think, not just fill fields. Good questions expose audience tension, desired movement, tradeoffs, stakes, or what the talk must not become.
3. Offer 2-4 candidate frames only as low-commitment hypotheses. Keep them abstract enough to invite correction. Do not make them sound like the user's position.
4. Always include a zoom-out option, for example: "None of these; help me step back and name the conversation this deck should create."
5. Iterate from broad to specific. If the user's answers are still forming, produce another `Intent Exploration` instead of an `Intent Brief`.
6. Convert vague goals into a desired change only after the user has supplied or selected the direction: `from [current state] to [desired state]`.
7. Draft a success test that can be observed after the talk, but keep it provisional until the user accepts it.
8. Present an `Intent Brief` for approval only after the readiness checks pass.

## Readiness Checks

Before writing an `Intent Brief`, verify:

- The primary audience is specific enough to predict questions and resistance.
- The desired change is stated or chosen by the user, not invented by the agent.
- The current state has a user-provided signal, evidence source, or is explicitly marked open.
- Stakes and success test have at least been sketched by the user.
- Constraints and non-goals are known enough to prevent obvious scope errors.

If any check fails, return an `Intent Exploration`, not an `Intent Brief`.

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
- Producing a polished intent brief after sparse answers.
- Leading the witness: making the agent's assumptions concrete enough that the user can only approve or correct them.
- Asking only confirmation questions instead of activating questions.
- Jumping to slide titles, visuals, or narrative structure too early.
- Inventing audience beliefs when the user has not supplied them.
- Inventing stakes, objections, regulatory framing, or organizational politics from domain knowledge alone.
- Optimizing for polish instead of the desired audience change.
- Ignoring political, time, source, or approval constraints.

## Handoff

Handoff an approved `Intent Brief` to `insight-externalizer` as the normal next step. An `Intent Exploration` is not approval and does not satisfy the intent gate. Proceed beyond `insight-externalizer` only when the user has explicitly supplied an already-approved insight artifact equivalent to the required insight outputs. Do not skip the insight gate merely because the idea seems clear. Mark downstream artifacts stale if the audience, desired change, stakes, constraints, or insight changes.
