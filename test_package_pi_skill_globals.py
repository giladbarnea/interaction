import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class PackageAtPathsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        self.plugin = self.root / "plugin"
        self.skill = self.plugin / "skills" / "alpha"
        self.skill.mkdir(parents=True)
        self.generated = self.root / "generated"

    def package(self, markdown: str) -> subprocess.CompletedProcess[str]:
        (self.skill / "SKILL.md").write_text(markdown)
        shutil.copytree(self.plugin / "skills", self.generated)
        return subprocess.run(
            [
                sys.executable,
                str(Path(__file__).with_name("package-pi-skill-globals.py")),
                str(self.plugin),
                str(self.generated),
            ],
            capture_output=True,
            text=True,
        )

    def test_packages_transitive_at_paths_in_prose_and_code(self) -> None:
        (self.plugin / "roles.md").write_text("Read @shared.md\n")
        (self.plugin / "shared.md").write_text("# Shared\n")
        markdown = "Read @../../roles.md\n`@../../roles.md`\n```text\n@../../roles.md\n```\n"
        result = self.package(markdown)
        self.assertEqual(result.returncode, 0, result.stderr)
        packaged = self.generated / "alpha" / "_interaction"
        self.assertTrue((packaged / "roles.md").is_file(), "The referenced global file was not packaged")
        self.assertTrue((packaged / "shared.md").is_file(), "The transitive global file was not packaged")
        self.assertEqual((packaged / "roles.md").read_text(), "Read @shared.md\n")
        self.assertEqual((packaged / "shared.md").read_text(), "# Shared\n")
        self.assertEqual(
            (self.generated / "alpha" / "SKILL.md").read_text(),
            markdown.replace("../../roles.md", "_interaction/roles.md"),
        )

    def test_rejects_missing_relative_at_path(self) -> None:
        result = self.package("Read @../../missing.md\n")
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("Missing link target", result.stderr)

    def test_ignores_absolute_at_paths_and_email_addresses(self) -> None:
        markdown = "@/path/to/example.md\n```text\n@/path/to/example.md\n```\nauthor@example.com\n"
        result = self.package(markdown)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.generated / "alpha" / "SKILL.md").read_text(), markdown)

    def test_still_rejects_missing_markdown_target(self) -> None:
        result = self.package("[Missing](../../missing.md)\n")
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("Missing link target", result.stderr)


if __name__ == "__main__":
    unittest.main()
