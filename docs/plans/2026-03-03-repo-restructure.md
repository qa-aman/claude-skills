# Repo Restructure Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Restructure claude-skills into a role-based, community-ready public repo targeting 1M GitHub stars.

**Architecture:** Skills organized under `skills/by-role/<role>/` and `skills/shared/`. A `skills.json` registry drives the install script - contributors add a folder, never touch scripts. Personalization stays in `~/.claude/skills/skill-context.md`, keeping skill files immutable.

**Tech Stack:** Bash (install.sh), Python 3 (init_skill.py, validate_skill.py), JSON (skills.json), GitHub Actions (CI), MIT License.

**Design reference:** `docs/plans/2026-03-03-repo-design.md`

---

## Skill Migration Map

Existing skills → new locations:
| Skill | New Location |
|-------|-------------|
| linkedin-post | `skills/by-role/content-creator/` |
| reddit-post | `skills/by-role/content-creator/` |
| newsletter-ideation | `skills/by-role/content-creator/` |
| substack-post | `skills/by-role/content-creator/` |
| substack-notes | `skills/by-role/content-creator/` |
| substack-toc | `skills/by-role/content-creator/` |
| presentation-builder | `skills/shared/` |
| 11-star-framework | `skills/by-role/pm/` |

---

### Task 1: Create Folder Structure

**Files:**
- Create: `skills/by-role/pm/.gitkeep`
- Create: `skills/by-role/engineer/.gitkeep`
- Create: `skills/by-role/qa/.gitkeep`
- Create: `skills/by-role/designer/.gitkeep`
- Create: `skills/by-role/content-creator/.gitkeep`
- Create: `skills/by-role/devops/.gitkeep`
- Create: `skills/shared/.gitkeep`

**Step 1: Create role directories**

```bash
mkdir -p skills/by-role/pm
mkdir -p skills/by-role/engineer
mkdir -p skills/by-role/qa
mkdir -p skills/by-role/designer
mkdir -p skills/by-role/content-creator
mkdir -p skills/by-role/devops
mkdir -p skills/shared
```

**Step 2: Move existing skills to new locations**

```bash
# content-creator skills
mv skills/linkedin-post skills/by-role/content-creator/
mv skills/reddit-post skills/by-role/content-creator/
mv skills/newsletter-ideation skills/by-role/content-creator/
mv skills/substack-post skills/by-role/content-creator/
mv skills/substack-notes skills/by-role/content-creator/
mv skills/substack-toc skills/by-role/content-creator/

# pm skills
mv skills/11-star-framework skills/by-role/pm/

# shared skills
mv skills/presentation-builder skills/shared/
```

**Step 3: Verify structure**

```bash
find skills/ -type d | sort
```

Expected output:
```
skills/
skills/by-role
skills/by-role/content-creator
skills/by-role/content-creator/linkedin-post
skills/by-role/content-creator/newsletter-ideation
...
skills/by-role/pm
skills/by-role/pm/11-star-framework
skills/shared
skills/shared/presentation-builder
```

**Step 4: Commit**

```bash
git add skills/
git commit -m "restructure: move skills into by-role and shared folders"
```

---

### Task 2: Create skills.json Registry

**Files:**
- Create: `skills.json`

**Step 1: Create registry**

```json
{
  "version": "1.0",
  "skills": {
    "content-creator/linkedin-post": {
      "role": "content-creator",
      "description": "Write LinkedIn posts",
      "tags": ["content", "social"]
    },
    "content-creator/reddit-post": {
      "role": "content-creator",
      "description": "Write Reddit posts",
      "tags": ["content", "social"]
    },
    "content-creator/newsletter-ideation": {
      "role": "content-creator",
      "description": "Ideate newsletter topics",
      "tags": ["content", "newsletter"]
    },
    "content-creator/substack-post": {
      "role": "content-creator",
      "description": "Write Substack posts",
      "tags": ["content", "newsletter"]
    },
    "content-creator/substack-notes": {
      "role": "content-creator",
      "description": "Write Substack notes",
      "tags": ["content", "newsletter"]
    },
    "content-creator/substack-toc": {
      "role": "content-creator",
      "description": "Generate Substack table of contents",
      "tags": ["content", "newsletter"]
    },
    "pm/11-star-framework": {
      "role": "pm",
      "description": "Apply 11-star experience framework",
      "tags": ["product", "framework"]
    },
    "shared/presentation-builder": {
      "role": "shared",
      "description": "Build structured presentations",
      "tags": ["productivity", "presentations"]
    }
  }
}
```

