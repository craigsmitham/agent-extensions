# Stakeholders template

Use for the people and groups with an interest in the system who do not use
it, what each values, and any authority each holds over it.

## Type contract

- **STK-1** The title MUST be "<System> stakeholders".
- **STK-2** A Stakeholders document MUST include these sections:
  - **Stakeholders**: one entry for each stakeholder or class of
    stakeholders, headed by its name.
- **STK-3** An entry's interest in the system MUST be the first paragraph
  below its heading, and the rest of the entry MUST be entry lines.
- **STK-4** An entry's **Values** line MUST state what the stakeholder values
  from the system, and its **Authority** line what the stakeholder decides,
  approves, or can veto about it; both lines are binding content.
- **STK-5** A stakeholder MUST NOT be a person or group that uses the system
  or its outputs directly.

## Suggested document

```markdown
---
type: Stakeholders
title: <System> stakeholders
description: Who has an interest in <system> without using it, and what each values
---

# <System> stakeholders

## Stakeholders

### <Stakeholder>

<Their interest in the system.>

- **Values:** <what they value from the system>
- **Authority:** <what they decide, approve, or can veto>

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

### Values and authority

- Record what a stakeholder values as they state it. Ask them, or cite a
  source such as a contract or policy; a value inferred from their role is an
  open question.
- State **Authority** when the stakeholder decides, approves, or can veto
  something about the system, such as acceptance, funding, or compliance, so
  that a reader knows whose decision governs a change. Omit the line when
  they hold none.
- A value that becomes an obligation on the system, such as a condition of
  insurance cover, is a Requirement or Business Rule, and the entry links it
  rather than restating it.

~~~markdown
### Equipment insurer

Insures the equipment the business rents, and so has an interest in which
equipment the rental system allows to be rented.

- **Values:** Equipment with an overdue inspection is withdrawn from rental,
  as [Overdue inspection withdrawal](<link>) requires.
~~~
