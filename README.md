# Claude Code Skills

A collection of reusable skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Each skill is a self-contained `SKILL.md` that teaches Claude a specific content creation or product thinking pattern. Drop them into your `.claude/skills/` directory and invoke with `/skill-name`.

## Skills

| Skill | Category | Description |
|-------|----------|-------------|
| [linkedin-post](skills/linkedin-post/) | Content | Write high-performing LinkedIn posts with hook patterns, post structures, and anti-patterns |
| [reddit-post](skills/reddit-post/) | Content | Write Reddit posts that earn upvotes without triggering self-promotion flags |
| [newsletter-ideation](skills/newsletter-ideation/) | Content | Generate 5-7 topic angles using SCAMPER, JTBD, Contrarian, and other frameworks |
| [substack-post](skills/substack-post/) | Content | Write long-form Substack articles with narrative arc and sustained depth |
| [substack-notes](skills/substack-notes/) | Content | Generate short-form Substack notes using 10 proven structural formulas |
| [substack-toc](skills/substack-toc/) | Content | Create numbered table of contents with working Substack anchor links |
| [presentation-builder](skills/presentation-builder/) | Productivity | Transform ideas into structured slide content for pitch decks, reviews, and talks |
| [11-star-framework](skills/11-star-framework/) | Product | Rate any product or feature on the 11-star experience scale (Brian Chesky method) |

## Install

### Option 1: Copy manually

Copy any skill folder into your Claude Code skills directory:

```bash
cp -r skills/linkedin-post ~/.claude/skills/
```

### Option 2: Use the install script

```bash
# Install specific skills
./scripts/install.sh linkedin-post substack-post

# Install all skills
./scripts/install.sh --all

# Install to a custom directory
./scripts/install.sh --target ./my-project/.claude/skills/ --all

# List available skills
./scripts/install.sh --list
```

## Customizing

Many skills contain placeholder brackets like `[your niche]`, `[your newsletter]`, or `[your-domain]`. After installing, edit the `SKILL.md` to replace these with your specifics:

- `[your niche]` - your professional focus area (e.g., "AI/tech/PM")
- `[your newsletter]` - your newsletter name
- `[your-domain]` - your Substack domain (e.g., `yourname.substack.com`)
- `[your topic]` - the subject area you write about

## Skill Format

Each skill follows the [Anthropic skill standard](https://github.com/anthropics/skills/tree/main/skills/skill-creator):

```
skills/
  skill-name/
    SKILL.md          # YAML frontmatter (name + description) + instructions
    references/       # Optional: examples, templates
```

The `description` field in frontmatter controls when Claude suggests the skill. The body contains the actual instructions, frameworks, and quality checklists.

## Contributing

To add a new skill:

1. Create a folder under `skills/` with a descriptive kebab-case name
2. Add a `SKILL.md` with YAML frontmatter (`name` + `description`) and a markdown body
3. Keep the body under 500 lines - use `references/` for overflow
4. Remove any personal or project-specific content - use `[placeholder]` brackets instead
5. Include at least: a workflow (step-by-step), anti-patterns, and a quality checklist
6. Open a PR

## License

MIT
