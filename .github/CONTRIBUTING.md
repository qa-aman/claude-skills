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

2. **Create your skill folder and SKILL.md**

   Every skill needs a `SKILL.md` with this structure:
   ```
   ---
   name: your-skill-name
   description: When to use this skill. This is the trigger - put all context here.
   ---

   ## Workflow
   [step-by-step instructions]

   ## Anti-Patterns
   [what NOT to do]

   ## Quality Checklist
   - [ ] item 1
   ```

3. **Use placeholders - no personal references**

   Replace specifics with: `[your industry]`, `[your stack]`, `[your team]`, `[your newsletter]`, `[your niche]`

4. **Register in skills.json**
   ```json
   "role/skill-name": {
     "role": "role",
     "description": "One line description",
     "tags": ["tag1", "tag2"]
   }
   ```

5. **Validate locally**
   ```bash
   python3 scripts/validate_skill.py
   ```

6. **Open a PR** - CI validates automatically.

## Skill Quality Bar

A good skill:
- Solves a real, recurring task for that role
- Works for any user in any project
- Has a clear trigger in the `description` field
- Includes a workflow, anti-patterns, and quality checklist
- Uses placeholders instead of specifics

## Questions?

Open an issue with the "New Skill Request" template.
