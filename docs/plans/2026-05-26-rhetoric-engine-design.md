# Rhetoric Engine Design

## Goal

Build `rhetoric-engine` as one installable Claude Code/Codex-style plugin that gives agents a staged presentation cognition pipeline. The plugin should help users communicate their own view, not let the model substitute a plausible deck-shaped answer.

## Package Shape

Use the Superpowers precedent: one installable plugin containing many separate skills.

```text
rhetoric-engine/
├── .codex-plugin/plugin.json
├── .claude-plugin/plugin.json
├── skills/
│   ├── rhetorical-orchestrator/
│   ├── intent-framer/
│   ├── insight-externalizer/
│   ├── argument-spine-builder/
│   ├── slide-thesis-mapper/
│   ├── cognitive-designer/
│   ├── visual-reasoner/
│   ├── evidence-curator/
│   ├── deck-compiler/
│   ├── content-distiller/
│   ├── critique-iterator/
│   └── delivery-coach/
└── research-reports/
```

`rhetorical-orchestrator` is the master bootstrap gatekeeper. Its job is to route the agent to the right stage skill, enforce approval gates, and stop premature deck generation.

## Phases

### Phase 1: Alignment And Structural Spine

`intent-framer` turns a topic into one audience-specific intent: belief shift, decision, approval, action, or durable understanding. It emits an intent brief with audience, stakes, success test, objections, constraints, and non-goals.

`insight-externalizer` turns the user's tacit understanding into inspectable artifacts: plain-language explanation, concept map, assumptions ledger, facts/inferences/assumptions split, and open questions.

`argument-spine-builder` turns the approved intent and insight artifacts into an answer-first argument: core claim, support branches, warrants, evidence needs, and rebuttals.

`slide-thesis-mapper` converts the argument into slide-level audience questions and answer theses. This is the main hard gate before design or rendering.

### Phase 2: Design And Cognitive Modeling

`cognitive-designer` applies multimedia learning, attention, accessibility, reading order, contrast, hierarchy, and slide grammar.

`visual-reasoner` chooses the visual form that helps the audience reason: comparison, process, hierarchy, timeline, map, annotated figure, chart, before/after, or decision tree.

`evidence-curator` builds a claim-evidence matrix, ranks support by credibility and audience legibility, and identifies backup evidence for likely challenges.

### Phase 3: Execution And Compression

`deck-compiler` turns approved slide theses, visual specs, evidence choices, and style constraints into an editable deck spec or deck artifact. It should use whatever slide backend is available: PPTX, Google Slides, HTML slides, Markdown slides, or a local artifact pipeline.

`content-distiller` optimizes signal. It cuts, moves detail to notes, splits overloaded slides, protects the argument from over-cutting, and makes the deck fit the time and attention budget.

### Phase 4: Refinement And Delivery

`critique-iterator` turns reviews, rehearsal feedback, rubric scores, and stakeholder comments into a ranked revision backlog with severity, root cause, fix path, and retest plan.

`delivery-coach` covers written, visual, and verbal delivery: transitions, timing, notes, pacing, emphasis, Q&A setup, and final presenter readiness.

## Core Workflow Contract

The orchestrator should default to a staged pipeline:

1. Frame intent.
2. Externalize insight.
3. Build argument spine.
4. Map slide theses.
5. Model cognition and visuals.
6. Curate evidence.
7. Compile an editable deck.
8. Distill content.
9. Iterate critique.
10. Coach delivery.

The orchestrator may skip stages only when the user supplies an already-approved artifact for that stage or explicitly asks for a narrow operation such as "review this deck" or "make slide 7 clearer."

## Hard Gates

Do not compile slides until these artifacts are explicit enough to review:

- intent brief
- insight artifacts or a clear user-provided substitute
- argument spine
- slide thesis map

Do not perform visual polish before slide theses are stable.

Do not compress content by shortening text alone. Preserve one idea per slide and move nuance into notes or backup slides.

Do not treat critique as taste. Convert feedback into observable comprehension, credibility, action, design, or delivery risks.

## Artifact Model

Each stage should emit a compact Markdown artifact and, when useful, a JSON-compatible structure. The canonical fields should be stable enough for later renderers:

- `intent_brief`
- `insight_model`
- `argument_spine`
- `slide_thesis_map`
- `visual_plan`
- `evidence_matrix`
- `deck_spec`
- `distillation_log`
- `critique_backlog`
- `delivery_plan`

## Tool Philosophy

The plugin must be tool-agnostic. It should work when the agent has access to a filesystem, wiki, Google Drive, Google Slides, PPTX tooling, HTML slide tooling, diagramming tools, or mindmapping tools. Tool-specific instructions belong inside the relevant stage skill as optional routing, not in the package-level architecture.

## Skill Design Rules

Each skill should be concise enough to load often. Put only the stage workflow, inputs, outputs, gates, failure modes, and prompt patterns in each `SKILL.md`. Move long research notes, rubrics, examples, schemas, and backend-specific guidance into `references/` only if needed.

Use imperative instructions. Describe triggers in the YAML `description`, because that is what agents see before loading the skill body.

## Success Criteria

The first shippable version succeeds when:

- Installing one plugin exposes all stage skills.
- The orchestrator reliably prevents premature deck generation.
- Each stage has clear triggers, inputs, outputs, evaluation checks, and failure modes.
- The stage names match the `rhetoric-engine` taxonomy above.
- The package validates as a Codex skill plugin.
- A fresh agent can use the package to turn a vague presentation topic into approved pre-deck artifacts before drafting slides.

