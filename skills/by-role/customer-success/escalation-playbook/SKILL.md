---
name: escalation-playbook
description: >
  De-escalate a customer crisis using a structured acknowledge-triage-DRI-cadence-resolution
  framework. Use when user says "customer escalation", "angry customer", "exec escalation",
  "customer threatening to leave", "fire drill", "critical customer issue", "customer is
  livid", "customer complaint escalated", or "how do I handle this" about a tense situation -
  even if they don't say "escalation" explicitly. Applies to CSMs and CS managers managing
  high-stakes customer crises.
---

## Overview

An escalation is a moment of peak emotional intensity and minimum trust. Based on de-escalation
principles from CS literature and conflict resolution frameworks, the goal is not to win the
argument - it is to restore enough trust to solve the problem together.

The core insight: customers escalate because they feel unheard, not just unsolved. Acknowledging
the experience before defending the product is the single biggest trust lever in an escalation.
Speed of response and clarity of ownership are close seconds.

## Workflow

### Step 1: Acknowledge within 2 hours

Acknowledge does not mean apologize for things not yet understood. It means recognizing impact.

Send within 2 hours of escalation reaching you:

> "[Customer name] team - I hear you. What you've described is not acceptable and I take
> personal ownership of getting this resolved. I'm pulling together the right people right
> now and will have a status update to you by [specific time today]."

Key elements:
- Personal ownership: "I" not "we" or "the team"
- No defensiveness, no explanation
- Specific next communication time (not "soon" or "ASAP")

If the issue is a product outage or data problem, also loop in support or engineering immediately.

### Step 2: Triage - understand before acting

Within 30 minutes of your acknowledgment, complete internal triage:

| Question | Answer |
|----------|--------|
| What is the customer's stated problem? | |
| What is the actual technical or business impact? | |
| When did this start? | |
| Has this happened before? | |
| Who at the customer is most affected? | |
| What is the ARR / renewal timeline? | |
| Is this a product bug, configuration issue, or process failure? | |
| What outcome does the customer want? | |

The last question matters most. Customers often want three different things: acknowledgment,
a fix, or accountability. Know which one before your next call.

### Step 3: Assign a single DRI (Directly Responsible Individual)

Every escalation must have one named DRI. Not a team. One person who owns resolution.

The DRI is responsible for:
- All external communication to the customer
- Coordinating internally across support, engineering, product, and management
- The daily status update until the escalation is closed

The DRI is typically the CSM for standard escalations. It escalates to CS Manager for
executive-level situations or when the issue is a product defect requiring engineering.

Announce the DRI to the customer: "I am your single point of contact until this is resolved."

### Step 4: Daily status cadence until resolved

Once triage is complete, start a daily status cadence. Send one update per day even if there
is no new resolution to report. Silence is the fastest way to re-escalate.

**Format for daily status update**:

> **[Customer name] - Escalation Update [Date]**
>
> **Status**: [In progress / Resolved / Pending information from your side]
>
> **What happened today**: [1-2 sentences on actions taken]
>
> **What is happening next**: [specific next step with owner and date]
>
> **ETA for resolution**: [date or "we don't have one yet - here's why"]
>
> **Questions for you**: [if you need anything from the customer]

### Step 5: Root cause + resolution summary

When the issue is resolved, send a formal close-out document within 48 hours. Do not just
declare "it's fixed." The close-out document is what prevents the next escalation.

**Format**:

**Issue**: [1 sentence description]
**Impact**: [who was affected, for how long, what they could not do]
**Root cause**: [specific, honest, no jargon]
**What we did**: [actions taken, in order]
**What we're doing to prevent recurrence**: [specific changes to process, product, or monitoring]
**What you should expect next**: [any follow-up from your team]

If the root cause was a product defect, include a link to the bug report or roadmap item.
If it was a process failure on your side, say so directly.

### Step 6: Post-escalation recovery

An escalation that is "resolved" is not the same as a relationship that is restored. After
close-out, take three steps within 30 days:

1. **Executive check-in call**: Thank the customer for raising the issue. Do not just send email.
2. **Health score reset**: Reassess the account health score - the escalation may have revealed
   underlying risk that predates this incident.
3. **Success plan review**: Confirm that stated goals are still on track. An escalation often
   delays customer adoption. Acknowledge this and recalibrate timelines.

## Anti-Patterns

**1. Explaining before acknowledging**
Bad: "The reason this happened is that our infrastructure team was doing a scheduled migration..."
Good: "I hear that this has disrupted your team. That's not okay. Here's what I'm doing right now."

**2. Escalation ownership by committee**
Bad: "The support team, engineering team, and your CSM are all looking into this."
Good: "I am your single point of contact. [Name] owns this until it is resolved."

**3. Silence between updates**
Bad: No communication for 3 days because the fix is still in progress.
Good: Daily update even if it says "No new resolution yet. Here is what is happening and when
you'll hear from me next."

**4. Treating the technical fix as the full resolution**
Bad: Ticket closed = escalation over.
Good: Technical fix + close-out document + executive relationship call + health score reassessment.

**5. Over-promising to calm the customer**
Bad: "This will be fixed by end of day" when you don't control the timeline.
Good: "I don't have an ETA yet and I won't make one up. I will have a confirmed date to you
by [specific time]."

## Quality Checklist

- [ ] Acknowledgment sent within 2 hours - personal, no defensiveness, specific next update time
- [ ] Internal triage complete - impact, root cause hypothesis, and customer's desired outcome known
- [ ] Single named DRI assigned and communicated to the customer
- [ ] Daily status updates sent every day until resolved
- [ ] Each update includes: what happened today, what's next, ETA, and any customer asks
- [ ] Root cause + resolution summary sent within 48 hours of fix
- [ ] Post-escalation recovery plan: exec call, health score reset, success plan review
- [ ] No personal names, internal tool names, or company-specific references in template
