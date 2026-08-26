# Gen Stack Update Log

## 2026-08-26

- **Bugs and corrective work**: Added [Bugs and bugfix
  specifications](work-items/bugs-and-bugfix-specifications.md) and [Writing
  bugfix specifications](work-items/writing-bugfix-specifications.md), defined
  Defect as a broad imperfection, Bug as concrete defective system behavior,
  kept Bugfix Specifications separate from provenance-bearing Defect reports,
  and gave their briefs distinct naming rules for observed discrepancies and
  authorized corrected behavior.
- **Specification vocabulary**: Defined Specification as a composition role
  whose constituents retain their canonical authority, distinguished its
  container from its content, defined Change Specification for bounded
  proposed or authorized system and Architecture change, and retained Bugfix
  Specification as its corrective specialization without requiring a new
  document type or corpus collection.
- **Change work items**: Replaced request-centered work-item guidance with
  [Change specifications and delivery
  work](work-items/change-specifications-and-delivery-work.md) and [Writing
  change specifications](work-items/writing-change-specifications.md), while
  keeping raw requests as Signals or source evidence until a candidate change
  has a recognizable boundary.
- **Change Design**: Defined Change Design as proportional technical reasoning
  for one bounded change, added guidance for developing it in conversation and
  capturing it in a work item, and deferred standalone repository documents
  until an explicit persistence lifecycle exists.
- **Profile simplification**: Retired the Just Enough Gen Stack pattern,
  corpus-organization guide, minimal-conformance reference, and synthetic
  example. The [Gen Stack vocabulary](glossary.md) remains the semantic
  authority, and the [Gen Stack application
  profile](profile/gen-stack-application-profile.md) remains the normative
  representation and conformance contract.
- **Control-loop cleanup**: Retired the redundant intent-to-feedback
  explanation, change-signal reconciliation guide, and change-signal Process.
  The [OODA control loop](control-loop/ooda-control-loop.md) retains the
  adaptive authority model, while [Analyzing Requirement
  impact](control-loop/analyzing-requirement-impact.md) retains bounded
  work-item intake guidance.
- **Action-document discovery**: Revised every Gen Stack Guide description to
  name the situation or intent that makes the guide relevant and the outcome
  it supports, then synchronized the descriptions into their enclosing
  indexes.
- **Process routing**: Required Process previews to expose their triggering
  condition and intended closing outcome, and kept Process triggers distinct
  from participant preconditions.
- **Work-item placement**: Promoted [Software work
  items](work-items/) from `control-loop/` to the top-level `work-items/`
  collection so durable case-record guidance remains distinct from OODA and
  from reusable Processes.
- **Principle and pattern collections**: Placed the [YAGNI
  principle](principles/yagni-and-speculative-complexity.md) and [Tidy First
  pattern](patterns/tidy-first.md) in distinct top-level `principles/` and
  `patterns/` collections.
- **Evaluation guidance consolidation**: Kept Evaluation identities and
  relationships in the [Gen Stack vocabulary](glossary.md), retained
  uncertainty and evaluator-failure handling in Signal reconciliation, and
  removed the redundant one-document `evaluations/` collection.
- **Pace and trust consolidation**: Expanded `Pace layer` and added `Trust
  gradient` in the [Gen Stack vocabulary](glossary.md), retained their
  application in OODA and bounded regeneration, and retired the underspecified
  standalone principle.
- **Process collection boundary**: Established top-level `processes/` for
  reusable Process definitions and authoring guidance, kept OODA and
  change-intake guidance in `control-loop/`, and gave principles and patterns
  distinct top-level collections.
- **Change-signal Process (retired)**: Defined `Reconcile a change signal` as
  a recommended standing Process for OODA reconciliation, then retired it
  during control-loop cleanup.
- **Adoption guide retirement**: Retired the standalone Gen Stack adoption
  ladder; the bundle overview retains its bounded-adoption guidance.
- **EARS requirement syntax**: Added an explanation of the Easy Approach to
  Requirements Syntax and a focused authoring guide for selecting, ordering,
  composing, and reviewing EARS clauses with synthetic Gen Stack examples.
- **Vocabulary authority**: Established the [Gen Stack vocabulary and
  relationship model](glossary.md) as the semantic authority for preferred
  terms, stable local identifiers, canonical relationship direction, domain,
  range, cardinality, recording location, and prohibited inference; narrowed
  the application profile to governed OKF representation, relationship
  encoding, and conformance.
- **Subject-first organization**: Reorganized the Knowledge bundle around the
  Gen Stack profile's semantic neighborhoods while keeping the bundle distinct
  from an instantiated profile corpus.
- **Cross-cutting governance**: Moved System, lifecycle, ownership, decision
  policy, and assurance authoring guidance into `governance/`.
- **Architecture colocation**: Replaced form-first Architecture `foundations/`
  and `guides/` shelves with Requirements, Decisions, Capabilities, Features,
  Surfaces, Domains, and C4 Structure collections.
- **Control-loop organization**: Consolidated OODA, feedback, Signal
  reconciliation, Process, and software work-item guidance under
  `control-loop/`.
- **Foundation retirement**: Colocated Requirement authority and Compaction
  with Architecture Requirements and Implementation respectively; removed the
  generic root `foundations/` collection.
