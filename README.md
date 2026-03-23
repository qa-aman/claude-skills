# Claude Skills

> Role-based Claude Code skills for every team. Install what your team needs, skip what they don't.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Validate Skills](https://github.com/qa-aman/claude-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/qa-aman/claude-skills/actions/workflows/validate.yml)

## What This Is

A curated collection of [Claude Code](https://claude.ai/claude-code) skills organized by job role. Each skill is a packaged workflow grounded in a proven book or methodology - Claude invokes it automatically, or you trigger it with a `/skill-name` command.

**129 skills across 21 roles.** PM, QA, Engineer, Designer, DevOps, Leadership, Program Delivery, Customer Success, Recruiter, Consultant, Sales, Marketing, Founder, Data Engineer, Data Scientist, Security, Researcher, Accountant, Business Analyst, Content Creator, and more.

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
| `discovery-interview-prep` | Generate user research interview scripts using Mom Test principles | The Mom Test - Fitzpatrick |
| `epic-breakdown` | Decompose large epics into sprint-ready sub-epics using 9 splitting patterns | Agile Estimating and Planning - Cohn |
| `go-to-market-checklist` | Generate pre-launch readiness checklists for feature releases | Crossing the Chasm - Moore |
| `metrics-dashboard-spec` | Generate dashboard specifications from product spec success metrics | Lean Analytics - Croll |
| `opportunity-solution-tree` | Build OSTs mapping outcome to opportunities, solutions, experiments | Continuous Discovery Habits - Torres |
| `persona-updater` | Update user personas from new feedback, pilot data, or research | About Face - Cooper |
| `pilot-debrief` | Synthesize pilot observations into structured debrief reports | Lean Startup - Ries |
| `compliance-auditor` | Audit feature specs against India's DPDP Act 2023 — consent, children's data, retention, rights | DPDP Act 2023 |
| `product-thinking` | Run 5 structured exercises before writing a spec (problem, 11-star, positioning, principles, vision) | Inspired - Cagan + Shape Up - Singer |
| `release-notes-writer` | Generate user-facing and internal release notes from specs and tickets | Technical writing best practices |
| `retro-synthesizer` | Synthesize sprint retro notes into categorized action items and patterns | Agile Retrospectives - Derby & Larsen |
| `risk-register` | Maintain a centralized living risk register with likelihood x impact matrix | The Art of Project Management - Berkun |
| `spec-reviewer` | Quality gate for specs — pass/fail scorecard before stakeholder review | Shape Up + enterprise spec standards |
| `sprint-review-prep` | Generate sprint review talking points and demo scripts | Agile ceremonies best practices |
| `stakeholder-update` | Generate structured weekly status updates for leadership | Radical Candor - Kim Scott |
| `workshop-synthesizer` | Distill workshop notes into ranked themes and roadmap findings | Design Sprint - Knapp |
| `wsjf-scorer` | Calculate WSJF scores for data-driven feature prioritization | SAFe - Leffingwell |

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

### Accountant (`--role accountant`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `financial-statement-review` | Analyze income statement, balance sheet, and cash flow to surface performance signals and red flags | Financial Intelligence - Berman & Knight; The Interpretation of Financial Statements - Graham |
| `month-end-close` | Run a controlled period-end close: cutoff, adjusting entries, reconciliations, trial balance review, and sign-off | Intermediate Accounting - Kieso, Weygandt, Warfield |
| `audit-workpaper` | Write a reviewable workpaper with objective, population, procedures, tick marks, and conclusion anchored to assertions | Auditing and Assurance Services - Arens, Elder, Beasley |
| `budget-variance-analysis` | Decompose budget vs. actual variances into price, volume, and mix; write the management commentary | Cost Accounting: A Managerial Emphasis - Horngren, Datar, Rajan |
| `tax-position-memo` | Write a FIRAC-structured tax memo with authorities, analysis, confidence level, and disclosure guidance | Federal Tax Research - Sawyers & Gill |

### Business Analyst (`--role business-analyst`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `requirements-elicitation` | Facilitate structured requirements gathering using interviews, workshops, and observation | BABOK Guide - IIBA + Mastering the Requirements Process - Robertson |
| `brd-writer` | Write a Business Requirements Document from stakeholder inputs | Software Requirements - Wiegers + BABOK Guide - IIBA |
| `frd-writer` | Write a Functional Requirements Document from a BRD or feature brief | Software Requirements - Wiegers + User Stories Applied - Cohn |
| `use-case-writer` | Generate structured use cases with main flow, alternate flows, and extensions | Writing Effective Use Cases - Cockburn |
| `acceptance-criteria-writer` | Write measurable acceptance criteria using Fit Criteria and Given-When-Then | Mastering the Requirements Process - Robertson + User Stories Applied - Cohn |
| `process-mapper` | Map as-is and to-be business processes using BPMN-style notation | Business Process Change - Harmon + Business Analysis Techniques - Cadle |
| `gap-analysis` | Identify gaps between current and desired state with Brown Cow Model | BABOK Guide - IIBA + Mastering the Requirements Process - Robertson |
| `root-cause-analysis` | Run structured root cause analysis using 5 Whys, fishbone, and A3 | Business Process Change - Harmon + Lean Business Analysis - Sherrington |
| `cost-benefit-analysis` | Build a CBA with ROI, NPV, payback period, and benefits mapping | The Business Analysis Handbook - Winter + Business Process Change - Harmon |
| `stakeholder-map` | Map stakeholders by power/interest with engagement strategies | Business Analysis Techniques - Cadle + The Business Analysis Handbook - Winter |
| `impact-assessment` | Assess business impact of a proposed change across people, process, technology, policy | The Business Analysis Handbook - Winter + Requirements Engineering - Hull |
| `data-dictionary` | Generate a data dictionary with CRUD matrix and data lineage | BABOK Guide - IIBA + Business Analysis Techniques - Cadle |
| `decision-matrix` | Build a weighted decision matrix using Wiegers Priority Matrix | Software Requirements - Wiegers + Business Analysis Techniques - Cadle |
| `traceability-matrix` | Create an RTM linking requirements to design, test, and delivery | Requirements Engineering - Hull + BABOK Guide - IIBA |
| `uat-plan` | Generate a UAT plan with scenarios derived from use cases and fit criteria | Writing Effective Use Cases - Cockburn + Mastering the Requirements Process - Robertson |

### Content Creator (`--role content-creator`)
| Skill | What it does | Grounded in |
|-------|-------------|-------------|
| `linkedin-post` | Write high-performing LinkedIn posts with proven hook types and structures | LinkedIn content strategy |
| `newsletter-ideation` | Generate 5-7 differentiated topic angles using SCAMPER, JTBD, Contrarian frameworks | Design thinking + JTBD - Christensen |
| `reddit-post` | Write Reddit posts that earn genuine engagement without triggering spam flags | Community-first content strategy |
| `substack-notes` | Generate short-form Substack notes using 10 proven structural patterns | Content psychology + platform best practices |
| `substack-post` | Write long-form Substack articles with narrative arc and sustained depth | On Writing - King + Show Your Work - Kleon |
| `substack-toc` | Create numbered TOC with working anchor links for Substack articles | Substack platform mechanics |

### Shared (installed with every role)
| Skill | What it does |
|-------|-------------|
| `presentation-builder` | Build structured presentations for any audience |
| `jira-ticket-creator` | Create Jira tickets from meeting notes, user stories, or quick lists |
| `flowchart` | Generate Mermaid flowchart diagrams from any input source |

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
