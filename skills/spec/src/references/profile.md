# Spec profile

Version **0.1.0** · Base **OKF v0.2** · Maintainer **@craigsmitham** · Status
**draft**.

This profile describes the specification of a software system as an OKF v0.2
bundle. It defines the core concept types, the corpus structure, where each
concept lives, which type owns content that two types border, how concepts
relate, how their status changes, and the rules every document follows.
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
| [`External Interface`](../templates/external-interface.md) | A connection across the boundary of the system or a subsystem to an external system or a device, and what passes across it. |
| [`Feature`](../templates/feature.md) | A coherent unit of capability that the system provides to its users. |
| [`Use Case`](../templates/use-case.md) | How an actor pursues a goal at a boundary, through success and failure paths. |
| [`Requirement`](../templates/requirement.md) | An obligation, other than a required level of quality, that the system or a subsystem must satisfy under identified conditions. |
| [`Glossary`](../templates/glossary.md) | The agreed terms of the system, and what each one means. |

This profile does not describe the system's architecture. A feature, or a
subsystem or feature component that a module adds, is a specification
boundary or placement level, not an architecture element; design and
implementation structure belong to records.

## Modules

A module adds concept types, with the structure, placement, ownership tests,
relationships, vocabulary, and interim practices they need. Its tables extend
the tables of the same name in this profile. Adopt a module when the system
needs its types.

| Module | Types | Without the module |
| --- | --- | --- |
| [Decomposition](modules/decomposition.md) | `Subsystem`, `Feature Component` | Use cases and requirements are placed at the system or at a feature. |
| [Rules](modules/rules.md) | `Business Rule` | A rule that the business would keep without the system is stated through the Requirements that enforce it, with the rule's source under **Rationale**. |
| [Quality](modules/quality.md) | `Quality Characteristic`, `Quality Requirement` | A required level of quality is a Requirement that states its measure in the statement. |
| [Data](modules/data.md) | `Entity Type`, `Value Type` | The meaning of data is a glossary entry, and its detail is stated where it is used. |

- **P-MOD-1** A corpus MUST NOT contain a document of a type from a module it
  has not adopted.
- **P-MOD-2** A corpus that adopts a module MUST apply the module's rules as
  part of this profile.
- **P-MOD-3** Content whose owning type belongs to a module the corpus has not
  adopted MUST be written as the **Without the module** column gives.

## Vocabulary

Each term below has one meaning throughout this profile, its modules, and its
templates.

