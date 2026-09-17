# Principles template

Use for the guidance by which the business or product that the system serves
decides between reasonable options that conflict, in order of precedence.

## Type contract

- **PRI-1** The title MUST be "<Business or product> principles".
- **PRI-2** A Principles document MUST include these sections:
  - **Principles**: one entry for each principle, headed by its short name.
- **PRI-3** An entry's principle MUST be the first paragraph below its
  heading, and the rest of the entry MUST be entry lines.
- **PRI-4** Principles MUST be listed so that an earlier principle prevails
  over a later one that conflicts with it, unless a paragraph before the first
  entry states that they are unranked.
- **PRI-5** Each principle MUST decide between options that the business
  would otherwise find reasonable.
- **PRI-6** A principle MUST NOT state an obligation, a rule, or design.
- **PRI-7** A Principles document SHOULD NOT state more than seven principles.

## Suggested document

```markdown
---
type: Principles
title: <Business or product> principles
description: How <business or product> decides between reasonable options that conflict
---

# <Business or product> principles

## Principles

### <Short name>

<What to prefer, and what it prevails over.>

- **Rationale:** <why the business holds the principle>
- **Example:** <a decision the principle settles>

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

Principles for visual or interaction design, such as a style guide's, are
design and belong to design records.

### Writing a principle

- Take a stand: name what the principle prevails over, as in "safe equipment
  over availability". A principle that no one would dispute, such as "be
  easy to use", decides nothing.
- Name the principle in a few words, and state it in one to three sentences.
- Give why the business holds it on the **Rationale** line when the
  principle does not make that plain, and a decision it has settled on the
  **Example** line. A real decision shows that the principle decides between
  reasonable options. Only the principle is binding.
- Write only principles that a person or a source states. Do not compose
  them from what the system does; a decision that the stated principles do
  not settle is an open question where it arises.

~~~markdown
### Safe equipment over availability

The business rents only equipment it knows to be safe, even when a contractor
goes without the equipment they want.

- **Rationale:** An accident with rented equipment harms the contractor and
  the business, and no rental is worth that risk.
- **Example:** Equipment whose inspection is overdue is withdrawn from rental
  rather than rented until it can be inspected.

### Contractors' time over depot convenience

When a choice saves contractors time at the cost of more work for depot staff,
the business chooses contractors' time.

- **Rationale:** Contractors rent to keep work moving, and a lost working day
  costs them more than the rental.
- **Example:** Customers reserve equipment online at any hour, although depot
  staff then prepare equipment reserved overnight.
~~~

### Precedence

The order of entries is binding: when two principles conflict, the earlier
prevails, so the business decides the order when it agrees the principles.
Priorities between user classes or between qualities, such as which user
class prevails when their needs conflict, are principles, linking the user
classes or quality characteristics they rank.

### Shared principles

When several systems serve one business or product, one corpus holds the
principles and the others link them, as the profile's
[Structure](../references/profile.md#structure) requires.
