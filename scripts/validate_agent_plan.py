"""Validate that an agent plan contains the basic sections needed for safe execution."""

from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Goal",
    "## Context",
    "## Assumptions",
    "## Proposed steps",
    "## Files likely to change",
    "## Risks",
    "## Validation",
    "## Approval",
]


def validate_plan(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    missing = [section for section in REQUIRED_SECTIONS if section not in text]
    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an agent-plan.md file.")
    parser.add_argument("plan_path", type=Path)
    args = parser.parse_args()

    missing = validate_plan(args.plan_path)
    if missing:
        print("Plan is missing required sections:")
        for section in missing:
            print(f"- {section}")
        return 1

    print(f"Plan looks valid: {args.plan_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
