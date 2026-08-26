---
type: Standard
title: Gen Stack application profile for OKF v0.2
description: The application profile for a durable human-authored corpus of cross-cutting system governance, Intent, Architecture, subject-colocated Requirements, and a discoverable System Evaluation Approach.
tags: [gen-stack, okf, application-profile, intent, architecture, requirements, evaluations, governance]
status: draft
sources:
  - id: gen-stack-vocabulary
    resource: ../glossary.md
    title: Gen Stack vocabulary and relationship model
  - id: okf-v0.2
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Open Knowledge Format v0.2
  - id: dcmi-application-profile
    resource: https://www.dublincore.org/resources/glossary/application_profile/
    title: DCMI definition of an application profile
  - id: iso-29148
    resource: https://www.iso.org/standard/72089.html
    title: ISO/IEC/IEEE 29148:2018 — Requirements engineering
  - id: iso-25010
    resource: https://www.iso.org/standard/78176.html
    title: ISO/IEC 25010:2023 — Product quality model
generated:
  by: codex/gpt-5
  at: 2026-08-26T13:07:31Z
---

# Gen Stack application profile for OKF v0.2

## Profile identity

| Property | Value |
| --- | --- |
| Profile identity | `gen-stack` |
| Profile version | `0.1.0` |
| Base specification | OKF v0.2 |
| Status | Draft |
| Applies to | The required root kernel, System Evaluation Approach, and admitted concepts under `intent/`, `architecture/`, and subject-colocated `requirements/` collections |
| Audience | Intent, requirements, architecture, and governance authors; maintainers; reviewers; and profile validators |

## Purpose and scope

This profile governs the durable, human-authored part of a Gen Stack:

- root concepts establish cross-cutting system context and governance;
- Intent preserves what outcomes matter and why;
- Requirements canonically express accepted obligations derived from Intent;
  and
- Architecture defines the eligible subjects those obligations shape; and
- the System Evaluation Approach makes the repository-native evaluation
  portfolio discoverable and explains how its evidence is navigated and
  reported.

The root is a scope boundary, not another semantic layer. `system.md` defines
the documented subject and context. `lifecycle.md`, `ownership.md`,
`decisions.md`, and `assurance.md` govern concerns that cut across Intent and
Architecture. Root placement expresses that cross-cutting scope; it does not
make these concepts containers for the other concepts.

Implementation and concrete Evaluation artifacts are peer authorities outside
this corpus contract. The repository owns code, configuration, schemas,
Evaluation Definitions, Suites, Executions, Results, Reports, and their exact
current organization. The corpus owns only the governed System Evaluation
Approach and navigation into those authorities. Signals, Observations, and
Evaluation Results are inputs and evidence in the operating loop. The
[Gen Stack vocabulary and relationship model](../glossary.md) defines their
relationships to governed concepts. This profile MUST NOT require corpus
`implementation/`, `feedback/`, `signals/`, or `observations/` collections or
place concrete evaluation artifacts in the corpus.

Requirements are canonicalized Intent. A Requirement is the sole normative
expression of one accepted obligation and is assigned to exactly one eligible
Architecture subject. Intent concepts may source a Requirement but MUST NOT be
its subject. Implementation and evaluation artifacts may repeat its predicate
for realization or assessment, but they do not acquire authority over the
obligation.

OKF defines the document envelope, path-derived identity, provenance,
lifecycle metadata, and ordinary links. This profile defines the exact governed
type usage, canonical paths, containment, relationship encodings, and
additional validation rules. The [Gen Stack vocabulary and relationship
model](../glossary.md) is normative for preferred terms, definitions,
distinctions, relationship identifiers, cardinalities, and prohibited
inferences. This human-readable profile is normative for representation and
profile conformance; supporting guides are explanatory.

A conforming corpus MUST be an OKF v0.2 bundle. Its root `index.md` MUST state
that it adopts and link `gen-stack` version `0.1.0`. This is an open-world
profile: other OKF concepts may coexist, but local conventions MUST NOT
redefine a governed type or waive a profile rule.

