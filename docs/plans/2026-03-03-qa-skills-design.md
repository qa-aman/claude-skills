# QA Skills Design

**Date:** 2026-03-03
**Status:** Approved

## Goal

Add a `qa` role to the claude-skills repo with 5 skills covering the full day-to-day workflow of both individual contributor QA engineers and QA leads/managers.

## Skills

| Skill | Role Level | Coverage |
|-------|-----------|----------|
| `qa-test-design` | IC | test cases, acceptance criteria, API test specs, PR testability review |
| `qa-execution` | IC | smoke tests, regression runs, exploratory sessions, release checklists |
| `qa-release` | Lead | go/no-go decisions, sign-off reports, defect triage |
| `qa-strategy` | Lead | test strategy docs, risk-based prioritization, coverage analysis |
| `qa-metrics` | Lead | quality dashboards, defect density, escape rate, trend reporting |

## Directory Structure

```
skills/by-role/qa/
  qa-test-design/SKILL.md
  qa-execution/SKILL.md
  qa-release/SKILL.md
  qa-strategy/SKILL.md
  qa-metrics/SKILL.md
```

## Design Decisions

**Why 5 skills over 2 (by role) or 8+ (by task):**
- 2 skills (IC + Lead): body becomes too large, trigger descriptions overlap, harder to load selectively
- 8 skills (one per task): install overhead, descriptions become too granular, harder to maintain
- 5 skills (by workflow stage): distinct triggers per stage, each body stays under 500 lines, maps to how QA actually thinks

**Why workflow-stage grouping works:**
Each stage has a distinct mindset, input type, and output format. A QA engineer writing test cases is not in release sign-off mode. Natural separation = accurate triggering.

**`qa-strategy` vs `qa-metrics` split:**
Strategy = what to test and why (planning artifact). Metrics = how well we tested (reporting artifact). Different triggers, different outputs, different audiences.

## Anthropic Skill Standard Compliance

- Each skill: YAML frontmatter (name + description), workflow, anti-patterns, quality checklist
- Descriptions are "pushy" to prevent undertriggering
- All bodies target under 500 lines
- Generic placeholders only - no personal/project-specific content
- Registered in `skills.json`, listed in `README.md`
