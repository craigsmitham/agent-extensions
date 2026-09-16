# Spec

Create and manage the specification of a software system as an OKF v0.2
bundle that follows the [Spec profile](src/references/profile.md) and its
modules.

## Maintaining the templates

The profile, its modules, and each template's **Type contract** are the
normative contract. Keep them coherent with these conventions when adding or
changing a template, and run the lint before committing:

```sh
python3 skills/spec/scripts/lint_spec.py
```

The lint exits non-zero on any error. `--warn-only` reports without failing.

### Core and modules

The core profile holds what most systems need: the core types and the rules
that apply to every document. A module holds a group of types that not every
system needs, with everything that exists only for them.

- A module file has the sections it needs from **Concept types**,
  **Vocabulary**, **Structure** (with **Folders**), **Placement** (with
  **Placement levels** and **Fixed locations**), **Ownership tests** (with
  **Where content goes**), **Relationships**, and **Not yet defined**, in that
  order. Each table extends the profile's table of the same name, whose rule
  names module tables as extension points.
- A rule, term, relationship, or interim practice that exists only for a
  module's types lives in that module. The core may name a module's types in
  a rule that holds whether or not the module is adopted.
- The profile's **Modules** table gives, for each module, how content is
  written without it.
- A module takes a type from the core only when the core rules no longer need
  that type.

### One home for each rule

- A rule that applies to more than one type lives in the profile or a module.
  A rule for one type lives in that type's contract, including when to create
  a concept of that type.
- An interim practice for a deferred concern lives only in a
  **Not yet defined** table; templates link to it rather than restating it.
- Writing guidance explains and illustrates rules; it links to them and never
  states a rule of their own. The numbered rules are the checklist, so no
  section restates them as questions. Uppercase MUST, SHOULD, and MAY
  appear only in normative statements.
- Terms are used as a **Vocabulary** table defines them. Add or change a row
  there before giving a term a new meaning.
- Relationships between documents are named and assigned to one side in a
  **Relationships** table. Templates use those names in bold.

### Rule identifiers

Every normative statement is a list item that begins with a bold identifier:
`**P-<AREA>-<n>**` in the profile or a module, or `**<CODE>-<n>**` in a Type
contract.

- A tagged item states rules of one strength only: MUST and MUST NOT, SHOULD
  and SHOULD NOT, or MAY. Split an item that mixes them.
- Nested bullets under a tagged item, such as the fields a document
  identifies, belong to that item.
