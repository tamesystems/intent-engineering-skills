#!/usr/bin/env python3
"""Keep independently installable skill references in sync with canonical sources."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFERENCE_COPIES = {
    "references/mechanism-ladder.md": (
        "skills/create-check/references/mechanism-ladder.md",
        "skills/ratchet/references/mechanism-ladder.md",
    ),
    "references/progress.md": ("skills/intent/references/progress.md",),
    "references/ratchets.md": (
        "skills/create-check/references/ratchets.md",
        "skills/ratchet/references/ratchets.md",
    ),
}


def drift_errors(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for source_name, copy_names in REFERENCE_COPIES.items():
        source = root / source_name
        if not source.is_file():
            errors.append(f"{source_name}: canonical reference is missing")
            continue
        expected = source.read_bytes()
        for copy_name in copy_names:
            copy = root / copy_name
            if not copy.is_file():
                errors.append(f"{copy_name}: packaged copy is missing; run python3 scripts/sync_references.py")
            elif copy.read_bytes() != expected:
                errors.append(
                    f"{copy_name}: differs from canonical {source_name}; "
                    "run python3 scripts/sync_references.py"
                )
    return errors


def sync(root: Path = ROOT) -> None:
    for source_name, copy_names in REFERENCE_COPIES.items():
        source = root / source_name
        for copy_name in copy_names:
            destination = root / copy_name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report drift without changing files")
    args = parser.parse_args()

    if args.check:
        errors = drift_errors()
        if errors:
            for error in errors:
                print(error)
            return 1
        print(f"Validated {sum(map(len, REFERENCE_COPIES.values()))} packaged reference copies.")
        return 0

    sync()
    print(f"Synchronized {sum(map(len, REFERENCE_COPIES.values()))} packaged reference copies.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
