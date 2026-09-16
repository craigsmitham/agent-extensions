# Glossary template

Use for the agreed terms of the system, and what each one means. Apply the
[Spec profile](../references/profile.md). The Type contract is normative; the
remaining sections guide authoring.

## Type contract

A Glossary document is placed as the profile's
[fixed locations](../references/profile.md#fixed-locations) rules state, and
holds every term of the system, including terms specific to one subsystem.

- **GLO-1** The title MUST be "<System> glossary".
- **GLO-2** A Glossary document MUST include these sections:
  - **Terms**: one entry for each term, headed by the term exactly as the
    specification writes it.
- **GLO-3** An entry's definition, when the entry has one, MUST be the first
  paragraph below its heading, and the rest of the entry MUST be entry lines.
- **GLO-4** Entries SHOULD be ordered alphabetically.

## Suggested document

```markdown
---
type: Glossary
title: <System> glossary
description: Agreed terms of <system> and what each one means
status: draft
---

# <System> glossary

## Terms

### <Term>

<Definition, when the entry has one.>

- **Also called:** <accepted synonym>, …
- **Defined by:** [<Quality characteristic, entity type, or value type>](<link>)
- **Decided by:** [<Business rule>](<link>)
- **Example:** <illustration>
- **Note:** <clarification, name to avoid, or [<similar term>](<link>) not to be confused with>

## Open questions
## Related
```

## Writing guidance

### Choosing terms

Include a term when readers could misunderstand it, when the business uses it
with a meaning specific to its domain, or when several words are used for the
same thing. Words used in their ordinary sense do not need entries. Record the
business's own words; do not coin terms to tidy the language. Add or revise an
entry when the language changes.

Include an abbreviation as its own entry only when readers use the
abbreviation; otherwise give it under **Also called**.

A term whose meaning is not yet agreed goes under **Open questions** rather
than into a definition, as
[record gaps instead of inventing](../references/profile.md#record-gaps-instead-of-inventing)
requires. A term whose meaning is specific to one subsystem has a name distinct
from the system's other terms, as
[P-DEC-2](../references/modules/decomposition.md#fixed-locations) requires, and
a **Note** line can name the subsystem. **Related** links records that readers
use alongside the glossary, such as a business vocabulary or a style guide.

### Kinds of entry

The **Where content goes** tables of the
[Quality](../references/modules/quality.md#where-content-goes),
[Rules](../references/modules/rules.md#where-content-goes), and
[Data](../references/modules/data.md#where-content-goes) modules decide which
kind of entry a term has when the corpus adopts them:

| Kind | Entry |
| --- | --- |
| A term the glossary defines | A definition, then any entry lines. |
| The name of a quality characteristic, entity type, or value type | No definition. A **Defined by** line links to the concept whose **Definition** is the only definition, so that readers who look for the name here find it. |
| A classification | A definition of what the classification means, and a **Decided by** line linking to the Business Rule that decides membership. |

~~~markdown
### depot

A site from which equipment is rented and to which it is returned.

### high-risk customer

A customer whom the business treats as likely to return equipment late.

- **Decided by:** [High-risk customer](<link>)

### late return

The return of rented equipment after the last day of its
[rental period](<link>).

### reservation

- **Defined by:** [Reservation](<link>)
~~~

Only the definition of an entry is binding. Its other lines are not, and its
**Example** line is the place for illustrations.

### Definitions

A definition that follows the profile's
[definition rules](../references/profile.md#definitions) is a phrase that can
replace its term: "Equipment is returned to *a site from which equipment is
rented and to which it is returned*" reads as a sentence about a depot. The
same practice applies to the **Definition** of a quality characteristic,
entity type, or value type. A good definition:

- is stated in the singular, and says what the thing is, not only what it is
  not;
- uses the same structure as the definitions of related terms;
- links each defined term it uses, such as *rental period* in the definition
  of *late return*, rather than embedding that term's definition; and
- leaves out rationale, usage, procedure, and examples, and links to, rather
  than states, how data is represented, the criteria or calculations a
  Business Rule owns, and the obligations a Requirement owns.

### Entry lines

| Line | Content |
| --- | --- |
| Also called | Accepted synonyms, including a quality model's name for a quality characteristic. The specification uses the entry's term. |
| Defined by | For the name of a quality characteristic, entity type, or value type: the concept that holds its definition. |
| Decided by | For a classification: the Business Rule that decides whether something belongs to it. The definition says what the classification means; the rule owns the criteria. |
| Example | An illustration of the term. |
| Note | A clarification that is not part of the meaning, such as a name readers should avoid, a similar term with a different meaning, with a link, or the subsystem a term is specific to. |

Other documents link to an entry by its heading anchor, such as
`glossary.md#rental-period`, so a renamed entry changes its inbound links.
