# Principles template

Use for the guidance by which the system's business decides between
reasonable options that conflict, whether that business is a whole enterprise
or product or sits within an enclosing business.

## Type contract

- **PRI-1** The title MUST be "<Business> principles".
- **PRI-2** A Principles document MUST include these sections:
  - **Principles**: one entry for each principle, headed by its short name.
- **PRI-3** An entry's principle MUST be the first paragraph below its
  heading, and the rest of the entry MUST be entry lines.
- **PRI-4** Principles MUST be unranked unless a paragraph before the first
  entry states that they are listed in an agreed order of precedence, in which
  case an earlier principle prevails over a later one that conflicts with it.
- **PRI-5** Each principle MUST decide between options that the business
  would otherwise find reasonable, and MUST name what it prevails over.
- **PRI-6** A principle MUST NOT state an obligation, a rule, design, a value
  of the business's culture, how the system is built or the work on it is
  done, or a strategy for a current challenge.
- **PRI-7** A Principles document SHOULD NOT state more than seven principles.

## Suggested document

```markdown
---
type: Principles
title: <Business> principles
description: How <business> decides between reasonable options that conflict
---

# <Business> principles

## Principles

### <Short name>

<What to prefer, and what it prevails over.>

- **Rationale:** <the conflict or risk that makes the stand necessary>
- **Example:** <a decision the principle settles, or a link to the rule or requirement that records it>

## Open questions
## Related
```

## Writing guidance

### Principles and obligations

A principle guides a decision that needs judgment; an obligation or rule can
be checked case by case. "The business rents only equipment it knows to be
safe" guides many decisions; "Equipment whose inspection is overdue must be
withdrawn from rental" is the [Overdue inspection withdrawal](<link>) rule,
which follows from it and links it under **Rationale**. The profile's
[ownership tests](../references/profile.md#principle-or-obligation)
decide which is which.

### Principles, values, and strategy

A principle holds whichever system serves the business and whatever it is
working on now. Three kinds of guidance that resemble principles belong
elsewhere:

- A value of the business's culture, such as "we are transparent", takes no
  stand between options for what the business offers.
- Guidance for how the system is built or how work on it is done, such as
  engineering principles, a style guide, or "ship in small increments", belongs
  to design or work-management records, as the profile's
  [P-CON-7 and P-CON-8](../references/profile.md#work-management-and-design)
  require.
- A stand taken to overcome a current challenge, such as concentrating on
  dependable reservation confirmations before delivery from more depots, is
  [strategy](strategy.md), which changes when the challenge does.

### Writing a principle

- Take a stand: name what the principle prevails over, as in "safe equipment
  over availability". A principle that no one would dispute, such as "be
  easy to use", decides nothing.
- Name the principle in a few words, and state it in one to three sentences.
- Give the conflict or risk that makes the stand necessary on the
  **Rationale** line, when the principle does not make it plain. A principle
  whose conflict no longer arises is due for review.
- Give a decision the principle has settled on the **Example** line, to show
  that it decides between reasonable options. When a rule or requirement
  records that decision, link it rather than restating it. Only the principle
  is binding.
- Write only principles that a person or a source states. Do not compose
  them from what the system does; a decision that the stated principles do
  not settle is an open question where it arises.

~~~markdown
These principles are listed in the order of precedence that the business
has agreed.

### Safe equipment over availability

The business rents only equipment it knows to be safe, even when a contractor
goes without the equipment they want.

- **Rationale:** An accident with rented equipment harms the contractor and
  the business, and no rental is worth that risk.
- **Example:** [Overdue inspection withdrawal](<link>)

### Contractors' time over depot convenience

When a choice saves contractors time at the cost of more work for depot staff,
the business chooses contractors' time.

- **Rationale:** Depot staff would prefer to prepare equipment only during
  opening hours, but contractors rent to keep work moving, and a lost working
  day costs them more than the rental.
- **Example:** Customers reserve equipment online at any hour, although depot
  staff then prepare equipment reserved overnight.
~~~

### Precedence

A principle's own stand says what prevails within it. Between principles, an
order binds only when the business has agreed it; the order in which
principles happen to be written is not a ranking, so do not state that the
list is ordered unless a person or a source says so. When two unranked
principles conflict in a decision, record the conflict as an open question.

Priorities between user classes or between qualities, such as which user
class prevails when their needs conflict, are principles, linking the user
classes or quality characteristics they rank.

### Shared and enclosing principles

When several systems serve one business, one corpus holds the principles and
the others link them. A business within an enclosing business links the
enclosing principles and states its own for decisions that only it faces, such
as which of its user classes prevails; its principles add to the enclosing
ones and do not restate or contradict them, as the profile's
[Structure](../references/profile.md#structure) requires. A principle that
seems to conflict with an enclosing one is an open question, and until it is
resolved the enclosing principle prevails.
