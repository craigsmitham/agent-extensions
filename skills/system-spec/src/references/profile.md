# Spec profile

Version **0.1.0** · Base **OKF v0.2** · Maintainer **@craigsmitham** · Status
**draft**.

This profile describes the specification of a software system as an OKF v0.2
bundle. It defines the concept types, the corpus structure, where each concept
lives, which type owns content that two types border, how concepts link, how
they change, and the rules every document follows. The normative
contract comprises this file and the **Type contract** section of each
template. Other template sections are authoring guidance.

MUST and MUST NOT are requirements; SHOULD and SHOULD NOT are recommendations;
MAY denotes an option. Each normative statement is a list item that begins
with a rule identifier, such as **P-STR-1** in this profile or **UC-3** in a
Type contract, so that reviews can cite it. Text without an identifier defines
or explains; it adds no requirement.

Profiles are a producer convention beyond OKF v0.2. No `okf_profile` field is
introduced. Examples in the templates use the [running example](example.md).

## Concept types

- **P-TYP-1** Each concept document in the corpus MUST use one of the `type`
  values in this table.

| Type | Description |
| --- | --- |
| [`Mission`](../templates/mission.md) | Why the business or product exists: whom it serves and what it does for them. |
| [`Vision`](../templates/vision.md) | The future that the business or product pursues, beyond the horizon of the system's objectives. |
| [`Principles`](../templates/principles.md) | The guidance by which the business or product decides between reasonable options that conflict, in order of precedence. |
| [`Opportunity`](../templates/opportunity.md) | What the system is built or changed to make possible: the need that is unmet, the current gap, and why now. |
| [`Job to Be Done`](../templates/job-to-be-done.md) | The progress that a group of people seek in their circumstances, whatever product, service, or system helps them make it. |
| [`Stakeholders`](../templates/stakeholders.md) | The people and groups with an interest in the system who do not use it, what each values, and any authority each holds over it. |
| [`Objectives`](../templates/objectives.md) | The results that the system must bring about, each with the indicators by which its achievement is recognized. |
| [`Scope`](../templates/scope.md) | The business area under consideration, and what the system includes and excludes within it. |
| [`System`](../templates/system.md) | The software system being specified, and the boundary that its other concepts describe. |
| [`Subsystem`](../templates/subsystem.md) | A part of the system with its own boundary, because it has its own user classes, external interfaces, required levels of quality, or delivery or operation. |
| [`User Class`](../templates/user-class.md) | A distinct group of the system's users, identified by how they use the system and what they need from it. |
| [`External Interface`](../templates/external-interface.md) | A connection across the system's boundary to an external system or a device, and what passes across it. |
| [`Feature`](../templates/feature.md) | A coherent unit of capability that the system provides to its users. |
| [`Feature Component`](../templates/feature-component.md) | A distinct part of a feature's behavior, such as a command, workflow, or screen, that has its own use cases or requirements. |
| [`Use Case`](../templates/use-case.md) | How an actor pursues a goal at a boundary, through success and failure paths. |
| [`Requirement`](../templates/requirement.md) | An obligation that the system must satisfy under identified conditions. |
| [`Business Rule`](../templates/business-rule.md) | A rule under the business's jurisdiction that restricts conduct, requires an action, infers a fact, or computes a value, and that the system must respect. |
| [`Quality Characteristic`](../templates/quality-characteristic.md) | A property of how well the system works, such as availability or response time. |
| [`Quality Requirement`](../templates/quality-requirement.md) | A required level of a quality characteristic for the system, under stated conditions. |
| [`Glossary`](../templates/glossary.md) | The agreed terms of the system, and what each one means. |
| [`Entity Type`](../templates/entity-type.md) | A kind of thing in the business domain that has identity and about which the system keeps data. |
| [`Value Type`](../templates/value-type.md) | A kind of value in the business domain that has no identity and is defined by its meaning, attributes or domain, and allowed values. |

Only the System document is required. A document of another type is written
when there is content for it, and only when its Type contract's creation test,
where it has one, is met; a corpus has no documents of the types it does not
need.

This profile does not describe the system's architecture. A subsystem, a
feature, or a feature component is a specification boundary or placement
level, not an architecture element; design and implementation structure
belong to records.

## Vocabulary

Each term below has one meaning throughout this profile and its templates.

