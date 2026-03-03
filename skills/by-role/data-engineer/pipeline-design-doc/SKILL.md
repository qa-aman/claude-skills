---
name: pipeline-design-doc
description: >
  Write a data pipeline design document. Use when the user says "pipeline design doc",
  "document this pipeline", "pipeline architecture doc", "data flow document",
  "how does this pipeline work", "design doc for ETL", "pipeline spec", or needs
  to capture the architecture, data flow, and operational details of a data pipeline
  - even if they don't explicitly say "design doc".
---

## Overview

Based on **Fundamentals of Data Engineering** (Reis & Housley) and **Designing Data-Intensive Applications** (Kleppmann). A pipeline design doc is the architectural contract for a data flow: what data moves, from where to where, how it transforms, and what guarantees it provides. Kleppmann's standard: document the data system's reliability, scalability, and maintainability properties - not just the happy path.

The test: can a new engineer understand what this pipeline does, debug it when it breaks, and extend it safely - without asking anyone?

## Workflow

### Step 1: Write the pipeline overview

```
Pipeline: [name]
Owner: [team or person]
Purpose: [1-2 sentences on why this pipeline exists and what decision it enables]
Source systems: [list of upstream data sources]
Destination: [where data lands - warehouse, lake, API, etc.]
Schedule: [batch frequency or streaming latency SLA]
Data volume: [approx rows/day or GB/day]
SLA: [when downstream consumers need data available by]
```

### Step 2: Document the data flow

Draw or describe each stage linearly:

```
[Source] → [Ingest] → [Raw/Landing Zone] → [Transform] → [Serving Layer] → [Consumer]
```

For each stage, document:
- What enters the stage (schema, format, expected volume)
- What the stage does (filter, join, aggregate, enrich)
- What exits the stage (output schema, format)
- Technology used (Spark, dbt, Airflow, Kafka, etc.)

### Step 3: Document data contracts

For each source, specify the contract:

```
Source: [system name]
Schema: [fields and types]
Delivery method: [push/pull, API, file drop, CDC, etc.]
Delivery frequency: [real-time / hourly / daily]
SLA: [when source guarantees data is available]
Schema change policy: [how the source team notifies of changes]
Known quirks: [nulls in required fields, late-arriving data, duplicates, etc.]
```

For the output, specify the guarantee:

```
Output table/topic: [name]
Schema: [fields and types]
Freshness SLA: [data is no older than X]
Completeness guarantee: [how to detect missing data]
Deduplication: [how duplicates are handled]
```

### Step 4: Document transformation logic

For each non-trivial transformation, explain:

- **What**: what business logic is applied
- **Why**: why this transformation exists (not obvious from code)
- **Assumptions**: data quality or format assumptions baked in
- **Edge cases**: known cases that need special handling

Example:
```
Transform: revenue_attribution
What: assigns each order to the last marketing touch within 30 days
Why: finance requires last-touch model per FY23 attribution policy
Assumptions: user_id is consistent across sessions (not always true for guests)
Edge cases: guest checkouts with no touch - attributed to "direct"
```

### Step 5: Document failure modes and recovery

```
Failure mode: [source is late / schema change / job fails mid-run]
Impact: [what downstream consumers experience]
Detection: [how we know it's happening - alert name or monitoring link]
Recovery:
  1. [first action]
  2. [verify: command or query]
  3. [reprocessing steps if data needs backfill]
Escalate if: [condition that exceeds this runbook]
```

### Step 6: Document operational details

- **Monitoring**: links to dashboards, key metrics and alert thresholds
- **Logs**: where to find them, what to search for
- **Backfill procedure**: how to rerun historical data safely
- **Idempotency**: is the pipeline safe to rerun? If yes, how? If no, what guards exist?
- **Dependencies**: what must run before this pipeline (orchestration DAG link)

## Anti-Patterns

**1. Happy path only**
Bad: "The pipeline reads from Postgres and loads to BigQuery daily."
Good: Document what happens when Postgres is slow, when a schema column is dropped, when the daily job misses its window.

**2. Undocumented assumptions**
Bad: "Joins on user_id."
Good: "Joins on user_id. Assumes user_id is stable post-registration. Guest users (user_id = null) are excluded from this join and handled in the guest_orders pipeline."

**3. No data contract**
Bad: "Takes whatever the source sends."
Good: Define the expected schema, the schema change notification process, and how the pipeline handles unexpected fields.

**4. No idempotency statement**
Bad: Doc doesn't say whether reruns are safe.
Good: "This pipeline is idempotent. Reruns use MERGE (upsert) on event_id. Safe to rerun for any date range."

## Quality Checklist

- [ ] Pipeline overview covers purpose, source, destination, schedule, volume, SLA
- [ ] Data flow is documented stage by stage with input/output schemas
- [ ] Source data contracts are defined (schema, delivery SLA, schema change policy)
- [ ] Output guarantees are specified (freshness, completeness, deduplication)
- [ ] Non-trivial transformation logic explains the "why", not just the "what"
- [ ] Top 3 failure modes documented with recovery steps
- [ ] Backfill procedure exists
- [ ] Idempotency is explicitly stated
- [ ] Monitoring and log access documented
