# Interaction

![Late-shift desk with a terminal showing trusted AI delegation](assets/interaction-banner.png)

> **Communication toolkit for burnt-out humans and collaborative AI's.**

[![Release](https://img.shields.io/github/v/release/giladbarnea/interaction?style=flat-square&color=111111&label=release)](https://github.com/giladbarnea/interaction/releases/latest)
![Works with Claude Code, Codex, and Pi](https://img.shields.io/badge/works%20with-Claude%20Code%20%7C%20Codex%20%7C%20Pi-111111?style=flat-square)
[![MIT license](https://img.shields.io/badge/license-MIT-111111?style=flat-square)](LICENSE)

## Four skills keep the work usable

- **`ai-to-human`** makes answers clear and simple.
- **`ai-to-ai`** makes delegation and collaboration work.
- **`handoff`** carries decisions, tacit knowledge and "why" into the next session.
- **`peer-review`** collapses complexity like tetris blocks.

**When nobody can understand it, delegate it, resume it, or review it, it's not working.**

## Pleasant to the brain

`ai-to-human`: 
- uses ASD-STE-100, plain language and stable names.
- assumes the human has one brain, and is juggling work, family, and a dozen unfinished AI projects.

## Delegation that doesn't suck

`ai-to-ai`:
- makes AI delegate, not micro manage.
- teaches trust, avoiding biasing your directs, and how to scope parallel work effectively.
- teaches sub-agents how to manage up their main.
- teaches main signal vs noise: what to surface to the human and what to solve without making a fuss.

## Handoffs that preserve judgment

`handoff`:
- captures intent, pitfalls, decisions and the rationale behind them.
- leads the next agent from a fresh spawn to a fully onboarded replacement.

## Reviews that simplify

`peer-review`:
- studies the work with a fresh set of eyes and a wide look.
- reports proven issues.
- points out opportunities to collapse complexity, remove code, and gain elegance.

## Install

### Claude Code

```text
/plugin marketplace add giladbarnea/interaction
/plugin install interaction@interaction
```

### Codex

```bash
codex plugin marketplace add giladbarnea/interaction
codex plugin add interaction@interaction
```

### Pi

Download [`interaction-pi-skills.zip`](https://github.com/giladbarnea/interaction/releases/latest/download/interaction-pi-skills.zip), then run:

```bash
mkdir -p ~/.pi/agent/skills
unzip interaction-pi-skills.zip -d ~/.pi/agent/skills
```

Start a new Pi session after installation.

## Usage examples

**`ai-to-user`:**

```
# User:

  /ai-to-human i have had a long day. what are you talking about


# Assistant:
  
  We've been designing a plugin that makes AI's effective communicators.

  It packages four skills: `ai-to-human`, `ai-to-ai`, `handoff`, and `peer-review`.

  The four skills map cleanly to four critical interaction needs: clarity, delegation, continuity, and quality.

  The plugin is almost ready for release. I only need your decision on how to package it for Pi, since Pi does not support plugins natively.
  
  I can either package it as a single `interaction` skill, or as four separate skills. Which do you prefer?
```

**`ai-to-ai`:**
```
# User:

  study the plan and implement it. delegate work.

# Assistant:

  [loaded skill: `ai-to-ai`]

  I’ll assign research, implementation and review to separate sub-agents. This will prevent biasing the process.

  I will only surface issues that need your attention. Finally, I will plainly summarize the end result.

  Go take a break. We’ll manage.
```

## Only Markdown

`interaction` has no MCP server, executable code, network calls, hooks, or background process. Your laptop can remain disappointed by the missing daemon.

Pi installs each skill separately, because Pi does not support plugins natively. Its release contains self-contained references. See [`pi/README.md`](pi/README.md) for the layout.

## Develop from one source

`plugins/interaction` is the canonical content. `./build-plugins.sh` generates tracked `pi/skills` and ignored `interaction-pi-skills.zip`.

The build also copies the root `LICENSE` into the plugin. The `.githooks/pre-commit` hook runs the build and stages generated tracked files.

## License

[MIT](LICENSE).
