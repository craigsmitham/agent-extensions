# Business Rule template

Use for one rule under the business's jurisdiction that restricts conduct,
requires an action, infers a fact, or computes a value, and that the system
must respect. Apply the [Spec profile](../references/profile.md). The Type
contract is normative; the remaining sections guide authoring.

It parallels the [Requirement template](requirement.md), with the
[differences](#differences-from-the-requirement-template) recorded below.

## Type contract

A Business Rule document is placed as the Rules module's
[fixed locations](../references/modules/rules.md#fixed-locations) state, when
its
[business rule or requirement](../references/modules/rules.md#business-rule-or-requirement)
test makes the content a Business Rule.

- **BR-1** The title MUST name the rule briefly as a noun phrase, such as
  "Minimum renter age" or "Late return fee".
- **BR-2** A Business Rule document MUST identify these fields:
  - **Source**: the policy, regulation, contract, standard, or expert whose
    authority the rule has, linked where possible.
- **BR-3** A Business Rule document MUST include these sections:
  - **Rule**: the rule, in the form that states it most clearly, such as a
    statement, a decision table, or a formula, declarative, in terms of the
    business, and complete with its conditions and any exceptions.
  - **Rationale** *(optional)*: the business goal or risk the rule answers.
- **BR-4** A Business Rule document MUST state exactly one rule.
- **BR-5** A rule MUST NOT describe the steps of a process or procedure.

## Suggested document

```markdown
---
type: Business Rule
title: <Short name of the rule>
description: <The rule statement, or a one-sentence summary of it>
status: draft
---

# <Short name of the rule>

| Context | Value |
| --- | --- |
| Source | [<Policy, regulation, contract, standard, or expert>](<link>) |

## Rule

<Business term> <must | must not | may … only if | is> <predicate>.

## Illustrations
## Rationale
## Open questions
## Related
```

## Writing guidance

### Differences from the Requirement template

A business rule governs the business; a requirement obligates the system.
Rules drive requirements, but rarely one to one: one rule may need several
requirements, and several rules may shape one requirement. "Equipment may be
rented to a customer only if the customer is at least 18 years old." is
[Minimum renter age](<link>). "When depot staff record a rental for a customer
who is under 18, the rental system shall reject the rental." is
[Underage rentals are rejected](<link>), which **enforces** it.

| Difference | Reason |
| --- | --- |
| Governs the business, its people, and the things it deals with, rather than the system | A rule would still apply if the business worked without the system, as [Business rule or requirement](../references/modules/rules.md#business-rule-or-requirement) decides. |
| Uses *must*, *must not*, or *may … only if*, or states a fact, rather than *shall* | Readers can tell a rule from a requirement at a glance. |
| States the business term first, never a condition, rather than a condition first as EARS orders it | A rule states a fact about business terms; a requirement states a response to a trigger. |

### Source

Give the policy, regulation, contract, industry standard, or recognized expert
that gives the rule its authority, with a stable link or citation. **Source**
is the rule's provenance, so the rule needs no `sources` frontmatter for it.
An unknown source is kept in its row and recorded under **Open questions**.
For whether the rule's values are expected to change, follow
[Not yet defined](../references/modules/rules.md#not-yet-defined).

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
  [High-risk customer](<link>) or [Late return fee](<link>), states a fact, as
  [Not yet defined](../references/modules/rules.md#not-yet-defined) describes.
- Use each term as the glossary defines it, and link to the entry. A
  classification that a rule decides, such as *high-risk customer*, has a
  glossary entry whose **Decided by** line links to the rule.
- Keep rationale out of **Rule**; the business goal or risk the rule serves
  belongs under **Rationale**, and worked examples, such as a computed late
  return fee for a sample rental, under **Illustrations**.

Use a decision table when a result depends on combinations of conditions, and
introduce it in business terms, such as "The late return fee for a rental is
the amount the following table gives." Name the table's result precisely.

### Exceptions

State an exception in the rule, such as with *only if* or *unless*, as
[Exceptions](../references/profile.md#exceptions) requires. For an exception
with its own source or rationale, follow
[Not yet defined](../references/modules/rules.md#not-yet-defined).

### Related

A rule states **replaces** for the deprecated rule it supersedes, such as
[Late return fee](<link>) replacing [Flat late fee](<link>). Under
**Related**, link the entity types and value types the rule is about, and any
rule whose result this rule uses.

Requirements state **enforces**, and glossary entries link to the rule with
**Decided by**. Guidance that restricts, requires, infers, and computes nothing
is advice, not a business rule.
