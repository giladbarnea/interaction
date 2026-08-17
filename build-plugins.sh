#!/usr/bin/env bash

set -euo pipefail

readonly REPOSITORY_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly PLUGIN_DIRECTORY="$REPOSITORY_ROOT/plugins/interaction"
readonly PI_SKILLS_DIRECTORY="$REPOSITORY_ROOT/pi/skills"
readonly PI_ARCHIVE="$REPOSITORY_ROOT/interaction-pi-skills.zip"
readonly ARCHIVE_TIMESTAMP="198001010000"
readonly TEMPORARY_DIRECTORY="$(mktemp -d "${TMPDIR:-/tmp}/interaction-build.XXXXXX")"

trap 'rm -rf "$TEMPORARY_DIRECTORY"' EXIT

fail() {
  printf '✗ %s\n' "$1" >&2
  exit 1
}

for command_name in rsync sed touch zip; do
  command -v "$command_name" >/dev/null 2>&1 || fail "Missing command: $command_name"
done

[[ -d "$PLUGIN_DIRECTORY/skills" ]] || fail "Missing canonical skills directory: $PLUGIN_DIRECTORY/skills"
[[ -d "$PLUGIN_DIRECTORY/references" ]] || fail "Missing canonical references directory: $PLUGIN_DIRECTORY/references"
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

  grep -R -qF '../../references/' "$generated_skill_directory" || continue

  mkdir -p "$generated_skill_directory/references"
  rsync -a "$PLUGIN_DIRECTORY/references"/ "$generated_skill_directory/references"/

  while IFS= read -r markdown_file; do
    grep -qF '../../references/' "$markdown_file" || continue
    relative_markdown_file="${markdown_file#"$generated_skill_directory/"}"
    sed 's#../../references/#references/#g' "$markdown_file" > "$markdown_file.tmp"
    mv "$markdown_file.tmp" "$markdown_file"
    touch -r "${source_skill_directory%/}/$relative_markdown_file" "$markdown_file"
  done < <(find "$generated_skill_directory" -type f -name '*.md' -print)
done

((${#skill_names[@]} > 0)) || fail "No canonical skills found"

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

if grep -R -qF '../../references/' "$PI_SKILLS_DIRECTORY"; then
  fail "Generated Pi skills still contain plugin-root references"
fi

printf '✓ Built Claude/Codex plugin, Pi skills, and %s\n' "$(basename "$PI_ARCHIVE")"
