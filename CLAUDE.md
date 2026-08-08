# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A public collection of generic, reusable Claude Code skills, organised by job role. Skills here must work for any user in any project. There is no application code: the "product" is the `skills/` tree plus the installer that copies it into a user's `~/.claude/skills/`.

## Commands

```bash
# Validate every SKILL.md (frontmatter + 500-line limit). Run before committing.
python3 scripts/validate_skill.py

# Validate skills.json parses (what CI runs first)
python3 -c "import json; json.load(open('skills.json'))"

# Scaffold a new skill and auto-register it in skills.json
python3 scripts/init_skill.py <skill-name> --role <role> --description "..." --tags "a,b"

# Install locally to test the packaging path
bash scripts/install.sh --list
bash scripts/install.sh --role pm            # global: ~/.claude/skills
bash scripts/install.sh --role pm --project  # project: ./.claude/skills
bash scripts/install.sh --all
bash scripts/install.sh --update
bash scripts/install.sh --uninstall qa
```

There is no test suite. `validate_skill.py` is the only checked gate, and it validates all skills at once. To check one skill, run the validator and grep its path.

## Architecture

Three surfaces must agree, and nothing enforces the agreement automatically:

1. `skills/` on disk. Two shapes only: `skills/by-role/<role>/<skill>/SKILL.md` and `skills/shared/<skill>/SKILL.md`. `install.sh` derives the source path from the registry key, so a skill in the wrong directory shape fails at install time, not at validation time.
2. `skills.json` - the registry, and the real source of truth for installation. Keys are `<role>/<skill-name>` (shared skills use the literal key `shared/<skill-name>`). `install.sh` reads only this file to decide what exists, which roles are offered by `--list`, and what `--all` installs. **A skill folder that is not registered here is invisible to users.**
3. `README.md` - the public skills table plus the "N skills across M roles" tagline. Purely manual, drifts silently.

`validate_skill.py` accepts the registry as an argument but never checks against it, so registry drift passes CI. Before finishing any skill work, reconcile all three:

```bash
python3 -c "
import json,pathlib
reg=set(json.load(open('skills.json'))['skills'])
disk={('shared/'+p.parent.name) if p.parts[1]=='shared' else p.parent.parent.name+'/'+p.parent.name
      for p in pathlib.Path('skills').rglob('SKILL.md')}
print('on disk, unregistered (invisible to install):', sorted(disk-reg))
print('registered, missing folder (install will error):', sorted(reg-disk))
"
```

Known current drift: several `marketing/*` and `shared/*` skills exist on disk but are unregistered, and the `content-creator/*` plus four `pm/*` entries are registered with no folder. Fix the reconciliation for any role you touch rather than adding to it.

Adding a new role means adding it to `VALID_ROLES` in `scripts/init_skill.py` first. `install.sh` discovers roles dynamically from `skills.json`, so no installer change is needed.

CI (`.github/workflows/validate.yml`) runs only on PRs touching `skills/**` or `skills.json`.

## Required Reading

`.claude/rules/prompt-writing.md` - the prompt-writing rubric (scored out of 100, target >95). Follow it when authoring or editing any skill description or body.

## Internal Skills

- `.claude/skills/create-skill/` - the Anthropic skill standard reference and creation guide.
- `.claude/skills/sync-skills/` - fetch and genericize skills from another machine's projects, deduplicate against this repo, and update `skills.json` plus `README.md`.

## Rules for Skills in This Repo

1. **No personal content.** Replace names, domains, newsletter titles, and project references with `[placeholder]` brackets. Standard placeholders: `[your niche]`, `[your newsletter]`, `[your-domain]`, `[your topic]`, `[your name]`, `[your audience]`.
2. **No project-specific paths or configs.** A skill must work when dropped into any `.claude/skills/` directory, with no dependency on another skill or on a project file.
3. **The `description` field is the trigger.** All "when to use" context goes there, not in the body. The body is the instruction set.
4. **Body under 500 lines** (validator hard-fails past it). Overflow goes into a `references/` subdirectory, and `SKILL.md` must say explicitly when to read each reference file.
5. **Every skill contains** a step-by-step workflow, anti-patterns, and a quality checklist.

## Skill Creation Standard (MANDATORY)

Follow the Anthropic skill-creator guidelines: https://github.com/anthropics/skills/tree/main/skills/skill-creator

Do not skip steps:

1. Capture intent - what the skill does and when it should trigger.
2. Write `SKILL.md` with the FIRAC body structure (Overview, Workflow, Anti-Patterns, Quality Checklist).
3. Create 2-3 realistic test prompts, then run with-skill and baseline subagents in the same turn.
4. Draft assertions while the runs are in progress.
5. Grade the results and show the user a qualitative comparison.
6. Iterate based on feedback.
7. Add `references/` files for domain data the skill needs but cannot hold inline (benchmarks, templates, authority hierarchies, procedure maps).
8. Point `SKILL.md` at those reference files with explicit read-when guidance.

When importing a skill from another project, read the source skill first, then strip every personal and project reference before it lands here.

## Commit Conventions

Lowercase, imperative mood, under 72 characters: `add linkedin-post skill`, `update install script`. Prefixes: add, update, remove, fix, sync.
