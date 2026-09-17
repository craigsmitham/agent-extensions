# Spec

Create and manage the specification of a software system as an OKF v0.2
bundle that follows the [Spec profile](src/references/profile.md) and its
modules.

## Maintaining the templates

The profile, its modules, and each template's **Type contract** are the
normative contract. Keep them coherent with these conventions when adding or
changing a template, and run the lint from the repository root before
committing:

```sh
scripts/lint-spec.py
```

The lint checks what breaks silently: links and anchors, rule identifiers and
references to them, where uppercase keywords appear, and agreement between
each template's Type contract and Suggested document. It exits non-zero on
any finding. The other conventions here are kept by review.

### Core and modules

The core profile holds what most systems need: the core types and the rules
that apply to every document. A module holds a group of types that not every
system needs, with everything that exists only for them.

- A module file has the sections it needs from **Concept types**,
  **Vocabulary**, **Structure**, **Placement** (with **Placement levels** and
  **Fixed locations**), **Ownership tests** (with **Where content goes**), and
  **Named links**, in that order. Each table extends the profile's table of
  the same name, whose rule names module tables as extension points. The
  directory tree in **Structure** is the folder contract, with a comment on
  each folder that holds concepts.
- A rule, term, named link, or interim practice that exists only for a
  module's types lives in that module, including guidance that only matters
  when the module is adopted.
- Core rules never depend on a module's types. Core examples, glossary entry
  lines, and named link rows may mention them, because they add nothing a
  corpus without the module must do. A module rule names another module's
  types only conditionally, such as "in a corpus without the Rules module".
- The Decomposition module makes a subsystem equivalent to a system at its own
  boundary, so no other file restates how a rule applies to subsystems.
- The profile's **Modules** table gives, for each module, how content is
  written without it.
- A module takes a type from the core only when the core rules no longer need
  that type.

### One home for each rule

- A rule that applies to more than one type lives in the profile or a module.
  A rule for one type lives in that type's contract, including when to create
  a concept of that type.
- A deferred concern is listed once, in the profile's **Not yet defined**.
  An interim practice for it lives in the Writing guidance of the type it
  concerns, or in the profile's prose when it concerns several types.
- Writing guidance explains and illustrates rules; it links to them and never
  states a rule of their own. The numbered rules are the checklist, so no
  section restates them as questions. Uppercase MUST, SHOULD, and MAY
  appear only in normative statements.
- Terms are used as a **Vocabulary** table defines them. Add or change a row
  there before giving a term a new meaning.
- Named links between documents are defined and assigned to one side in one
  row of one **Named links** table. Templates use those names in bold.

### Rule identifiers

Every normative statement is a list item that begins with a bold identifier:
`**P-<AREA>-<n>**` in the profile or a module, or `**<CODE>-<n>**` in a Type
contract.

- A tagged item states rules of one strength only: MUST and MUST NOT, SHOULD
  and SHOULD NOT, or MAY. Split an item that mixes them.
- Nested bullets under a tagged item, such as the sections a document
  includes, belong to that item.
- Identifiers are unique and never reused for a different rule. Existing
  identifiers are not renumbered, so gaps are expected: a new rule takes the
  next number never used with its prefix, which the history of the file
  shows.

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

Profile areas are TYP, STR, PLC, OWN, LNK, STA, CON, and DOC. Each
module has one area: DEC for Decomposition, RUL for Rules, QUA for Quality,
and DAT for Data.

### Deferring a concern

To keep a version small, defer a concern rather than half-specify it: remove
its rules, named links, and sections, and list it in the profile's
**Not yet defined**. The profile's general practice for undefined concerns,
P-CON-5, then applies: state it in prose in the nearest section, link records
under **Related**, and record what is undecided under **Open questions**. Add
an interim practice to the Writing guidance of the type it concerns only when
it is more specific than that. When the concern is taken up, it returns under
new identifiers.

Links are plain unless a named link applies; a named link is added to a table
only when readers need its meaning and a plain link's place does not show it.

Rules that apply to every type, such as the optional **Open questions**,
**Related**, and **Illustrations** sections and the meaning of *(optional)*
and conditional markers, live in the profile's **Document conventions** and
are not repeated in each Type contract.

### Template anatomy

Every template has this shape, in this order:

1. `# <Type> template`.
2. A purpose paragraph beginning "Use for". That the Type contract is
   normative and the rest guides authoring is stated once, in the profile.
3. `## Type contract`, containing, in this order:
   1. when the profile's or a module's **Fixed locations** table does not
      settle placement alone, an untagged placement paragraph beginning
      "A <Type> document is placed as", linking the placement rules or
      creation test that apply;
   2. the tagged title rule;
   3. the tagged "MUST include these sections:" rule, listing every section
      of the type's own in document order, each marked *(optional)* or with a
      condition, such as *(when …)*, unless it is always required, and
      described in a few words;
   4. tagged type-specific rules;
   5. tagged MUST NOT and SHOULD NOT rules.

   There are no "MAY include" rules. Binding content is
   everything but the supporting sections, as the profile's
   [binding and illustrative content](src/references/profile.md#binding-and-illustrative-content)
   states, so the contract does not declare it. Untagged paragraphs in the
   contract explain; they contain no uppercase keyword.
4. `## Suggested document`: one fenced Markdown block, with frontmatter
   carrying only `type`, `title`, `description`, `status: draft`, and
   `sources` when the contract requires it; a `Context | Value` table
   exactly when a type-specific rule requires one, as for Use Case; and
   supporting sections last
   in the profile's order. Nothing follows the block.
5. `## Writing guidance`: topic subsections that add what the contract does
   not say, such as how to write one section, how the type differs from a
   type it resembles, or worked examples; no subsection restates the
   contract's fields or sections as a table, or relists the profile sections
   that the contract already links.

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

### Types that resemble each other

When a type is written like another, such as a Quality Requirement like a
Requirement, its Writing guidance says so in a short subsection that names
only what an author writes differently and why. It does not restate the other
contract.

### Examples

Every example uses the [running example](src/references/example.md). Add a
name to its **Names** table, or a fact to its **Facts**, before using it in a
template.
