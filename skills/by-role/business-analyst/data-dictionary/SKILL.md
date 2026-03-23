---
name: data-dictionary
description: >
  Generate a data dictionary documenting entities, fields, and business rules. Use when the
  user says "data dictionary", "document the data model", "what fields are in this table",
  "data definitions", "field descriptions", "CRUD matrix", "entity relationship",
  "data catalogue", "what data does this system store" - even if they don't explicitly
  say "data dictionary".
---

## Reference Files

- `references/data-dictionary-template.md` - Template table with all standard columns (field name, description, data type, format, valid values, source, owner, business rules, nullable, example). Read this in Step 3 when documenting individual entities.

## Overview

Based on the **BABOK Guide v3 (IIBA)** - Data Dictionary technique, which defines a data dictionary as a structured repository of data element definitions that eliminates ambiguity about what data means, where it comes from, and who owns it. Also draws on **Business Analysis Techniques** by James Cadle for Entity-Relationship Diagrams, CRUD Matrix, and Data Dictionary best practices. The key insight: a data dictionary is not a database schema dump. It is a business-facing document that defines what each data element means in business terms, who is the authoritative source, and what rules govern its values.

## Workflow

### Step 1: Identify data sources and scope
```
SYSTEM(S): [which systems are in scope]
PURPOSE: [why this data dictionary is being created - new build, migration, integration, audit]
AUDIENCE: [who will use this - developers, testers, business users, auditors]
SOURCES: [where to get the data definitions - database schemas, APIs, existing docs, SMEs]
```

### Step 2: List entities and relationships
Identify the key business entities and how they relate:
```
| Entity | Description | Relationships |
|--------|-------------|---------------|
| Customer | A person or organization that purchases products | Has many Orders; Belongs to one Segment |
| Order | A purchase transaction | Belongs to one Customer; Has many Line Items |
| Product | An item available for sale | Appears in many Line Items |
```

Draw or describe the Entity-Relationship model: cardinality (1:1, 1:N, M:N), mandatory vs. optional.

### Step 3: Document each entity's fields
For each entity, use the template from `references/data-dictionary-template.md`:
```
ENTITY: [name]

| Field | Description | Type | Format | Valid Values | Source | Nullable | Business Rules |
|-------|-------------|------|--------|-------------|--------|----------|---------------|
| customer_id | Unique identifier | UUID | xxxxxxxx-xxxx | System-generated | [system] | No | Immutable after creation |
| email | Primary contact email | String | name@domain.com | Valid email format | User input | No | Must be unique per customer |
| status | Account status | Enum | - | active, suspended, closed | [system] | No | Can only transition: active->suspended->closed |
```

### Step 4: Build the CRUD matrix
Map which functions Create, Read, Update, or Delete each entity:

```
| Entity / Function | Registration | Order Mgmt | Reporting | Admin |
|-------------------|-------------|------------|-----------|-------|
| Customer | C, R | R | R | C, R, U, D |
| Order | - | C, R, U | R | R, U, D |
| Product | - | R | R | C, R, U, D |
```

This reveals: which functions are authoritative (C), which are consumers (R only), and where delete authority sits.

### Step 5: Document data lineage
For shared or derived fields, trace the data path:
```
FIELD: total_revenue (Reporting Dashboard)
SOURCE: orders.line_items.unit_price * orders.line_items.quantity
TRANSFORMATION: Sum by customer_id, grouped by month
REFRESH: Daily batch at 02:00 UTC
AUTHORITATIVE SOURCE: Order Management System
```

### Step 6: Identify data quality rules
For each critical field:
```
FIELD: [name]
QUALITY RULE: [validation, format, range, uniqueness, referential integrity]
CURRENT QUALITY: [% compliant if known]
REMEDIATION: [what to do when data violates the rule]
```

### Step 7: Output the data dictionary
Deliver: entity list with relationships, field-level definitions per entity, CRUD matrix, data lineage for derived/shared fields, and data quality rules.

## Anti-Patterns

**1. Database schema dump labeled as a data dictionary**
Bad: Exporting column names and data types from the database and calling it done.
Good: Each field has a business description, valid values, source system, and business rules.

**2. Technical descriptions only**
Bad: "VARCHAR(255), NOT NULL" (That's the schema, not the dictionary.)
Good: "Customer's primary email address. Used for order confirmations and password reset. Must be unique per customer account."

**3. No ownership or source attribution**
Bad: Field definitions without noting which system is the authoritative source.
Good: Every field traces to its source system and data owner. When systems disagree, the authoritative source is explicit.

**4. Static document that's never updated**
Bad: Data dictionary written at project start, never maintained.
Good: Data dictionary is a living document updated whenever entities, fields, or rules change. Version-controlled.

**5. Missing CRUD matrix**
Bad: Field definitions without documenting which functions interact with each entity.
Good: CRUD matrix reveals who creates, reads, updates, and deletes each entity - critical for integration and security design.

## Quality Checklist

- [ ] Scope and purpose defined (which systems, why, for whom)
- [ ] All entities listed with business descriptions and relationships
- [ ] Every field has: name, description, type, format, valid values, source, nullable flag
- [ ] Business rules documented per field (not just data types)
- [ ] CRUD matrix completed for all entities and functions
- [ ] Data lineage documented for derived or shared fields
- [ ] Authoritative source identified for each entity
- [ ] Data quality rules defined for critical fields
- [ ] Descriptions are in business language, not just technical notation
