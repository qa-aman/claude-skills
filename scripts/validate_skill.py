#!/usr/bin/env python3
"""Validate SKILL.md files against required standards."""

import sys
import json
from pathlib import Path

REQUIRED_FRONTMATTER = ["name", "description"]
MAX_LINES = 500


def parse_frontmatter(content: str) -> dict:
    lines = content.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}
    fields = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def validate_skill(skill_path: Path, registry: dict) -> list:
    errors = []
    skill_md = skill_path / "SKILL.md"

    if not skill_md.exists():
        errors.append(f"{skill_path}: missing SKILL.md")
        return errors

    content = skill_md.read_text()

    # Check frontmatter
    frontmatter = parse_frontmatter(content)
    for field in REQUIRED_FRONTMATTER:
        if field not in frontmatter:
            errors.append(f"{skill_md}: missing frontmatter field '{field}'")

    # Check length
    lines = content.split("\n")
    if len(lines) > MAX_LINES:
        errors.append(f"{skill_md}: exceeds {MAX_LINES} lines ({len(lines)} lines)")

    return errors


def main():
    repo_root = Path(__file__).parent.parent
    registry_path = repo_root / "skills.json"

    if not registry_path.exists():
        print("Error: skills.json not found")
        sys.exit(1)

    registry = json.loads(registry_path.read_text())
    skills_dir = repo_root / "skills"
    all_errors = []

    for skill_md in sorted(skills_dir.rglob("SKILL.md")):
        errors = validate_skill(skill_md.parent, registry)
        all_errors.extend(errors)

    if all_errors:
        print("Validation failed:")
        for error in all_errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        count = sum(1 for _ in skills_dir.rglob("SKILL.md"))
        print(f"All {count} skills valid.")


if __name__ == "__main__":
    main()
