# Claude Skills Repository

A public collection of generic, reusable Claude Code skills. Skills here must work for any user in any project - no personal or project-specific content.

## Project Structure

```
claude-skills/
  skills/                  # Generic skills (each with SKILL.md)
  scripts/
    install.sh             # User-facing installer
  .claude/
    skills/
      create-skill/        # Internal skill: Anthropic skill standard reference + creation guide
      sync-skills/         # Internal skill: fetch + genericize skills from other systems
  CLAUDE.md                # This file (project instructions)
  README.md                # Public-facing documentation
```

## Rules for Skills in This Repo

1. **No personal content.** Replace names, domains, newsletter titles, project references with `[placeholder]` brackets.
2. **No project-specific paths or configs.** Skills must work when dropped into any `.claude/skills/` directory.
3. **Every skill follows Anthropic skill standard.** YAML frontmatter with `name` + `description`, markdown body under 500 lines, overflow in `references/` subdirectory.
4. **The `description` field is the trigger.** Put all "when to use" context there. Body is the instruction set.
5. **Each skill must include:** a workflow (step-by-step), anti-patterns, and a quality checklist.
6. **Placeholders to use:** `[your niche]`, `[your newsletter]`, `[your-domain]`, `[your topic]`, `[your name]`, `[your audience]`.

## Skill Creation Standard (MANDATORY)

**Always follow the Anthropic skill-creator guidelines when creating or updating any skill:**
https://github.com/anthropics/skills/tree/main/skills/skill-creator

The full process (do not skip steps):
1. Capture intent - understand what the skill should do and when it should trigger
2. Write the SKILL.md following the FIRAC body structure (Overview, Workflow, Anti-Patterns, Quality Checklist)
3. Create 2-3 realistic test prompts and run with-skill + baseline subagents in the same turn
4. Draft assertions while runs are in progress
5. Grade results and show user a qualitative comparison
6. Iterate on the skill based on feedback
7. Add reference files in `references/` for any domain-specific data the skill references but cannot include inline (benchmarks, templates, authority hierarchies, procedure maps)
8. Update SKILL.md to point to reference files with explicit guidance on when to read each one

## When Adding a Skill

- Follow the Anthropic skill-creator process above (mandatory).
- Scaffold with `python3 scripts/init_skill.py <name> --role <role>` - registers in `skills.json` automatically.
- If adding a new role, add it to `VALID_ROLES` in `scripts/init_skill.py` first.
- Read the source skill from the original project first.
- Strip all personal/project references. Replace with placeholders.
- Verify the skill works standalone - no dependencies on other skills or project-specific files.
- Run `python3 scripts/validate_skill.py` before committing.
- Update `README.md` skills table (skill count + role count in tagline, add role section).

## When Syncing from Another System

Use `/sync-skills` to fetch skills from another machine's projects. The skill handles:
- Scanning all projects under a given root for `.claude/skills/` directories
- Deduplicating against skills already in this repo
- Genericizing content (stripping project-specific references)
- Updating skills.json and README.md

## Commit Conventions

- Lowercase, imperative mood: `add linkedin-post skill`, `update install script`
- Prefixes: add, update, remove, fix, sync
- Short first line (under 72 chars)
