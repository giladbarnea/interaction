#!/usr/bin/env bash

set -euo pipefail

readonly REPOSITORY_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly PLUGIN_DIRECTORY="$REPOSITORY_ROOT/plugins/interaction"
readonly PI_SKILLS_DIRECTORY="$REPOSITORY_ROOT/pi/skills"
readonly PI_ARCHIVE="$REPOSITORY_ROOT/interaction-pi-skills.zip"
readonly GLOBAL_PACKAGER="$REPOSITORY_ROOT/package-pi-skill-globals.py"
readonly ARCHIVE_TIMESTAMP="198001010000"
readonly TEMPORARY_DIRECTORY="$(mktemp -d "${TMPDIR:-/tmp}/interaction-build.XXXXXX")"

trap 'rm -rf "$TEMPORARY_DIRECTORY"' EXIT

fail() {
  printf '✗ %s\n' "$1" >&2
  exit 1
}

for command_name in python3 rsync touch zip; do
  command -v "$command_name" >/dev/null 2>&1 || fail "Missing command: $command_name"
done

[[ -d "$PLUGIN_DIRECTORY/skills" ]] || fail "Missing canonical skills directory: $PLUGIN_DIRECTORY/skills"
[[ -f "$GLOBAL_PACKAGER" ]] || fail "Missing Pi global-file packager: $GLOBAL_PACKAGER"
[[ -f "$REPOSITORY_ROOT/LICENSE" ]] || fail "Missing repository license"

mkdir -p "$TEMPORARY_DIRECTORY/skills"
skill_names=()

for source_skill_directory in "$PLUGIN_DIRECTORY"/skills/*/; do
  [[ -f "$source_skill_directory/SKILL.md" ]] || continue

  skill_name="$(basename "$source_skill_directory")"
  generated_skill_directory="$TEMPORARY_DIRECTORY/skills/$skill_name"
  skill_names+=("$skill_name")

  mkdir -p "$generated_skill_directory"
  rsync -a --delete "$source_skill_directory"/ "$generated_skill_directory"/
done

((${#skill_names[@]} > 0)) || fail "No canonical skills found"

python3 "$GLOBAL_PACKAGER" "$PLUGIN_DIRECTORY" "$TEMPORARY_DIRECTORY/skills"

mkdir -p "$PI_SKILLS_DIRECTORY"
rsync -a --delete "$TEMPORARY_DIRECTORY/skills"/ "$PI_SKILLS_DIRECTORY"/
rsync -a "$REPOSITORY_ROOT/LICENSE" "$PLUGIN_DIRECTORY/LICENSE"

rsync -a "$REPOSITORY_ROOT/LICENSE" "$TEMPORARY_DIRECTORY/skills/LICENSE"
find "$TEMPORARY_DIRECTORY/skills" -exec touch -t "$ARCHIVE_TIMESTAMP" {} +
(
  cd "$TEMPORARY_DIRECTORY/skills"
  zip -q -r -X "$TEMPORARY_DIRECTORY/interaction-pi-skills.zip" "${skill_names[@]}" LICENSE
)
mv "$TEMPORARY_DIRECTORY/interaction-pi-skills.zip" "$PI_ARCHIVE"

printf '✓ Built Claude/Codex plugin, Pi skills, and %s\n' "$(basename "$PI_ARCHIVE")"
