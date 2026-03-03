---
name: sync-skills
description: Fetch skills from projects on the current system, genericize them, and add to the claude-skills repository. Use when user says "sync skills", "fetch skills", "import skills from projects", or wants to pull skills from their local projects into this public repo.
---

# Sync Skills from Local Projects

## Overview

This skill scans projects on the current system for Claude Code skills (`.claude/skills/` directories), identifies new or updated skills, genericizes them by stripping project-specific content, and adds them to this repository.

## Workflow

### Step 1: Identify the Claude Skills Repo

The target repo is the `claude-skills` project. Confirm its location - it should be the current working directory or specified by the user.

### Step 2: Scan for Skills

Search for skills across local projects:

```
Find all directories matching: <projects-root>/*/.claude/skills/*/SKILL.md
```

Default projects root: `~/Documents/AI-PM/Projects/`

The user may override this with a different path. If invoking from a different system, the user will specify the projects root for that system.

For each found skill, collect:
- Skill name (directory name)
- Source project name
- SKILL.md content
- Any files in references/, assets/, scripts/ subdirectories

### Step 3: Deduplicate

Compare found skills against skills already in `skills/` directory of this repo:
- **New skill**: not present in repo - proceed to genericize
- **Updated skill**: present but source has newer/different content - show diff, ask user whether to update
- **Identical**: skip silently

### Step 4: Genericize

For each new or updated skill, apply these transformations:

**Replace personal references:**
- Author names, handles, usernames -> remove or replace with `[your name]`
- Newsletter/blog names -> `[your newsletter]`
- Specific domains (e.g., `name.substack.com`) -> `[your-domain]`
- Specific niche mentions tied to the author -> `[your niche]` or `[your topic]`

**Remove project-specific content:**
- File paths referencing the source project
- References to other project-specific skills, configs, or workflows
- Environment variables specific to the source project
- API keys, tokens, or credentials (should never exist, but check)

**Preserve:**
- The skill's core logic, frameworks, and checklists
- Generic examples and templates
- Anti-patterns and quality criteria
- References to general tools or platforms (LinkedIn, Substack, etc.)

**Verify:**
- YAML frontmatter has `name` and `description` fields
- Body is under 500 lines
- No personal/project-specific content remains
- Skill is self-contained (no broken references to removed content)

### Step 5: Add to Repo

For each genericized skill:

1. Copy to `skills/<skill-name>/SKILL.md` (and references/ if applicable)
2. Update `scripts/install.sh` - add to AVAILABLE_SKILLS array
3. Update `README.md` - add row to skills table with: name, category, description

### Step 6: Report

Output a summary:
- Skills added (with source project)
- Skills updated (with what changed)
- Skills skipped (already identical)
- Any skills that need manual review (couldn't fully genericize)

## Anti-Patterns

- **Don't blindly copy.** Always read the source skill first. Some skills are deeply project-specific and can't be genericized.
- **Don't merge skills.** If two projects have different versions of the same skill, ask the user which to keep.
- **Don't strip too much.** The goal is to remove personal references, not gut the content. Frameworks, examples, and checklists should survive intact.
- **Don't forget the supporting files.** Check for references/, assets/, scripts/ subdirectories.

## Quality Checklist

Before completing sync:

- [ ] Each new skill has valid YAML frontmatter (name + description)
- [ ] No personal names, domains, or project paths remain
- [ ] Placeholder brackets used consistently: `[your niche]`, `[your newsletter]`, `[your-domain]`, `[your topic]`, `[your name]`
- [ ] install.sh AVAILABLE_SKILLS array is updated and sorted
- [ ] README.md skills table is updated
- [ ] Each skill is self-contained and works standalone
- [ ] Body under 500 lines per SKILL.md
