---
name: churn-risk-analysis
description: >
  Analyze customer health signals, identify churn risk flags, and generate an intervention
  playbook. Use when user says "churn risk", "customer at risk", "red account", "at-risk
  customer", "health score dropped", "renewal at risk", "customer going dark", "cancel risk",
  or "what's wrong with this account" - even if they don't say "churn" explicitly.
  Applies to CSMs triaging accounts or building proactive retention workflows.
---

## Overview

Based on "Customer Success" by Mehta, Steinman & Murphy, churn rarely happens by surprise.
The signals appear weeks or months before a customer cancels - they just go unread. This skill
structures those signals into a scored risk model and prescribes specific interventions for
each risk tier.

The core insight: churn is a lagging indicator. The leading indicators are low usage, missing
stakeholders, unresolved complaints, and strategic misalignment. Act on those, not the
cancellation notice.

## Workflow

### Step 1: Score the account across six risk dimensions

Rate each dimension 1 (healthy) to 3 (at risk):

| Dimension | 1 - Healthy | 2 - Watch | 3 - At Risk |
|-----------|-------------|-----------|-------------|
| **Usage** | MAU >80% of licenses, core feature adoption >70% | MAU 50-80%, spotty feature use | MAU <50%, logins declining MoM |
| **Stakeholder coverage** | Champion active, exec sponsor engaged | Champion disengaged, no exec relationship | Champion left, no internal advocate |
| **Support load** | <3 tickets/month, all resolved | 4-8 tickets/month, 1-2 lingering | >8 tickets/month or critical unresolved |
| **NPS / sentiment** | NPS 8-10, positive qualitative signals | NPS 6-7, neutral | NPS 0-5, complaints escalating |
| **Goal progress** | On track for agreed outcomes | Behind on 1-2 goals | No measurable progress, ROI questioned |
| **Renewal proximity** | >6 months out | 3-6 months | <3 months with unresolved issues |

**Composite score = sum of all dimensions (6-18)**
- 6-9: Healthy - standard cadence
- 10-13: Watch - increase touchpoint frequency
- 14-18: At Risk - immediate intervention required

### Step 2: Identify which risk flags are present

Check for these specific churn signals from the CS literature:

- **Champion left**: The person who bought and championed the product is no longer at [customer name]
- **Budget scrutiny**: Customer mentions cost reviews, budget freezes, or consolidation initiatives
- **Silent period**: No product login or CSM response for 3+ weeks without explanation
- **Executive disengagement**: Exec sponsor declined last QBR or stopped attending
- **Competitive mention**: Customer references a competitor by name in conversation
- **Support frustration**: Repeated tickets on the same issue, escalating tone in communications
- **Failed expansion refusal**: Customer declined an upsell or said "we need to right-size first"
- **Org change**: Merger, acquisition, leadership change, or restructuring announced

Document which flags are active for [customer name].

### Step 3: Assign risk tier and intervention playbook

**Tier 1 - Healthy (score 6-9)**
Standard success motion:
- Monthly check-in call
- Quarterly health review
- Proactive feature enablement aligned to goals

**Tier 2 - Watch (score 10-13)**
Elevated engagement:
- Bi-weekly calls until score improves
- Build or refresh the Success Plan with new goals
- Loop in 1-2 additional stakeholders to reduce champion dependency
- Identify 1 quick win to re-establish momentum

**Tier 3 - At Risk (score 14-18)**
Immediate intervention:
1. CSM escalates to CS Manager within 24 hours
2. Executive sponsor meeting booked within 2 weeks
3. Remediation plan prepared with specific commitments and dates
4. Internal coordination: loop in sales, support, and product if needed
5. Weekly status cadence until score drops to Tier 2

### Step 4: Map root cause to intervention type

| Root Cause | Primary Intervention |
|------------|---------------------|
| Low usage | Activation sprint - identify unused high-value features, run targeted enablement |
| Champion left | Stakeholder mapping - identify new champion, executive introduction via your sponsor |
| Unresolved support issue | Escalation - assign DRI, set resolution SLA, provide daily updates |
| ROI not demonstrated | Value audit - pull outcome data, schedule executive value review |
| Competitive threat | Competitive positioning call - address gaps directly, accelerate roadmap items |
| Budget pressure | Value consolidation story - quantify ROI, provide cost justification data |

### Step 5: Write the intervention brief

For at-risk accounts, produce a one-page brief for internal stakeholders:

**Account**: [customer name]
**ARR**: [value]
**Renewal date**: [date]
**Risk score**: [X/18] - Tier [1/2/3]
**Active flags**: [list]
**Root cause hypothesis**: [1-2 sentences]
**Proposed intervention**: [specific actions, owners, dates]
**Success criteria**: [what "recovered" looks like with a measurable signal]

## Anti-Patterns

**1. Waiting for the customer to say they're leaving**
Bad: Only flagging churn risk when a customer sends a cancellation email.
Good: Scoring all accounts monthly. Catching at-risk signals 90+ days before renewal.

**2. One-dimensional health scoring**
Bad: Defining "at risk" as only low usage.
Good: Scoring across six dimensions. An account with high usage but no executive sponsor and
a recent support escalation is still at risk.

**3. Intervention without root cause**
Bad: "Account is red, scheduling an EBR."
Good: "Champion left 6 weeks ago. We have no internal advocate. First step is stakeholder
mapping to identify a new champion before any executive outreach."

**4. No internal escalation path**
Bad: CSM handles Tier 3 accounts alone without manager involvement.
Good: Tier 3 automatically triggers manager review and cross-functional coordination.

**5. Treating all at-risk accounts the same**
Bad: Same playbook for low-usage accounts and accounts with executive disengagement.
Good: Match intervention to root cause. Low usage needs activation. Lost champion needs
relationship rebuilding. Support frustration needs escalation and resolution.

## Quality Checklist

- [ ] Account scored across all six risk dimensions (not just usage)
- [ ] Composite score calculated and risk tier assigned
- [ ] Active churn flags identified and documented
- [ ] Root cause hypothesis stated (not just symptoms)
- [ ] Intervention playbook matches the root cause, not just the tier
- [ ] For Tier 3: manager notified, executive meeting booked, weekly cadence set
- [ ] Intervention brief written for at-risk accounts with ARR and renewal date visible
- [ ] Success criteria defined - what does "recovered" look like?
- [ ] No personal names, internal tool names, or company-specific references in template