**Step 2: Verify JSON is valid**

```bash
python3 -c "import json; json.load(open('skills.json')); print('Valid JSON')"
```

Expected: `Valid JSON`

**Step 3: Commit**

```bash
git add skills.json
git commit -m "add skills.json registry"
```

---

### Task 3: Rewrite install.sh

**Files:**
- Modify: `scripts/install.sh`

**Step 1: Replace install.sh with new version**

```bash
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$SCRIPT_DIR/.."
SKILLS_DIR="$REPO_DIR/skills"
REGISTRY="$REPO_DIR/skills.json"
TARGET_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

# Requires python3 and jq or python3 for JSON parsing
if ! command -v python3 &>/dev/null; then
  echo "Error: python3 is required"
  exit 1
fi

get_skills_for_role() {
  local role="$1"
  python3 -c "
import json, sys
data = json.load(open('$REGISTRY'))
for key, val in data['skills'].items():
    if val['role'] == '$role' or '$role' == 'shared':
        print(key)
"
}

get_all_skills() {
  python3 -c "
import json
data = json.load(open('$REGISTRY'))
for key in data['skills']:
    print(key)
"
}

get_all_roles() {
  python3 -c "
import json
data = json.load(open('$REGISTRY'))
roles = set(v['role'] for v in data['skills'].values())
for r in sorted(roles):
    print(r)
"
}

install_skill() {
  local skill_key="$1"  # e.g. content-creator/linkedin-post
  local src="$SKILLS_DIR/by-role/$skill_key"

  # Check shared if not found in by-role
  if [ ! -d "$src" ]; then
    src="$SKILLS_DIR/shared/$(basename $skill_key)"
  fi

  if [ ! -d "$src" ]; then
    echo "Error: skill '$skill_key' not found"
    return 1
  fi

  local dest="$TARGET_DIR/$(basename $skill_key)"
  mkdir -p "$dest"
  cp -r "$src"/* "$dest"/
  echo "  Installed: $(basename $skill_key)"
}

uninstall_role() {
  local role="$1"
  while IFS= read -r skill_key; do
    local skill_name
    skill_name="$(basename "$skill_key")"
    local dest="$TARGET_DIR/$skill_name"
    if [ -d "$dest" ]; then
      rm -rf "$dest"
      echo "  Removed: $skill_name"
    fi
  done < <(get_skills_for_role "$role")
}

init_context() {
  local context_file="$TARGET_DIR/skill-context.md"
  if [ -f "$context_file" ]; then
    echo "skill-context.md already exists at $context_file"
    echo "Edit it directly to update your context."
    return
  fi

  echo "Setting up skill-context.md for personalized skill behavior..."
  echo ""

  read -rp "Your industry (e.g. Fintech, EdTech, SaaS): " industry
  read -rp "Your primary tech stack (e.g. React + Node.js): " stack
  read -rp "Any compliance requirements (e.g. PCI-DSS, HIPAA, or 'none'): " compliance

  cat > "$context_file" <<EOF
# Skill Context
# This file personalizes generic skills for your project.
# Skills read this at invocation time. Edit anytime.

- Industry: $industry
- Stack: $stack
- Compliance: $compliance
EOF

  echo ""
  echo "Created: $context_file"
}

list_skills() {
  echo "Available skills by role:"
  echo ""
  while IFS= read -r role; do
    echo "  [$role]"
    while IFS= read -r skill_key; do
      echo "    - $(basename "$skill_key")"
    done < <(get_skills_for_role "$role")
    echo ""
  done < <(get_all_roles)
  echo "  [shared]"
  while IFS= read -r skill_key; do
    local role
    role=$(python3 -c "import json; d=json.load(open('$REGISTRY')); print(d['skills'].get('$skill_key',{}).get('role',''))")
    if [ "$role" = "shared" ]; then
      echo "    - $(basename "$skill_key")"
    fi
  done < <(get_all_skills)
}

usage() {
  echo "Usage: $0 [options]"
  echo ""
  echo "Options:"
  echo "  --role ROLE[,ROLE]   Install skills for one or more roles"
  echo "  --all                Install all skills"
  echo "  --update             Update all installed skills"
  echo "  --uninstall ROLE     Remove skills for a role"
  echo "  --init               Set up skill-context.md for personalization"
  echo "  --list               List all available skills"
  echo "  --target DIR         Override install directory (default: ~/.claude/skills)"
  echo ""
  echo "Examples:"
  echo "  $0 --role qa"
  echo "  $0 --role pm,content-creator"
  echo "  $0 --role qa --init"
  echo "  $0 --all"
  echo "  $0 --update"
  echo "  $0 --uninstall qa"
}

# Defaults
ROLES=()
DO_ALL=false
DO_UPDATE=false
DO_INIT=false
UNINSTALL_ROLE=""

if [ $# -eq 0 ]; then
  usage
  exit 1
fi

# Parse args
while [ $# -gt 0 ]; do
  case "$1" in
    --role)
      IFS=',' read -ra ROLES <<< "$2"
      shift 2
      ;;
    --all)
      DO_ALL=true
      shift
      ;;
    --update)
      DO_UPDATE=true
      shift
      ;;
    --uninstall)
      UNINSTALL_ROLE="$2"
      shift 2
      ;;
    --init)
      DO_INIT=true
      shift
      ;;
    --list)
      list_skills
      exit 0
      ;;
    --target)
      TARGET_DIR="$2"
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      usage
      exit 1
      ;;
  esac
done

mkdir -p "$TARGET_DIR"

# Uninstall
if [ -n "$UNINSTALL_ROLE" ]; then
  echo "Uninstalling $UNINSTALL_ROLE skills..."
  uninstall_role "$UNINSTALL_ROLE"
  echo "Done."
  exit 0
fi

# Collect skills to install
SKILLS_TO_INSTALL=()

if [ "$DO_ALL" = true ]; then
  while IFS= read -r skill; do
    SKILLS_TO_INSTALL+=("$skill")
  done < <(get_all_skills)
elif [ ${#ROLES[@]} -gt 0 ]; then
  for role in "${ROLES[@]}"; do
    while IFS= read -r skill; do
      SKILLS_TO_INSTALL+=("$skill")
    done < <(get_skills_for_role "$role")
    # Always include shared skills
    while IFS= read -r skill; do
      SKILLS_TO_INSTALL+=("$skill")
    done < <(get_skills_for_role "shared")
  done
fi

# Install
if [ ${#SKILLS_TO_INSTALL[@]} -gt 0 ]; then
  echo "Installing skills to $TARGET_DIR..."
  installed=0
  for skill in "${SKILLS_TO_INSTALL[@]}"; do
    if install_skill "$skill"; then
      ((installed++))
    fi
  done
  echo ""
  echo "$installed skill(s) installed."
fi

# Init context
if [ "$DO_INIT" = true ]; then
  echo ""
  init_context
fi
```