Profile conformance establishes representation conformance and conformance to
the semantic contracts this profile references. It does not establish corpus
coverage, completeness of requirements,
implementation satisfaction, evaluation coverage, or operational fitness.

## Conformance

Report three separate results when they are in scope:

1. **OKF conformance** — whether the bundle satisfies OKF v0.2.
2. **Profile conformance** — whether governed concepts satisfy this profile.
3. **Coverage or fitness assessment** — any separately bounded claim about
   completeness, satisfaction, evaluation coverage, or operation.

The third result is never implied by the first two. Missing evidence produces
`unknown`, not pass. Complete profile conformance combines executable
structural validation with a named manual semantic review.

A conforming corpus MUST contain the five required root concepts and the
System Evaluation Approach, use governed types at canonical paths, keep every
maintained concept reachable from the root, maintain one normative Requirement
authority per accepted obligation, and colocate each Requirement with its one
canonical Architecture subject.

## Common frontmatter

Every governed concept MUST include `type`, `title`, `description`, and
`status`. `status` MUST be `draft`, `stable`, or `deprecated`. `tags` are
recommended. Standard OKF `sources`, `generated`, `verified`, `stale_after`,
and `resource` fields may be used truthfully. OKF `status` describes the
knowledge document, not the system lifecycle or requirement acceptance state.

## Required cross-cutting kernel

The corpus root MUST contain these concepts:

| Path | Exact type | Responsibility |
| --- | --- | --- |
| `system.md` | `System` | Defines the documented subject, purpose, boundary, material exclusions, and important environmental relationships. It is the subject for genuinely system-wide Requirements. |
| `lifecycle.md` | `System Lifecycle` | Defines accepted support state, change horizon or expected evolution, and review triggers. |
| `ownership.md` | `System Ownership` | Defines stable maintenance accountability, stewardship boundary, and continuity, transfer, or escalation routes without copying volatile rosters. |
| `decisions.md` | `Architecture Decision Policy` | Defines which choices need ADRs, acceptance and supersession authority, record location and minimum content, and reconsideration triggers. |
| `assurance.md` | `System Assurance` | Defines required confidence, evidence authorities, review or approval, and reassessment triggers for architecture-significant change. |

These concepts are cross-cutting context and governance, not Requirement
subjects other than `System`. When lifecycle, ownership, decision, or assurance
governance contains an independently maintained binding obligation on system
development, operation, or governance, that obligation MUST be represented as
a `process` Requirement owned by an eligible Architecture subject, normally
System, and linked from the governance concept.

`decisions.md` owns decision governance. Individual accepted architecture
decisions are `Architecture Decision Record` concepts under
`architecture/decisions/`. `assurance.md` identifies the required evidence and
review model; evaluation definitions and results remain repository-native.

## System Evaluation Approach

The corpus MUST contain `evaluations/index.md` as navigation and
`evaluations/system-evaluation-approach.md` with exact type `System Evaluation
Approach`. The Approach is cross-cutting governance and discovery for one
documented System; it is not an Evaluation Definition, Suite, Result, Report,
or assurance decision.

Its body MUST use these sections and satisfy their contracts:

| Section | Minimum semantic contract |
| --- | --- |
| `## Scope and objectives` | Identifies the System and realized-state boundary, decisions supported, material exclusions, and relationship to System Assurance. |
| `## Evaluation portfolio` | Explains the methods, lifetimes, primary Evaluation Roles, evidence diversity, and route map to canonical repository-native Definitions, Suites, protocols, Executions, Results, and Reports. |
| `## Navigation and reporting` | Defines navigable projections by canonical Architecture subject and stable Requirement ID, with distinct reports for `requirement-satisfaction` and `architecture-realization`; other bounded claims are named. |
| `## Evidence and lifecycle` | Defines provenance, result statuses, treatment of `unknown` and harness errors, roll-up rules, stewardship, recency, and review triggers. |
| `## Gaps and maintenance` | Records material coverage gaps, unsupported conditions, stale or missing evaluators, and the route for repair without presenting absence as pass. |

