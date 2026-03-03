# Claude Skills

> Role-based Claude Code skills for every team. Install what your team needs, skip what they don't.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Validate Skills](https://github.com/[your-username]/claude-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/[your-username]/claude-skills/actions/workflows/validate.yml)

## What This Is

A curated collection of [Claude Code](https://claude.ai/claude-code) skills organized by job role. Each skill is a packaged workflow that Claude invokes automatically - or that you trigger with a `/skill-name` command.

**PM?** Install PM skills. **QA?** Install QA skills. No bloat, no irrelevant prompts.

## Install

```bash
# Clone once
git clone https://github.com/[your-username]/claude-skills.git
cd claude-skills

# Install skills for your role
bash scripts/install.sh --role pm
bash scripts/install.sh --role qa
bash scripts/install.sh --role content-creator

# Install for multiple roles
bash scripts/install.sh --role pm,content-creator

# Install everything
bash scripts/install.sh --all

# See what's available
bash scripts/install.sh --list
```

Skills install to `~/.claude/skills/` and are immediately available in any Claude Code session.

## Available Skills

### Product Manager (`--role pm`)
| Skill | What it does |
|-------|-------------|
| 11-star-framework | Apply the 11-star experience framework to product decisions |

### Content Creator (`--role content-creator`)
| Skill | What it does |
|-------|-------------|
| linkedin-post | Write LinkedIn posts for [your niche] |
| reddit-post | Write Reddit posts for [your community] |
| newsletter-ideation | Ideate newsletter topics |
| substack-post | Write full Substack posts |
| substack-notes | Write Substack notes |
| substack-toc | Generate Substack table of contents |

### Shared (installed with every role)
| Skill | What it does |
|-------|-------------|
| presentation-builder | Build structured presentations for any audience |

### Coming Soon
- `--role engineer` - Code review, debugging, PR workflows
- `--role qa` - Test plans, bug reports, coverage analysis
- `--role designer` - Design critique, component specs, handoff docs
- `--role devops` - Incident response, runbooks, deployment checklists

**Want to add skills for your role?** [Contribute](#contributing)

## Personalize Skills for Your Context

Generic skills get smarter when they know your context. After installing, run:

```bash
bash scripts/install.sh --role qa --init
```

This creates `~/.claude/skills/skill-context.md` - a file that skills read at invocation time to tailor output to your industry, stack, and compliance needs. Edit it anytime.

Example `skill-context.md`:
```markdown
- Industry: Fintech
- Stack: React Native + Node.js
- Compliance: PCI-DSS
```

Skills stay generic and update-safe. Your context stays persistent.

## Update Skills

```bash
bash scripts/install.sh --update
```

## Remove Skills

```bash
bash scripts/install.sh --uninstall qa
```

## Contributing

We welcome skills for every role and industry. Adding a skill takes about 10 minutes.

See [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the full guide. The short version:

1. Create `skills/by-role/<role>/<skill-name>/SKILL.md`
2. Register it in `skills.json`
3. Run `python3 scripts/validate_skill.py`
4. Open a PR

CI validates every PR automatically.

## License

MIT - see [LICENSE](LICENSE)
