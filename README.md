# Interaction

Communication toolkit for burnt-out humans and collaborative AI's.

## For Claude Code, run

```text
/plugin marketplace add giladbarnea/interaction
/plugin install interaction@interaction
```

## For Codex, run

```bash
codex plugin marketplace add giladbarnea/interaction
codex plugin add interaction@interaction
```

## For Pi

Download [`interaction-pi-skills.zip`](https://github.com/giladbarnea/interaction/releases/latest/download/interaction-pi-skills.zip), then run:

```bash
mkdir -p ~/.pi/agent/skills
unzip interaction-pi-skills.zip -d ~/.pi/agent/skills
```

Start a new Pi session after installation.

Pi installs the package as four separate skills:

- `ai-to-ai`
- `ai-to-human`
- `handoff`
- `peer-review`

See [`pi/README.md`](pi/README.md) for the flattened Pi layout.