**Step 2: Make executable**

```bash
chmod +x scripts/install.sh
```

**Step 3: Test --list**

```bash
cd /path/to/claude-skills && bash scripts/install.sh --list
```

Expected: Prints all skills grouped by role.

**Step 4: Test --role install**

```bash
bash scripts/install.sh --role content-creator --target /tmp/test-skills
ls /tmp/test-skills/
```

Expected: linkedin-post, reddit-post, etc. in /tmp/test-skills/

**Step 5: Test --uninstall**

```bash
bash scripts/install.sh --uninstall content-creator --target /tmp/test-skills
ls /tmp/test-skills/
```

Expected: content-creator skills removed.

**Step 6: Cleanup and commit**

```bash
rm -rf /tmp/test-skills
git add scripts/install.sh
git commit -m "rewrite install.sh with role filter, update, uninstall, init"
```

---

### Task 4: Create validate_skill.py

**Files:**
- Create: `scripts/validate_skill.py`

**Step 1: Write validator**

```python
#!/usr/bin/env python3
"""Validate SKILL.md files against required standards."""

import sys
import json
from pathlib import Path


REQUIRED_FRONTMATTER = ["name", "description"]
PERSONAL_PATTERNS = [
    "amanparmar", "aman parmar", "@aman",
    # Add more as needed
]


def parse_frontmatter(content: str) -> dict:
    lines = content.split("\n")
    if not lines[0].strip() == "---":
        return {}
    fields = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def validate_skill(skill_path: Path, registry: dict) -> list[str]:
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
    if len(lines) > 500:
        errors.append(f"{skill_md}: exceeds 500 lines ({len(lines)} lines)")

    # Check personal content
    content_lower = content.lower()
    for pattern in PERSONAL_PATTERNS:
        if pattern.lower() in content_lower:
            errors.append(f"{skill_md}: contains personal reference '{pattern}'")

    # Check registry
    skill_name = frontmatter.get("name", "")
    if skill_name and skill_name not in str(registry):
        errors.append(f"{skill_md}: skill '{skill_name}' not found in skills.json")

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

    for skill_path in sorted(skills_dir.rglob("SKILL.md")):
        errors = validate_skill(skill_path.parent, registry)
        all_errors.extend(errors)

    if all_errors:
        print("Validation failed:")
        for error in all_errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print(f"All skills valid.")


if __name__ == "__main__":
    main()
```

