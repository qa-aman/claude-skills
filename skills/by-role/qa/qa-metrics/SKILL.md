---
name: qa-metrics
description: Build QA quality dashboards, calculate defect metrics, analyze escape rates, and produce quality trend reports. Use this skill whenever a QA lead or manager needs to measure and communicate quality outcomes. Trigger on phrases like "quality metrics", "defect density", "escape rate", "bug trends", "quality dashboard", "sprint quality report", "test coverage metrics", "QA KPIs", "how is quality trending", "defect leakage", "production bugs this quarter", "mean time to detect", "quality scorecard", or any request to quantify, visualize, or report on the quality of a product or testing process. Also trigger when a manager asks "how is QA performing?" or an engineering lead asks "what does our defect data tell us?".
---

# QA Metrics

Measure, analyze, and communicate quality outcomes through data.

## Context Personalization

At the start of every invocation, read `~/.claude/skills/skill-context.md` if it exists. Use the values there to replace generic placeholders in your output:
- `[your industry]` → actual industry (e.g. Fintech, HealthTech)
- `[your stack]` → actual tech stack (e.g. React + Node.js)
- `[your compliance]` → actual compliance requirements (e.g. PCI-DSS, HIPAA, none)
- `[your defect tracker]` → actual tool (e.g. Jira, Linear, GitHub Issues)
- `[your monitoring tool]` → actual tool (e.g. Datadog, PagerDuty, Sentry)

If the file does not exist, use generic placeholders and proceed normally.

## When to Use

- Building a quality dashboard for a sprint review or exec report
- Calculating defect density or escape rate for a release
- Analyzing defect trends over time to surface systemic issues
- Producing a weekly or monthly QA health report
- Demonstrating the value of QA investment to leadership

## Core Metrics

### Defect Metrics

**Defect Density**
Number of defects per unit of functionality.
- Formula: Total defects / feature area (story points, function points, or KLOC)
- Use: compare quality across sprints or modules
- Target: trending down over time in stable areas

**Defect Escape Rate (Leakage)**
Percentage of defects found by customers (production) vs QA (pre-release).
- Formula: (Production defects / Total defects) × 100
- Use: measures QA effectiveness at catching defects before they ship
- Target: < 10% escape rate is strong. > 20% signals a coverage problem.

**Defect Detection Efficiency (DDE)**
How early defects are caught in the development lifecycle.
- Formula: (Defects found pre-release / Total defects including production) × 100
- Use: rewards early-stage testing; earlier detection = cheaper fix
- Target: > 90%

**Defect Aging**
Average time from defect open to resolution.
- Formula: Sum of (close date - open date) / number of defects closed
- Use: identifies bottlenecks in the fix cycle
- Watch for: P1/P2 defects staying open > 48 hours

### Test Execution Metrics

**Test Pass Rate**
Percentage of test cases that passed in a given cycle.
- Formula: (Passed cases / Total executed) × 100
- Caveat: pass rate is only meaningful if test cases are well-designed. High pass rate + high escape rate = weak test suite.

**Test Coverage**
Percentage of requirements or features covered by test cases.
- Formula: (Features with test cases / Total features) × 100
- Track separately: unit, integration, E2E coverage

**Automation Coverage**
Percentage of regression cases automated.
- Formula: (Automated cases / Total regression cases) × 100
- Target: 70%+ automation in stable product areas

**Test Execution Velocity**
Test cases executed per day or per sprint.
- Use: capacity planning, identifying execution bottlenecks

### Release Quality Metrics

**Production Defect Rate**
Defects per release found in production within 30 days of ship.
- Use: lagging indicator of release quality
- Track by severity: P1/P2 in production is a critical signal

**Mean Time to Detect (MTTD)**
Average time between a defect being introduced and being found.
- Shorter MTTD = earlier detection = cheaper fix

**Regression Rate**
Percentage of releases where a previously passing feature breaks.
- Formula: (Releases with regressions / Total releases) × 100
- Use: measures stability of the regression suite

## Workflow

