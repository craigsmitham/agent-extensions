# Spec profile

Version **0.1.0** · Base **OKF v0.2** · Maintainer **@craigsmitham** · Status
**draft**.

This profile describes the specification of a software system as an OKF v0.2
bundle. It defines the core concept types, the corpus structure, where each
concept lives, which type owns content that two types border, how concepts
link, how their status changes, and the rules every document follows.
[Modules](#modules) add concept types that not every system needs. The
normative contract comprises this file, each adopted module, and the
**Type contract** section of each template the corpus uses. Other template
sections are authoring guidance.

MUST and MUST NOT are requirements; SHOULD and SHOULD NOT are recommendations;
MAY denotes an option. Each normative statement is a list item that begins
with a rule identifier, such as **P-STR-1** in this profile, **P-DAT-1** in a
module, or **UC-3** in a Type contract, so that reviews can cite it. Text
without an identifier defines or explains; it adds no requirement.

Profiles are a producer convention beyond OKF v0.2. No `okf_profile` field is
introduced. Examples in the templates use the [running example](example.md).

## Concept types

- **P-TYP-1** Each concept document in the corpus MUST use one of the `type`
  values in this table or in the **Concept types** table of an adopted module.

| Type | Description |
| --- | --- |
| [`System`](../templates/system.md) | The software system being specified, and the boundary that its other concepts describe. |
| [`Business Requirements`](../templates/business-requirements.md) | The business objectives, expected outcomes, and scope that justify building or changing the system. |
| [`User Class`](../templates/user-class.md) | A distinct group of the system's users, identified by how they use the system and what they need from it. |
| [`External Interface`](../templates/external-interface.md) | A connection across the system's boundary to an external system or a device, and what passes across it. |
| [`Feature`](../templates/feature.md) | A coherent unit of capability that the system provides to its users. |
| [`Use Case`](../templates/use-case.md) | How an actor pursues a goal at a boundary, through success and failure paths. |
| [`Requirement`](../templates/requirement.md) | An obligation that the system must satisfy under identified conditions. |
| [`Glossary`](../templates/glossary.md) | The agreed terms of the system, and what each one means. |

This profile does not describe the system's architecture. A feature, or a
placement level that a module adds, is a specification boundary or placement
level, not an architecture element; design and implementation structure
belong to records.

## Modules

A module adds concept types, with the structure, placement, ownership tests,
named links, vocabulary, and interim practices they need. Its tables extend
the tables of the same name in this profile. Adopt a module when the system
needs its types.

| Module | Types | Without the module |
| --- | --- | --- |
| [Decomposition](modules/decomposition.md) | `Subsystem`, `Feature Component` | Use cases and requirements are placed at the system or at a feature. |
| [Rules](modules/rules.md) | `Business Rule` | A rule that the business would keep without the system is stated through the Requirements that enforce it, with the rule's source under **Rationale**. |
| [Quality](modules/quality.md) | `Quality Characteristic`, `Quality Requirement` | A required level of quality is a Requirement that states its measure in the statement. |
| [Data](modules/data.md) | `Entity Type`, `Value Type` | The meaning of data is a glossary entry, and its detail is stated where it is used. |

- **P-TYP-2** A corpus MUST NOT contain a document of a type from a module it
  has not adopted.
- **P-TYP-3** A corpus that adopts a module MUST apply the module's rules as
  part of this profile.
- **P-TYP-4** Content whose owning type belongs to a module the corpus has not
  adopted MUST be written as the **Without the module** column gives.

## Vocabulary

Each term below has one meaning throughout this profile, its modules, and its
templates.

| Term | Meaning |
| --- | --- |
| Boundary | What separates the system from the parties it interacts with. |
| Subject | The System whose boundary a Use Case or Requirement describes. It is never a feature or an external interface. |
| Placement level | The system or a feature, or a level that an adopted module adds, as a place where Use Cases and Requirements live. |
| Home | The one location of a concept. The home of a Use Case or Requirement is the placement level at which it is placed, as [Rule-placed types](#rule-placed-types) decides. |
| Owning type | The type that the [Ownership tests](#ownership-tests) assign content to. |
| Named link | A link whose meaning a [Named links](#named-links) table gives, stated in bold with its name. |
| Scope | What the system includes and excludes, as the Business Requirements document states it. What a feature includes is its *coverage*. |
| Design constraint | A Requirement whose obligation is to use, or not use, a specific technology, platform, or design. |
| Stakeholder | A person or group with an interest in the system who does not use it or its outputs directly. People who use the system, including those who operate it, belong to a User Class. |
| User interface | What the system presents to people and the actions it offers them. *Interface* alone means an External Interface. |
| Counterpart | The external system or device at the other end of an External Interface. |
| Supporting sections | **Illustrations**, **Rationale**, **Verification**, **Open questions**, and **Related**, which several types share and which hold no binding content. |
| Operations concerns | Instrumentation, service level objectives and agreements, alerting, and operational responses. They belong to operations records. |
| Record | Material maintained outside the corpus, such as architecture, operations, engineering, or work-management records. |

## Structure

- **P-STR-1** An adopting repository MUST place the corpus in
  `<repository-root>/spec/`, abbreviated `/spec/`. The corpus specifies one
  system.

```text
spec/
  README.md                        # Adoption declaration
  index.md                         # Navigation; carries okf_version: "0.2"
  system.md                        # System
  business.md                      # Business Requirements
  glossary.md                      # Glossary
  users/                           # User Class documents
  interfaces/                      # External Interface documents
  use-cases/                       # Use Cases placed at the system
  requirements/                    # Requirements placed at the system
  features/                        # A folder for each Feature
    <feature>/
      <feature>.md                 # Feature
      use-cases/                   # Use Cases placed at the feature
      requirements/                # Requirements placed at the feature
```

- **P-STR-2** `spec/` MUST contain `README.md`, `index.md`, and `system.md`.
- **P-STR-3** `README.md` MUST satisfy base OKF, use `Reference` as its type,
  and declare the adopted profile version, each adopted module, and any local
  exceptions.
- **P-STR-4** Folders MUST be named as this structure or an adopted module's
  **Structure** shows, and each folder MUST hold only its reserved `index.md`
  and `log.md` and what the structure shows in it.

- **P-STR-5** Each Feature, and each type that a module makes a folder, MUST
  be a folder containing a concept document with the same name as the folder,
  whether or not the folder holds other concepts, and every other concept
  MUST be a single file.
- **P-STR-6** A folder that holds documents of a type, such as `users/` or
  `use-cases/`, MUST NOT exist without a concept document in it.
- **P-STR-7** Every populated folder MUST contain an `index.md`, except a
  concept folder that holds only its concept document.
- **P-STR-8** Concept filenames and concept folder names SHOULD be the
  kebab-case form of the concept's title.

Every placement level has the same shape: its concept document, which for the
system is `system.md`; `use-cases/` and `requirements/` for the documents
placed at it; and a folder for the placement levels below it. A concept's
shape follows its type, not its contents: a feature with no use cases yet is
still a folder, so that adding one never moves the feature.

## Placement

- **P-PLC-1** Each concept MUST have exactly one home and MUST NOT be copied
  to another location; other documents link to it.

Placement expresses ownership and, for a Use Case or Requirement, its subject.
It does not make a concept conditional on the feature it is placed under;
every other connection between concepts is a link, as
[Named links](#named-links) states.

### Placement levels

Features belong to the system. A Use Case or Requirement is placed at the
system or at a feature. An adopted module can add placement levels.

### Fixed locations

- **P-PLC-2** These types, and the types in an adopted module's
  **Fixed locations** table, MUST live at the locations given.

| Type | Location |
| --- | --- |
| `System` | `system.md` |
| `Business Requirements` | `business.md` |
| `Glossary` | `glossary.md` |
| `User Class` | `users/` |
| `External Interface` | `interfaces/` |
| `Feature` | `features/<feature>/` |

Features do not contain the types in this table; they link to them.

### Rule-placed types

- **P-PLC-3** A Use Case or Requirement MUST be placed at its home: the
  narrowest placement level whose removal would remove the concept or change
  its meaning.
- **P-PLC-4** When that test does not settle the home, the concept SHOULD be
  placed at the higher level.

A concept used by two features has their nearest common placement level as
its home.

### Names and meanings

- **P-PLC-5** Each meaning MUST be defined exactly once in the corpus, and each
  defined name MUST have one meaning.

## Ownership tests

When content could belong to more than one type, this section and the
**Ownership tests** of adopted modules decide its owning type. Each test is a
list of questions, and the first answered yes decides. Templates link to these
tests rather than restating them.

### Where content goes

- **P-OWN-1** Content MUST be placed with the owning type that this table or
  an adopted module's **Where content goes** table gives, and content that
  more than one row could describe MUST be placed as the ownership tests
  decide.

| Concern | Owning type |
| --- | --- |
| What a term means to the business | Glossary |
| The formats and protocols that a counterpart or a named standard requires at a connection | External Interface |
| What a user interface presents and offers | The **Illustrations** of the narrowest placement level whose use cases it serves |
| A binding obligation on a user interface, such as accessibility | Requirement |
| The conditions the system must work in | System operating environment |
| A condition that more than one requirement uses | A named condition in the System's **Operating environment** |

A row for a definition that more than one document uses, such as a named
condition, gives its shared home. A definition that one document alone uses
can be stated where it is used or in its shared home; one stated in place
moves to its shared home when its second use appears. Documents link to the
shared definition.

### Defined names

- **P-OWN-2** A concept document with a **Definition** section MUST be the
  only definition of its title's name, and a glossary entry for that name
  MUST have no definition and a **Defined by** line that links to the
  concept.

A glossary entry for such a name is present when readers look for the name in
the glossary.

### Use case extension or requirement

- **P-OWN-3** Detail about how a use case step or extension is handled MUST be
  placed by the first of these questions answered yes.

1. Would a reviewer need more detail than the condition detected and how the
   interaction continues or ends to decide whether the system complies, such
   as what it rejects, records, or sends, with values or timing? That detail
   is a Requirement, and the step or extension states **specified by**.
2. Otherwise, it stays in the use case, at low precision.

## Named links

A link from one document to another is plain unless a named link applies. A
plain link sits in the place its type contract gives it, such as a use case's
**Primary actor**; links to a glossary entry or named condition that the
document uses; or sits under **Related** for a concept the document is about.
A link whose meaning this table or an adopted module's **Named links** table
gives is stated in bold with that name, such as
"**specified by** [Reservations of unavailable equipment are rejected](<link>)".

- **P-LNK-1** A document MUST link to each concept it depends on, summarizes,
  belongs to, is about, or uses, and MUST state the link as a named link when
  one applies.
- **P-LNK-2** Each named link MUST be stated only in the document that the
  table's **Stated in** column names.
- **P-LNK-3** A document SHOULD NOT list the concepts that link to it or that
  its folder contains; each folder's `index.md` lists what the folder
  contains.

| Named link | Meaning | Stated in | Links to |
| --- | --- | --- | --- |
| specified by | The requirement that states a step's or extension's binding detail | Use Case step or extension | Requirement |
| serves | What a concept exists to support or help achieve | Feature, Requirement, Quality Characteristic | User Class, business objective, or, from a Requirement, Quality Characteristic |
| replaces | A concept that supersedes a deprecated one | The replacing concept | The deprecated concept |

## Status and change

The status of a concept document uses the OKF v0.2 frontmatter fields `status`
and `verified`.

| Status | Meaning |
| --- | --- |
| `draft` | Not yet accepted. It may hold gaps, recorded under **Open questions**. |
| `stable` | Accepted by a person with authority to accept it. In OKF, an absent `status` means `stable`. |
| `deprecated` | No longer current, and kept so that links and history survive. |

- **P-STA-1** A concept document that has not been accepted MUST carry
  `status: draft`.
- **P-STA-2** A document MUST become `stable` only when a person with
  authority to accept it does so, recorded as a `verified` entry whose `by`
  is a `human:<id>` actor.
- **P-STA-3** A `stable` document MUST NOT have open questions that affect its
  binding content.
- **P-STA-4** A change to the binding content of a `stable` document MUST be
  accepted again, as P-STA-2 requires, or the document returned to `draft`.
- **P-STA-5** A concept that is no longer current MUST be marked
  `status: deprecated` rather than deleted while any document links to it, and
  a concept that supersedes it MUST state **replaces**.
- **P-STA-6** A move or rename MUST update every inbound link.

Release planning, including release priority and assignment, is work
management, not status. Version control holds the history of changes, moves,
and renames.

## Content rules

These rules apply to every concept document.

### Link instead of restating

- **P-CON-1** A document MUST NOT restate content that another concept owns;
  it summarizes only what the reader needs in place and links to the owning
  document.
- **P-CON-2** A document MUST use each term as the glossary defines it, and
  link to the entry rather than redefine the term.
- **P-CON-3** A term that readers could interpret differently SHOULD have a
  glossary entry once its meaning is agreed.

### Record gaps instead of inventing

- **P-CON-4** A document MUST NOT invent content to complete a section, such
  as objectives, measures, targets, figures, sources, evidence, or authority;
  what is unknown or undecided, including a term whose meaning is not agreed,
  is recorded under **Open questions**, and a required field or section whose
  content is unknown is kept with its gap recorded there.

### Concerns not yet defined

- **P-CON-5** Content about a concern that this profile and the adopted
  modules do not define SHOULD follow the practice that the Writing guidance
  of the document's type gives for it, and otherwise be stated in prose in the section
  nearest to it, with the records that hold it linked under **Related** and
  what is undecided recorded under **Open questions**.

[Not yet defined](#not-yet-defined) lists the concerns this version leaves
undefined.

### Exceptions

- **P-CON-6** Binding content MUST state its exceptions in the same section.

An exception that has its own source or rationale is still stated in the
concept it is an exception to, with its source or rationale under
**Rationale**.

### Work management and design

- **P-CON-7** A document MUST NOT include release priority, release
  assignment, estimates, delivery status, or roadmaps; it links to
  work-management records.
- **P-CON-8** A document MUST NOT state design, other than a choice that a
  design constraint makes an obligation; it links to the records that
  describe design. Design includes:
  - internal architecture, implementation, and physical data design;
  - detailed user interface design, such as layout, visual styling, exact
    wording, or control types; and
  - a storage, display, or transmission format, length, or limit, unless the
    meaning of the data, a named business or industry standard, the
    business's own use, or the counterpart at an External Interface sets it.

A reservation number given to customers is used by the business; a
12-character limit chosen for a database column is design.

### Definitions

- **P-CON-9** Every definition, whether a glossary entry's or a concept's
  **Definition** section, MUST be a phrase that could replace the term in a
  sentence, naming the broader kind of thing and then what distinguishes it
  from others of that kind, without circular wording.

The [Glossary template](../templates/glossary.md#definitions) describes how
to write a definition well.

### Binding and illustrative content

Binding content establishes the obligations, rules, or definitions that a
document exists to state. It is everything in a concept document except its
supporting sections and, in the Glossary, the lines of each entry after its
definition. It takes the form that states it most clearly: prose, a list, a
table, a diagram, a formula, or a combination. Illustrative content, such as
examples, scenarios, sample data, user interface sketches, and explanatory
diagrams, helps a reader understand it, and lives under **Illustrations** or
on a glossary entry's **Example** line.

- **P-CON-10** When binding content uses more than one form, the forms MUST
  agree.
- **P-CON-11** A binding table or diagram MUST be complete: it covers every
  case or states what happens in the rest.
- **P-CON-12** Illustrative content MUST NOT add to, restrict, or contradict
  binding content; when the two disagree, the binding content governs and the
  illustration is corrected.

A user interface sketch that reveals an obligation is not the obligation's
home; the obligation is a Requirement.

### Document conventions

A Type contract lists the sections a document includes. An entry marked
*(optional)* need not be present, and an entry marked with a condition, such
as *(when a step calls on another party)*, is required only when the
condition holds. Every concept document can also
include **Open questions**, **Related**, and **Illustrations**, and a rough
sketch in an illustrative section can take any form, including an image.

- **P-DOC-1** Optional Context rows, entry lines, and sections that have no
  content SHOULD be omitted.
- **P-DOC-2** The section for unresolved matters MUST be named
  **Open questions**, the section for links to neighboring concepts and records
  **Related**, and the section for illustrative content **Illustrations**,
  except for the **Example** line of a glossary entry.
- **P-DOC-3** Supporting sections SHOULD come last, in this order:
  **Illustrations**, **Rationale**, **Verification**, **Open questions**,
  **Related**.
- **P-DOC-4** Diagrams SHOULD be written in Mermaid, so that they remain text
  that can be reviewed and changed with the rest of the document.
- **P-DOC-5** The provenance of a document's content, such as the stakeholder
  decisions, regulations, incidents, or research it came from, SHOULD be
  recorded in OKF `sources` frontmatter rather than in a body section.

## Not yet defined

This version leaves these concerns undefined. Content about them follows base
OKF v0.2, the conventions already present in the bundle, and
[P-CON-5](#concerns-not-yet-defined). For some of them, the Writing guidance
of the type they concern gives a more specific practice.

- frontmatter keys beyond base OKF v0.2;
- who may accept each type, and review dates such as `stale_after`;
- stable identifiers for linked headings, such as business objective numbers;
- a product vision, initiative priorities and constraints, assumptions and
  dependencies, and risks;
- use case goal levels, such as summary and subfunction use cases;
- how the parts of a system or feature fit together beyond folder indexes;
- optional features, and features that require or exclude each other;
- requirement classifications, such as functional, conformance, human
  factors, and process;
- kinds of external interface counterpart;
- obligations that cannot both be fully met;
- in the Decomposition module: operating conditions and quality priorities
  specific to one subsystem, connections between sibling subsystems, folders
  for concepts specific to one subsystem, and use cases and requirements whose
  subject is a subsystem but that belong to a system-level feature;
- in the Rules module: business rule categories, volatility, enforcement
  levels, and relationships between business rules;
- in the Quality module: correspondence with a quality model, baselines, and
  quality characteristics nested within other quality characteristics; and
- in the Data module: what causes each lifecycle transition, where a data
  attribute's value comes from, the sensitivity and purpose of personal data,
  specialization between entity types or value types, and an overall data
  model spanning entity types.
