---
name: delivery-coach
description: Use when a presentation, talk, pitch, demo, or deck needs timing, transitions, pacing, speaker notes, rehearsal guidance, Q&A preparation, or presenter readiness.
---

# Delivery Coach

Prepare the presentation to be delivered by a real person in a real setting. Coach timing, transitions, pacing, written delivery, visual delivery, verbal delivery, Q&A, and rehearsal without defaulting to a brittle full script.

## Inputs

- Draft deck, outline, talk track, speaker notes, delivery constraints, audience, venue, format, duration, and speaker comfort level.
- Approved intent, insight, argument spine, slide thesis map, critique backlog, evidence dossier, and design guidance when available.
- Required language, demo moments, handoffs, Q&A format, and rehearsal deadline.

## Outputs

- `delivery_plan`: timing map, section pace, slide pace, transition cues, emphasis plan, and required pauses.
- `speaker_notes_guidance`: concise cue notes, signposts, proof reminders, examples, and caution points.
- `written_delivery_guidance`: clearer phrasing, transitions, note structure, handout language, and takeaway wording.
- `visual_delivery_guidance`: where to look, reveal, point, annotate, pause, or let a visual carry the message.
- `verbal_delivery_guidance`: emphasis, cadence, pause, volume, simplification, and recovery moves.
- `qa_plan`: likely questions, concise answers, bridges, evidence backups, and boundaries.
- `rehearsal_plan`: practice sequence, timing checkpoints, retest criteria, and final readiness checks.

## Workflow

1. Confirm audience, medium, duration, stakes, and success criteria before coaching delivery.
2. Build a timing map across sections and slides; reserve time for setup, transitions, examples, pauses, Q&A, and close.
3. Tune written delivery through compact cue notes and transition language; avoid writing a full script unless the user explicitly needs one.
4. Tune visual delivery by deciding when the speaker should introduce, point to, reveal, annotate, or stay silent for a visual.
5. Tune verbal delivery by assigning emphasis, cadence, simplification, pause points, and recovery language for dense or risky moments.
6. Align pacing across written notes, visual complexity, and spoken explanation so the audience can keep up.
7. Prepare Q&A with expected objections, backup evidence, bridge phrases, and answers that do not overclaim.
8. Create a rehearsal plan with timed runs, stumble points, retest checks, and revisions after each run.
9. Route back to critique, distillation, design, evidence, or deck compilation if delivery problems expose content or slide defects.

## Evaluation Checks

- The timing plan fits the required duration with realistic pauses and Q&A.
- Transitions make the argument sequence easier to follow.
- Written notes support delivery without becoming a brittle script by default.
- Visual guidance reduces competition between reading, looking, and listening.
- Verbal guidance improves pace, emphasis, clarity, and recovery under pressure.
- Q&A preparation covers likely objections, evidence backups, and boundaries.
- Rehearsal checks produce actionable revisions, not just practice volume.

## Failure Modes

- Writing a word-for-word script when cue notes, beats, or transitions would be more robust.
- Optimizing spoken flow while ignoring slide density, visual timing, or written notes.
- Leaving no time for silence, transitions, audience processing, or Q&A.
- Coaching performance style without preserving the approved intent and argument.
- Creating Q&A answers that invent support, overclaim, or contradict evidence.
- Treating rehearsal as repetition without timed checkpoints or revision triggers.

## Next Route

- If delivery practice exposes argument, evidence, slide density, design, or deck defects: route to the earliest affected upstream skill rather than masking the problem with speaker coaching.
- If the user needs another review loop after rehearsal: load `critique-iterator`.
- If delivery changes require deck edits while preserving approved strategy: load `deck-compiler`.
- If the delivery plan, Q&A plan, and rehearsal plan are stable: hand off to the presenter for timed rehearsal and user review.
- This artifact feeds the whole presentation by making the approved deck deliverable in a real room, with timing, transitions, Q&A boundaries, and rehearsal checks tied back to the intended audience change.

## Handoff

Handoff the `delivery_plan`, speaker notes guidance, Q&A plan, and rehearsal plan to the presenter, user review, or `critique-iterator` for another loop. Send unresolved slide density, evidence, design, or argument problems back to the relevant upstream skill before final rehearsal.
