#!/usr/bin/env python3
"""Scaffold a new skill folder with SKILL.md template and register it in skills.json."""

import argparse
import json
import sys
from pathlib import Path

VALID_ROLES = ["pm", "engineer", "qa", "designer", "content-creator", "devops", "shared", "leadership", "program-delivery-manager", "customer-success", "founder", "data-scientist", "marketing", "sales", "recruiter", "consultant"]

SKILL_TEMPLATE = """\
---
name: {name}
description: >
  Use this skill when [describe the trigger - when should Claude invoke this?].
  Applies to [your role] working on [type of task].
---

## Workflow

1. Step one
2. Step two
3. Step three

## Anti-Patterns

- Don't do X
- Avoid Y when Z

## Quality Checklist

- [ ] Output is specific, not generic
- [ ] Uses `[your context]` placeholders where user input is needed
- [ ] No personal names, domains, or project-specific references
"""


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new Claude skill")
    parser.add_argument("name", help="Skill name (e.g. write-test-plan)")
    parser.add_argument("--role", required=True, choices=VALID_ROLES,
                        help="Job role this skill belongs to")
    parser.add_argument("--description", default="",
                        help="One-line description for skills.json")
    parser.add_argument("--tags", default="",
                        help="Comma-separated tags (e.g. testing,quality)")
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent
    registry_path = repo_root / "skills.json"

    # Determine skill path
    if args.role == "shared":
        skill_dir = repo_root / "skills" / "shared" / args.name
    else:
        skill_dir = repo_root / "skills" / "by-role" / args.role / args.name

    if skill_dir.exists():
        print(f"Error: skill already exists at {skill_dir}")
        sys.exit(1)

    # Create skill directory and SKILL.md
    skill_dir.mkdir(parents=True)
    skill_md = skill_dir / "SKILL.md"
    skill_md.write_text(SKILL_TEMPLATE.format(name=args.name))

    print(f"Created: {skill_md}")

    # Register in skills.json
    registry = json.loads(registry_path.read_text())
    skill_key = f"{args.role}/{args.name}"
    tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    registry["skills"][skill_key] = {
        "role": args.role,
        "description": args.description or f"[Describe what {args.name} does]",
        "tags": tags
    }

    registry_path.write_text(json.dumps(registry, indent=2) + "\n")
    print(f"Registered: {skill_key} in skills.json")
    print()
    print(f"Next steps:")
    print(f"  1. Edit {skill_md}")
    print(f"  2. Update the description in skills.json")
    print(f"  3. Run: python3 scripts/validate_skill.py")


if __name__ == "__main__":
    main()
