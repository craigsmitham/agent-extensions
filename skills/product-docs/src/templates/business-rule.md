# Business Rule template

Use for one rule under the business's jurisdiction that restricts conduct,
requires an action, infers a fact, or computes a value, and that the system
must respect.

## Type contract

- **BR-1** The title MUST name the rule briefly as a noun phrase, such as
  "Minimum renter age" or "Late return fee".
- **BR-2** A Business Rule document MUST include these sections:
  - **Rule**: the rule, in the form that states it most clearly, such as a
    statement, a decision table, or a formula, declarative, in terms of the
    business, and complete with its conditions and any exceptions.
  - **Rationale** *(optional)*: the business goal or risk the rule answers.
- **BR-3** A Business Rule document MUST state exactly one rule.
- **BR-4** A Business Rule that an outside authority imposes, such as a law,
  regulation, contract, or standard, MUST record that authority in its
  `sources` frontmatter.
- **BR-5** A rule MUST NOT describe the steps of a process or procedure.

## Suggested document

```markdown
---
type: Business Rule
title: <Short name of the rule>
description: <The rule statement, or a one-sentence summary of it>
sources:
  - id: <source-id>
    resource: <Link to the law, regulation, contract, or standard, when one imposes the rule>
    title: <Name of the source>
---

# <Short name of the rule>

## Rule

<Business term> <must | must not | may … only if | is> <predicate>.

## Illustrations
## Rationale
## Open questions
## Related
```

## Writing guidance

### Business rules and requirements

A business rule governs the business, its people, and the things it deals
with; a [Requirement](requirement.md) obligates the system. Rules drive
requirements, but rarely one to one: one rule may need several requirements,
and several rules may shape one requirement. "Equipment may be rented to a
customer only if the customer is at least 18 years old." is
[Minimum renter age](<link>). "When depot staff record a rental for a customer
who is under 18, the rental system shall reject the rental." is
[Underage rentals are rejected](<link>), which **enforces** it. A rule uses
*must*, *must not*, or *may … only if*, or states a fact, rather than *shall*,
and puts the business term first rather than a condition, so that readers can
tell a rule from a requirement at a glance.

### Source

When a law, regulation, contract, or industry standard imposes the rule, give
it in `sources`, with a stable link or citation. A rule that the business
chose needs no source; omit `sources` rather than citing the conversation or
the author. Whether the rule's values are expected to change can be noted
under **Rationale**.

### Statement

- State one rule. Split a rule whose condition contains *or*, or whose result
  contains *and*, when the parts could be decided independently.
- Write declaratively, with the business term first, such as "Equipment may be
  rented to a customer only if the customer is at least 18 years old" rather
  than "If a customer is under 18, …".
- Use *may* only to mean *is permitted to*, and prefer *may … only if* to a
  double negative.
- A rule that people could break, such as
  [Overdue inspection withdrawal](<link>), uses *must*, *must not*, or
  *may … only if*. A rule that defines, infers, or computes, such as
  [High-risk customer](<link>) or [Late return fee](<link>), states a fact.
  Rule categories are not yet defined, so the wording carries the
  distinction.
- Use each term as the glossary defines it, and link to the entry. A
  classification that a rule decides, such as *high-risk customer*, has a
  glossary entry whose **Decided by** line links to the rule.
- Keep rationale out of **Rule**; the business goal or risk the rule serves
  belongs under **Rationale** when the rule and its source do not make it
  plain, and worked examples, such as a computed late return fee for a sample
  rental, under **Illustrations** when the rule is hard to apply without
  them.

Use a decision table when a result depends on combinations of conditions, and
introduce it in business terms, such as "The late return fee for a rental is
the amount the following table gives." Name the table's result precisely.

### Exceptions

State an exception in the rule, such as with *only if* or *unless*, as
[Exceptions](../references/profile.md#exceptions) requires, and give the
source or rationale of an exception that has its own under **Rationale**.

### Related

Under **Related**, link the entity types and value types the rule is about,
and any rule whose result this rule uses.

Requirements state **enforces**, and glossary entries link to the rule with
**Decided by**. Guidance that restricts, requires, infers, and computes nothing
is advice, not a business rule.
