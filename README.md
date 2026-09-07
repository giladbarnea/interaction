# Interaction

![Late-shift desk with a terminal showing trusted AI delegation](assets/interaction-banner.png)

> **Communication toolkit for burnt-out humans and collaborative AI's.**

[![Release](https://img.shields.io/github/v/release/giladbarnea/interaction?style=flat-square&color=111111&label=release)](https://github.com/giladbarnea/interaction/releases/latest)
![Works with Claude Code, Codex, and Pi](https://img.shields.io/badge/works%20with-Claude%20Code%20%7C%20Codex%20%7C%20Pi-111111?style=flat-square)
[![MIT license](https://img.shields.io/badge/license-MIT-111111?style=flat-square)](LICENSE)

## Five skills keep the work usable

- **`theory-of-mind`** restores common ground with readers whose context differs from yours.
- **`ai-to-leader`** makes answers to your leader — human or AI — clear and simple.
- **`ai-to-delegated`** makes delegation and collaboration work.
- **`handoff`** carries decisions, tacit knowledge and "why" into the next session.
- **`peer-review`** collapses complexity like tetris blocks.

**When nobody can understand it, delegate it, resume it, or review it, it's not working.**

## Pleasant to the brain

`ai-to-leader`: 
- uses ASD-STE-100, plain language and stable names.
- assumes the human has one brain, and is juggling work, family, and a dozen unfinished AI projects.
- teaches sub-agents how to manage up their main.
- teaches signal vs noise: what to surface to your leader and what to solve without making a fuss.

## Delegation that doesn't suck

`ai-to-delegated`:
- makes AI delegate, not micro manage.
- teaches trust, avoiding biasing your directs, and how to scope parallel work effectively.

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

**`ai-to-leader`:**

```
# User:

  /ai-to-leader i have had a long day. what are you talking about


# Assistant:
  
  We've been designing a plugin that makes AI's effective communicators.

  It packages five skills: `theory-of-mind`, `ai-to-leader`, `ai-to-delegated`, `handoff`, and `peer-review`.

  `theory-of-mind` provides the shared foundation. The other four skills cover reporting, delegation, handoffs, and reviews.

  The plugin is almost ready for release. I only need your decision on how to package it for Pi, since Pi does not support plugins natively.
  
  I can either package it as a single `interaction` skill, or as five separate skills. Which do you prefer?
```

**`ai-to-delegated`:**
```
# User:

  study the plan and implement it. delegate work.

# Assistant:

  [loaded skill: `ai-to-delegated`]

  I’ll assign research, implementation and review to separate sub-agents. This will prevent biasing the process.

  I will only surface issues that need your attention. Finally, I will plainly summarize the end result.

  Go take a break. We’ll manage.
```

## Only Markdown

`interaction` has no MCP server, executable code, network calls, hooks, or background process. Your laptop can remain disappointed by the missing daemon.

Pi installs five sibling skills without a plugin root. Install the full set: dependent skills load `theory-of-mind` by name rather than carrying reference copies. See [`pi/README.md`](pi/README.md) for the layout.

## Develop from one source

`plugins/interaction` is the canonical content. `./build-plugins.sh` generates tracked `pi/skills` and ignored `interaction-pi-skills.zip`.

The build also copies the root `LICENSE` into the plugin. The `.githooks/pre-commit` hook runs the build and stages generated tracked files.

## Release from a version tag

Pushing a `vMAJOR.MINOR.PATCH` tag starts the [release workflow](.github/workflows/release.yml).

1. Set the same version in `plugins/interaction/.claude-plugin/plugin.json` and `plugins/interaction/.codex-plugin/plugin.json`.
2. Run `./build-plugins.sh`.
3. Commit the source, manifests, workflow, and generated files. Push the commit.
4. Create and push the matching tag. For version `1.1.0`:

   ```bash
   git tag -a v1.1.0 -m "Interaction v1.1.0"
   git push origin v1.1.0
   ```

CI checks that both manifest versions match the tag and that generated files are current. It then publishes **Interaction v1.1.0**, with generated release notes and `interaction-pi-skills.zip` attached.

The workflow uses GitHub's built-in token. No extra secret is required. Branch pushes alone do not publish releases.

## License

[MIT](LICENSE).
