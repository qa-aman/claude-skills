# Claude Skills Repo - Design Document

## Goal
Public GitHub repo of Claude Code skills organized by job role. Target: 1M stars, community contributions via PRs, used by teams across industries.

---

## Key Decisions

### License
**MIT** - most permissive, zero friction for adoption, highest reach. Aligns with React, Vue, Tailwind. No attribution overhead.

### Skill Organization
**By job role**, not by industry or function. Industry-specific needs are solved via `[placeholder]` content inside skills, not folder structure.

Roles planned:
- `pm/`
- `engineer/`
- `qa/`
- `designer/`
- `content-creator/`
- `devops/`

**Industry rule:** If a skill is genuinely different by industry (e.g., compliance testing in Fintech), name it explicitly - `qa/compliance-testing-fintech` - never a subfolder. Infinite subfolders kill discoverability.

**Scope rule:** Action types (content creation, code review, testing) are absorbed into the role folder, not a separate dimension.

### Folder Structure
```
claude-skills/
  skills/
    by-role/
      pm/
      engineer/
      qa/
      designer/
      content-creator/
      devops/
    shared/              # skills useful across all roles (commit, debug, code-review)
  scripts/
    install.sh           # role-filtered installer
    init_skill.py        # scaffold new skill
    validate_skill.py    # validate SKILL.md format
  docs/
    plans/               # design docs (this file)
  .github/
    CONTRIBUTING.md
    PULL_REQUEST_TEMPLATE.md
    ISSUE_TEMPLATE/
    workflows/           # CI validation
  CLAUDE.md
  README.md
  skills.json            # machine-readable skill registry
```

### Installation Model
Single repo (all stars in one place). Install script handles role filtering - no need to clone subfolders separately.

```bash
install.sh --role qa              # install only QA skills
install.sh --role pm,qa           # install multiple roles
install.sh --all                  # install everything
install.sh --update               # update installed skills to latest
install.sh --uninstall qa         # remove a role's skills
install.sh --role qa --init       # install + prompt for context setup
```

### Personalization Model (skill-context.md)
Skills stay generic and immutable. Personalization lives in a separate context file that skills read at invocation time.

```
~/.claude/skills/
  qa/write-test-plan/
    SKILL.md              # generic, never modified by users
  skill-context.md        # user's project context, read by all skills
```

`skill-context.md` example:
```markdown
- Industry: Fintech
- Stack: React Native + Node.js
- Test framework: Jest + Appium
- Compliance: PCI-DSS
```

**Why this model:** Modifying skill files directly creates update conflicts - `install.sh --update` would overwrite customizations. Separating context from skills keeps both intact. Skills stay immutable, context stays persistent.

---

## What Needs to Be Built

### P0 - Core Product
- [ ] Folder structure (by-role + shared)
- [ ] `skills.json` registry - replaces hardcoded array in install.sh
- [ ] Install script with `--role` filter, multi-role support, `--update`, `--uninstall`, `--init`
- [ ] `CONTRIBUTING.md` + PR template - ensures consistent skill quality from contributors

### P1 - Community Scale
- [ ] GitHub Actions CI - validates SKILL.md frontmatter, checks skills.json registration, blocks personal content
- [ ] `skill-context.md` spec + `--init` flow in install script
- [ ] Issue templates (new skill request, bug report)

### P2 - Discoverability
- [ ] GitHub Pages skill browser - filterable by role, searchable, shows all skills before install

### P3 - Long-term Maintenance
- [ ] Skill versioning - `version` field in frontmatter + per-skill changelog

---

## What Makes This Hit 1M Stars
- One-command install with role filter
- Beautiful README with demo GIF
- Active response to issues and PRs
- Clear CONTRIBUTING.md so anyone can add a skill
- `skills.json` registry - contributors just add a folder, no script edits needed
- `skill-context.md` - personalization without fork
- Featured in AI/dev tooling newsletters and communities

---

## Constraints
- No personal content in skills - use `[your name]`, `[your niche]`, `[your industry]` placeholders
- Every skill: `SKILL.md` with YAML frontmatter (`name` + `description`), body under 500 lines
- `description` field is the trigger mechanism - all "when to use" context goes there
- `shared/` skills must work for all roles - no role-specific assumptions
- Skills stay immutable - personalization via `skill-context.md`, never by editing skill files
