# Pi installs skills without a plugin root

Claude and Codex preserve the `interaction` plugin root. Their skills can read the shared plugin reference through a plugin-relative path.

Pi discovers each skill directly under `~/.pi/agent/skills`. The plugin root does not exist there. This distribution copies the shared reference `roles.md` into dependent skills and rewrites plugin-reference paths.

`theory-of-mind` is a standalone skill. Other skills load it by name, so install the full set together.

The Pi archive contains these five skill directories:

- `ai-to-leader`
- `ai-to-delegated`
- `handoff`
- `peer-review`
- `theory-of-mind`

Download the latest [`interaction-pi-skills.zip`](https://github.com/giladbarnea/interaction/releases/latest/download/interaction-pi-skills.zip), then run:

```bash
mkdir -p ~/.pi/agent/skills
unzip interaction-pi-skills.zip -d ~/.pi/agent/skills
```
