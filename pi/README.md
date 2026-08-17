# Pi needs self-contained skills

Claude and Codex preserve the `interaction` plugin root. Their skills can read the shared plugin reference through a plugin-relative path.

Pi discovers each skill directly under `~/.pi/agent/skills`. The plugin root does not exist there. This distribution copies `theory-of-mind.md` into each dependent skill and uses skill-relative links.

The Pi archive contains these four skill directories:

- `ai-to-ai`
- `ai-to-human`
- `handoff`
- `peer-review`

Download the latest [`interaction-pi-skills.zip`](https://github.com/giladbarnea/interaction/releases/latest/download/interaction-pi-skills.zip), then run:

```bash
mkdir -p ~/.pi/agent/skills
unzip interaction-pi-skills.zip -d ~/.pi/agent/skills
```
