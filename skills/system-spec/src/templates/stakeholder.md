# Stakeholder template

Use for a person, group, or class of them who must be satisfied, or can
withhold consent, for the system to achieve its results: their interest, what
they value, and any authority they hold over it.

## Type contract

- **STK-1** The title MUST name the stakeholder or class of stakeholders, such
  as "Equipment insurer".
- **STK-2** A Stakeholder document MUST include these sections:
  - **Interest**: the stakeholder's interest in the system.
  - **Values**: what the stakeholder values from the system.
  - **Authority** *(optional)*: what the stakeholder decides, approves, or can
    veto about the system, such as acceptance, funding, or a constraint.
- **STK-4** A stakeholder MUST be created only when the system cannot
  achieve its results without the stakeholder's satisfaction or consent.
- **STK-5** A Stakeholder document MUST NOT describe how the stakeholder uses
  the system or what they need from it in that use.

## Suggested document

```markdown
---
type: Stakeholder
title: <Stakeholder>
description: <Who they are>, with an interest in <what about the system>
---

# <Stakeholder>

## Interest
## Values
## Authority
## Open questions
## Related
```

## Writing guidance

### Stakeholders, users, and job performers

The people whose progress a [job to be done](job-to-be-done.md) describes are
those the system is for. A stakeholder is someone else the system must
satisfy, because they can say no: a sponsor, insurer, regulator, partner,
funder, or the staff whose work it changes. How people use the system is
described by [user classes](user-class.md#users-and-stakeholders), so a group
can be a user class for its use and a stakeholder for an interest apart from
it, such as a staff group whose agreement a change of working hours needs.
Each is described where its type belongs.

Write one document for each stakeholder whose interest, values, or authority
differ from the others'. Stakeholders who share all three, such as several
funders with the same terms, are one class of stakeholders.

### Values and authority

- Record what a stakeholder values as they state it. Ask them, or cite a
  source such as a contract or policy in `sources` frontmatter; a value
  inferred from their role is an open question.
- Include **Authority** when the stakeholder decides, approves, or can veto
  something about the system, such as acceptance, funding, or compliance, so
  that a reader knows whose decision governs a change. Omit it when they hold
  none.
- State authority as the constraints a stakeholder sets and the decisions they
  approve. A stakeholder's preferred solution is not authority over the
  specification; the constraint behind it is, and the choice of solution
  stays with those accountable for the system.
- A value that becomes an obligation on the system, such as a condition of
  insurance cover, is a Requirement or Business Rule, and the stakeholder
  links it rather than restating it.

~~~markdown
# Equipment insurer

## Interest

Insures the equipment the business rents, and so has an interest in which
equipment the rental system allows to be rented.

## Values

Equipment with an overdue inspection is withdrawn from rental, as
[Overdue inspection withdrawal](<link>) requires.
~~~
