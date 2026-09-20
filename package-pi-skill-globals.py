#!/usr/bin/env python3

from __future__ import annotations

import os
import re
import shutil
import sys
from collections.abc import Callable, Sequence
from functools import partial
from pathlib import Path
from urllib.parse import unquote, urlsplit

INLINE_LINK_PATTERN = re.compile(
    r"(?P<prefix>!?\[[^\]\n]*\]\(\s*)"
    r"(?P<destination><[^>\n]+>|[^)\s\n]+)"
    r"(?P<suffix>[^)\n]*\))"
)
REFERENCE_LINK_PATTERN = re.compile(
    r"(?P<prefix>^[ \t]{0,3}\[[^\]\n]+\]:[ \t]*)"
    r"(?P<destination><[^>\n]+>|[^\s\n]+)"
    r"(?P<suffix>.*$)"
)
AT_PATH_PATTERN = re.compile(r"(?<![\w/@])@(?P<destination>[^\s`<>\[\](){}\"',;]+)")
FENCE_PATTERN = re.compile(r"^[ \t]{0,3}(?P<fence>`{3,}|~{3,})")
GENERATED_GLOBAL_DIRECTORY_NAME = "_interaction"


class PackagingError(RuntimeError):
    """Report an invalid plugin link or generated layout."""


def parse_local_destination(destination: str) -> tuple[str, str, str] | None:
    """Return the path, query, and fragment for a relative local link.

    >>> parse_local_destination("../../roles.md#classifier")
    ('../../roles.md', '', 'classifier')
    >>> parse_local_destination("https://example.com/roles.md") is None
    True
    """
    unwrapped_destination = (
        destination[1:-1] if destination.startswith("<") else destination
    )
    parsed_destination = urlsplit(unwrapped_destination)
    if (
        not parsed_destination.path
        or parsed_destination.scheme
        or parsed_destination.netloc
        or parsed_destination.path.startswith(("/", "~"))
    ):
        return None

    return (
        unquote(parsed_destination.path),
        parsed_destination.query,
        parsed_destination.fragment,
    )


def format_destination(relative_path: str, query: str, fragment: str) -> str:
    """Format a rewritten Markdown link destination.

    >>> format_destination("../_interaction/roles.md", "", "classifier")
    '../_interaction/roles.md#classifier'
    """
    formatted_path = f"<{relative_path}>" if " " in relative_path else relative_path
    query_suffix = f"?{query}" if query else ""
    fragment_suffix = f"#{fragment}" if fragment else ""
    return f"{formatted_path}{query_suffix}{fragment_suffix}"


def rewrite_markdown(
    markdown: str,
    rewrite_destination: Callable[[str], str],
) -> str:
    """Rewrite Markdown links outside fences and @path references everywhere."""
    rewritten_lines: list[str] = []
    fence_character: str | None = None
    fence_length = 0

    for line in markdown.splitlines(keepends=True):
        fence_match = FENCE_PATTERN.match(line)
        inside_fence = fence_character is not None
        closes_fence = (
            inside_fence
            and fence_match is not None
            and fence_match.group("fence").startswith(fence_character)
            and len(fence_match.group("fence")) >= fence_length
        )
        if closes_fence:
            fence_character = None
        if inside_fence:
            rewritten_lines.append(line)
            continue

        if fence_match:
            fence = fence_match.group("fence")
            fence_character = fence[0]
            fence_length = len(fence)
            rewritten_lines.append(line)
            continue

        def replace_link(match: re.Match[str]) -> str:
            return (
                match.group("prefix")
                + rewrite_destination(match.group("destination"))
                + match.group("suffix")
            )

        rewritten_line = INLINE_LINK_PATTERN.sub(replace_link, line)
        rewritten_lines.append(REFERENCE_LINK_PATTERN.sub(replace_link, rewritten_line))

    return AT_PATH_PATTERN.sub(
        lambda match: "@" + rewrite_destination(match.group("destination")),
        "".join(rewritten_lines),
    )


def generated_target_for(
    source_target: Path,
    generated_skill_directory: Path,
    plugin_directory: Path,
    generated_skills_directory: Path,
) -> tuple[Path, bool]:
    """Map a plugin target to its generated Pi location."""
    plugin_skills_directory = plugin_directory / "skills"
    if source_target.is_relative_to(plugin_skills_directory):
        return (
            generated_skills_directory
            / source_target.relative_to(plugin_skills_directory),
            False,
        )

    if not source_target.is_relative_to(plugin_directory):
        raise PackagingError(
            f"Plugin link escapes the plugin directory: {source_target}"
        )

    return (
        generated_skill_directory
        / GENERATED_GLOBAL_DIRECTORY_NAME
        / source_target.relative_to(plugin_directory),
        True,
    )


