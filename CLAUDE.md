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

## When Adding a Skill

- Use `/create-skill` for guidance on Anthropic's official skill standard (description triggers, body structure, writing style).
- Read the source skill from the original project first.
- Strip all personal/project references. Replace with placeholders.
- Verify the skill works standalone - no dependencies on other skills or project-specific files.
- Scaffold with `python3 scripts/init_skill.py <name> --role <role>` - registers in `skills.json` automatically.
- Run `python3 scripts/validate_skill.py` before committing.
- Update `README.md` skills table.

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