The Approach MUST NOT require physical Suites or report stores to mirror an
Architecture tree. It MUST instead make current evidence navigable through
the canonical subject hierarchies and cross-view relationships. For maintained
Surfaces, this includes their recursive interaction hierarchy. For maintained
C4 elements, this includes Software System → Container → Component; C4 Views
remain projections and MUST NOT be treated as evaluation subjects. A claimed
covered Requirement is navigable through its stable ID and canonical subject.

## Intent

Intent captures desired outcomes, motivations, actor goals, interaction
scenarios, value, and problem-space distinctions. Governed Intent types are:

The type names below map to the same-named preferred terms and stable local
identifiers in the [Gen Stack vocabulary and relationship
model](../glossary.md). Their minimum contracts specify what a conforming
concept must record; they do not redefine those terms.

| Type | Minimum semantic contract | Canonical collection |
| --- | --- | --- |
| `Offering` | Coherent value made available, audiences and circumstances in scope, boundary, exclusions, and authority. | `intent/offerings/` |
| `Audience` | Durable group and circumstances, contextual roles, exclusions, and evidence for consequential segmentation. | `intent/audiences/` |
| `Need` | Solution-independent problem, constraint, opportunity, or desired outcome, affected audience and circumstances, exclusions, and evidence. | `intent/needs/` |
| `Job to Be Done` | Audience, progress sought, circumstances, forces, exclusions, and evidence without prescribing a solution. | `intent/jobs/` |
| `Value Proposition` | Offering, audience, need or job, promised benefit, recognizable value, limitations, and evidence without claiming achieved outcome. | `intent/value-propositions/` |
| `Use Case` | Interaction subject boundary, primary actor role, actor goal, successful outcome, technology-neutral scenario, and material extensions. | `intent/use-cases/` |
| `Subdomain` | Problem-space responsibility, important distinctions, exclusions, and classification rationale. | `intent/domains/{core|supporting|generic}/` |

Intent concepts may be `requirement_sources`. They MUST NOT be Requirement
subjects and MUST NOT contain a second binding `shall` formulation of an
admitted Requirement. A Use Case is a source and bridge to Architecture and
Evaluations, not a Requirement or exhaustive test inventory.

## Architecture

Architecture owns durable subjects, responsibilities, boundaries,
relationships, decisions, and response meaning.

### Architecture concepts

The governed Architecture concept types are:

The type names below map to the same-named preferred terms and stable local
identifiers in the [Gen Stack vocabulary and relationship
model](../glossary.md). Their minimum contracts specify what a conforming
concept must record; they do not redefine those terms.

| Type | Minimum semantic contract | Canonical collection |
| --- | --- | --- |
| `Architecture Decision Record` | One accepted durable choice, context, rationale, consequences, useful alternatives, and reconsideration or supersession conditions. | `architecture/decisions/` |
| `Capability` | Bearer and level, outcome-oriented ability, value, exclusions, and consequential decomposition or evidence. | `architecture/capabilities/` |
| `Feature` | Independently recognizable behavior, intended outcome, actors and conditions, durable cross-view identity, exclusions, and failure context. | `architecture/features/` |
| `Surface` | Actor-facing encounter point, actors, interaction boundary, recognizable behavior, exclusions, and consequential accessibility, trust, or operational concerns. | `architecture/surfaces/` |
| `Bounded Context` | Coherent model and language scope, authority, purpose, exclusions, and realization evidence. | `architecture/domains/contexts/` |
| `Context Map` | Contexts in scope, directional dependencies and translation boundaries, consistency and failure concerns, and architectural consequences. | `architecture/domains/context-maps/` |
| `C4 Software System` | Software boundary, value, responsibility, exclusions, direct interactors, and consequential relationships. | `architecture/structure/systems/` |
| `C4 Container` | Exactly one containing C4 Software System, application or data-store responsibility, runtime boundary, consequential technology, interactions, and exclusions. | `architecture/structure/containers/` |
| `C4 Component` | Exactly one owning C4 Container, cohesive responsibility, defined interface, dependencies, and exclusions. | beneath its owning Container |
| `C4 View` | Scope, primary question, consistently identified canonical elements, labeled interactions, technology, notation, and view-specific context. | `architecture/structure/views/` |

