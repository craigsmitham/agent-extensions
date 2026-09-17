# Glossary template

Use for the agreed terms of the system, and what each one means.

## Type contract

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
---

# <System> glossary

## Terms

### <Term>

<Definition, when the entry has one.>

- **Also called:** <accepted synonym>, …
- **Defined by:** [<Concept whose Definition defines the name>](<link>)
- **Decided by:** [<Rule that decides membership>](<link>)
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
requires. **Related** links records that readers use alongside the glossary,
such as a business vocabulary or a style guide.

### Entries

An entry has a definition, then any entry lines, unless another concept's
**Definition** defines its name; then it has no definition and a
**Defined by** line, because
[P-CON-2](../references/profile.md#one-home) allows one definition of each
meaning. Such an entry is present when readers look for the name in the
glossary. **Defined by** and **Decided by** are
[named links](../references/profile.md#named-links).

| Line | Content |
| --- | --- |
| Also called | Accepted synonyms. The specification uses the entry's term. |
| Defined by | For a name that another concept's **Definition** defines: that concept. |
| Decided by | For a classification: the rule that decides whether something belongs to it. The definition says what the classification means; the rule owns the criteria. |
| Example | An illustration of the term. |
| Note | A clarification that is not part of the meaning, such as a name readers should avoid, or a similar term with a different meaning, with a link. |

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
**Example** line is the place for illustrations. Most entries need only a
definition: add an **Example** or **Note** only when a reader could misapply
the definition without it, as
[P-DOC-6](../references/profile.md#document-conventions) states.

### Definitions

A definition that follows the profile's
[definition rules](../references/profile.md#definitions) is a phrase that can
replace its term: "Equipment is returned to *a site from which equipment is
rented and to which it is returned*" reads as a sentence about a depot. The
same practice applies to any concept's **Definition** section. A good
definition:

- is stated in the singular, and says what the thing is, not only what it is
  not;
- uses the same structure as the definitions of related terms;
- links each defined term it uses, such as *rental period* in the definition
  of *late return*, rather than embedding that term's definition; and
- leaves out rationale, usage, procedure, and examples, and links to, rather
  than states, how data is represented, the criteria or calculations a rule
  owns, and the obligations a requirement owns.

### Anchors

Other documents link to an entry by its heading anchor, such as
`glossary.md#rental-period`, so a renamed entry changes its inbound links.