| Term | Meaning |
| --- | --- |
| Specification | The agreed account of what a software system does, whom and what it serves, and why, in whatever form holds it. A corpus is the form this profile gives it. |
| Boundary | What separates the system from the parties it interacts with. |
| Subject | The System or Subsystem whose boundary a Use Case or Requirement describes. It is never a feature, a feature component, or an external interface. |
| Placement level | The system, a subsystem, a feature, or a feature component, as a place where Use Cases and Requirements live. |
| Home | The one location of a concept. The home of a Use Case or Requirement is the placement level at which it is placed, as [Rule-placed types](#rule-placed-types) decides. |
| Owning type | The type that the [Ownership tests](#ownership-tests) assign content to. |
| Named link | A link whose meaning the [Named links](#named-links) table gives, stated in bold with its name. |
| Direction | The mission, vision, and principles of a business or product, which hold whichever system serves it. Direction is intent and guidance, not obligation. |
| Principle | A statement of how to decide between reasonable options that conflict, as an entry of a Principles document. |
| Job performer | The person or group whose progress a Job to Be Done describes, as the job itself describes them. A job performer need not use the system, and is described in the job rather than as a User Class or stakeholder. |
| Business area | The business activities and parties under consideration, whether or not the system supports them, as the Scope document states it. |
| Scope | What the system includes and excludes, as the Scope document states it. What a feature includes is its *coverage*. |
| Objective | A result that the system must bring about, stated as an outcome for the business or those it serves rather than as an output, as an entry of the Objectives document. |
| Indicator | An observable sign by which an objective's achievement is recognized: quantitative, with a target and timeframe, or qualitative, naming the evidence observed. It is neither a Measure nor a key result of a plan. |
| System-level feature | A feature placed directly under the system. |
| Subsystem-level feature | A feature placed under a subsystem. |
| Design constraint | A Requirement whose obligation is to use, or not use, a specific technology, platform, or design. |
| Measure | A quantity on which a Quality Requirement states a level, defined under a Quality Characteristic's **Measures**. |
| Stakeholder | A person or group with an interest in the system who does not use it or its outputs directly. People who use the system, including those who operate it, belong to a User Class. |
| User interface | What the system presents to people and the actions it offers them. *Interface* alone means an External Interface. |
| Counterpart | The external system or device at the other end of an External Interface. |
| Attribute | A data attribute: an item of data kept about an Entity Type's instance or making up a Value Type's value. |
| Instance | An item of the data that an Entity Type describes. |
| Invariant | A condition that every instance of an Entity Type, or every value of a Value Type, satisfies because of what the data means. |
| Supporting sections | **Illustrations**, **Rationale**, **Verification**, **Open questions**, and **Related**, which several types share and which hold no binding content. |
| Operations concerns | Instrumentation, service level objectives and agreements, alerting, and operational responses. They belong to operations records. |
| Record | Material maintained outside the corpus, such as architecture, operations, engineering, or work-management records. |

A subsystem is specified as a system is, at its own boundary:

- **P-DEC-1** Wherever this profile or a template describes the system as a
  boundary or the other end of an External Interface, or places
  features, use cases, or requirements under the system, the same MUST apply
  to a subsystem at its own boundary, except where this profile states
  otherwise.

A Use Case or Requirement placed within a subsystem has that Subsystem as its
subject.

## Structure

- **P-STR-1** An adopting repository MUST place the corpus in
  `<repository-root>/spec/`, abbreviated `/spec/`. The corpus specifies one
  system.

```text
spec/
  README.md                        # Adoption declaration
  index.md                         # Navigation; carries okf_version: "0.2"
  business/                        # Why the system exists, whom it serves, and what it must achieve
    index.md                       # Entry point, arranged as P-STR-9 requires
    mission.md                     # Mission
    vision.md                      # Vision
    principles.md                  # Principles
    opportunity.md                 # Opportunity
    stakeholders.md                # Stakeholders
    objectives.md                  # Objectives
    scope.md                       # Scope
    jobs/                          # Job to Be Done documents
  system.md                        # System
  glossary.md                      # Glossary
  users/                           # User Class documents
  interfaces/                      # External Interface documents
  rules/                           # Business Rule documents
  entities/                        # Entity Type documents
  values/                          # Value Type documents
  quality/                         # A folder for each Quality Characteristic
    <characteristic>/
      <characteristic>.md          # Quality Characteristic
      <quality-requirement>.md     # Quality Requirement
  use-cases/                       # Use Cases placed at the system
  requirements/                    # Requirements placed at the system
  features/                        # A folder for each Feature
    <feature>/
      <feature>.md                 # Feature
      use-cases/                   # Use Cases placed at the feature
      requirements/                # Requirements placed at the feature
      components/                  # A folder for each Feature Component
        <component>/
          <component>.md           # Feature Component
          use-cases/
          requirements/
  subsystems/                      # A folder for each Subsystem
    <subsystem>/
      <subsystem>.md               # Subsystem
      use-cases/                   # Placed at the subsystem
      requirements/
      features/                    # Same structure as spec/features/
```

- **P-STR-2** `spec/` MUST contain `README.md`, `index.md`, and `system.md`.
- **P-STR-3** `README.md` MUST satisfy base OKF, use `Reference` as its type,
  and declare the adopted profile version and any local exceptions.
- **P-STR-4** Files and folders MUST be named and placed as this structure
  shows, and each folder MUST hold only its reserved `index.md` and `log.md`
  and what the structure shows in it.
- **P-STR-5** Each Subsystem, Feature, Feature Component, and Quality
  Characteristic MUST be a folder containing a concept document with the same
  name as the folder, whether or not the folder holds other concepts, and every
  other concept MUST be a single file.
- **P-STR-6** A folder that holds documents of a type, such as `users/` or
  `use-cases/`, MUST NOT exist without a concept document in it.
- **P-STR-7** Every populated folder MUST contain an `index.md`, except a
  concept folder that holds only its concept document.
- **P-STR-8** Concept filenames and concept folder names SHOULD be the
  kebab-case form of the concept's title.

`business/` holds what justifies and directs the system; the rest of the
corpus specifies the system. Its index is where a reader starts to learn what
the business cares about, so its headings follow Peter Drucker's questions of
mission, customer and value, results, and plan, and it shows each of those
concerns that the corpus leaves unanswered. OKF index entries are links, so a
concern without a document is stated in a paragraph rather than as an entry.

- **P-STR-9** `business/index.md` MUST use these level-2 headings in this
  order, each present whether or not it has entries, and under each MUST link
  every document or folder of the types it lists that the corpus holds or uses
  from another corpus, or, for each of those types that it neither holds nor
  uses, state "<Type>: not defined." in a paragraph:
  - **Why we exist**: Mission, Vision, and Principles.
  - **Opportunity**: Opportunity.
  - **Whom we serve**: the `jobs/` folder, Stakeholders, and the corpus's
    `users/` folder.
  - **Results we seek**: Objectives.
  - **What we will and won't do**: Scope.

Every placement level has the same shape: its concept document, which for the
system is `system.md`; `use-cases/` and `requirements/` for the documents
placed at it; and a folder for the placement levels below it. A concept's
shape follows its type, not its contents: a feature with no use cases yet is
still a folder, so that adding one never moves the feature. Features do not
contain the documents the structure places outside them, such as user classes,
external interfaces, and entity types; they link to them. A data attribute
that only one feature needs still belongs to its entity type.

A Quality Requirement is placed in the folder of the characteristic that the
[Quality Requirement contract](../templates/quality-requirement.md#type-contract)
chooses. A measure has one home however many quality requirements use it, as
the
[Quality Characteristic contract](../templates/quality-characteristic.md#type-contract)
requires, because those quality requirements are placed beside it.

A business or product that several systems serve has one direction, held by
one corpus and used by the others.

- **P-DIR-1** A corpus that uses a Mission, Vision, or Principles document held
  by another corpus MUST NOT hold its own document of that type, and its
  `README.md` MUST link each document it uses.

A job that several systems help with is likewise held by one corpus.

- **P-JOB-1** A corpus that uses a Job to Be Done held by another corpus MUST
  NOT hold its own document of that job, and its `README.md` MUST link each
  job it uses from another corpus.

## Placement

Each type other than Use Case and Requirement has the one location that
[Structure](#structure) shows. Placement expresses ownership and, for a Use
Case or Requirement, its subject. It does not make a concept conditional on the
feature it is placed under; every other connection between concepts is a link,
as [Named links](#named-links) states. Each concept has one home, as
[One home](#one-home) requires.

### Placement levels

Features belong to the system or to one subsystem, and feature components
belong to one feature. A Use Case or Requirement is placed at the system, a
subsystem, a feature, or a feature component. One whose subject is a
Subsystem is placed within that subsystem: at the subsystem, or at one of its
features or feature components. A concept shared by two subsystems is placed
at the system, and its subject is the System.

Every type other than those placed within a subsystem lives at the system
level, even when it is specific to one subsystem, such as a user class, an
external interface, or a glossary term.

- **P-DEC-2** A concept that lives at the system level but is specific to one
  subsystem SHOULD link that subsystem under **Related**.
- **P-DEC-3** A meaning specific to one subsystem MUST take a name distinct
  from the system's other names.
- **P-DEC-4** The **In scope** section of the Scope MUST link each subsystem
  it includes.

### Rule-placed types

- **P-PLC-3** A Use Case or Requirement MUST be placed at its home: the
  narrowest placement level whose removal would remove the concept or change
  its meaning.
- **P-PLC-4** When that test does not settle the home, the concept SHOULD be
  placed at the higher level.

A concept used by two features has their nearest common placement level as
its home.

## Ownership tests

When content could belong to more than one type, this section decides its
owning type. After the **Where content goes** table, each test is a list of
questions, and the first answered yes decides. Templates link to these tests
rather than restating them.

### Where content goes

- **P-OWN-1** Content MUST be placed with the owning type that this table
  gives, and content that more than one row could describe MUST be placed as
  the ownership tests decide.

| Concern | Owning type |
| --- | --- |
| Why the business or product exists, whatever system serves it | Mission |
| The progress that people seek in their circumstances, whatever solution helps them | Job to Be Done |
| Who makes that progress, and the circumstances in which they seek it | The Job to Be Done, not a User Class |
| The future that the business or product pursues, without an indicator or target | Vision |
| How to decide between reasonable options that conflict, such as which user class or quality prevails | Principles |
| The interest in the system of a person or group who does not use it, what they value, and any authority they hold over it | Stakeholders, not a User Class |
| Guidance for design decisions, such as visual style or interaction patterns | Not Principles; design records, as [P-CON-8](#work-management-and-design) requires |
| What a term means to the business | Glossary |
| How the business decides whether something belongs to a classification, such as *high-risk customer* | Business Rule. The classification's meaning is a glossary entry with a **Decided by** line. |
| The formats and protocols that a counterpart or a named standard requires at a connection | External Interface |
| What a user interface presents and offers | The use case steps it serves, stated without user interface design, which belongs to design records, as [P-CON-8](#work-management-and-design) requires. A rough sketch can illustrate those steps. |
| A binding obligation on a user interface, such as accessibility | Requirement |
| The conditions the system must work in | The System's **Operating environment**, where a condition that more than one requirement uses is named |
| The states of an entity type's instances, the permitted transitions, what creates an instance, and whether an ended instance is removed, retained, or anonymized | The Entity Type's **Lifecycle** |
| What the system must do when a transition occurs, or when a transition that the lifecycle does not permit is attempted | Requirement, linking to the lifecycle |
| How long instances or their data are kept, and who may see them | Not the Entity Type; the rule or obligation that sets it, placed by the other ownership tests |
| A value that more than one entity type, value type, or external interface uses | A Value Type |

A row for a definition that more than one document uses, such as a named
condition, gives its shared home. A definition that one document alone uses
can be stated where it is used or in its shared home; one stated in place
moves to its shared home when its second use appears. Documents link to the
shared definition.

### Direction, job, opportunity, objectives, or scope

- **P-DIR-2** Content that could be direction, a Job to Be Done, the
  Opportunity, Objectives, or Scope MUST be placed by the first of these
  questions answered yes.

1. Does it state, or need, an indicator or target? It is an objective or one
   of its indicators.
2. Does it describe progress that people seek for themselves, whether or not
   the business helps them make it, rather than what the business does,
   pursues, or decides? It is a Job to Be Done.
3. Does it say why the business or product exists, what future it pursues, or
   how it decides between options, whatever system serves it? It is
   direction, and [where content goes](#where-content-goes) decides its type.
4. Does it say what need is unmet, what gap exists today, or why the system
   is built or changed now? It is the Opportunity.
5. Does it say which business activities and parties are under consideration,
   or what the system includes or excludes? It is Scope.
6. Otherwise, it belongs to none of these types, and the other ownership
   tests decide.

### Job to be done or use case

- **P-JOB-2** Content that could be a Job to Be Done or the goal of a Use Case
  or Feature MUST be placed by the first of these questions answered yes.

1. Does it name the system, one of its functions or user interfaces, or an
   interaction with it? It is a Use Case goal or step, or a Feature's
   capability, placed by the other ownership tests.
2. Otherwise, it is a Job to Be Done, and the use cases and features that
   help with it link it.

### Principle or obligation

- **P-DIR-3** Content that could be a principle or an obligation MUST be
  placed by the first of these questions answered yes.

1. Could two readers decide whether a single case complies without weighing
   one option against another? It is an obligation or rule, placed by the
   other ownership tests, and it can link the principle it follows under
   **Rationale**.
2. Otherwise, it guides a decision, and it is a principle.

### Business rule or requirement

- **P-RUL-1** Content that could be a Business Rule or a Requirement MUST be
  placed by the first of these questions answered yes.

1. Would it still apply if the business worked without the system, whether
   the business chose it or an outside authority, such as a law, regulation,
   standard, or contract, imposes it? It is a Business Rule.
2. Otherwise, it is a Requirement.

How the system detects, prevents, permits an override of, or reports a
violation of a rule is a Requirement that **enforces** the rule.

### Quality requirement or requirement

- **P-QUA-1** An obligation that could be a Requirement or a Quality
  Requirement MUST be placed by the first of these questions answered yes.

1. Can it be satisfied only by providing a specific function, or by using a
   specific technology, platform, or design? It is a Requirement, a design
   constraint when it names a technology, platform, or design, and it
   **serves** the quality characteristic it helps achieve.
2. Is compliance decided on each occurrence of a single response, such as a
   deadline or value for each notice sent? It is a Requirement.
3. Is compliance decided on a measure taken over a population of occurrences
   or a period, such as a percentile or a proportion of time, or on a
   criterion that holds across the subject's functions? It is a Quality
   Requirement.

An obligation for which no question is answered yes is recorded under
**Open questions** until it is restated.

### Invariant, business rule, or requirement

- **P-DAT-1** A condition on data MUST be placed by the first of these
  questions answered yes.

1. Would changing the condition change what the data means? It is an
   invariant of the Entity Type or Value Type.
2. Did the business choose the condition, or does an outside authority impose
   it, such as a policy that limits a relationship's cardinality further than
   the data allows? It is a Business Rule.
3. Otherwise, the solution imposes it, and it is a Requirement that is a
   design constraint.

What the system must do to keep an invariant or rule true, across
transitions, concurrency, retries, and failures, is a Requirement.

### Entity type, value type, or data attribute

- **P-DAT-2** A kind of thing or value in the business data MUST be placed by
  the first of these questions answered yes.

1. Must its instances be told apart even when all their data is equal? It is
   an Entity Type.
2. Otherwise, its equal values are interchangeable, and it is a Value Type,
   or a data attribute defined where it is used when
   [where content goes](#where-content-goes) allows.

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
A link whose meaning this table gives is stated in bold with that name, such
as "**specified by** [Reservations of unavailable equipment are rejected](<link>)".

- **P-LNK-1** A document MUST link to each concept it depends on, summarizes,
  is about, or uses, and MUST state the link as a named link when one
  applies.
- **P-LNK-2** Each named link MUST be stated only in the document that the
  table's **Stated in** column names.
- **P-LNK-3** A document SHOULD NOT list the concepts that link to it or that
  its folder contains; each folder's `index.md` lists what the folder
  contains.

A document's own folder shows what it belongs to, so a use case placed at a
feature does not link the feature for that reason.

| Named link | Meaning | Stated in | Links to |
| --- | --- | --- | --- |
| specified by | The requirement that states a step's or extension's binding detail | Use Case step or extension | Requirement |
| serves | What a concept exists to support or help achieve | Feature, Requirement, Quality Characteristic | User Class, Job to Be Done, objective, or Quality Characteristic |
| enforces | How the system respects a rule | Requirement | Business Rule |
| Defined by | The concept whose **Definition** defines the entry's name | Glossary entry | Concept with a **Definition** section |
| Decided by | The rule that decides whether something belongs to the entry's classification | Glossary entry | Business Rule |

## Change

Version control holds the history of changes, moves, renames, and deletions,
and the repository's own review decides what the corpus contains. This version
defines no lifecycle for documents, as [Not yet defined](#not-yet-defined)
lists.

- **P-CHG-1** A move or rename MUST update every inbound link.
- **P-CHG-2** A concept that is no longer current MUST be deleted, and every
  inbound link updated or removed.

Release planning, including release priority and assignment, is work
management, as [P-CON-7](#work-management-and-design) states.

## Content rules

These rules apply to every concept document.

### One home

- **P-CON-1** Each concept MUST have exactly one home and MUST NOT be copied
  to another location, and a document MUST NOT restate content that another
  concept owns; it summarizes only what the reader needs in place and links to
  the owning document.
- **P-CON-2** Each meaning MUST be defined exactly once in the corpus, by a
  glossary entry or by a concept's **Definition** section; each defined name
  MUST have one meaning; and a document MUST use each term as its definition
  gives, linking to it rather than redefining the term.
- **P-CON-3** A term that readers could interpret differently SHOULD have a
  glossary entry once its meaning is agreed.

### Record gaps instead of inventing

- **P-CON-4** A document MUST NOT invent content to complete a section, such
  as objectives, indicators, measures, targets, figures, sources, evidence, or
  authority; what is unknown or undecided, including a term whose meaning is
  not agreed, is recorded under **Open questions**, and a required field or
  section whose content is unknown is kept with its gap recorded there.

### Concerns not yet defined

- **P-CON-5** Content about a concern that this profile does not define SHOULD
  follow the practice that the Writing guidance of the document's type gives
  for it. Otherwise, it SHOULD be stated in prose in the section nearest to it
  only when readers need it to understand that section's binding content, and
  the records that hold it SHOULD be linked under **Related**, with what is
  undecided recorded under **Open questions**.

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

Binding content establishes the obligations, rules, definitions, or direction
that a document exists to state. It is everything in a concept document except
its supporting sections and the entry lines of a document made of entries,
such as the lines of each Glossary entry after its definition, other than
entry lines that a Type contract makes binding, such as an objective's
**Indicator** lines. It takes the
form that states it most clearly: prose, a list, a table, a diagram, a
formula, or a combination. Illustrative content, such as examples, scenarios,
sample data, user interface sketches, and explanatory diagrams, helps a reader
understand it, and lives under **Illustrations** or on an entry's **Example**
line.

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
- **P-DOC-3** Supporting sections SHOULD come last, in this order:
  **Illustrations**, **Rationale**, **Verification**, **Open questions**,
  **Related**.
- **P-DOC-4** Diagrams SHOULD be written in Mermaid, so that they remain text
  that can be reviewed and changed with the rest of the document.
- **P-DOC-5** The provenance of a document's content, such as the stakeholder
  decisions, regulations, incidents, or research it came from, SHOULD be
  recorded in OKF `sources` frontmatter rather than in a body section.
- **P-DOC-6** A supporting section, or an entry line that is not a named
  link, SHOULD be included only when it tells a reader something that the
  binding content and its links do not, and SHOULD NOT restate either; in
  particular, **Related** SHOULD NOT repeat a link that the body states.
- **P-DOC-7** **Open questions** SHOULD record only what a person must decide
  or find out before binding content can be completed, and SHOULD NOT keep a
  question once it is answered.
- **P-DOC-8** A concept document SHOULD NOT carry `status`, `verified`, or
  `stale_after` frontmatter, unless the corpus `README.md` declares a
  lifecycle as a local exception.

## Not yet defined

This version leaves these concerns undefined. Content about them follows
[P-CON-5](#concerns-not-yet-defined).

- frontmatter keys beyond base OKF v0.2;
- a lifecycle for the specification and its documents, such as review,
  acceptance, status, and review dates;
- stable identifiers for linked headings other than objectives;
- product strategy and goals between the vision and the objectives,
  initiative priorities and constraints, assumptions and dependencies, and
  risks;
- principles for one system that add to the principles another corpus holds;
- for jobs to be done: desired outcome statements, job maps and job steps,
  relationships between jobs, the forces that drive or resist a change of
  solution, and jobs of buying or supporting a solution;
- use case goal levels, such as summary and subfunction use cases;
- how the parts of a system or feature fit together beyond folder indexes;
- optional features, and features that require or exclude each other;
- requirement classifications, such as functional, conformance, human
  factors, and process;
- kinds of external interface counterpart;
- obligations that cannot both be fully met;
- for subsystems: connections between sibling subsystems, folders for concepts
  specific to one subsystem, and use cases and requirements whose subject is a
  subsystem but that belong to a system-level feature;
- for business rules: rule categories, volatility, enforcement levels, and
  relationships between business rules;
- for quality: correspondence with a quality model, baselines, and quality
  characteristics nested within other quality characteristics; and
- for data: what causes each lifecycle transition, where a data attribute's
  value comes from, the sensitivity and purpose of personal data,
  specialization between entity types or value types, and an overall data
  model spanning entity types.
