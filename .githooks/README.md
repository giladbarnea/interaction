# The pre-commit hook keeps generated packages current

`plugins/interaction` is the canonical plugin. The tracked `pi/skills` tree and the Pi archive are generated from it.

## Each commit rebuilds the distributions

`.githooks/pre-commit` runs [`build-plugins.sh`](../build-plugins.sh). The build:

1. Copies every canonical skill into a temporary Pi layout.
2. Runs [`package-pi-skill-globals.py`](../package-pi-skill-globals.py).
3. Replaces the tracked `pi/skills` tree with the generated Pi layout.
4. Copies the root `LICENSE` into the Claude and Codex plugin.
5. Creates the ignored `interaction-pi-skills.zip` archive with stable timestamps.

The hook stages `pi/skills` and `plugins/interaction/LICENSE`. It does not stage source edits or the ignored archive.

## Pi receives only the plugin-global files each skill needs

Pi installs sibling skills without the `interaction` plugin root. A Pi skill cannot use a link that climbs from its skill directory into that missing root.

The packager resolves relative Markdown links and relative `@path` references. When a reference targets a file inside `plugins/interaction` but outside `skills`, the packager:

1. Copies that file into the generated skill at the same plugin-relative path.
2. Rewrites the reference to the generated location.
3. Follows plugin-global references from packaged Markdown files and packages them too.

The scanner ignores Markdown link syntax inside fenced code blocks. It scans relative `@path` references everywhere, including code blocks. Absolute paths and external URLs remain unchanged.

## Broken package graphs block the commit

The build fails when a recognized relative target is missing, escapes the plugin, or collides with a skill-owned path. It also verifies all recognized generated local links before updating tracked files.

Run the checks directly with:

```bash
python3 -m unittest test_package_pi_skill_globals.py
./build-plugins.sh
```

## A clone must activate the versioned hook

Git does not activate repository hooks from the working tree automatically. Run this once after cloning:

```bash
git config core.hooksPath .githooks
```
