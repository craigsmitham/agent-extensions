# Requirement template

Use for one obligation that the system or a subsystem must satisfy, other than
a required level of quality, which is a
[Quality Requirement](quality-requirement.md). Apply the
[Spec profile](../references/profile.md). The Type contract is normative; the
remaining sections guide authoring.

## Type contract

A Requirement document is placed as the profile's
[rule-placed types](../references/profile.md#rule-placed-types) rules state,
at its owner, which also sets its subject.

- **REQ-1** The title MUST name the obligation briefly as a declarative
  phrase, such as "Reservations of unavailable equipment are rejected".
- **REQ-2** A Requirement document MUST include these sections:
  - **Requirement**: the obligation, in the form that states it most clearly,
    naming the subject, any conditions or trigger under which the obligation
    applies, the observable outcome, limit, or prohibition, and any
    exceptions, with *shall* for the obligation.
  - **Rationale** *(optional)*: why the obligation exists.
  - **Verification** *(optional)*: how satisfaction will be assessed, and what
    counts as satisfied.
- **REQ-3** A Requirement document MUST state exactly one obligation.

## Suggested document

```markdown
---
type: Requirement
title: <Obligation as a short declarative phrase>
description: <The requirement statement, or a one-sentence summary of it>
status: draft
---

# <Obligation as a short declarative phrase>

## Requirement

<When <trigger>, the <subject> shall <response>.>

## Illustrations
## Rationale
## Verification
## Open questions
## Related
```

## Writing guidance

### Subject and sections

The document's location shows its owner, which can be a feature or feature
component, and its subject: the subsystem it is placed within, or otherwise
the system. Name that subject in the statement.

Keep the binding obligation, with its exceptions, in **Requirement**, and
keep rationale out of the statement. **Illustrations** can hold acceptance
examples; they support **Verification**, which assesses satisfaction by test,
analysis, inspection, or demonstration, but they do not replace the
requirement. Record unresolved meaning, feasibility, or targets under
**Open questions**, and handle obligations that cannot both be fully met as
[Not yet defined](../references/profile.md#not-yet-defined) describes.

Record where the obligation came from, such as a stakeholder decision,
regulation, incident, or research, in the `sources` frontmatter.

### Statement

A well-formed requirement is necessary, appropriate to its subject,
unambiguous, complete, singular, feasible, verifiable, and correct against its
source, as ISO/IEC/IEEE 29148 describes; the same holds for a quality
requirement.

- State one obligation. Several conditions may apply to one obligation; split
  the requirement when its parts could be decided or assessed independently.
- Write in the active voice, naming the subject after any condition. Use
  *shall* for the obligation. Avoid *shall be able to*, and prefer a positive
  statement to *shall not* where one reads as clearly.
- Replace vague qualifiers such as *fast*, *secure*, or *user-friendly* with a
  link to the Quality Requirement that states the required level, or, without
  the Quality module, with the level itself, as the profile's
  [modules](../references/profile.md#modules) table describes.
- Use each term as the glossary defines it, and link to the entry, the value
  type, or the named condition the statement uses.

EARS patterns keep conditions and responses distinct:

| Pattern | Use for | Form |
| --- | --- | --- |
| Ubiquitous | An obligation that always applies | The <subject> shall <response>. |
| Event-driven | A response to a trigger | When <trigger>, the <subject> shall <response>. |
| State-driven | An obligation that holds while a state persists | While <state>, the <subject> shall <response>. |
| Unwanted behavior | A response to an undesired condition | If <condition>, then the <subject> shall <response>. |

Combine keywords for a complex requirement, such as "While <state>, when
<trigger>, the <subject> shall <response>." Use EARS for a statement; when
another form is clearer, use it, as [Form](#form) describes.

### Form

Choose the form that leaves the least room for misreading, and make it the
binding content rather than a supplement to a vaguer statement.

| Form | Suits | Introduce with |
| --- | --- | --- |
| Statement | A single condition and response | The statement itself |
| Decision table | A response that depends on combinations of conditions | The <subject> shall respond to each combination of conditions as the following table specifies. |
| Sequence or flow diagram | A required order of observable interactions | The <subject> shall exchange messages in the order the following diagram shows. |
| Formula or limit table | Calculations, thresholds, or values that vary by condition | The <subject> shall compute <value> as the following formula states. |

A requirement that responds to lifecycle transitions links to the Entity
Type's **Lifecycle** for the states and transitions, as
[Where content goes](../references/modules/data.md#where-content-goes) assigns. A
deadline for each notice sent is a Requirement rather than a Quality
Requirement, as
[Quality requirement or requirement](../references/modules/quality.md#quality-requirement-or-requirement)
decides:

~~~markdown
## Requirement

When a [reservation](<link to Reservation lifecycle>) changes state, the rental
system shall send the customer the notice that the following table lists for
that change within 5 minutes of the change, and shall send no other
reservation notice.

| Change | Notice |
| --- | --- |
| Held to Confirmed | Confirmation, with the rental period and collection depot |
| Held to Expired | Expiry, with the reason |
| Confirmed to Cancelled | Cancellation, with any deposit refund |
~~~

Where one form would carry several independently decidable obligations, such
as a large table covering unrelated behavior, split it into several
requirements.

### Design constraints

A requirement that names a technology, platform, or design is a design
constraint, such as
[Deposits are taken only through the payment service](<link>), and only a
design constraint may name one, as
[Work management and design](../references/profile.md#work-management-and-design)
states. Other kinds of obligation, such as those whose authority is a law or
standard, or that concern delivery or migration, name that law, standard, or
activity in the statement or rationale, such as
[Card payments meet PCI DSS](<link>) and
[Open reservations are migrated from the previous system](<link>).

### Related

State each relationship once, in bold, as the relationships tables of the
[profile](../references/profile.md#relationships) and the
[Rules module](../references/modules/rules.md#relationships) assign to a
Requirement:

- **serves**: the business objective, user class, or quality characteristic
  that justifies the obligation;
- **enforces**: the business rule the requirement makes the system respect,
  such as [Underage rentals are rejected](<link>) enforcing
  [Minimum renter age](<link>); and
- **replaces**: the deprecated requirement this one supersedes.

Link the entity types, value types, and external interfaces the obligation is
about under **Related**.
