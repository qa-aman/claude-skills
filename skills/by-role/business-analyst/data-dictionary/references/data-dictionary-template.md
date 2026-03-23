# Data Dictionary Template

Use this template in Step 3 when documenting each entity's fields. Copy the table structure for each entity and fill in every column. If a column doesn't apply, write "N/A" - don't leave it blank.

---

## Field Definition Table

| Column | What to Write | Example |
|--------|--------------|---------|
| **Field Name** | Technical name as it appears in the system | customer_email |
| **Business Name** | Human-readable name used by business stakeholders | Customer Email |
| **Description** | What this field means in business terms (not technical) | Primary email address used for order confirmations and account communications |
| **Data Type** | Technical type | String, Integer, UUID, Boolean, Date, Enum, Decimal |
| **Format** | Pattern or mask | name@domain.com, YYYY-MM-DD, ###-###-####, 2 decimal places |
| **Length / Precision** | Maximum length or decimal precision | Max 255 chars, Decimal(10,2) |
| **Valid Values** | Allowed values or range | Enum: [active, suspended, closed]; Range: 0-100; Regex pattern |
| **Default Value** | Value assigned if not provided | "active", 0, NULL, current_timestamp |
| **Nullable** | Can this field be empty? | Yes / No |
| **Unique** | Must values be unique? | Yes (globally) / Yes (per tenant) / No |
| **Source System** | Which system creates or owns this data | Order Management System, User Registration |
| **Data Owner** | Business role responsible for data quality | Customer Success Manager, Finance Team |
| **Business Rules** | Rules governing this field | Must be unique per customer; immutable after order confirmation; cannot be blank for active customers |
| **Security Classification** | Sensitivity level | Public, Internal, Confidential, PII, PHI |
| **Example Value** | A realistic sample | jane.doe@example.com |

---

## Blank Template (Copy Per Entity)

```
ENTITY: [Entity Name]
DESCRIPTION: [What this entity represents in business terms]
PRIMARY KEY: [field name]
AUTHORITATIVE SOURCE: [which system is the master]

| Field Name | Business Name | Description | Data Type | Format | Valid Values | Default | Nullable | Source | Business Rules |
|------------|--------------|-------------|-----------|--------|-------------|---------|----------|--------|---------------|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
```

---

## Tips for Writing Good Field Descriptions

| Bad Description | Good Description | Why |
|-----------------|-----------------|-----|
| "The email" | "Primary email address used for order confirmations and password reset" | States the business purpose |
| "Status field" | "Current account lifecycle status. Transitions: active -> suspended -> closed. Only Admin can reactivate." | Documents the state machine |
| "Amount" | "Total order amount including tax and discounts, in the customer's local currency" | Specifies what's included and the unit |
| "Date" | "Date the order was placed, in UTC. Set automatically at checkout completion." | Specifies timezone and trigger |
| "Flag" | "Whether the customer has opted in to marketing emails. Default false. Can only be set by the customer." | Documents who can change it |
