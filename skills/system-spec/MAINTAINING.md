# Maintaining System Spec

Conventions for changing this skill. For what the skill does, see the
[README](README.md).

## Serving the job

The skill serves one job, growing and maintaining a software system's
specification, which [The job this skill serves](src/references/job.md)
describes with its job map. That page is the job's one home. It steers the
agent where the rules are silent, explains and never states a rule, and uses
no uppercase MUST, SHOULD, or MAY.

Use the job to improve the skill:

- A new type, rule, or workflow step names the step of the job map it serves
  and the outcome it improves.
- The outcomes are criteria for evaluation cases, such as whether the agent
  recognizes, at Define, that a change to how the system works alters a
  required level of quality.
- An observed shortfall in use is attributed to the step at which it
  occurred.

### Alternatives

Stewards make the same progress today by other means, each of which falls
short:

| Alternative | Where it falls short |
| --- | --- |
| People's memory | Lost with turnover; agents have none. |
| Code and tests | Show what the system does, not whom it serves or why, and cannot tell a defect from a decision. |
| Tickets and pull request descriptions | Tied to one change, scattered, and never consolidated. |
| Agent instruction files | Mix instructions with facts about the product, without structure. |
| Freeform documents, PRDs, and wikis | Have no ownership rules, so duplicated content drifts apart. |
| Formal requirements specifications, such as those of ISO/IEC/IEEE 29148, Volere, or Wiegers and Beatty | Thorough but costly, rarely kept current, and not shaped for agents. |
| Specification-per-change tooling | Plans one change but does not consolidate across changes. |
| Asking an agent to infer it | Invented and inconsistent. |

The skill's reason to exist is what none of these do: keep one consolidated
account, across changes, of what the system does and whom and what it serves.

### Coverage

| Step | What the skill provides | Gap |
| --- | --- | --- |
| Define | Mission, Vision, Principles, Opportunity, Job to Be Done, Stakeholders, Objectives, Scope, System; `business/index.md` shows which are not defined | Strong. |
| Locate | Finding the corpus; `sources` frontmatter | Thin: no model of sources, or of recovering a specification from behavior. |
| Prepare | Ownership tests, Glossary, Structure, Placement | Strong. |
| Confirm | Open questions; P-CON-4 | Weak: lifecycle, status, acceptance, and obligations that cannot both be met are not yet defined. |
| Execute | Templates and Type contracts | Strongest. |
| Monitor | Review against the rules | Weak: no check against behavior; stable identifiers are not yet defined. |
| Modify | P-CHG-1, P-CHG-2, and version control | Thin: no impact analysis. |
| Conclude | P-CHG-2 and index updates | Partial. |

The workflow in SKILL.md has no step for Define, and nothing in it checks the
corpus against the system's behavior. Update this table when a change closes
or opens a gap.

### Open questions

- Does Monitor include checking the system's behavior, or only providing the
  authority that tests and reviews witness?
- Is a first pass over an existing system with no recorded specification
  different enough to map separately?
- Since whom and what the system serves is the specification's core value,
  should Job to Be Done or User Class join the types most systems start with?
- Should the job cite Genesis 2:15, "to work it and keep it", as the source of
  "grow and maintain"?

## Maintaining the templates

The profile and each template's **Type contract** are the normative
contract. Keep them coherent with these conventions when adding or
changing a template, and run the lint from the repository root before
committing:

```sh
scripts/lint-system-spec.py
```

The lint checks what breaks silently: links and anchors, rule identifiers and
references to them, where uppercase keywords appear, and agreement between
each template's Type contract and Suggested document. It exits non-zero on
any finding. The other conventions here are kept by review.

### The business folder

`business/` holds what justifies and directs the system, and the rest of the
corpus specifies the system. Its index follows Peter Drucker's five questions
(mission, customer, what the customer values, results, and plan), so that a
reader sees what the business cares about and which of those concerns the
corpus leaves unanswered. A new type belongs in `business/` only when it
answers one of those questions for the system rather than specifying the
system. Business rules stay outside it: they would hold if another system
served the business, but they bind the system.

### One profile

The profile holds the rules for every type. Only the System is required, and
the profile marks no type as core; SKILL.md groups the types most systems
start with, for navigation only.

- The directory tree in the profile's **Structure** is the file and folder
  contract, and so the only statement of where a type with one location lives,
  with a comment on each folder that holds concepts.
- Rules state what a document of a type must do when it exists. No rule
  requires a corpus to hold a document of another type, or gives a second way
  to write content whose owning type the corpus does not use.
- P-DEC-1 makes a subsystem equivalent to a system at its own boundary, so no
  other file restates how a rule applies to subsystems.

### One home for each rule

- A rule that applies to more than one type lives in the profile.
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
- Named links between documents, including glossary entry lines that link a
  concept, are defined and assigned to one side in one row of one
  **Named links** table. Templates use those names in bold.

### Rule identifiers

