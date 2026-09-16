# External Interface template

Use for one connection across the boundary of the system or a subsystem to an
external system or a device, and what passes across it. Apply the
[Spec profile](../references/profile.md). The Type contract is normative; the
remaining sections guide authoring.

## Type contract

- **EI-1** The title MUST name the counterpart, such as "Payment service".
- **EI-2** An External Interface document MUST include these sections:
  - **Purpose**: why the connection exists and what the system or subsystem
    relies on it for.
  - **Exchanges**: every item that passes across the connection, when it
    passes, and in which direction.
  - **Formats and protocols** *(when the counterpart or a named standard
    requires a format or protocol)*: each required format or protocol, and
    who requires it.
- **EI-3** **Exchanges** MUST link each exchanged item that is a Value Type.
- **EI-4** An External Interface document MUST NOT describe how the system or
  the counterpart implements the connection, or operations concerns for it.

## Suggested document

```markdown
---
type: External Interface
title: <Counterpart name>
description: <What passes between the system or subsystem and the counterpart, and why, in one sentence>
status: draft
---

# <Counterpart name>

## Purpose

## Exchanges

No item other than those listed passes across the connection.

| Item | Direction | When | Definition |
| --- | --- | --- | --- |
| <Item name> | <Inbound \| Outbound> | <Event or schedule> | [<Value type>](<link>), or <what the item is, and its kind, allowed values, range, units, or precision> |

## Formats and protocols
## Illustrations
## Open questions
## Related
```

## Writing guidance

### Boundary

The counterpart is an external system, such as the payment service, or a
device, such as equipment telematics units. Every External Interface lives in
the system's `interfaces/` folder. A connection that crosses only a subsystem's
boundary links that subsystem under **Related**, such as
[Fleet maintenance](<link>) for equipment telematics, and each item's direction
is seen from that subsystem.

An External Interface describes a system or device, not people: a group of
people who use the system is a [User Class](user-class.md). A counterpart's
goals in an interaction are stated by the use cases in which it is an actor.

### Purpose

State why the connection exists and what the system relies on it for, such as
the rental system relying on the payment service to authorize deposits, charge
fees, and refund deposits.

### Exchanges

List each item once, with the event or schedule on which it passes. An item
that an entity type, value type, or another external interface also uses is a
Value Type, as
[P-DAT-3](../references/modules/data.md#entity-type-value-type-or-data-attribute) requires. An
item that only this connection uses can be defined here, following the
profile's [definitions](../references/profile.md#definitions) rules.

~~~markdown
## Exchanges

No item other than those listed passes between equipment telematics and
fleet maintenance.

| Item | Direction | When | Definition |
| --- | --- | --- | --- |
| Equipment condition | Inbound | Every 15 minutes, for each equipment item | [Equipment condition](<link>) |
| Operating hours | Inbound | Every 15 minutes, for each equipment item | [Operating hours](<link>) |
| Fuel level | Inbound | Every 15 minutes, for each equipment item | The proportion of an equipment item's fuel capacity that its tank holds, as a whole-number percentage from 0 to 100 |
~~~

A required level for a connection, such as how quickly the payment service
must answer, is a Quality Requirement whose **Requirement** names and links
this document.

### Formats, illustrations, and related records

- **Formats and protocols** states only the formats and protocols that the
  counterpart publishes or a named standard defines, each with who requires
  it. A format the system chooses for itself is design.
- **Illustrations** holds sample messages or sequence diagrams that help a
  reader follow the exchanges.
- **Open questions** records undecided items, timing, or formats, and
  requirements of the counterpart that are not yet confirmed.
- **Related** links the counterpart's own documentation, and the records that
  describe how the connection is implemented or operated.
