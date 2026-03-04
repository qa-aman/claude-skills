# Claude Skills

> Role-based Claude Code skills for every team. Install what your team needs, skip what they don't.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Validate Skills](https://github.com/qa-aman/claude-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/qa-aman/claude-skills/actions/workflows/validate.yml)

## What This Is

A curated collection of [Claude Code](https://claude.ai/claude-code) skills organized by job role. Each skill is a packaged workflow grounded in a proven book or methodology - Claude invokes it automatically, or you trigger it with a `/skill-name` command.

**95 skills across 17 roles.** PM, QA, Engineer, Designer, DevOps, Leadership, Program Delivery, Customer Success, Recruiter, Consultant, Sales, Marketing, Founder, Data Engineer, Security, Researcher, and more.

## Install

```bash
# Clone once
git clone https://github.com/qa-aman/claude-skills.git
cd claude-skills

# Install skills for your role
bash scripts/install.sh --role pm
bash scripts/install.sh --role qa
bash scripts/install.sh --role engineer

# Install for multiple roles
bash scripts/install.sh --role pm,qa

# Install everything
bash scripts/install.sh --all

# See what's available
bash scripts/install.sh --list
```

## Global vs Project Install

Skills can be installed in two scopes:

| Scope | Command | Where | Available |
|-------|---------|-------|-----------|
| **Global** (default) | `--global` or no flag | `~/.claude/skills/` | Every Claude Code session, across all projects |
| **Project** | `--project` | `./.claude/skills/` | Only when Claude Code is opened in that specific project |

**Global install** is right for most people. Your role skills (write-prd, qa-strategy, feedback-delivery) follow you everywhere — not tied to any single codebase.

```bash
# Global — skills available in all projects (default)
bash scripts/install.sh --role pm

# Project — skills available in this project only
bash scripts/install.sh --role pm --project
```

**When to use `--project`:** Team-specific workflows where everyone on the project needs the same skills, or project-specific conventions that don't apply to your other work.

## Available Skills

### Product Manager (`--role pm`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `write-prd` | Write a PRD from a brief or problem statement | Shape Up |
| `write-user-stories` | Convert requirements into user stories with acceptance criteria | User Story Mapping - Patton |
| `prioritization` | Prioritize a backlog using RICE or MoSCoW scoring | Continuous Discovery Habits - Torres |
| `feature-spec` | Write a concise feature spec one-pager for engineering handoff | Shape Up - Singer |
| `okr-writer` | Write measurable OKRs from strategic goals or intent | Measure What Matters - Doerr |
| `competitive-analysis` | Structure a competitive analysis for a feature, product, or market | Blue Ocean Strategy |
| `product-discovery` | Run structured discovery to identify what to build before building it | Inspired - Cagan |
| `team-brief` | Write an empowered team brief giving engineers a problem, not a solution | Empowered - Cagan |
| `outcome-vs-output` | Audit a roadmap to distinguish outcomes from outputs | Escaping the Build Trap - Perri |
| `retention-design` | Design habit-forming product features | Hooked - Eyal |
| `experiment-design` | Design product experiments with build-measure-learn loops | Lean Startup - Ries |
| `product-market-fit` | Assess and improve product-market fit | Lean Product Playbook - Olsen |
| `11-star-framework` | Apply 11-star experience framework to product decisions | The Experience Economy |

### QA (`--role qa`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `qa-test-design` | Write test cases, acceptance criteria, API test specs | The Art of Software Testing - Myers |
| `qa-execution` | Run smoke tests, regression cycles, and SBTM sessions | How Google Tests Software |
| `qa-strategy` | Test strategy docs, coverage matrices, risk prioritization | Agile Testing - Crispin |
| `qa-metrics` | Quality dashboards, defect density, escape rate, trend reporting | Accelerate - Forsgren |
| `qa-release` | Go/no-go decisions, release sign-off, defect triage | SRE - Google |
| `risk-based-testing` | Allocate testing effort using Google's SET/SWE/TE model | How Google Tests Software |
| `exploratory-testing` | Run charter-based testing sessions with HICCUPPS heuristics | Explore It! - Hendrickson |

### Engineer (`--role engineer`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `code-review` | Review code for quality, bugs, and design issues | Clean Code - Martin |
| `debug` | Debug systematically using reproduce-isolate-fix methodology | Pragmatic Programmer |
| `write-tests` | Write unit and integration tests using TDD red-green-refactor | TDD by Example - Beck |
| `tech-debt` | Document, scope, and prioritize technical debt | Working Effectively with Legacy Code - Feathers |
| `api-design` | Design clean, consistent REST or GraphQL APIs | Philosophy of Software Design - Ousterhout |
| `pr-description` | Write clear, reviewable pull request descriptions | Pragmatic Programmer |

### Designer (`--role designer`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `design-critique` | Critique a design for usability, hierarchy, and accessibility | Design of Everyday Things - Norman |
| `ux-audit` | Audit a user flow for friction and drop-off points | Don't Make Me Think - Krug |
| `component-spec` | Write a component spec for engineering handoff | Atomic Design - Frost |
| `design-system-doc` | Document a design system component with usage rules and tokens | Atomic Design - Frost |

### DevOps (`--role devops`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `incident-response` | Structure and run an incident response | SRE - Google |
| `runbook` | Write an operational runbook for a service or on-call procedure | SRE - Google |
| `deployment-checklist` | Run a pre/post-deployment checklist | Checklist Manifesto + Accelerate |
| `postmortem` | Write a blameless postmortem after a production incident | SRE + Dekker |

### Leadership (`--role leadership`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `team-health-check` | Assess team health across trust, conflict, commitment, accountability, results | Five Dysfunctions - Lencioni |
| `feedback-delivery` | Deliver feedback using care personally + challenge directly | Radical Candor - Kim Scott |
| `one-on-one` | Run structured 1:1s with direct reports | Manager's Path + High Output Management |
| `leadership-transition` | Navigate a new leadership role using 30/60/90 framework | First 90 Days - Watkins |
| `team-multiplier` | Shift from Diminisher to Multiplier leadership style | Multipliers - Wiseman |
| `psychological-safety` | Build conditions where the team speaks up without fear | Leaders Eat Last - Sinek |

### Program Delivery Manager (`--role program-delivery-manager`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `dependency-mapping` | Surface and visualize hidden cross-team dependencies | Making Work Visible - DeGrandis |
| `release-planning` | Build a velocity-based release roadmap with risk buffers | Agile Estimating and Planning - Cohn |
| `delivery-risk-review` | Identify, score, and mitigate delivery risks | The Phoenix Project |
| `milestone-scoping` | Scope a milestone to fixed time with variable scope | Shape Up + Art of Project Management |
| `program-status-report` | Write a structured program status report with RAG and decisions needed | Delivery management best practices |
| `flow-metrics-review` | Analyze cycle time, WIP, throughput, and DORA metrics | Making Work Visible + Accelerate |

### Customer Success (`--role customer-success`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `qbr-deck` | Build a structured Quarterly Business Review deck | Customer Success - Mehta et al. |
| `churn-risk-analysis` | Identify churn risk flags and generate intervention playbook | Customer Success - Mehta et al. |
| `escalation-playbook` | De-escalate a customer crisis with a structured response framework | CS de-escalation frameworks |
| `health-scorecard` | Build a customer health scorecard across six dimensions | Customer Success - Mehta et al. |
| `onboarding-plan` | Design a 100-day customer onboarding plan with phase gates | Never Lose a Customer Again - Coleman |
| `expansion-discovery` | Identify expansion signals and structure upsell conversations | Farm Don't Hunt - Nirpaz |

### Recruiter (`--role recruiter`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `job-description` | Write a performance-based JD anchored to 90-day outcomes | Hire With Your Head - Adler |
| `interview-scorecard` | Build a structured scorecard with competencies and A/B/C rubric | Who - Smart & Street |
| `candidate-debrief` | Run a structured debrief with calibration protocol | Who + Work Rules! - Bock |
| `offer-letter` | Construct a compelling offer with comp philosophy and equity explanation | The Alliance - Hoffman |
| `sourcing-strategy` | Build a multi-channel pipeline with outbound templates | Recruiting in the Age of Googlization |
| `intake-meeting` | Run a recruiter-hiring manager intake to define scorecard and process | Who + Topgrading - Smart |

### Consultant (`--role consultant`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `client-proposal` | Write a proposal with situation, approach, deliverables, and value ROI | Consulting Bible - Weiss |
| `engagement-scoping` | Define scope, success criteria, roles, and boundaries | Flawless Consulting - Block |
| `exec-summary` | Write an executive summary using SCQA structure | Pyramid Principle - Minto |
| `issue-tree` | Decompose a problem MECE and generate hypotheses | McKinsey Way + Bulletproof Problem Solving |
| `status-report` | Write a client status report with RAG, blockers, and decisions needed | Consulting best practices |
| `findings-presentation` | Structure a findings deck using situation-complication-resolution | Pyramid Principle - Minto |

### Sales (`--role sales`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `discovery-call` | Structure a discovery call with SPIN question sequence | SPIN Selling - Rackham |
| `deal-qualification` | Qualify a deal using MEDDIC framework | MEDDIC methodology |
| `objection-handling` | Handle objections using tactical empathy and labeling | Never Split the Difference - Voss |
| `sales-proposal` | Write a proposal using teach-tailor-take-control structure | The Challenger Sale - Dixon |
| `account-plan` | Build a strategic account plan with key players and expansion paths | Strategic Selling - Miller Heiman |

### Marketing (`--role marketing`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `positioning-doc` | Write a positioning doc using competitive alternatives framework | Positioning - Ries & Trout |
| `customer-persona` | Build a buyer persona anchored to buying context and JTBD | Obviously Awesome - Odden |
| `messaging-framework` | Build brand messaging using customer-as-hero structure | Building a StoryBrand - Miller |
| `campaign-brief` | Write a campaign brief with OMTM, audience, and channel plan | Lean Analytics - Croll & Yoskovitz |
| `growth-experiment` | Design a channel growth experiment using Bullseye Framework | Traction - Weinberg & Mares |

### Founder (`--role founder`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `customer-discovery` | Run structured discovery interviews without leading the witness | The Mom Test - Fitzpatrick |
| `pitch-narrative` | Craft a compelling startup pitch using secret-first framework | Zero to One - Thiel |
| `business-model-canvas` | Design and stress-test a business model canvas | Lean Startup - Ries |
| `investor-update` | Write a structured monthly/quarterly investor update | Venture-backed startup norms |
| `fundraising-email` | Write a cold investor outreach email using traction-first framing | Traction - Weinberg |

### Data Engineer (`--role data-engineer`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `pipeline-design-doc` | Document a data pipeline's architecture, data flow, contracts, and failure modes | Fundamentals of Data Engineering - Reis & Housley |
| `schema-spec` | Write a schema spec with field definitions, constraints, business rules, and evolution policy | DDIA - Kleppmann |
| `etl-runbook` | Operational runbook for ETL jobs covering monitoring, diagnosis, and backfill | Data Pipelines Pocket Reference - Densmore |

### Security (`--role security`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `threat-model` | Identify and prioritize threats using STRIDE per system component | Threat Modeling - Shostack |
| `pentest-scope` | Define pentest targets, rules of engagement, and deliverables | Penetration Testing - Weidman |
| `vuln-report` | Write a vulnerability report with reproduction steps, impact, and remediation | Penetration Testing - Weidman |

### Researcher (`--role researcher`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `literature-review` | Synthesize prior research by theme, surface contradictions, frame the gap | Research Design - Creswell |
| `hypothesis-framing` | Write falsifiable hypotheses with operationalized variables and null/alternative forms | Research Methodology - Kumar |
| `study-design` | Design a study with method selection, sample size, procedure, instruments, and analysis plan | Research Design - Creswell |

### Shared (installed with every role)
| Skill | What it does |
|-------|-------------|
| `presentation-builder` | Build structured presentations for any audience |

## Personalize Skills for Your Context

Skills stay generic and immutable. Personalization lives in a separate file that skills read at invocation time - your edits are never overwritten by `--update`.

**Step 1:** Run install with `--init` to create your context file in the current project:
```bash
bash scripts/install.sh --role qa --init
# Creates ./.claude/skills/skill-context.md in your current directory
```

**Step 2:** Fill in your values:
```markdown
# .claude/skills/skill-context.md

- Industry: Fintech
- Stack: React Native + Node.js
- Test framework: Playwright
- Defect tracker: Jira
- Compliance: PCI-DSS
```

Skills installed globally (`~/.claude/skills/`) automatically read your project-level context file when Claude Code is opened in that project.

See [`skill-context.example.md`](skill-context.example.md) for the full template with all role-specific fields.

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