def rewrite_destination_for_pi(
    destination: str,
    *,
    source_markdown_file: Path,
    generated_markdown_file: Path,
    source_file_is_global: bool,
    generated_skill_directory: Path,
    plugin_directory: Path,
    generated_skills_directory: Path,
    queue_global_file: Callable[[Path, Path], None],
) -> str:
    """Rewrite one link when Pi needs a packaged or rebased target."""
    parsed_destination = parse_local_destination(destination)
    if parsed_destination is None:
        return destination

    source_path, query, fragment = parsed_destination
    source_target = (source_markdown_file.parent / source_path).resolve()
    if not source_target.exists():
        raise PackagingError(
            f"Missing link target in {source_markdown_file}: {source_path}"
        )

    generated_target, is_plugin_global = generated_target_for(
        source_target,
        generated_skill_directory,
        plugin_directory,
        generated_skills_directory,
    )
    if is_plugin_global and not source_target.is_file():
        raise PackagingError(
            f"Plugin-global link target is not a file: {source_target}"
        )
    if is_plugin_global:
        queue_global_file(source_target, generated_target)
    if not is_plugin_global and not source_file_is_global:
        return destination

    relative_target = os.path.relpath(
        generated_target,
        generated_markdown_file.parent,
    )
    return format_destination(
        Path(relative_target).as_posix(),
        query,
        fragment,
    )


def package_skill_globals(
    source_skill_directory: Path,
    generated_skill_directory: Path,
    plugin_directory: Path,
    generated_skills_directory: Path,
) -> None:
    """Package the plugin-global files referenced by one Pi skill."""
    generated_global_directory = (
        generated_skill_directory / GENERATED_GLOBAL_DIRECTORY_NAME
    )
    if generated_global_directory.exists():
        raise PackagingError(
            f"Reserved generated directory already exists: {generated_global_directory}"
        )

    markdown_queue: list[tuple[Path, Path]] = [
        (
            source_markdown_file,
            generated_skill_directory
            / source_markdown_file.relative_to(source_skill_directory),
        )
        for source_markdown_file in sorted(source_skill_directory.rglob("*.md"))
    ]
    queued_markdown_files = {source_file for source_file, _ in markdown_queue}
    processed_markdown_files: set[Path] = set()
    copied_global_files: dict[Path, Path] = {}

    def queue_global_file(source_target: Path, generated_target: Path) -> None:
        existing_target = copied_global_files.get(source_target)
        if existing_target == generated_target:
            return
        if existing_target is not None:
            raise PackagingError(f"Conflicting generated targets for {source_target}")

        if generated_target.exists():
            raise PackagingError(
                f"Generated global file collides with {generated_target}"
            )

        generated_target.parent.mkdir(parents=True, exist_ok=True)
        copied_global_files[source_target] = generated_target
        if source_target.suffix.lower() != ".md":
            shutil.copy2(source_target, generated_target)
            return
        if source_target in queued_markdown_files:
            return

        markdown_queue.append((source_target, generated_target))
        queued_markdown_files.add(source_target)

    queue_index = 0
    while queue_index < len(markdown_queue):
        source_markdown_file, generated_markdown_file = markdown_queue[queue_index]
        queue_index += 1
        if source_markdown_file in processed_markdown_files:
            continue
        processed_markdown_files.add(source_markdown_file)

        source_file_is_global = not source_markdown_file.is_relative_to(
            plugin_directory / "skills"
        )
        destination_rewriter = partial(
            rewrite_destination_for_pi,
            source_markdown_file=source_markdown_file,
            generated_markdown_file=generated_markdown_file,
            source_file_is_global=source_file_is_global,
            generated_skill_directory=generated_skill_directory,
            plugin_directory=plugin_directory,
            generated_skills_directory=generated_skills_directory,
            queue_global_file=queue_global_file,
        )
        rewritten_markdown = rewrite_markdown(
            source_markdown_file.read_text(),
            destination_rewriter,
        )
        generated_markdown_file.parent.mkdir(parents=True, exist_ok=True)
        generated_markdown_file.write_text(rewritten_markdown)
        shutil.copystat(source_markdown_file, generated_markdown_file)


def verify_destination(destination: str, *, markdown_file: Path) -> str:
    """Fail when one generated link points to a missing local target."""
    parsed_destination = parse_local_destination(destination)
    if parsed_destination is None:
        return destination

    target_path, _, _ = parsed_destination
    target = (markdown_file.parent / target_path).resolve()
    if not target.exists():
        raise PackagingError(
            f"Missing generated link target in {markdown_file}: {target_path}"
        )
    return destination


def verify_generated_links(generated_skills_directory: Path) -> None:
    """Fail when a generated Markdown link points to a missing local target."""
    for markdown_file in sorted(generated_skills_directory.rglob("*.md")):
        rewrite_markdown(
            markdown_file.read_text(),
            partial(verify_destination, markdown_file=markdown_file),
        )


def package_plugin_globals(
    plugin_directory: Path,
    generated_skills_directory: Path,
) -> None:
    """Package referenced plugin-global files into each generated Pi skill."""
    for source_skill_directory in sorted((plugin_directory / "skills").iterdir()):
        if not (source_skill_directory / "SKILL.md").is_file():
            continue

        generated_skill_directory = (
            generated_skills_directory / source_skill_directory.name
        )
        package_skill_globals(
            source_skill_directory,
            generated_skill_directory,
            plugin_directory,
            generated_skills_directory,
        )

    verify_generated_links(generated_skills_directory)


def main(arguments: Sequence[str]) -> int:
    if len(arguments) != 3:
        print(
            "Usage: package-pi-skill-globals.py PLUGIN_DIRECTORY GENERATED_SKILLS_DIRECTORY",
            file=sys.stderr,
        )
        return 2

    plugin_directory = Path(arguments[1]).resolve()
    generated_skills_directory = Path(arguments[2]).resolve()
    try:
        package_plugin_globals(plugin_directory, generated_skills_directory)
    except PackagingError as error:
        print(f"✗ {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
