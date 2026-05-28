# Biolytics Rhetoric Engine

Biolytics Rhetoric Engine is an installable agent skill package for creating better presentations through a staged cognition pipeline.

It helps an agent work with the presenter before, during, and after deck assembly: clarifying intent, surfacing insight, building an argument spine, mapping slide theses, reasoning about audience cognition, curating evidence, distilling content, compiling an editable deck, iterating critique, and preparing delivery.

## Not a One-Shot Deck Generator

Rhetoric Engine is not a prompt-to-deck shortcut. It is designed for user-led presentation creation where the important work is thinking, framing, selecting, sequencing, and revising.

One-shot generators tend to produce plausible generic decks from a topic. Rhetoric Engine instead treats a deck as the result of a staged rhetorical process: the user owns the point of view, the agent helps externalize and pressure-test it, and the final artifact emerges from explicit choices.

## Install Shape

Install one plugin, get many stage skills.

The package includes install metadata for:

- OpenAI Codex plugin consumers: `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json`
- Anthropic Claude Code plugin consumers: `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`
- Google Gemini CLI extension consumers: `gemini-extension.json` and `GEMINI.md`
- Generic agent consumers: `AGENTS.md` and the `skills/` directory

For step-by-step setup, see [INSTALL.md](INSTALL.md).

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

## Quick Start

For ChatGPT web, ChatGPT Agent Studio, or Claude web, download the latest web skill artifact:

- [Download `rhetoric-engine.skill`](https://github.com/Biolytics-AI/rhetoric-engine/releases/latest/download/rhetoric-engine.skill) for ChatGPT web and ChatGPT Agent Studio.
- [Download `rhetoric-engine-chatgpt.zip`](https://github.com/Biolytics-AI/rhetoric-engine/releases/latest/download/rhetoric-engine-chatgpt.zip) as a ChatGPT zip fallback.
- [Download `rhetoric-engine-claude.zip`](https://github.com/Biolytics-AI/rhetoric-engine/releases/latest/download/rhetoric-engine-claude.zip) for Claude web.

For coding agents, install from the GitHub repo:

```bash
git clone https://github.com/Biolytics-AI/rhetoric-engine.git
```

Then install it for your agent platform using [INSTALL.md](INSTALL.md). When in doubt, start by invoking `rhetorical-orchestrator`; it coordinates the gated workflow and routes to the right stage skill.

## Web Install

### ChatGPT Web Skills

1. Download [`rhetoric-engine.skill`](https://github.com/Biolytics-AI/rhetoric-engine/releases/latest/download/rhetoric-engine.skill).
2. Open ChatGPT.
3. Open your profile menu, then `Skills`.
4. Click `New skill`.
5. Upload the downloaded `.skill` file.

![ChatGPT Skills upload](docs/assets/screenshots/chatgpt-skills-upload.png)

### ChatGPT Agent Studio

1. Download [`rhetoric-engine.skill`](https://github.com/Biolytics-AI/rhetoric-engine/releases/latest/download/rhetoric-engine.skill).
2. Open the agent in ChatGPT Agent Studio.
3. Click `Add skill`.
4. Choose `Upload skill`.
5. Upload the downloaded `.skill` file.

![ChatGPT Agent Studio add skill](docs/assets/screenshots/chatgpt-agent-add-skill.png)

### Claude Web

1. Download [`rhetoric-engine-claude.zip`](https://github.com/Biolytics-AI/rhetoric-engine/releases/latest/download/rhetoric-engine-claude.zip).
2. Open Claude.
3. Go to `Settings` / `Customize` / `Skills`.
4. Upload the downloaded zip file.

![Claude Skills upload](docs/assets/screenshots/claude-skills-upload.png)

## Core Rule

Do not compile slides before the user has approved:

- intent
- insight
- argument spine
- slide thesis map

Rhetoric Engine exists to help the user communicate their view, not the model's generic version of it.
