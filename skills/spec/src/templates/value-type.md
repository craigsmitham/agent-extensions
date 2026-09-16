# Value Type template

Use for one kind of value in the business domain that has no identity, such as
money, a rental period, or an email address. Apply the
[Spec profile](../references/profile.md). The Type contract is normative; the
remaining sections guide authoring.

It parallels the [Entity Type template](entity-type.md), with the
[differences](#differences-from-the-entity-type-template) recorded below.

## Type contract

A Value Type document is placed as the Data module's
[fixed locations](../references/modules/data.md#fixed-locations) state, when its
[entity type, value type, or data attribute](../references/modules/data.md#entity-type-value-type-or-data-attribute)
test makes the content a Value Type.

- **VT-1** The title MUST name the kind of value as a singular noun phrase,
  such as "Money" or "Email address".
- **VT-2** A Value Type document MUST include these sections:
  - **Definition**: what a value of this type is, following the profile's
    [definition rules](../references/profile.md#definitions).
  - **Structure**: either the data attributes that make up a value, each with
    its definition, representation, and whether it is required; or the value's
    domain: its kind and its allowed values, range, units, precision, or
    pattern.
  - **Invariants** *(optional)*: the invariants of the value type.
- **VT-3** A domain that lists allowed values MUST list every allowed value with
  its meaning; a value not listed is not allowed.

## Suggested document

```markdown
---
type: Value Type
title: <Singular noun phrase>
description: <What a value of this type is, in one sentence>
status: draft
---

# <Singular noun phrase>

## Definition

<A phrase naming the broader kind of value and what distinguishes it.>

## Structure

| Attribute | Definition | Representation | Required |
| --- | --- | --- | --- |
| <Name> | <What it is> | <[<Value type>](<link>), or a kind with allowed values, range, units, or precision> | <Yes \| No \| Condition> |

<For a value with no parts, its domain instead of the table.>

## Invariants
## Illustrations
## Open questions
## Related
```

## Writing guidance

### Differences from the Entity Type template

| Difference | Reason |
| --- | --- |
| No **Identity**, **Relationships**, or **Lifecycle** | A value is interchangeable with an equal value, so there are no instances to tell apart, relate, or track; a kind of thing that has them is an Entity Type, as [entity type, value type, or data attribute](../references/modules/data.md#entity-type-value-type-or-data-attribute) decides. |

### Definition

The value type's **Definition** says what a value of this type is, as a phrase
that could replace the value type's name, and is the only definition of that
name.

### Structure

A value made of parts lists each data attribute. *Money* has an amount, a
decimal to the precision of the currency's minor unit, and a currency, an
ISO 4217 currency code. A part may itself link another value type.

A value with no parts states its domain:

| Domain | Example |
| --- | --- |
| Enumeration | Equipment condition: one of *Serviceable*, *Needs repair*, or *Withdrawn*, each with its meaning |
| Range, units, and precision | Operating hours: whole hours, never negative |
| Pattern or standard | Email address: an address as defined by RFC 5322 |

Two values are equal when all their attributes are equal or, for a value with
a domain, when they are the same allowed value. When the business treats
values as equal on another basis, state that equality in **Structure**.

A format, length, or limit belongs here only as
[work management and design](../references/profile.md#work-management-and-design)
allows, as ISO 4217 sets currency codes.

### When to create one

A value that more than one entity type, value type, or external interface uses
is a Value Type, as
[P-DAT-3](../references/modules/data.md#entity-type-value-type-or-data-attribute) requires. A
value used in one place can have one too, or be defined where it is used: fuel
level, which only the equipment telematics interface carries, is defined
there.

### Invariants

State conditions every value satisfies across its attributes because of what
it means, such as "A rental period's last day is not earlier than its first
day". A condition on values made by combining others, such as a sum of money
having the one currency of the amounts added, is placed by
[invariant, business rule, or requirement](../references/modules/data.md#invariant-business-rule-or-requirement):
it is an invariant because it follows from what money means.

### Illustrations and related

Illustrate valid values and, where the edge of the allowed values is not
obvious, invalid values with the reason each is invalid. Under **Related**,
link the value types this one is made of beyond those linked in **Structure**.
Record undecided parts, allowed values, or invariants under
**Open questions**.