**Step 2: Make executable**

```bash
chmod +x scripts/validate_skill.py
```

**Step 3: Run validator**

```bash
python3 scripts/validate_skill.py
```

Expected: `All skills valid.` (or errors to fix)

**Step 4: Commit**

```bash
git add scripts/validate_skill.py
git commit -m "add validate_skill.py for SKILL.md format checking"
```

---

### Task 5: Create .github Community Files

**Files:**
- Create: `.github/CONTRIBUTING.md`
- Create: `.github/PULL_REQUEST_TEMPLATE.md`
- Create: `.github/ISSUE_TEMPLATE/new-skill.md`
- Create: `.github/ISSUE_TEMPLATE/bug-report.md`

**Step 1: Create .github directory**

```bash
mkdir -p .github/ISSUE_TEMPLATE
```

**Step 2: Write CONTRIBUTING.md**

```markdown
# Contributing to Claude Skills

## Adding a New Skill

1. **Pick the right role folder**
   - `skills/by-role/pm/` - Product managers
   - `skills/by-role/engineer/` - Engineers
   - `skills/by-role/qa/` - QA and testers
   - `skills/by-role/designer/` - Designers
   - `skills/by-role/content-creator/` - Writers and content creators
   - `skills/by-role/devops/` - DevOps and SRE
   - `skills/shared/` - Useful to all roles

2. **Scaffold the skill**
   ```bash
   python3 scripts/init_skill.py <skill-name> --role <role>
   ```

3. **Write your SKILL.md** following the standard:
   - YAML frontmatter with `name` and `description`
   - `description` is the trigger - put all "when to use" context there
   - Body under 500 lines
   - Use placeholders: `[your industry]`, `[your stack]`, `[your team]`
   - No personal names, domains, or project-specific references

4. **Register in skills.json**
   ```json
   "engineer/my-skill": {
     "role": "engineer",
     "description": "One line description",
     "tags": ["tag1", "tag2"]
   }
   ```

5. **Validate**
   ```bash
   python3 scripts/validate_skill.py
   ```

6. **Open a PR** - CI will validate automatically.

## Skill Quality Bar

A good skill:
- Solves a real, recurring task for that role
- Works for any user in any project (no specifics baked in)
- Has a clear trigger in the `description` field
- Includes a workflow, anti-patterns, and quality checklist

## Questions?

Open an issue with the "New Skill Request" template and we'll help you design it.
```

**Step 3: Write PULL_REQUEST_TEMPLATE.md**

```markdown
## Skill PR Checklist

- [ ] Skill is in the correct role folder (`skills/by-role/<role>/` or `skills/shared/`)
- [ ] `SKILL.md` has `name` and `description` in YAML frontmatter
- [ ] `description` field contains all "when to use" context
- [ ] Skill body is under 500 lines
- [ ] No personal names, domains, or project-specific references
- [ ] Placeholders used: `[your industry]`, `[your stack]`, `[your team]`
- [ ] Skill registered in `skills.json`
- [ ] `python3 scripts/validate_skill.py` passes locally
- [ ] Includes: workflow, anti-patterns, quality checklist

## What does this skill do?

<!-- One paragraph: what problem it solves, who uses it, when they invoke it -->

## Example invocation

<!-- Show how a user would trigger this skill -->
```

