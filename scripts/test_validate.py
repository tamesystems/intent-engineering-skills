#!/usr/bin/env python3
"""Negative tests for repository structural validation."""

from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from validate import ROOT, frontmatter, validate, validate_eval


class ValidatorTests(unittest.TestCase):
    def copy_repository(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name) / "repo"
        shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        return temporary, root

    def test_clean_repository_passes(self) -> None:
        self.assertEqual(validate(ROOT), [])

    def test_unclosed_frontmatter_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "unclosed YAML frontmatter"):
            frontmatter("---\nname: intent\ndescription: test\n", Path("skills/intent/SKILL.md"))

    def test_missing_packaged_reference_is_rejected(self) -> None:
        temporary, root = self.copy_repository()
        self.addCleanup(temporary.cleanup)
        target = root / "skills" / "intent" / "references" / "progress.md"
        target.unlink()
        self.assertTrue(any("packaged copy is missing" in error for error in validate(root)))

    def test_reference_drift_is_rejected(self) -> None:
        temporary, root = self.copy_repository()
        self.addCleanup(temporary.cleanup)
        target = root / "skills" / "ratchet" / "references" / "ratchets.md"
        target.write_text("stale\n", encoding="utf-8")
        self.assertTrue(any("differs from canonical" in error for error in validate(root)))

    def test_malformed_eval_is_rejected(self) -> None:
        temporary, root = self.copy_repository()
        self.addCleanup(temporary.cleanup)
        target = root / "evals" / "cases" / "investigate.yaml"
        target.write_text(
            "skill: wrong\ncases:\n  - name: empty-expect\n    prompt: \"unclosed\n    expect:\n      - \n    reject:\n      - guessing\n",
            encoding="utf-8",
        )
        errors = validate(root)
        self.assertTrue(any("must match filename" in error for error in errors))
        self.assertTrue(any("malformed quoted string" in error for error in errors))
        self.assertTrue(any("value must be a nonempty string" in error for error in errors))

    def test_eval_rejects_cases_outside_the_cases_list(self) -> None:
        temporary, root = self.copy_repository()
        self.addCleanup(temporary.cleanup)
        target = root / "evals" / "cases" / "investigate.yaml"
        target.write_text(
            "skill: investigate\ncases: null\nother:\n  - name: misplaced\n    prompt: test\n    expect: [evidence]\n    reject: [guessing]\n",
            encoding="utf-8",
        )
        errors = validate_eval(target, {"investigate"}, root)
        self.assertTrue(any("cases must be a block list" in error for error in errors))
        self.assertTrue(any("unsupported eval YAML shape" in error for error in errors))

    def test_eval_accepts_quoted_skill_and_inline_assertions(self) -> None:
        temporary, root = self.copy_repository()
        self.addCleanup(temporary.cleanup)
        target = root / "evals" / "cases" / "investigate.yaml"
        target.write_text(
            'skill: "investigate"\ncases:\n  - name: sample\n    prompt: test\n    expect: [evidence]\n    reject: [guessing]\n',
            encoding="utf-8",
        )
        self.assertEqual(validate_eval(target, {"investigate"}, root), [])


if __name__ == "__main__":
    unittest.main()