- **Gen Stack profile 0.1.0**: Replaced the architecture-specific application
  profile with the clean `gen-stack` identity and canonical `intent/` and
  `architecture/` namespaces.
- **Cross-cutting root governance**: Defined System, Lifecycle, Ownership,
  Decision Policy, and Assurance as root-scoped context and governance rather
  than members of Intent or Architecture.
- **Repository-native peers**: Kept Implementation, Evaluations, Signals,
  Observations, Feedback, and results in the shared vocabulary and relationship
  model while excluding their artifact collections from the corpus profile.
- **Workflow identities**: Replaced the architecture-specific author, setup,
  and reconcile skills with `author-gen-stack`, `setup-gen-stack`, and
  `reconcile-gen-stack` without aliases or compatibility paths.
- **Process concept**: Defined Process as a distinct, bounded,
  outcome-oriented model of coordinated work, with explicit boundaries from
  work items, workflows, procedures, practices, Capabilities, Process
  Requirements, and OODA.
- **Process authoring**: Added [Defining a
  Process](processes/defining-a-process.md), including an adaptable
  process-definition template for value, authority, events, activities,
  resources, work-item participation, measures, and views.
- **Process provenance**: Recorded the Business Process Manifesto as a
  conceptual source for an original Gen Stack synthesis without reproducing
  its text, worksheet, or diagram.
- **Knowledge consolidation**: Moved the complete software-architecture and
  software-engineering corpora, architecture profile validator, synthetic
  example, work-item guidance, YAGNI principle, and Tidy First pattern into Gen
  Stack as one canonical, locally cross-referenced knowledge authority.
- **Package retirement**: Removed the legacy project-authored pack and
  knowledge package roots after preserving their published-version migration
  guidance in the Gen Stack pack and their source history in version control.
- **License continuity**: Changed Gen Stack knowledge to CC-BY-SA-4.0 to
  preserve the reciprocal licensing of the consolidated knowledge packages.
- **OODA control model**: Adopted Observe, Orient, Decide, and Act as the
  adaptive control loop governing learning and repair across Gen Stack
  authorities without making them additional artifact layers.
- **Signal and Observation boundary**: Defined Signals as indications requiring
  attention and Observations as contextual evidence, both outside
  human-oriented Intent.
- **Self-healing flow**: Reorganized signal reconciliation around evidence-bound
  Orientation, an authorized repair hypothesis, bounded Action as a test, and
  closure evidence returned to Observe.
- **Attribution**: Recorded John R. Boyd's *The Essence of Winning and Losing*
  as the source of the adapted OODA semantics without reproducing its briefing
  or diagram.

## 2026-08-25

- **Update**: Defined Requirements as canonical accepted obligations derived
  from Intent and assigned to exactly one eligible Architecture subject;
  removed Offering and every other Intent concept from the subject set.
- **Update**: Removed raw Intent as a direct Compilation input and replaced the
  ambiguous `Compilation targets Architecture` wording with Architecture
  constraining Compilation into Implementation Units.
- **Update**: Replaced Realization as a peer-layer noun with Implementation,
  split Evaluation into Definition, Execution, and Result throughout the
  feedback loop, and standardized replacement scope on Implementation Unit.
- **Update**: Revised signal reconciliation as human-governed self-healing that
  repairs the first incoherent authority, establishes a missing Architecture
  subject before Requirement placement, and preserves human gates for accepted
  meaning.
- **Update**: Added a controlled relationship model to the [Gen Stack glossary](glossary.md), with canonical directions, derived inverse readings, cardinalities, authoritative recording locations, and prohibited inferences across authority, realization, evidence, and architecture views.
- **Update**: Clarified Compilation as the transformation that produces an
  Implementation, Architecture and its Requirements as the mostly human-authored
  constraining contract, and Implementation as the materialized output.
- **Update**: Added Evaluation, Evaluation Definition, Evaluation Execution, and Evaluation Result as a top-level glossary section between Architecture and Implementation, preserving Evaluation as a peer authority rather than part of Architecture.
- **Update**: Moved Subdomain under Intent in the [Gen Stack glossary](glossary.md) as a problem-space concept while retaining Bounded Context and Context Map under Architecture as model-authority and relationship concepts.
- **Update**: Reorganized the [Gen Stack glossary](glossary.md) around Intent, Architecture with subject-colocated Requirements, Implementation, and the Gen Stack method, and defined Implementation and Implementation Unit without introducing a separate grain concept.
- **Update**: Expanded the [Gen Stack glossary](glossary.md) to cover the then-governed architecture-profile concept types, grouped Value concepts flat under Intent, and documented the eligible Requirement subjects. This predates the clean `gen-stack` profile.
- **Addition**: Added the [Gen Stack glossary](glossary.md), a minimal reference for the method's load-bearing terms, actor-facing Surfaces, and governed C4 architecture concepts.
- **Addition**: Added a human-governed change-signal diagnostic and
  repair-recommendation flow, later retired during control-loop cleanup.
- **Creation**: Established the Gen Stack method, its authority and evidence boundaries, Requirement-impact workflow, evaluation semantics, bounded-regeneration guidance, and adoption ladder.
