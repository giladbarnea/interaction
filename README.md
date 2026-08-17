# Interaction

![Late-shift desk with a terminal showing trusted AI delegation](assets/interaction-banner.png)

**Communication toolkit for burnt-out humans and collaborative AI's.**

[![Release](https://img.shields.io/github/v/release/giladbarnea/interaction?style=flat-square&color=111111&label=release)](https://github.com/giladbarnea/interaction/releases/latest)
![Works with Claude Code, Codex, and Pi](https://img.shields.io/badge/works%20with-Claude%20Code%20%7C%20Codex%20%7C%20Pi-111111?style=flat-square)
[![MIT license](https://img.shields.io/badge/license-MIT-111111?style=flat-square)](LICENSE)

## Four skills keep the work usable

- **`ai-to-human`** makes answers clear and simple.
- **`ai-to-ai`** makes delegation and collaboration work.
- **`handoff`** carries decisions, tacit knowledge and “why” into the next session.
- **`peer-review`** collapses complexity like tetris blocks.

**When nobody can explain it, delegate it, resume it, or review it, it's not working.**

## Context should survive context switching

`ai-to-human` uses ASD-STE-100, plain language and stable names. It assumes the human has one brain, and is juggling work, family, and a dozen unfinished AI projects.

## Delegation should reduce work

`ai-to-ai` helps agents choose between subagents and teams. It gives delegates enough context without scripting their every move.

## Handoffs should preserve judgment

`handoff` captures state, decisions, failed paths, and necessary next steps. A transcript dump is not a handoff, even when it is impressively long.

## Reviews should earn attention

`peer-review` studies the requirements and blast radius first. It reports consequential bugs, missed constraints, complexity, and scope drift.

## Install all four skills

Three hosts, three installation paths. Standardization had other plans.

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

## Ask for a skill directly

```text
Load ai-to-human and bring me back into the project.
Load ai-to-ai before delegating this research.
Use handoff to prepare the next session.
Use peer-review to review the completed work.
```

The host can also load a skill when its description matches the task.

## Only Markdown, no mystery

Interaction has no MCP server, executable code, network calls, hooks, or background process. Your laptop can remain disappointed by the missing daemon.

Pi installs each skill separately, so its release contains self-contained references. See [`pi/README.md`](pi/README.md) for the layout.

## Develop from one source

`plugins/interaction` is the canonical content. `./build-plugins.sh` generates tracked `pi/skills` and ignored `interaction-pi-skills.zip`.

The build also copies the root `LICENSE` into the plugin. The `.githooks/pre-commit` hook runs the build and stages generated tracked files.

## License

[MIT](LICENSE). Use it, change it, and share it.
