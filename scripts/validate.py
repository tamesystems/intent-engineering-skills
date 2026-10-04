#!/usr/bin/env python3
"""Validate the repository's portable Agent Skills structure without dependencies."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

from sync_references import drift_errors

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REFERENCE_RE = re.compile(r"references/[a-zA-Z0-9._/-]+\.md")


def frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    closing = text.find("\n---\n", 4)
    if closing == -1:
        raise ValueError(f"{path}: unclosed YAML frontmatter")
    raw = text[4:closing]

    values: dict[str, str] = {}
    for line in raw.splitlines():
        match = re.match(r"^(name|description):\s*(.+?)\s*$", line)
        if match:
            values[match.group(1)] = match.group(2).strip('"\'')
    return values


def eval_scalar(raw: str, location: str) -> str:
    value = raw.strip()
    if not value:
        raise ValueError(f"{location}: value must be a nonempty string")
    if value[0] in "\"'":
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError) as error:
            raise ValueError(f"{location}: malformed quoted string") from error
        if not isinstance(parsed, str) or not parsed:
            raise ValueError(f"{location}: value must be a nonempty string")
        return parsed
    if value in {"null", "Null", "NULL", "~", "[]", "{}"}:
        raise ValueError(f"{location}: value must be a nonempty string")
    return value


def eval_inline_list(raw: str, location: str) -> list[str]:
    value = raw.strip()
    if not value:
        return []
    if not (value.startswith("[") and value.endswith("]")):
        raise ValueError(f"{location}: assertions must use a block list or inline list")
    body = value[1:-1].strip()
    if not body:
        return []
    return [eval_scalar(item, location) for item in body.split(",")]


def validate_eval(path: Path, skill_names: set[str], root: Path) -> list[str]:
    """Validate the strict YAML subset used by eval fixtures without a YAML dependency."""
    relative = path.relative_to(root)
    errors: list[str] = []
    declared = ""
    saw_cases = False
    cases: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    current_list: str | None = None

    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        location = f"{relative}:{number}"
        try:
            if line.startswith("skill:") and not line.startswith("skill: "):
                raise ValueError(f"{location}: skill must be a nonempty string")
            if line.startswith("skill: ") and not line.startswith(" "):
                if declared or saw_cases:
                    raise ValueError(f"{location}: skill must appear once before cases")
                declared = eval_scalar(line.split(":", 1)[1], location)
                continue
            if line == "cases:":
                if saw_cases:
                    raise ValueError(f"{location}: duplicate cases list")
                saw_cases = True
                continue
            if line.startswith("cases:"):
                raise ValueError(f"{location}: cases must be a block list")
            if line.startswith("  - name:"):
                if not saw_cases:
                    raise ValueError(f"{location}: case appears before cases")
                name = eval_scalar(line.split(":", 1)[1], location)
                current = {"name": name, "line": number}
                cases.append(current)
                current_list = None
                continue
            if line.startswith("    ") and not line.startswith("      "):
                if current is None:
                    raise ValueError(f"{location}: case field appears outside a case")
                match = re.fullmatch(r"    (prompt|expect|reject):(.*)", line)
                if not match:
                    raise ValueError(f"{location}: unsupported case field or indentation")
                field, raw = match.groups()
                if field in current:
                    raise ValueError(f"{location}: duplicate {field} field")
                if field == "prompt":
                    current[field] = eval_scalar(raw, location)
                    current_list = None
                else:
                    current[field] = eval_inline_list(raw, location)
                    current_list = field
                continue
            if line.startswith("      - "):
                if current is None or current_list is None:
                    raise ValueError(f"{location}: assertion appears outside expect or reject")
                assertion = eval_scalar(line.removeprefix("      - "), location)
                assertions = current[current_list]
                assert isinstance(assertions, list)
                assertions.append(assertion)
                continue
            raise ValueError(f"{location}: unsupported eval YAML shape or indentation")
        except ValueError as error:
            errors.append(str(error))

    if declared != path.stem:
        errors.append(f"{relative}: skill {declared!r} must match filename {path.stem!r}")
    if declared not in skill_names:
        errors.append(f"{relative}: unknown skill {declared!r}")
    if not saw_cases:
        errors.append(f"{relative}: missing cases list")
    if not cases:
        errors.append(f"{relative}: must contain at least one named case")

    case_names: set[str] = set()
    for case in cases:
        name = str(case["name"])
        line = int(case["line"])
        if name in case_names:
            errors.append(f"{relative}:{line}: duplicate case name {name!r}")
        case_names.add(name)
        for field in ("prompt", "expect", "reject"):
            if field not in case:
                errors.append(f"{relative}:{line}: case {name!r} is missing {field}")
            elif field != "prompt" and not case[field]:
                errors.append(f"{relative}:{line}: case {name!r} has an empty {field} list")
    return errors


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    skills_dir = root / "skills"
    names: set[str] = set()
    skill_files = sorted(skills_dir.glob("*/SKILL.md"))

    if not skill_files:
        errors.append("No skills/*/SKILL.md files found")

    for skill_file in skill_files:
        skill_dir = skill_file.parent
        text = skill_file.read_text(encoding="utf-8")
        try:
            metadata = frontmatter(text, skill_file.relative_to(root))
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

    eval_files = sorted((root / "evals" / "cases").glob("*.yaml"))
    eval_names = {path.stem for path in eval_files}
    for missing in sorted(names - eval_names):
        errors.append(f"evals/cases/{missing}.yaml: missing eval file for skill {missing!r}")
    for extra in sorted(eval_names - names):
        errors.append(f"evals/cases/{extra}.yaml: eval has no matching skill")
    for eval_file in eval_files:
        errors.extend(validate_eval(eval_file, names, root))

    errors.extend(drift_errors(root))

    manifest_path = root / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("skills") != "./skills/":
            errors.append(f"{manifest_path}: skills must be './skills/'")
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{manifest_path}: {error}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    skill_count = len(list((ROOT / "skills").glob("*/SKILL.md")))
    eval_count = len(list((ROOT / "evals" / "cases").glob("*.yaml")))
    print(f"Validated {skill_count} skills, {eval_count} eval files, references, and the Codex plugin manifest.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
