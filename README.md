# Interaction

**Communication toolkit for burnt-out humans and collaborative AI's.**

A technically correct answer can still be difficult to use. The user returns after two days and cannot retrieve the latest thread. An agent delegates work but spends more context managing delegates than doing the work. A handoff records activity but loses the decisions that matter. A review produces many observations but no useful signal.

Interaction packages four Markdown skills for these ordinary failure modes. They help agents communicate clearly, delegate with purpose, preserve context across sessions, and review work without creating noise.

## Good work must survive context switching

`ai-to-human` treats communication as part of the work. It favors short common words, stable names, active voice, and sentences that carry one idea. When recent context has gone cold, it re-establishes the wider situation, the motivation, and the latest progress before returning to detail.

This is not only a writing style. It reduces the cost of returning to a project after switching between several sessions.

## Delegation should create headroom

`ai-to-ai` explains when delegation saves context and when it only adds management overhead. It distinguishes isolated subagents from collaborating teams, and it favors prompts that provide the goal and necessary context without prescribing the implementation.

Its references cover delegation shapes, team roles, context management, and communication between agents with different knowledge.

## A handoff should transfer judgment

`handoff` writes a cold-entry continuation brief for a fresh session. It preserves the current state, decisions, failed approaches, important discoveries, and necessary next steps. It references existing artifacts instead of copying them into a second source of truth.

## Peer review should find material problems

`peer-review` asks a reviewer to understand the requirements and the full blast radius before judging completed work. It sets a high reporting threshold, so the review focuses on consequential bugs, missed constraints, unnecessary complexity, and scope drift.

## Install all four skills together

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

## The skills remain distinct

The package installs four skills:

| Skill | Use it for |
|---|---|
| `ai-to-human` | Clear user communication and context re-grounding |
| `ai-to-ai` | Delegation, subagents, agent teams, and AI-facing documents |
| `handoff` | Continuation briefs for a fresh session |
| `peer-review` | Focused review of completed work |

The host can load a skill when its description matches the task. You can also ask directly:

```text
Load ai-to-ai before delegating this research.
Load ai-to-human and bring me back into the project.
Use handoff to prepare the next session.
Use peer-review to review the completed work.
```

## Nothing runs in the background

Interaction contains Markdown instructions and references. It has no MCP server, executable code, network calls, lifecycle hooks, or background process.

Claude and Codex preserve the shared plugin layout. Pi installs each skill separately, so the Pi release copies shared references into each dependent skill. See [`pi/README.md`](pi/README.md) for that layout.