### Step 1: Identify What to Measure

Not every metric is useful for every context. Match metrics to questions:

| Question | Metrics to Use |
|----------|---------------|
| Is quality improving over time? | Defect density trend, escape rate trend |
| Is QA catching bugs early enough? | DDE, MTTD, defect by phase |
| Are we shipping stable releases? | Regression rate, production defect rate |
| Is automation keeping up? | Automation coverage, execution velocity |
| Where are the quality hotspots? | Defect density by module/team |

### Step 2: Collect Data

Define your data sources:
- **Defect tracker** (Jira, Linear, GitHub Issues): open/closed defects, severity, discovery phase, resolution time
- **Test management** (TestRail, Zephyr, spreadsheet): executed cases, pass/fail, coverage
- **CI/CD pipeline**: test run results, flaky test rate, build failure rate
- **Production monitoring** (Datadog, PagerDuty): production incidents, customer-reported bugs

### Step 3: Calculate and Visualize

For a sprint report, calculate at minimum:
- Defects opened vs closed (net trend)
- Escape rate for the sprint
- Regression pass rate
- Any P1/P2 defects in production

For a quarterly report, add:
- Defect density by module (hotspot map)
- Escape rate trend (12-week rolling)
- Automation coverage change
- DDE trend

### Step 4: Write the Quality Report

**Sprint Quality Report template:**

```
Sprint [n] Quality Report - [dates]
Team: [team name]
QA Lead: [name]

Test Execution:
  Cases executed: [n]
  Pass rate: [x]%
  Automation coverage: [x]%

Defects:
  Opened: [n] (P1: [n] | P2: [n] | P3: [n])
  Closed: [n]
  Escaped to production: [n]
  Escape rate: [x]%

Release Quality:
  Production defects (this release): [n]
  Regression rate: PASS / FAIL
  Sign-off: GO / NO-GO

Hotspots:
  [area with disproportionate defects and why]

Trend:
  [1-2 sentences: is quality improving, stable, or degrading?]

Actions:
  [specific action, owner, due date]
```

**Quarterly Quality Dashboard sections:**

1. Headline scorecard (4-5 KPIs with trend arrows)
2. Defect trend chart (12-week rolling, by severity)
3. Escape rate chart (by release)
4. Automation coverage progress
5. Module hotspot map (defect density by area)
6. Key wins and risks
7. Actions for next quarter

### Step 5: Drive Action

Metrics without action are reporting theater. For every negative trend:
- State the root cause hypothesis
- Propose one specific action
- Assign an owner and a deadline
- Track it to resolution in the next report

## Anti-Patterns

**Vanity metrics**
"We ran 500 test cases" is not a quality metric. It is a volume metric. Pass rate, escape rate, and defect density are quality metrics. Distinguish between activity (what QA did) and outcomes (what quality resulted).

**Reporting in isolation**
A 95% pass rate means nothing without context. Is that up or down from last sprint? Is the test suite getting weaker or stronger? Always show trend, not just point-in-time.

**No action items**
A quality report with no action items is a postcard. If metrics show a problem, someone must own fixing it. If metrics show everything is fine, note what is working and why.

**Measuring only pre-release defects**
Escape rate requires production data. QA teams that only track what they found - not what customers found - are grading their own homework. Include production defect rate in every quarterly review.

**Automation coverage without flaky test tracking**
An automation suite that is 80% automated but 30% flaky is worse than 60% automated with stable tests. Track flaky test rate alongside automation coverage. Flaky tests erode confidence faster than low coverage.

## Quality Checklist

Before publishing any quality report:

- [ ] Metrics are calculated from actual data, not estimates
- [ ] Escape rate includes production defects (not just pre-release)
- [ ] Trend context provided (not just point-in-time numbers)
- [ ] Every negative metric has a root cause hypothesis
- [ ] Every action item has an owner and a due date
- [ ] Automation coverage and flaky test rate reported together
- [ ] Report is versioned and stored where stakeholders can access it
- [ ] P1/P2 production defects called out by name, not buried in totals