**Step 4: Write new-skill issue template**

```markdown
---
name: New Skill Request
about: Request a new skill for a specific role
title: "[SKILL] "
labels: skill-request
---

## Role
<!-- Which job role needs this skill? pm / engineer / qa / designer / content-creator / devops / shared -->

## Problem
<!-- What recurring task does this skill solve? -->

## Example trigger
<!-- When would someone invoke this skill? What would they say? -->

## Notes
<!-- Anything else relevant - industry context, tools, edge cases -->
```

**Step 5: Write bug-report issue template**

```markdown
---
name: Bug Report
about: A skill isn't working as expected
title: "[BUG] "
labels: bug
---

## Skill
<!-- Which skill? e.g. qa/write-test-plan -->

## What happened
<!-- What did the skill do? -->

## What you expected
<!-- What should it have done? -->

## Claude version / context
<!-- Any relevant context -->
```

**Step 6: Commit**

```bash
git add .github/
git commit -m "add contributing guide, PR template, and issue templates"
```

---

### Task 6: GitHub Actions CI

**Files:**
- Create: `.github/workflows/validate.yml`

**Step 1: Write validation workflow**

```yaml
name: Validate Skills

on:
  pull_request:
    paths:
      - 'skills/**'
      - 'skills.json'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Validate skills.json
        run: python3 -c "import json; json.load(open('skills.json')); print('skills.json is valid JSON')"

      - name: Validate all SKILL.md files
        run: python3 scripts/validate_skill.py
```

**Step 2: Commit**

```bash
git add .github/workflows/
git commit -m "add GitHub Actions CI for skill validation"
```

---

### Task 7: Update LICENSE

**Files:**
- Modify: `LICENSE` (create if doesn't exist)

**Step 1: Check if LICENSE exists**

```bash
ls LICENSE 2>/dev/null || echo "not found"
```

**Step 2: Create MIT LICENSE**

```
MIT License

Copyright (c) 2026 claude-skills contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Step 3: Commit**

```bash
git add LICENSE
git commit -m "add MIT license"
```

---

### Task 8: Update README.md

**Files:**
- Modify: `README.md`

**Step 1: Read current README**

```bash
cat README.md
```

**Step 2: Rewrite README with new structure**

The README must cover:
- One-line pitch
- Install command (curl-based one-liner if possible, or clone + script)
- Role listing with skill counts
- `--role` flag examples
- `skill-context.md` personalization explanation
- Contributing section pointing to CONTRIBUTING.md
- License badge

**Step 3: Verify README renders correctly**

Preview on GitHub after push, or use a local markdown previewer.

**Step 4: Commit**

```bash
git add README.md
git commit -m "update README for role-based structure"
```

---

### Task 9: Final Verification

**Step 1: Full validation pass**

```bash
python3 scripts/validate_skill.py
```

**Step 2: Test install end-to-end**

```bash
bash scripts/install.sh --role pm --target /tmp/verify-install
ls /tmp/verify-install/
rm -rf /tmp/verify-install
```

**Step 3: Test multi-role**

```bash
bash scripts/install.sh --role pm,content-creator --target /tmp/verify-multi
ls /tmp/verify-multi/
rm -rf /tmp/verify-multi
```

**Step 4: Check git log**

```bash
git log --oneline
```

Expected: Clean commit history with one commit per task.

**Step 5: Final commit if anything remaining**

```bash
git add -A
git status  # should be clean
```

---

## Summary of Deliverables

| Deliverable | Path | Priority |
|-------------|------|----------|
| Role folders | `skills/by-role/*/` | P0 |
| Shared folder | `skills/shared/` | P0 |
| Skill registry | `skills.json` | P0 |
| Install script | `scripts/install.sh` | P0 |
| Validator | `scripts/validate_skill.py` | P0 |
| Contributing guide | `.github/CONTRIBUTING.md` | P0 |
| PR template | `.github/PULL_REQUEST_TEMPLATE.md` | P0 |
| Issue templates | `.github/ISSUE_TEMPLATE/` | P1 |
| CI workflow | `.github/workflows/validate.yml` | P1 |
| MIT License | `LICENSE` | P0 |
| Updated README | `README.md` | P0 |
