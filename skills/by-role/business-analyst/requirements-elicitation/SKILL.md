---
name: requirements-elicitation
description: >
  Facilitate structured requirements gathering. Use when the user says "gather requirements",
  "elicitation session", "stakeholder interview", "requirements workshop", "what do the users need",
  "discover requirements", "trawl for requirements", "understand the business need",
  "conduct interviews", or needs to systematically extract requirements from stakeholders -
  even if they don't explicitly say "elicitation".
---

## Reference Files

- `references/elicitation-techniques.md` - Lookup table of 15+ elicitation techniques with when to use, participants, output format, and time needed. Read this in Step 2 when selecting techniques and in Step 3 when planning sessions.

## Overview

Based on the **BABOK Guide v3 (IIBA)** - Elicitation & Collaboration knowledge area, which defines 50 standardized techniques across 6 knowledge areas. Also draws on **Mastering the Requirements Process** by Suzanne & James Robertson for the Volere "trawling" approach - their term for iterative elicitation driven by business events, not document templates. The key insight: elicitation is not a phase you complete; it is a continuous activity that starts with business events and stakeholders, not with a blank requirements template.

## Workflow

### Step 1: Identify stakeholders and business events
List every person, role, and adjacent system that touches the problem space. Use the BABOK's stakeholder categories: customer, end user, sponsor, domain expert, regulator, implementation team. Then list the business events that trigger the process or system under analysis - Robertson's Business Event List is the elicitation backbone.

### Step 2: Select elicitation techniques
Match techniques to stakeholder type and information need (see `references/elicitation-techniques.md`). Use a mix:
- **Interviews** for deep individual knowledge
- **Workshops** for cross-functional alignment and conflict surfacing
- **Observation/Apprenticing** (Robertson) for tacit knowledge users cannot articulate
- **Document Analysis** for existing rules, policies, and constraints
- **Prototyping** for validating understanding with users

### Step 3: Plan and schedule sessions
For each session, define:
```
SESSION: [type - interview / workshop / observation]
STAKEHOLDER(S): [names and roles]
OBJECTIVE: [what you need to learn]
TECHNIQUE: [from reference table]
DURATION: [estimated time]
PREPARATION: [materials, context docs, pre-reads]
```

### Step 4: Conduct elicitation
During sessions:
- Start with open-ended context questions ("Walk me through how you do X today")
- Progress to specific probes ("What happens when Y fails?")
- Capture requirements using Robertson's Volere Snow Card format: requirement number, type, description, rationale, source, fit criterion
- Note assumptions, constraints, and conflicts separately
- Record who said what - source traceability starts here

### Step 5: Confirm and validate
After each session:
- Write up findings within 24 hours
- Send back to stakeholders for confirmation (BABOK's "confirm elicitation results")
- Flag conflicts between stakeholders - do not resolve silently
- Identify gaps that need follow-up sessions

### Step 6: Organize and classify requirements
Classify using BABOK's hierarchy:
- **Business requirements** - why the organization needs this
- **Stakeholder requirements** - what users need to do
- **Solution requirements** - functional + non-functional
- **Transition requirements** - what's needed to move from current to future state

## Anti-Patterns

**1. Template-first elicitation**
Bad: Sending a requirements template to stakeholders and asking them to fill it in.
Good: Conduct interviews and workshops first, then organize findings into a structured format.

**2. Single-technique reliance**
Bad: Only conducting interviews, missing tacit knowledge that observation would reveal.
Good: Use at least 3 techniques per project - interviews for depth, workshops for alignment, observation for reality.

**3. Eliciting solutions instead of needs**
Bad: "The user wants a dropdown menu." (That's a solution.)
Good: "The user needs to select from a constrained set of valid values." (That's a requirement.)

**4. No source traceability**
Bad: Requirements listed without noting who requested them or why.
Good: Every requirement links back to a stakeholder, business event, or document source.

**5. One-pass elicitation**
Bad: Running a single round of interviews and declaring requirements "complete."
Good: Iterative trawling - each round reveals gaps that drive the next round.

## Quality Checklist

- [ ] All stakeholder categories identified (users, sponsors, domain experts, regulators)
- [ ] Business events listed as elicitation drivers
- [ ] At least 3 elicitation techniques selected
- [ ] Each session has a defined objective and preparation
- [ ] Requirements captured with source attribution
- [ ] Findings confirmed with stakeholders
- [ ] Conflicts between stakeholders flagged (not silently resolved)
- [ ] Requirements classified by BABOK hierarchy
- [ ] Gaps identified with follow-up sessions planned
