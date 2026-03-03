---
name: program-status-report
description: >
  Write a structured weekly or bi-weekly program status report for stakeholders.
  Use when the user says "write a status report", "program update", "stakeholder
  update", "weekly status", "RAG status", "program health report", "what do I send
  to leadership", "write the update for [program]", or needs to communicate delivery
  progress - even if they don't explicitly say "status report". Produces a concise,
  scannable report with RAG status, blockers, and decisions needed.
---

## Overview

A program status report has one job: give stakeholders the information they need to make decisions or remove blockers, in under 3 minutes. The failure mode is burying the lead - putting good news first and hiding the red items in paragraph 4. The format here front-loads risk and decisions needed, then provides supporting detail. Stakeholders who need detail can read further; those who only need the headline get it immediately.

## Workflow

### Step 1: Gather inputs
Ask the user for:
- Program name and reporting period (e.g., "Week of March 3")
- Overall RAG status (Red / Amber / Green) - if they are not sure, work through it in Step 2
- Key accomplishments since last report (what shipped, what was decided)
- Current blockers (what is slowing or stopping the program)
- Decisions needed from stakeholders (specific asks, not general concerns)
- Upcoming milestones (next 2-3 checkpoints and dates)
- Any risks that surfaced or changed this period

If the user provides a narrative or notes, extract these fields from their input before generating the report.

### Step 2: Determine the RAG status
If the user is unsure of the overall status, use this rubric:

**Green**: Program is on track. No unresolved blockers. Milestones will be met as planned.

**Amber**: Program is at risk. One or more of:
- A milestone is at risk but there is a recovery plan
- A dependency is unresolved but expected to resolve within 1 sprint
- Scope reduction is being discussed but not yet decided

**Red**: Program is off track. One or more of:
- A milestone will be missed with no recovery plan
- A dependency is unresolved with no clear path forward
- Scope or date change is required and has not been approved
- A critical team or resource issue has no mitigation

Amber should be used before a problem becomes Red - it is an early warning, not a failure state. Do not use Green if anything requires stakeholder action.

### Step 3: Write the report

Use this template exactly:

```
PROGRAM STATUS - [your program]
Period: [week / sprint / date range]
Updated: [date]
Owner: [your name]

STATUS: [GREEN / AMBER / RED]
[One sentence explaining the status. If Amber or Red, name the specific issue.]

---

DECISIONS NEEDED
[If none, write "None this period."]
1. [Decision needed from whom, by when, and what happens if it is not made]
2. [Next decision if any]

BLOCKERS
[If none, write "No active blockers."]
1. [Blocker description] - Owner: [name] - Target resolution: [date]
2. [Next blocker if any]

---

ACCOMPLISHMENTS (this period)
- [What shipped, what was accepted, what was decided]
- [Keep to 3-5 bullets max. Not every ticket - program-level progress only]

UPCOMING MILESTONES
| Milestone | Target Date | Status |
|-----------|------------|--------|
| [name] | [date] | On track / At risk / Delayed |
| [name] | [date] | [status] |

---

RISKS (new or changed)
[If none, write "No new risks this period."]
- [Risk]: [likelihood] / [impact] - Mitigation: [action and owner]

NOTES / CONTEXT
[Optional: 2-3 sentences of context that stakeholders need. Skip if nothing material.]
```

### Step 4: Apply the three-minute rule
After writing the report, verify:
- A stakeholder can read the STATUS line and DECISIONS NEEDED section in 30 seconds and know if action is required from them
- The report is 1 page max when pasted into Slack, email, or a wiki
- Accomplishments section is 3-5 bullets - not a sprint changelog
- If anything in the Blockers or Decisions section is more than 2 lines, it is too long - link to a separate doc

### Step 5: Calibrate frequency and audience
Recommend the right distribution based on program phase:
- **Weekly**: standard for active programs with external dependencies or stakeholder decisions pending
- **Bi-weekly**: appropriate for programs in steady-state delivery with no active escalations
- **Daily**: only when a program is Red and actively in recovery mode

Audience guidance:
- **Executives / leadership**: STATUS + DECISIONS NEEDED only. They do not need the milestone table.
- **Peer teams / dependencies**: BLOCKERS + UPCOMING MILESTONES. They need to know what you need from them.
- **Full team**: Full report including accomplishments and notes.

## Anti-Patterns

**1. Green-washing - everything is always green**
Bad: Status is Green every week until the release is 2 weeks late.
Good: Use Amber early. Amber means "we have a plan but it needs attention" - that is valuable signal, not failure.

**2. Accomplishments section as a ticket dump**
Bad: 15 bullets listing every closed Jira ticket.
Good: 3-5 program-level progress statements. "Core checkout flow accepted by QA" not "JIRA-1234, JIRA-1235, JIRA-1236 closed."

**3. Vague blockers**
Bad: "We're blocked on infrastructure."
Good: "Waiting on cloud team to provision staging environment. Owner: [name]. Target: [date]. If not resolved by [date], release date is at risk."

**4. Decisions buried at the bottom**
Bad: Status report where the decision needed from leadership is in paragraph 6.
Good: DECISIONS NEEDED is the second section - immediately after the RAG status line.

**5. No cadence - status reports only when things go wrong**
Bad: Stakeholders only hear from you when there is a crisis.
Good: Regular cadence trains stakeholders to expect updates and creates a paper trail. It also normalizes Amber status before it becomes Red.

## Quality Checklist

- [ ] RAG status is on the first line with a one-sentence explanation
- [ ] DECISIONS NEEDED section is above accomplishments and milestones
- [ ] Every blocker has a named owner and target resolution date
- [ ] Accomplishments are 3-5 bullets of program-level progress, not ticket lists
- [ ] Report is skimmable in under 3 minutes
- [ ] If status is Amber or Red, a recovery plan or escalation path is stated