- Identifiers are unique. Before version 1.0, identifiers are numbered in
  document order and renumbered when rules are added or removed. From 1.0,
  an identifier is never reused for a different rule: a removed rule's
  identifier is added to [Retired identifiers](#retired-identifiers), and a
  replacement rule takes the next unused number.

| Code | Type | Code | Type |
| --- | --- | --- | --- |
| SYS | System | QC | Quality Characteristic |
| SUB | Subsystem | QR | Quality Requirement |
| BIZ | Business Requirements | EI | External Interface |
| USR | User Class | GLO | Glossary |
| FEA | Feature | ET | Entity Type |
| CMP | Feature Component | VT | Value Type |
| UC | Use Case | BR | Business Rule |
| REQ | Requirement | | |

Profile areas are TYP, MOD, STR, PLC, OWN, REL, STA, CON, BIN, and DOC. Each
module has one area: DEC for Decomposition, RUL for Rules, QUA for Quality,
and DAT for Data.

### Retired identifiers

None. The list starts when version 1.0 is published.

### Deferring a concern

To keep a version small, defer a concern rather than half-specify it: remove
its rules, relationships, and sections, and add a row to the
**Not yet defined** table of the profile or of the module whose types it
concerns, giving the interim practice. When the concern is taken up, it
returns under new identifiers. A concern that needs no interim practice goes
in the [Roadmap](#roadmap) instead.

Links are plain unless a relationship in a relationships table applies; a
relationship is added to a table only when readers need its meaning and a
plain link's place does not show it.

Rules that apply to every type, such as the optional **Open questions**,
**Related**, and **Illustrations** sections and the meaning of *(optional)*
and conditional markers, live in the profile's **Document conventions** and
are not repeated in each Type contract.

### Roadmap

This version also leaves these concerns undefined, with no interim practice
beyond base OKF v0.2:

- frontmatter keys beyond base OKF v0.2;
- specialization or inheritance between entity types or value types; and
- an overall data model or diagram spanning entity types.

### Template anatomy

Every template has this shape, in this order:

1. `# <Type> template`.
2. A purpose paragraph beginning "Use for" and ending
   `Apply the [Spec profile](../references/profile.md). The Type contract is normative; the remaining sections guide authoring.`
3. For a template that parallels another, the paragraph
   `It parallels the [<X> template](<x>.md), with the [differences](#differences-from-the-<x>-template) recorded below.`
4. `## Type contract`, containing, in this order:
   1. when the profile's or a module's **Fixed locations** table does not
      settle placement alone, an untagged placement paragraph beginning
      "A <Type> document is placed as", linking the placement rules or
      creation test that apply;
   2. the tagged title rule;
   3. the tagged "MUST identify these fields:" rule, when the type identifies
      fields;
   4. the tagged "MUST include these sections:" rule, listing every section
      of the type's own in document order, each marked *(optional)* or with a
      condition, such as *(when …)*, unless it is always required, and
      described in a few words;
   5. tagged type-specific rules;
   6. tagged MUST NOT and SHOULD NOT rules.

   There are no "MAY identify" or "MAY include" rules. Binding content is
   everything but the supporting sections, as the profile's
   [binding and illustrative content](src/references/profile.md#binding-and-illustrative-content)
   states, so the contract does not declare it. Untagged paragraphs in the
   contract explain; they contain no uppercase keyword.
5. `## Suggested document`: one fenced Markdown block, with frontmatter
   carrying only `type`, `title`, `description`, and `status: draft`; a Context
   table exactly when the contract identifies fields; and supporting sections last
   in the profile's order. Nothing follows the block.
6. `## Writing guidance`, containing, in this order:
   1. `### Differences from the <X> template`, when the type parallels
      another: a `Difference | Reason` table;
   2. topic subsections that add what the contract does not say, such as how
      to write one section, or worked examples; no subsection restates the
      contract's fields or sections as a table, or relists the profile
      sections that the contract already links.

Templates carry what an author needs. Where a template's structure comes
from is recorded in [Template sources](#template-sources), not in the
template.

### Template sources

| Template | Follows |
| --- | --- |
| System | The system overview of ISO/IEC/IEEE 29148, and the product perspective and operating environment of Karl Wiegers and Joy Beatty's software requirements specification. |
| Subsystem | The same sources as the System template. |
| Business Requirements | The vision and scope document of Karl Wiegers and Joy Beatty, and the business requirements of ISO/IEC/IEEE 29148. |
| User Class | Karl Wiegers and Joy Beatty's user classes. |
| External Interface | The external interface requirements of ISO/IEC/IEEE 29148 and of Karl Wiegers and Joy Beatty's software requirements specification. |
| Feature, Feature Component | The features of Karl Wiegers and Joy Beatty. |
| Use Case | Alistair Cockburn's use case structure, as described in *The Mini-Book on Use Cases* and *Unifying User Stories, Use Cases, and Story Maps*. What Cockburn calls the scope, the system under discussion, is the use case's subject. |
| Requirement | The requirement construct and the characteristics of well-formed requirements in ISO/IEC/IEEE 29148, with the Easy Approach to Requirements Syntax (EARS) recommended for statements. |
| Business Rule | The Business Rules Manifesto and Ronald G. Ross's RuleSpeak. |
| Quality Characteristic | The product quality model of ISO/IEC 25010, whose term *quality characteristic* it adopts, and the quality requirements framework of ISO/IEC 25030. It separates the definition of a measure from the level required of it, as Tom Gilb's Planguage does. |
| Quality Requirement | The product quality requirements of ISO/IEC 25030. |
| Glossary | The ubiquitous language of domain-driven design, the glossary of the Volere template and of Karl Wiegers and Joy Beatty, and the principles of ISO/IEC 11179-4 and ISO 704 that the profile's definition rules adopt. |
| Entity Type | The business data model and data dictionary of the Volere template and of Karl Wiegers and Joy Beatty, and the domain-driven design distinction between entities and values. It describes business data, not a database design. |
| Value Type | The data dictionary practice of the Volere template and of Karl Wiegers and Joy Beatty, and the domain-driven design account of value objects. |

### Parallel types

| Pair | Where the differences are recorded |
| --- | --- |
| System and Subsystem | [Subsystem template](src/templates/subsystem.md#differences-from-the-system-template) |
| Requirement and Quality Requirement | [Quality Requirement template](src/templates/quality-requirement.md#differences-from-the-requirement-template) |
| Requirement and Business Rule | [Business Rule template](src/templates/business-rule.md#differences-from-the-requirement-template) |
| Entity Type and Value Type | [Value Type template](src/templates/value-type.md#differences-from-the-entity-type-template) |

Record a difference in its table only when it changes what an author writes
and its reason is not obvious from the profile or the two contracts. A
difference that the contracts already show, or that only adds or removes a
rule whose purpose the rule itself makes plain, needs no row.

### Examples

Every example uses the [running example](src/references/example.md). Add a
name to its **Names** table, or a fact to its **Facts**, before using it in a
template.
