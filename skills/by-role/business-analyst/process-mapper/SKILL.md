---
name: process-mapper
description: >
  Map business processes as-is and to-be. Use when the user says "map the process",
  "draw the workflow", "BPMN diagram", "process flow", "swimlane", "how does this process work",
  "document the current process", "redesign this process", "process improvement",
  "value stream map", "workflow analysis" - even if they don't explicitly say "process mapper".
---

## Reference Files

- `references/bpmn-notation.md` - BPMN 2.0 symbol reference table with events, activities, gateways, flows, and swimlanes. Read this in Step 3 when mapping processes using BPMN notation.

## Overview

Based on **Business Process Change** by Paul Harmon - the BPTrends 3-level process architecture (Enterprise, Business Process, Implementation) that prevents the most common process mapping mistake: starting at the wrong level of detail. Also draws on **Business Analysis Techniques** by James Cadle for BPMN notation and swimlane techniques, and Rummler-Brache's 3-level analysis (Organization, Process, Performer). The key insight from Harmon: before you draw a single box or arrow, locate the process within the enterprise value chain. A process mapped at the wrong level is either too abstract to act on or too detailed to see the real problems.

## Workflow

### Step 1: Identify the process level (Harmon's 3 levels)
Determine which level you are mapping:
- **Level 1 - Enterprise**: Value chain view - how this process fits into the organization's end-to-end value delivery
- **Level 2 - Business Process**: The process itself - trigger to outcome, with subprocesses
- **Level 3 - Implementation**: Detailed task-level steps within a subprocess

Most BA process mapping operates at Level 2. Start at Level 1 to establish context, then zoom into Level 2.

### Step 2: Define process boundaries
```
PROCESS NAME: [name]
TRIGGER: [what starts this process - event, request, schedule]
END EVENT: [what marks completion - output delivered, decision made, state changed]
IN SCOPE: [subprocesses included]
OUT OF SCOPE: [adjacent processes excluded]
OWNER: [who is accountable for this process]
```

### Step 3: Map the AS-IS process (current state)
Using BPMN notation (see `references/bpmn-notation.md`):
1. Draw the happy path first (main success flow from trigger to end)
2. Add swimlanes for each role, department, or system involved
3. Mark gateways (decision points) with labeled conditions
4. Add exception paths branching from gateways
5. Note handoffs between swimlanes - these are where delays and errors concentrate

### Step 4: Measure the current process (Rummler-Brache)
Apply metrics at each of Rummler-Brache's 3 levels:
- **Organization level**: Does this process align with business goals?
- **Process level**: Cycle time, error rate, cost per transaction, throughput
- **Performer level**: Handoff count, wait time between lanes, rework loops

Annotate the AS-IS map with actual metrics. Highlight pain points: bottlenecks, rework loops, unnecessary approvals, manual steps that could be automated.

### Step 5: Map the TO-BE process (future state)
Apply Harmon's redesign principles:
- **Eliminate**: Remove steps that add no value (approvals for low-risk items, duplicate data entry)
- **Simplify**: Reduce complexity (merge steps, standardize variations)
- **Integrate**: Combine handoffs between roles or systems
- **Automate**: Replace manual steps with system actions where ROI justifies it

### Step 6: Document the gap between AS-IS and TO-BE
```
| Change | AS-IS | TO-BE | Impact | Owner |
|--------|-------|-------|--------|-------|
| [description] | [current state] | [future state] | [who/what is affected] | [responsible] |
```

### Step 7: Output the process map with change summary
Deliver: process diagrams (AS-IS and TO-BE), metrics comparison, change register, and recommended implementation sequence.

## Anti-Patterns

**1. Mapping at the wrong level of detail**
Bad: Starting with Level 3 task-level detail before understanding where the process sits in the value chain.
Good: Start at Level 1 (context), zoom to Level 2 (process), drill into Level 3 only where pain points exist.

**2. Missing swimlane handoffs**
Bad: Process flow with all steps in a single lane - hides the cross-functional complexity.
Good: Every role or system gets its own lane; every arrow crossing a lane boundary is a handoff worth examining.

**3. AS-IS without metrics**
Bad: Drawing the current process without measuring it. ("We think it takes about a week.")
Good: Annotate with actual cycle time, error rates, and throughput. If data doesn't exist, that's a finding.

**4. TO-BE that's just "automate everything"**
Bad: Future state where every manual step is replaced by a system.
Good: Apply Harmon's sequence: eliminate first, then simplify, then integrate, then automate. Many problems are solved by removing steps, not by building software.

**5. No trigger or end event**
Bad: Process map that starts with "Step 1" and ends with "Done."
Good: BPMN start event (what triggers this?) and end event (what state marks completion?).

## Quality Checklist

- [ ] Process level identified (Enterprise / Business Process / Implementation)
- [ ] Trigger event and end event explicitly defined
- [ ] Swimlanes represent all participating roles and systems
- [ ] Every gateway has labeled decision paths
- [ ] No orphan activities (every activity has an incoming and outgoing flow)
- [ ] AS-IS process annotated with actual metrics
- [ ] TO-BE process applies eliminate/simplify/integrate/automate in that order
- [ ] Handoffs between lanes are explicitly marked
- [ ] Gap register documents every change between AS-IS and TO-BE