| Term | Meaning |
| --- | --- |
| Boundary | What separates the system, or a subsystem, from the parties it interacts with. |
| Subject | The System or Subsystem whose boundary a Use Case, Requirement, or Quality Requirement describes. It is the System unless an adopted module gives a Subsystem. It is never a feature, feature component, or external interface. |
| Placement level | The system or a feature, or a level that an adopted module adds, as the place where a Use Case or Requirement lives. A feature placed directly under the system is a *system-level feature*. |
| Owner | The placement level at which a Use Case or Requirement is placed, as [Rule-placed types](#rule-placed-types) decides. The type that [Ownership tests](#ownership-tests) assign content to is its *owning type*. |
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
  users/
  interfaces/
  use-cases/                       # Use Cases placed at the system
  requirements/                    # Requirements placed at the system
  features/
    <feature>/
      <feature>.md                 # Feature
      use-cases/                   # Placed at the feature
      requirements/                # Placed at the feature
```

- **P-STR-2** `spec/` MUST contain `README.md`, `index.md`, and `system.md`.
- **P-STR-3** `README.md` MUST satisfy base OKF, use `Reference` as its type,
  and declare the adopted profile version, each adopted module, and any local
  exceptions.
- **P-STR-4** Folders MUST be named as shown here or in an adopted module, and
  each folder MUST hold only its reserved `index.md` and `log.md` and what
  this table or a module's **Folders** table gives it.

  | Folder | Holds |
  | --- | --- |
  | `users/` | `User Class` documents |
  | `interfaces/` | `External Interface` documents |
  | `use-cases/` | The `Use Case` documents placed at its placement level |
  | `requirements/` | The `Requirement` documents placed at its placement level |
  | `features/` | A folder for each `Feature` at its placement level |
  | `<feature>/` | Its concept document, `use-cases/`, and `requirements/` |

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
every other relationship is a link, as [Relationships](#relationships) states.

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

- **P-PLC-3** A Use Case or Requirement MUST be placed at its owner: the
  narrowest placement level whose removal would remove the concept or change
  its meaning.
- **P-PLC-4** When that test does not settle the owner, the concept SHOULD be
  placed at the higher level.

A concept used by two features has their nearest common placement level as
its owner.

### Names and meanings

- **P-PLC-5** Each meaning MUST be defined exactly once in the corpus, and each
  defined name MUST have one meaning.

## Ownership tests

When content could belong to more than one type, this section and the
**Ownership tests** of adopted modules decide its owning type. Templates link
to these tests rather than restating them.

### Where content goes

- **P-OWN-1** Content MUST be placed with the owning type that this table or
  an adopted module's **Where content goes** table gives, and content that
  more than one row could describe MUST be placed as the ownership tests
  decide.

| Concern | Owning type |
| --- | --- |
| What a term means to the business | Glossary |
| The formats and protocols that a counterpart or a named standard requires at a connection | External Interface |
| What a user interface presents and offers | The **Illustrations** of the narrowest feature, or feature component, whose use cases it serves |
| A binding obligation on a user interface, such as accessibility | Requirement |
| The conditions the system must work in, including named conditions that requirements use | System operating environment |

### Use case extension or requirement

- **P-OWN-2** Detail about how a use case step or extension is handled MUST be
  placed as the following question decides.

A use case extension names the condition detected and how the interaction
continues or ends, at low precision. Would a reviewer need more detail to
decide whether the system complies, such as what it rejects, records, or
sends, with values or timing? If so, that detail is a Requirement, and the
step or extension states **specified by**.

## Relationships

A relationship is a link from one document to another. Most links are plain:
a link in the place its type contract gives it, such as a use case's
**Primary actor**; a link to a glossary entry or named condition that the
document uses; or a link under **Related** to a concept the document is
about. A link whose meaning this table or an adopted module's
**Relationships** table names is stated in bold with that relationship, such
as "**specified by** [Reservations of unavailable equipment are rejected](<link>)".

- **P-REL-1** A document MUST link to each concept it depends on, summarizes,
  belongs to, is about, or uses, and MUST name the link with a relationship
  from a relationships table when one applies.
- **P-REL-2** Each relationship MUST be stated only in the document that the
  table's **Stated in** column names.
- **P-REL-3** A document SHOULD NOT list the concepts that link to it or that
  its folder contains; each folder's `index.md` lists what the folder
  contains.

| Relationship | Meaning | Stated in | Links to |
| --- | --- | --- | --- |
| specified by | The requirement that states a step's or extension's binding detail | Use Case step or extension | Requirement |
| serves | What a concept exists to support | Feature, Requirement, Quality Characteristic | User Class, business objective, or Quality Characteristic |
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
management, not status.

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

### Exceptions

- **P-CON-5** Binding content MUST state its exceptions in the same section.

### Work management and design

- **P-CON-6** A document MUST NOT include release priority, release
  assignment, estimates, delivery status, or roadmaps; it links to
  work-management records.
- **P-CON-7** A document MUST NOT state design, other than a choice that a
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

- **P-CON-8** Every definition, whether a glossary entry's or a concept's
  **Definition** section, MUST be a phrase that could replace the term in a
  sentence, naming the broader kind of thing and then what distinguishes it
  from others of that kind, without circular wording.

The [Glossary template](../templates/glossary.md#definitions) describes how
to write a definition well.

### Shared definitions

- **P-CON-9** A condition that more than one requirement or quality
  requirement uses MUST be a named condition in the System's
  **Operating environment**.

A condition that one document alone uses can be defined where it is used or
in its shared home; one defined in place moves to its shared home when its
second use appears. Documents link to the shared definition.

### Binding and illustrative content

Binding content establishes the obligations, rules, or definitions that a
document exists to state. It is everything in a concept document except its
supporting sections and, in the Glossary, the lines of each entry after its
definition. It takes the form that states it most clearly: prose, a list, a
table, a diagram, a formula, or a combination. Illustrative content, such as
examples, scenarios, sample data, user interface sketches, and explanatory
diagrams, helps a reader understand it, and lives under **Illustrations** or
on a glossary entry's **Example** line.

- **P-BIN-1** When binding content uses more than one form, the forms MUST
  agree.
- **P-BIN-2** A binding table or diagram MUST be complete: it covers every
  case or states what happens in the rest.
- **P-BIN-3** Illustrative content MUST NOT add to, restrict, or contradict
  binding content; when the two disagree, the binding content governs and the
  illustration is corrected.

A user interface sketch that reveals an obligation is not the obligation's
home; the obligation is a Requirement.

### Document conventions

A Type contract lists the fields a document identifies and the sections it
includes. An entry marked *(optional)* need not be present, and an entry
marked with a condition, such as *(when a step calls on another party)*, is
required only when the condition holds. Every concept document can also
include **Open questions**, **Related**, and **Illustrations**, and a rough
sketch in an illustrative section can take any form, including an image.

- **P-DOC-1** Optional fields, entry lines, and sections that have no content
  SHOULD be omitted.
- **P-DOC-2** The section for unresolved matters MUST be named
  **Open questions**, the section for links to neighboring concepts and records
  **Related**, and the section for illustrative content **Illustrations**,
  except for the **Example** line of a glossary entry.
- **P-DOC-3** Supporting sections SHOULD come last, in this order:
  **Illustrations**, **Rationale**, **Verification**, **Open questions**,
  **Related**.
- **P-DOC-4** The fields that a document identifies MUST be presented in a
  two-column `Context | Value` table directly below the title, and a document
  that identifies no fields MUST NOT have a Context table.
- **P-DOC-5** Diagrams SHOULD be written in Mermaid, so that they remain text
  that can be reviewed and changed with the rest of the document.
- **P-DOC-6** The provenance of a document's content, such as the stakeholder
  decisions, regulations, incidents, or research it came from, SHOULD be
  recorded in OKF `sources` frontmatter rather than in a body section, unless
  the Type contract identifies a **Source** field for it.

Identified fields are short values or links that situate or classify the
document, such as its primary actor or source.

## Not yet defined

This version does not prescribe the following. Until it does, follow base OKF
v0.2, the conventions already present in the bundle, and the interim practice
given for each. Each module lists the interim practices for its types.
Templates link here rather than restating an interim practice.

### Structure and placement

| Topic | Interim practice |
| --- | --- |
| How the parts of a system or feature fit together, beyond what folder indexes show | Explain it in the concept's **Purpose**, linking each part named. |
| Optional features: conditions under which a feature is present, and features that require or exclude each other | State the condition or dependency in the feature's **Coverage**, or under **Open questions** while it is undecided. |

### Status and identifiers

| Topic | Interim practice |
| --- | --- |
| Who may accept each type, review dates such as `stale_after`, and a history of moves and renames | Record each acceptance in `verified`, as P-STA-2 requires; use version control for history. |
| Stable identifiers for linked headings, such as business objective numbers | Do not reuse a number that other documents link to for a different concept. |

### Business and requirements

| Topic | Interim practice |
| --- | --- |
| A product vision; initiative priorities, such as whether schedule, cost, features, and quality are fixed or flexible; initiative constraints, such as budget or deadlines; assumptions and dependencies; and risks | Link the records that hold them from the Business Requirements' **Related**. |
| Requirement classifications, such as functional, conformance, human factors, and process | Name the law, standard, or activity in the requirement's statement or rationale. A design constraint is recognized by its obligation, not by a field. |
| Kinds of external interface counterpart, such as external system or device | Say what the counterpart is in the External Interface's **Purpose**. |
| Obligations that cannot both be fully met | Record the conflict under **Open questions** in each document. |
| Exceptions that have their own source or rationale | State the exception in the concept it is an exception to, as [Exceptions](#exceptions) requires, and give its source or rationale under **Rationale**. |

### Use cases

| Topic | Interim practice |
| --- | --- |
| Goal levels, such as summary and subfunction use cases | Write use cases for goals that the primary actor completes in one sitting. When another use case achieves a step, link it at that step. |
