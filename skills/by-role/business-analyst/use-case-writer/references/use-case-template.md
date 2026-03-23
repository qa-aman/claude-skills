# Cockburn Fully Dressed Use Case Template

Use this template in Step 3 when writing individual use cases. The Fully Dressed format from **Writing Effective Use Cases** by Alistair Cockburn is the most complete style - use it for critical or complex use cases. For simpler cases, use the Casual style (narrative paragraph) or One-Column style (numbered steps only).

---

## Template

```
USE CASE: UC-[number]: [Title - verb phrase describing the goal]

PRIMARY ACTOR: [who initiates this use case]
SUPPORTING ACTORS: [other actors involved]
GOAL: [what the primary actor is trying to achieve]
SCOPE: [system under design - black-box or white-box]
LEVEL: [Cloud / Kite / Sea Level / Fish]
STAKEHOLDERS AND INTERESTS:
  - [Stakeholder 1]: [what they need from this use case]
  - [Stakeholder 2]: [what they need]

PRECONDITIONS:
  - [What must be true before this use case can start]
  - [e.g., Actor is authenticated, order exists in draft status]

SUCCESS GUARANTEE (Postconditions):
  - [What is true when the use case succeeds]
  - [e.g., Order is confirmed, inventory reserved, confirmation email sent]

MAIN SUCCESS SCENARIO:
  1. [Actor] [action - what they do]
  2. [System] [response - what the system does]
  3. [Actor] [next action]
  4. [System] [response]
  ...

EXTENSIONS:
  [step]a. [Condition that triggers this extension]:
    [step]a1. [System or actor action]
    [step]a2. [Next action]
    [step]a3. Return to step [N] / Use case fails with [outcome]

  [step]b. [Another condition]:
    [step]b1. [Action]

TECHNOLOGY AND DATA VARIATIONS:
  [step]. [Variation - e.g., "Payment may be credit card, PayPal, or bank transfer"]

RELATED INFORMATION:
  - Frequency: [how often this use case occurs]
  - Performance: [response time expectations]
  - Open issues: [unresolved questions]
```

---

## Worked Example

```
USE CASE: UC-003: Place Online Order

PRIMARY ACTOR: Customer
SUPPORTING ACTORS: Payment Gateway, Inventory System
GOAL: Purchase selected items and receive order confirmation
SCOPE: E-commerce Platform (black-box)
LEVEL: Sea Level (User Goal)
STAKEHOLDERS AND INTERESTS:
  - Customer: Wants a quick, reliable checkout experience
  - Finance: Wants payment captured before fulfillment
  - Warehouse: Wants accurate order details for picking

PRECONDITIONS:
  - Customer is logged in
  - Shopping cart contains at least one item

SUCCESS GUARANTEE (Postconditions):
  - Order is recorded with a unique order number
  - Payment is authorized
  - Inventory is reserved for ordered items
  - Customer receives confirmation email with order details

MAIN SUCCESS SCENARIO:
  1. Customer reviews shopping cart and selects "Checkout"
  2. System displays order summary with item details, quantities, and subtotal
  3. Customer confirms or updates shipping address
  4. System calculates shipping cost and tax, displays total
  5. Customer selects payment method and enters payment details
  6. System submits payment to Payment Gateway for authorization
  7. Payment Gateway confirms authorization
  8. System reserves inventory via Inventory System
  9. System records the order and generates order number
  10. System sends confirmation email to Customer
  11. System displays order confirmation page with order number

EXTENSIONS:
  3a. Customer wants to ship to a new address:
    3a1. Customer enters new shipping address
    3a2. System validates address format
    3a3. Return to step 4

  3a2a. Address validation fails:
    3a2a1. System displays validation errors
    3a2a2. Return to step 3a1

  5a. Customer selects saved payment method:
    5a1. System retrieves saved payment details
    5a2. Return to step 6

  7a. Payment authorization fails:
    7a1. System displays payment error message
    7a2. Customer re-enters payment details or selects different method
    7a3. Return to step 6

  7a2a. Customer fails payment 3 times:
    7a2a1. System suggests contacting support
    7a2a2. Use case fails: order not placed

  8a. Inventory insufficient for one or more items:
    8a1. System notifies customer which items are unavailable
    8a2. Customer removes or substitutes items
    8a3. Return to step 4

TECHNOLOGY AND DATA VARIATIONS:
  5. Payment may be credit card, digital wallet, or bank transfer
  3. Address may be domestic or international (affects tax calculation)

RELATED INFORMATION:
  - Frequency: ~500 orders per day
  - Performance: Steps 6-8 must complete within 5 seconds
  - Open issues: Should we support guest checkout (no login)?
```

---

## Goal Level Guide

| Level | Icon | Description | Example | When to Use |
|-------|------|-------------|---------|-------------|
| **Cloud** | (very high) | Enterprise strategic goal | "Run the business profitably" | Enterprise architecture only |
| **Kite** | (summary) | Multiple user sessions | "Manage customer lifecycle" | Overview documentation |
| **Sea Level** | (user goal) | One actor, one sitting, one goal | "Place an order" | **Most use cases go here** |
| **Fish** | (subfunction) | A step within a use case | "Validate payment" | Shared subfunctions (includes) |
| **Clam** | (too low) | Implementation detail | "Save to database" | **Never write at this level** |

If your use case has 15+ main steps, it's probably at Kite level - split it into multiple Sea Level use cases.
If your steps mention UI elements or database operations, you've dropped to Clam level - go back up.