Capability, Feature, and Surface are complementary lenses. A Capability names
an ability, a Feature names recognizable behavior, and a Surface names where
an actor encounters behavior. A Surface may form a recursive interaction tree,
such as CLI → command → subcommand or web application → page → panel. This is
not C4 containment.

Subdomains remain Intent because they partition problem space. Bounded Contexts
and Context Maps are Architecture because they define model authority and
relationships. C4 Software Systems, Containers, and Components are structural
Architecture elements; C4 Views are projections. Containers do not contain
containers, and components do not recursively contain components.

### Requirements

`Requirement` is the sole governed type for the canonical accepted expression
of an obligation derived from Intent and assigned to one eligible Architecture
subject.

```yaml
---
type: Requirement
title: Failed installation preserves the workspace
description: A failed installation leaves no partial workspace changes.
status: stable
requirement_id: AXM-REQ-0061
requirement_type: functional
subject: /architecture/surfaces/cli/install.md
requirement_sources:
  - /intent/use-cases/install-an-extension.md
derived_from:
  - AXM-REQ-0014
---
```

Every Requirement MUST include a bundle-unique, never-reused
`requirement_id`; exactly one `requirement_type`; and exactly one bundle-relative
`subject` link. Its body MUST contain a `## Requirement` section with one
necessary, bounded, verifiable `shall` statement and a `## Rationale` section.
Within governed concepts, author-authored binding `shall` statements MUST occur
only there.

The six `requirement_type` values are:

| Value | Use for |
| --- | --- |
| `functional` | Required behavior, transformation, state transition, response, or service. |
| `quality` | Required degree or condition of system, product, service, use, or data quality. |
| `process` | Obligation on an accepted lifecycle, development, operational, or governance process. |
| `human-factors` | Obligation arising from human capabilities, limitations, safety, workload, cognition, or environment. |
| `usability` | Interaction-quality obligation concerning effective, efficient, learnable, or satisfying use. |
| `constraint` | Binding limitation on design, implementation, technology, interfaces, law, policy, or operating conditions. |

Verification technique does not determine type. Classify the primary accepted
meaning. An invariant is preservation semantics, not a seventh requirement
type.

`requirement_sources` may list bundle-relative non-Requirement concepts or
external URIs that explain origin. It is distinct from OKF `sources`, which
records document provenance. `derived_from` may list maintained parent
`requirement_id` values and MUST NOT form self-references or cycles. This
profile does not define `allocated_to`, `implemented_by`, `verified_by`,
`verification_methods`, `priority`, or `owner` fields.

A quality Requirement MUST include `quality_model`,
`quality_characteristic`, and `quality_subcharacteristic`. When
`quality_model` is `ISO/IEC 25010:2023`, the characteristic MUST be one of
`functional-suitability`, `performance-efficiency`, `compatibility`,
`interaction-capability`, `reliability`, `security`, `maintainability`,
`flexibility`, or `safety`, and the subcharacteristic MUST use the applicable
kebab-case English name from that standard.

### Eligible Requirement subjects

`subject` MUST resolve to exactly one maintained concept of type System,
Capability, Feature, Surface, Bounded Context, C4 Software System, C4 Container,
or C4 Component. Offering, Audience, Need, Job to Be Done, Value Proposition,
Use Case, Subdomain, Context Map, C4 View, ADR, governance concept, Requirement,
and index documents MUST NOT be subjects.

Choose the subject whose accepted responsibility is obligated. Do not use
System as a catch-all, place the Requirement beneath the Intent source, or
select a subject from current implementation location. If no eligible subject
exists, preserve the architecture gap for human decision rather than inventing
one.

