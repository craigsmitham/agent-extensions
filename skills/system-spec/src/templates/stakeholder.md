# Stakeholder template

Use for a person, group, or class of them with an interest in the system who
does not use it, what they value, and any authority they hold over it.

## Type contract

- **STK-1** The title MUST name the stakeholder or class of stakeholders, such
  as "Equipment insurer".
- **STK-2** A Stakeholder document MUST include these sections:
  - **Interest**: the stakeholder's interest in the system.
  - **Values**: what the stakeholder values from the system.
  - **Authority** *(optional)*: what the stakeholder decides, approves, or can
    veto about the system.
- **STK-3** A stakeholder MUST NOT be a person or group that uses the system
  or its outputs directly.

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

A stakeholder is someone the system must satisfy without serving them
directly: a sponsor, insurer, regulator, partner, or funder. People who use
the system, including those who operate it, are
[user classes](user-class.md#users-and-stakeholders), and people whose
progress a [job to be done](job-to-be-done.md) describes are its job
performers. One organization can be all three through different people, and
each is described where its type belongs.

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
