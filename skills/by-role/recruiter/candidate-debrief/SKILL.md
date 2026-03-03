---
name: candidate-debrief
description: >
  Structure and run a post-interview candidate debrief. Use when the user says
  "run the debrief", "how do we decide on this candidate", "let's calibrate",
  "we need to make a hire/no-hire call", "prep the debrief meeting", or wants
  to structure the decision-making process after interviews are complete -
  even if they don't explicitly say "debrief". Also use when a recruiter wants
  to prevent groupthink or HiPPO effect (highest paid person's opinion) from
  dominating the decision.
---

## Overview

Based on **Who: The A Method for Hiring** (Smart & Street) and **Work Rules!** (Laszlo Bock). Unstructured debriefs default to the loudest voice, the most senior person, or whoever interviewed last. A calibrated debrief separates evidence from impression, surfaces disagreement before consensus forms, and produces a decision anchored in scorecard data - not gut feel.

## Workflow

### Step 1: Collect Scorecards Before the Debrief

This is the most important rule: scorecards must be submitted independently before anyone discusses the candidate. Once people hear each other's opinions, anchoring kicks in and individual assessments become unreliable.

Before the debrief meeting:
- Confirm every interviewer has submitted their scorecard
- Do not allow verbal previews or "quick takes" in Slack or email
- If a scorecard is missing, delay the debrief - not the reverse

### Step 2: Set the Meeting Structure (30-45 minutes)

Debrief agenda:
```
1. Ground rules (2 min) - recruiter facilitates
2. Independent scorecard read-out (10-15 min) - each interviewer shares their
   rating and top evidence before open discussion
3. Discuss disagreements (10-15 min) - focus on evidence gaps, not vibes
4. Decision (5 min) - hire / no-hire, or identify what's still unknown
5. Next steps (3 min) - offer, decline, or additional interview
```

### Step 3: Run the Independent Read-Out

Go around the room in reverse seniority order. Junior interviewers speak first to prevent anchoring on the hiring manager's view.

For each interviewer:
1. State your overall recommendation: Strong Yes / Yes / No / Strong No
2. Name the 1-2 competencies you assessed
3. State your rating per competency (A/B/C)
4. Share one specific piece of evidence (a quote or example from the candidate)

Recruiter records this without editorial comment. Do not allow discussion during the read-out phase.

### Step 4: Surface and Resolve Disagreements

After all read-outs, the recruiter identifies disagreements:
- Where do ratings differ by 2+ levels (e.g., one A and one C on the same competency)?
- Did interviewers ask the same questions and get different answers?
- Did interviewers assess different competencies and reach different overall conclusions?

For each disagreement, ask: "What specific evidence supports your rating?" Not "Why do you feel that way?"

Common disagreement sources:
- **Evidence gap:** Interviewer 1 asked a probing follow-up, Interviewer 2 didn't
- **Standard gap:** Interviewers have different thresholds for what "A" looks like
- **Context gap:** Candidate gave a different example to each interviewer

If the disagreement can't be resolved with existing evidence, name it explicitly: "We have conflicting data on [competency]. We either accept the uncertainty and decide, or schedule a targeted follow-up."

### Step 5: Apply the Calibration Check

From **Work Rules!** (Bock): the best hires come from calibrated committees, not from managers hiring in their own image. Run these checks before the final decision:

**Bar-raiser check:** Would this candidate raise the average performance level of the team? If the team is a 7/10, does this candidate rate above 7?

**Regret minimization:** Which is worse - hiring someone who underperforms, or losing this candidate to a competitor? Use this to calibrate risk tolerance, not to override data.

**Counterfactual test:** "If this candidate's resume showed up in our pipeline 6 months from now after we've hired someone else, would we be upset we missed them?"

### Step 6: Make the Decision

Decision categories:
```
HIRE - Strong Yes majority, no Strong No votes
  → Move to offer

HIRE WITH RESERVATIONS - Yes majority, at least one No
  → Document the specific reservation, define how it will be managed onboard

NO HIRE - No majority, or any Strong No with corroborating evidence
  → Decline. Do not "create a role" to accommodate someone who didn't clear the bar.

HOLD FOR MORE DATA - Genuine evidence gap on a critical competency
  → Schedule one targeted follow-up interview focused only on the gap.
     Cap at one hold per candidate. Two holds is a soft no.
```

If the group is split, the hiring manager makes the final call. The recruiter's role is to ensure the decision is based on scorecard evidence, not politics.

### Step 7: Document the Decision

For every candidate, document:
- Final recommendation
- Competency ratings summary
- The 2-3 specific evidence points that drove the decision
- Any reservations and how they'll be addressed (for hire decisions)
- The primary reason for decline (for no-hire decisions)

This documentation serves calibration for future hires and provides defensible records.

## Anti-Patterns

**1. Allowing pre-debrief discussion**
Bad: "Quick Slack before the meeting - she was fantastic, right?"
Good: Scorecards submitted independently. No discussion until the structured read-out.

**2. Starting with the hiring manager's opinion**
Bad: Hiring manager leads: "I thought she was great, especially her answer on X..."
Good: Junior interviewers speak first. Hiring manager synthesizes last.

**3. Conflating impression with evidence**
Bad: "I just got a great vibe from him. He'd fit our culture."
Good: "He described rebuilding the deployment pipeline solo at his last company - that's the ownership signal we need."

**4. The "create a role" trap**
Bad: "She's not right for this role but she seems talented - can we find something for her?"
Good: Evaluate against this role's scorecard only. If she doesn't clear the bar, decline. The "create a role" pattern inflates headcount and dilutes talent density.

**5. Over-indexing on one interview**
Bad: "Her system design interview was excellent, so I'm willing to overlook the weak behavioral round."
Good: All competencies on the scorecard are load-bearing. An A on one and C on another is a C-level hire.

**6. Treating "hold for more data" as the safe default**
Bad: Every close call gets a third interview to defer the decision.
Good: One hold is acceptable for a genuine evidence gap. Two is avoidance. Make the call.

## Quality Checklist

- [ ] All scorecards submitted independently before debrief begins
- [ ] Read-out goes in reverse seniority order
- [ ] Each rating is backed by a specific evidence point, not an impression
- [ ] Disagreements are documented and addressed, not smoothed over
- [ ] Decision uses the 4-category framework (Hire, Hire with Reservations, No Hire, Hold)
- [ ] Decision and key evidence documented for audit trail
- [ ] "Hold" decisions have a specific competency gap named, not a vague "want to know more"
