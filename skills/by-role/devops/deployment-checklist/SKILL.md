---
name: deployment-checklist
description: >
  Run a pre and post-deployment checklist. Use when the user says "deploy to production",
  "deployment checklist", "release checklist", "pre-deploy checks", "is this ready to deploy",
  "deployment readiness", "reduce deployment risk", "change management",
  or is about to ship code to production and wants to reduce failure risk
  - even if they don't explicitly say "deployment checklist".
---

## Overview

Based on **"The Checklist Manifesto"** by Atul Gawande and **"Accelerate"** by Forsgren, Humble & Kim.

Gawande's insight: checklists don't exist because people are stupid - they exist because complex, high-pressure situations cause smart people to skip steps they know matter. A pre-deployment checklist is not bureaucracy; it's the discipline that separates teams with 15% change failure rates from teams with 60%.

Accelerate's finding: high-performing teams deploy more frequently AND have lower failure rates. The checklist is what enables speed without sacrificing safety.

## Workflow

### Pre-Deployment Checklist

Run before every production deployment:

**Code and testing:**
- [ ] CI pipeline is green (all tests pass, no warnings suppressed)
- [ ] Code reviewed and approved by at least one other engineer
- [ ] No `TODO: fix before deploy` comments in the diff
- [ ] No hardcoded credentials, secrets, or API keys introduced
- [ ] Database migrations are backward-compatible (old code can run against new schema)

**Deployment mechanics:**
- [ ] Deployment plan documented: what is being deployed, to which environment, in what order
- [ ] Rollback plan documented: exact steps to revert if something goes wrong
- [ ] Feature flags configured (if applicable): new code is behind a flag for gradual rollout
- [ ] Deployment window confirmed: not during peak traffic hours or known high-risk periods

**Dependencies and coordination:**
- [ ] Dependent teams notified if this change affects shared APIs or contracts
- [ ] On-call engineer aware that a deployment is happening
- [ ] Monitoring dashboards open and baseline metrics noted before deploy begins

**Data and migrations:**
- [ ] Database migrations tested on a staging environment with production-scale data
- [ ] Data migration has a rollback path (or data is backed up)
- [ ] If schema change: old and new code can run simultaneously during deploy window

### Deployment Execution

During the deploy:
1. Note start time and deployer in the incident channel / deploy log
2. Monitor error rate and latency during and after deploy (minimum 10 minutes)
3. Verify key user journeys manually on production after deploy
4. Note end time and result

```
Deploy log entry:
Date/time: [start] to [end]
Deployer: [name]
Change: [what was deployed, link to PR/ticket]
Result: [Success / Rolled back]
Notes: [anything unusual observed]
```

### Post-Deployment Checklist

Run within 30 minutes of deployment:

- [ ] Error rate is at or below pre-deployment baseline
- [ ] p99 latency is at or below pre-deployment baseline
- [ ] Key user journeys verified manually (login, core feature, critical path)
- [ ] No new alerts firing
- [ ] Logs are clean (no unexpected errors in the first 10 minutes)
- [ ] Feature flag enabled for target percentage (if gradual rollout)
- [ ] Deployment logged with result, time, and deployer

### Rollback Triggers

Roll back immediately if:
- Error rate > 2x pre-deployment baseline for more than 2 minutes
- P0/P1 alert fires that was not present before deployment
- Core user journey is broken
- Data corruption is detected

Do not wait to diagnose before rolling back. Restore first, investigate after.

## Anti-Patterns

**1. Skipping the checklist under time pressure**
Bad: "We need to deploy this hotfix now, no time for checks."
Good: A 5-minute checklist prevents a 2-hour incident. The checklist is fastest under pressure, not slowest.

**2. Deploying during peak traffic**
Bad: Deploying at 2pm on a Friday.
Good: Deploy during low-traffic windows. Know your traffic patterns before setting deployment windows.

**3. No rollback plan**
Bad: "If something goes wrong, we'll figure it out."
Good: Rollback steps documented before every deploy. Tested quarterly.

**4. Checking boxes without checking**
Bad: Marking checklist items as done without actually verifying them.
Good: Gawande's insight: the checklist is a discipline tool, not a paperwork exercise. Each box represents a real check.

## Quality Checklist

- [ ] Pre-deployment checklist completed and all items pass
- [ ] Rollback plan documented before deployment begins
- [ ] On-call engineer aware of deployment
- [ ] Monitoring dashboards open with baseline metrics noted
- [ ] Post-deployment monitoring ran for at least 10 minutes
- [ ] Post-deployment checklist completed
- [ ] Deploy log entry written with result
- [ ] Rollback triggers defined in advance