Every normative statement is a list item that begins with a bold identifier:
`**P-<AREA>-<n>**` in the profile, or `**<CODE>-<n>**` in a Type
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
| OPP | Opportunity | EI | External Interface |
| USR | User Class | GLO | Glossary |
| FEA | Feature | ET | Entity Type |
| CMP | Feature Component | VT | Value Type |
| UC | Use Case | BR | Business Rule |
| REQ | Requirement | MIS | Mission |
| VIS | Vision | PRI | Principles |
| JOB | Job to Be Done | STK | Stakeholders |
| OBJ | Objectives | SCP | Scope |

BIZ, the code of the retired Business Requirements type, is not reused.

Profile areas are TYP, STR, PLC, OWN, LNK, CHG, CON, and DOC, and, for rules
that concern particular types, DIR for direction, JOB for jobs to be done, DEC for subsystems and
feature components, RUL for business rules, QUA for quality, and DAT for
data.

### Deferring a concern

To keep a version small, defer a concern rather than half-specify it: remove
its rules, named links, and sections, and list it in the profile's
**Not yet defined**, where P-CON-5 applies. Add an interim practice to the
Writing guidance of the type it concerns only when it is more specific than
P-CON-5. When the concern is taken up, it returns under
new identifiers.

Links are plain unless a named link applies; a named link is added to a table
only when readers need its meaning and a plain link's place does not show it.

Rules that apply to every type, such as the optional **Open questions**,
**Related**, and **Illustrations** sections and the meaning of *(optional)*
and conditional markers, live in the profile's **Document conventions** and
are not repeated in each Type contract. Every Suggested document lists
**Open questions** and **Related**. It lists **Illustrations** only when the
template's Writing guidance says what that type's illustrations hold, and
**Rationale** or **Verification** only when the Type contract lists them, so
that an empty heading does not invite filler. That guidance says when each
supporting section is worth adding, not only what it holds. The Glossary and Principles carry an
**Example** line on each entry instead.

### Template anatomy

Every template has this shape, in this order:

1. `# <Type> template`.
2. A purpose paragraph beginning "Use for". That the Type contract is
   normative and the rest guides authoring is stated once, in the profile.
3. `## Type contract`, containing, in this order:
   1. for a type placed by rule rather than by **Structure**, an untagged
      placement paragraph beginning "A <Type> document is placed as",
      linking the placement rules that apply;
   2. the tagged title rule;
   3. the tagged "MUST include these sections:" rule, listing every section
      of the type's own in document order, each marked *(optional)* or with a
      condition, such as *(when …)*, unless it is always required, and
      described in a few words;
   4. tagged type-specific rules, with any creation test phrased
      "A <type> MUST be created only when";
   5. tagged MUST NOT and SHOULD NOT rules.

   There are no "MAY include" rules. Binding content is
   everything but the supporting sections, as the profile's
   [binding and illustrative content](src/references/profile.md#binding-and-illustrative-content)
   states, so the contract does not declare it. Untagged paragraphs in the
   contract explain; they contain no uppercase keyword.
4. `## Suggested document`: one fenced Markdown block, with frontmatter
   carrying only `type`, `title`, `description`, and
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
| Mission | The mission of the Object Management Group's Business Motivation Model, as what the business does for whom, apart from any system. |
| Vision | The vision of the Business Motivation Model, and the product vision of Marty Cagan's *Inspired* and *Empowered*, as the future pursued rather than a specification. |
| Principles | The product principles of Marty Cagan's *Inspired*, Amazon's tenets, and the business policy of the Business Motivation Model: guidance for decisions rather than obligations, ranked only where the ranking is agreed. Richard Rumelt's guiding policy, from *Good Strategy Bad Strategy* and *The Crux*, supplies the test that a principle rules out options and answers a stated conflict, and the line between a lasting principle and strategy for a current challenge. |
| Job to Be Done | Clayton Christensen's account of a job as progress sought in circumstances, with functional, emotional, and social dimensions, and Tony Ulwick's job performer and solution-independent job statement, as the [Jobs to Be Done](../../knowledge/product-engineering/src/foundations/jobs-to-be-done.md) foundation of the product-engineering bundle explains them. |
| System | The system overview of ISO/IEC/IEEE 29148, and the product perspective and operating environment of Karl Wiegers and Joy Beatty's software requirements specification. |
| Subsystem | The same sources as the System template. |
| Opportunity | The business purpose (§9.3.2) and the definition of the problem or opportunity space (§6.2.3.3) of ISO/IEC/IEEE 29148, framed as an opportunity after Peter Drucker's *Managing for Results*. |
| Stakeholders | The major stakeholders of the business requirements specification in ISO/IEC/IEEE 29148 (§9.3.5), and the supporting customers of Peter Drucker's *The Five Most Important Questions*. |
| Objectives | The mission, goals, and objectives of ISO/IEC/IEEE 29148 (§9.3.7), whose measures of effectiveness (§6.2.3.3) indicators follow; the business objectives and success metrics of Karl Wiegers and Joy Beatty; and the results, measured qualitatively and quantitatively, of Peter Drucker's *The Five Most Important Questions*. |
| Scope | The business scope (§9.3.3) and system scope (§9.5.3) of ISO/IEC/IEEE 29148, the separation of the scope of the work from the scope of the product in the Volere template, the solution scope of the BABOK Guide, Alistair Cockburn's in/out list, and the scope, limitations, and exclusions of Karl Wiegers and Joy Beatty. |
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
