# Rhetoric Engine

Rhetoric Engine is a staged presentation cognition pipeline for turning user intent, insight, argument, evidence, design choices, and delivery constraints into effective slide decks.

It helps a skill-aware agent work with the presenter before, during, and after deck assembly: clarifying what the deck is for, surfacing the actual argument, shaping slide-level theses, reasoning about audience cognition, curating evidence, compiling the deck, tightening content, iterating critique, and preparing delivery.

## Not a One-Shot Deck Generator

Rhetoric Engine is not a prompt-to-deck shortcut. It is designed for user-led presentation creation where the important work is thinking, framing, selecting, sequencing, and revising.

One-shot generators tend to produce plausible generic decks from a topic. Rhetoric Engine instead treats a deck as the result of a staged rhetorical process: the user owns the point of view, the agent helps externalize and pressure-test it, and the final artifact emerges from explicit choices.

## Install Shape

Rhetoric Engine is one plugin containing many skills. Install the plugin once, then invoke the individual skills as needed, or start from the bootstrap skill when you want the agent to coordinate the gated workflow.

## Skills

### Bootstrap

- `rhetorical-orchestrator`

### Phase 1: Intent, Insight, Argument

- `intent-framer`
- `insight-externalizer`
- `argument-spine-builder`
- `slide-thesis-mapper`

### Phase 2: Cognition, Visuals, Evidence

- `cognitive-designer`
- `visual-reasoner`
- `evidence-curator`

### Phase 3: Distillation and Compilation

- `content-distiller`
- `deck-compiler`

### Phase 4: Critique and Delivery

- `critique-iterator`
- `delivery-coach`

## Local Install

For Codex-style or Claude-style skill consumers, install this repository as a local plugin directory:

1. Clone or copy the repository to a stable local path.
2. Point your skill consumer at the plugin root directory.
3. Confirm the consumer can read the plugin manifest and the `skills/` directory.
4. Invoke `rhetorical-orchestrator` to coordinate the gated workflow, or invoke an individual skill by name for a specific phase.

The plugin root contains both Codex and Claude plugin metadata, with all skill definitions under `skills/`.
