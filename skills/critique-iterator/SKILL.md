---
name: critique-iterator
description: Use when a presentation, outline, deck, rehearsal, rubric, or stakeholder review has feedback that must become prioritized revisions instead of taste-driven edits.
---

# Critique Iterator

Convert feedback into a ranked revision backlog. Treat critique as evidence about audience risk, not as a vote on preferences.

## Inputs

- Draft deck, outline, talk track, speaker notes, rehearsal notes, review comments, rubric scores, or stakeholder feedback.
- Approved intent, insight, argument spine, slide thesis map, evidence dossier, design guidance, delivery constraints, and success criteria when available.
- Audience, setting, duration, decision need, and required standards.
- Prior critique backlog and delta report when running another review loop.

## Outputs

- `severity_ranked_issues`: ordered issues with risk type, affected slide or section, evidence, severity, and owner when useful.
- `root_causes`: underlying causes such as unclear thesis, weak proof, broken sequence, overload, inaccessible design, or delivery mismatch.
- `concrete_fixes`: specific revisions that preserve approved artifacts or route upstream when they cannot.
- `retest_plan`: rubric checks, audience tests, rehearsal checks, and acceptance criteria for the next loop.
- `delta_report`: what changed since the prior version, what improved, what regressed, and what remains unresolved.

## Workflow

1. Normalize all feedback into observable audience risks before ranking it.
2. Classify each issue as comprehension, credibility, action, design, or delivery risk; label mere taste separately and do not let it outrank material risk.
3. Compare feedback against the approved intent, insight, argument spine, slide thesis map, evidence, and delivery constraints.
4. Identify root causes instead of only restating symptoms.
5. Rank by severity, audience impact, likelihood, dependency order, and effort only after impact is clear.
6. Propose concrete fixes that name the affected artifact, slide, note, transition, visual, or delivery behavior.
7. Support rubric-driven review loops by mapping issues to rubric dimensions, score changes, acceptance criteria, and retest actions.
8. Produce a delta report for repeat reviews; separate fixed, improved, unchanged, new, and regressed items.
9. Route upstream when a fix would change approved intent, insight, argument spine, slide thesis map, or evidence claims.

## Evaluation Checks

- Every high-severity issue maps to an audience risk, not a personal preference.
- Comprehension, credibility, action, design, and delivery risks are distinguished from taste comments.
- Root causes explain why the issue exists.
- Fixes are specific enough for a deck, content, evidence, design, or delivery pass to execute.
- The retest plan names what to check, how to check it, and what counts as resolved.
- The delta report shows progress and regressions across review loops.

## Failure Modes

- Treating the loudest stakeholder comment as the highest-severity issue.
- Rewriting approved strategy instead of routing upstream.
- Recording taste, tone, or visual preference without tying it to audience risk.
- Producing vague fixes such as "make clearer" or "improve design."
- Skipping root cause analysis and creating patchwork edits.
- Running rubric loops without tracking score deltas, acceptance criteria, or retest evidence.

## Handoff

Handoff the `critique_backlog`, root causes, fixes, retest plan, and delta report to `content-distiller`, `cognitive-designer`, `visual-reasoner`, `evidence-curator`, `deck-compiler`, or `delivery-coach`. Mark upstream strategy, thesis, evidence, or intent problems as upstream work rather than local revision tasks.
