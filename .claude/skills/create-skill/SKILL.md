---
name: create-skill
description: Create or update Claude Code skills following Anthropic's official skill standard. Use when user says "create a skill", "new skill", "write a skill", "update a skill", "skill standard", or any time a new SKILL.md file needs to be created. Also use when reviewing existing skills for standards compliance.
---

# Skill Creation Guide

Reference for creating skills that follow the Anthropic skill standard (github.com/anthropics/skills).

## Skill Anatomy

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions (<500 lines)
└── Bundled Resources (optional)
    ├── scripts/    - Executable code for deterministic tasks
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Templates, icons, fonts for outputs
```

## Progressive Disclosure

Skills load in three layers:
1. **Metadata** (name + description) - Always in context (~100 words)
2. **SKILL.md body** - Loaded when skill triggers (<500 lines)
3. **Bundled resources** - Loaded as needed (unlimited size)

Keep SKILL.md under 500 lines. If approaching the limit, move content to `references/` with clear pointers about when to read each file.

## YAML Frontmatter

Two required fields:

```yaml
---
name: skill-name
description: What the skill does AND when to trigger it. All "when to use" context goes here, not in the body.
---
```

### Description is the Trigger

The `description` field is the primary mechanism for skill invocation. Claude tends to undertrigger skills, so descriptions should be slightly pushy.

**Weak:**
"Generate LinkedIn posts for professional audiences."

**Strong:**
"Write high-performing LinkedIn posts. Use when user says 'write a LinkedIn post', 'LinkedIn content', 'post for LinkedIn', 'professional audience post', or wants to share insights, lessons, or updates with a professional network - even if they don't explicitly say LinkedIn."

Include:
- What the skill does (1 sentence)
- Explicit trigger phrases users might say
- Adjacent contexts where the skill applies ("even if they don't explicitly say X")

## Body Structure

Every skill body should include these components:

### 1. Overview (optional, 1-2 paragraphs)
What this skill does and the critical distinction that shapes how it works.

### 2. Workflow (required)
Step-by-step process. Use `### Step N:` headings. Each step should be actionable and specific.

### 3. Anti-Patterns (required)
What NOT to do. Format as Bad/Good pairs so the model can calibrate:

```markdown
## Anti-Patterns

**1. Descriptive name**
Bad: "example of wrong approach"
Good: "example of correct approach"
```

### 4. Quality Checklist (required)
Checkbox list the model uses to verify output before delivering:

```markdown
## Quality Checklist

- [ ] Check 1
- [ ] Check 2
```

## Writing Style

### Explain the "Why" Instead of Bare Directives

The model follows instructions better when it understands the reasoning. Heavy-handed MUSTs without context are less effective than explaining why something matters.

**Weak:**
"Never exceed 5 bullets per slide."

**Strong:**
"Keep slides to 3-5 bullets. Beyond 5, the audience reads instead of listening - the slide competes with the speaker instead of supporting them."

### Use Imperative Form
Write instructions as commands: "Open with a personal admission" not "You should open with a personal admission."

### Generalize, Don't Overfit
Write instructions that work across varied inputs. Avoid narrow tweaks targeting only specific examples - look for underlying patterns.

### Examples Are Valuable
Include concrete examples. Format with Input/Output or Bad/Good pairs. Examples calibrate the model's output better than abstract rules.

## Placeholders (for this repo)

When creating skills for the claude-skills public repo, replace all personal/project references:
- `[your name]` - personal name
- `[your newsletter]` - newsletter or blog name
- `[your-domain]` - website domain
- `[your niche]` - professional niche
- `[your topic]` - specific subject area
- `[your audience]` - target audience

## Creation Checklist

Before finalizing any skill:

- [ ] YAML frontmatter has `name` and `description`
- [ ] Description is pushy with multiple trigger phrases
- [ ] Body is under 500 lines
- [ ] Workflow has clear numbered steps
- [ ] Anti-patterns section exists with Bad/Good pairs
- [ ] Quality checklist exists
- [ ] Directives explain "why", not just "what"
- [ ] Examples are concrete and specific
- [ ] No personal/project-specific content (if for public repo)
- [ ] Overflow content moved to `references/` with clear pointers
