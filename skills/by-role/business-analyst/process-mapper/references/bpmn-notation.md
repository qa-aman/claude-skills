# BPMN 2.0 Notation Reference

Use this reference in Step 3 when mapping processes. BPMN (Business Process Model and Notation) is the international standard for process diagrams. Use these symbols consistently across all process maps.

---

## Events (Circles)

| Symbol | Name | Description | When to Use |
|--------|------|-------------|-------------|
| Thin circle | **Start Event** | Triggers the process | Every process has exactly one start event |
| Bold circle | **End Event** | Process completes | Every path must reach an end event |
| Double circle | **Intermediate Event** | Something happens during the process | Timer waits, message received mid-flow, escalation |
| Circle + clock | **Timer Event** | Time-based trigger or delay | Scheduled processes, SLA deadlines, wait periods |
| Circle + envelope | **Message Event** | Triggered by receiving a message | Email received, API callback, notification arrives |
| Circle + lightning | **Error Event** | Exception or failure | System errors, validation failures, timeouts |

## Activities (Rounded Rectangles)

| Symbol | Name | Description | When to Use |
|--------|------|-------------|-------------|
| Rounded rectangle | **Task** | A single unit of work | Atomic action performed by one actor |
| Rounded rect + [+] | **Sub-process** | Contains a nested process | Complex step that expands into its own diagram |
| Rounded rect + ~ | **Call Activity** | Reusable process referenced here | Shared sub-processes used across multiple flows |
| Rounded rect + user icon | **User Task** | Performed by a person | Manual approval, data entry, review |
| Rounded rect + gear icon | **Service Task** | Performed by a system | API calls, automated calculations, data sync |

## Gateways (Diamonds)

| Symbol | Name | Description | When to Use |
|--------|------|-------------|-------------|
| Diamond + X | **Exclusive (XOR)** | One path chosen, others blocked | If/else decisions: "Is order > $1000?" |
| Diamond + + | **Parallel (AND)** | All paths execute simultaneously | Tasks that happen in parallel: "Send email AND update database" |
| Diamond + O | **Inclusive (OR)** | One or more paths chosen | Multiple conditions may be true: "Notify email AND/OR SMS" |
| Diamond + pentagon | **Event-based** | Path chosen by which event occurs first | Wait for payment OR timeout after 7 days |

## Flows (Arrows)

| Symbol | Name | Description | When to Use |
|--------|------|-------------|-------------|
| Solid arrow | **Sequence Flow** | Order of activities | All steps within the same pool |
| Dashed arrow | **Message Flow** | Communication between pools | Messages between organizations or systems |
| Dotted line | **Association** | Links artifacts to elements | Connecting data objects or annotations |

## Swimlanes

| Symbol | Name | Description | When to Use |
|--------|------|-------------|-------------|
| Large rectangle | **Pool** | Represents an organization or participant | Each external organization gets its own pool |
| Horizontal band | **Lane** | Represents a role or department within a pool | Each role or system within your organization |

## Common Patterns

**Happy path first**: Always draw the main success scenario as a straight left-to-right flow. Add exceptions and alternatives branching off from gateways.

**Exclusive gateway for decisions**:
```
[Review Application] --> <Approved?> --Yes--> [Process Order]
                                     --No---> [Send Rejection]
```

**Parallel split and join**:
```
[Receive Order] --> <+> --> [Check Inventory]  --> <+> --> [Ship Order]
                        --> [Process Payment]  -->
```

**Error boundary event**:
```
[Call External API] --error--> [Log Failure] --> [Notify Support]
                    --success--> [Process Response]
```
