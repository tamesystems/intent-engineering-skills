#!/usr/bin/env python3
"""Validate the repository's portable Agent Skills structure without dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REFERENCE_RE = re.compile(r"references/[a-zA-Z0-9._/-]+\.md")


def frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    try:
        raw = text.split("---\n", 2)[1]
    except IndexError as error:
        raise ValueError(f"{path}: unclosed YAML frontmatter") from error

    values: dict[str, str] = {}
    for line in raw.splitlines():
        match = re.match(r"^(name|description):\s*(.+?)\s*$", line)
        if match:
            values[match.group(1)] = match.group(2).strip('"\'')
    return values


def main() -> int:
    errors: list[str] = []
    names: set[str] = set()
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))

    if not skill_files:
        errors.append("No skills/*/SKILL.md files found")

    for skill_file in skill_files:
        skill_dir = skill_file.parent
        text = skill_file.read_text(encoding="utf-8")
        try:
            metadata = frontmatter(text, skill_file.relative_to(ROOT))
        except ValueError as error:
            errors.append(str(error))
            continue

        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if name != skill_dir.name:
            errors.append(f"{skill_file}: name {name!r} must match directory {skill_dir.name!r}")
        if not NAME_RE.fullmatch(name) or len(name) > 64:
            errors.append(f"{skill_file}: invalid skill name {name!r}")
        if name in names:
            errors.append(f"{skill_file}: duplicate skill name {name!r}")
        names.add(name)
        if not description or len(description) > 1024:
            errors.append(f"{skill_file}: description must contain 1–1024 characters")

        for reference in sorted(set(REFERENCE_RE.findall(text))):
            if not (skill_dir / reference).is_file():
                errors.append(f"{skill_file}: missing packaged reference {reference}")

    manifest_path = ROOT / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("skills") != "./skills/":
            errors.append(f"{manifest_path}: skills must be './skills/'")
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{manifest_path}: {error}")

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_files)} skills and the Codex plugin manifest.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