## Canonical layout and colocation

```text
index.md
system.md
system/requirements/...
lifecycle.md
ownership.md
decisions.md
assurance.md
evaluations/
  index.md
  system-evaluation-approach.md
intent/
  offerings/
  audiences/
  needs/
  jobs/
  value-propositions/
  use-cases/
  domains/{core,supporting,generic}/
architecture/
  decisions/
  capabilities/
  features/
  surfaces/
  domains/contexts/
  domains/context-maps/
  structure/systems/
  structure/containers/
  structure/views/
```

The `evaluations/` collection is always required for its governed Approach.
Other collections exist only when they contain admitted concepts. Every present
collection has a navigational `index.md`. Plural catch-all concept documents
are prohibited.

Narrower Surfaces may use `architecture/surfaces/<surface>/<narrower>.md`.
Components use
`architecture/structure/containers/<container>/components/<component>.md`.
Canonical C4 View paths are:

```text
architecture/structure/views/system-landscape.md
architecture/structure/views/system-context.md
architecture/structure/views/containers.md
architecture/structure/views/components/<container>.md
architecture/structure/views/dynamics/<interaction>.md
architecture/structure/views/deployments/<environment>.md
architecture/structure/views/code/<component>.md
```

`Subdomain.classification` MUST be `core`, `supporting`, or `generic` and match
its directory. `C4 View.view_type` MUST be `system-landscape`,
`system-context`, `container`, `component`, `code`, `dynamic`, or `deployment`.

Requirements are placed in a same-named directory adjacent to their subject:

```text
<subject>.md
<subject>/
  requirements/
    index.md
    <requirement_type>/
      index.md
      <requirement>.md
```

The type-directory name MUST match `requirement_type`, and `subject` MUST match
the adjacent concept. Do not create empty subject, Requirement, or type
directories. Colocation expresses canonical ownership, not exclusivity.

## Relationship representation

The [Gen Stack vocabulary and relationship model](../glossary.md) owns the
canonical direction, domain, range, inverse reading, cardinality, recording
location, and inference boundaries of every controlled relationship. This
profile defines machine-readable encodings for only three of them in version
`0.1.0`:

| Vocabulary relationship | Profile encoding | Representation rule |
| --- | --- | --- |
| `requirement-source-is-source-of-requirement` | `requirement_sources` on the Requirement | A list of bundle-relative non-Requirement concept links or external URIs that preserve origin without transferring authority. |
| `requirement-has-subject` | `subject` on the Requirement plus subject-colocated placement | Exactly one bundle-relative link to an eligible Architecture subject; the adjacent path must resolve to the same subject. |
| `requirement-is-derived-from-requirement` | `derived_from` on the child Requirement | A list of maintained parent `requirement_id` values with no self-reference or cycle. |

Other controlled relationships use their vocabulary identifiers and meanings
in ordinary OKF links and prose or in generated views. This profile does not
introduce independent relationship definitions or additional relationship
frontmatter for them.

## Authority and maintenance

Intent owns desired outcomes and reasons. Requirements own accepted
obligations. Architecture owns durable response meaning. The corpus System
Evaluation Approach owns evaluation portfolio governance and discovery; the
repository owns Implementation and concrete Evaluation artifacts. Runtime and
observability systems own current operation and Observations. A passing test,
current code property, or runtime observation is evidence, not accepted
desired state by itself.

Each collection index states its grouping rule and links immediate concepts or
narrower collections. Every concept remains reachable from the root. A path
move changes OKF identity; update inbound links, generated consumers, and
`log.md` together.

## Validation

Run `scripts/validate-gen-stack-profile.py <corpus-root>` for mechanically
decidable profile rules. Also run the applicable OKF validator and a named
manual semantic review. Structural validation cannot establish correct Intent,
proper Requirement subject selection, completeness, satisfaction, coverage, or
fitness.
