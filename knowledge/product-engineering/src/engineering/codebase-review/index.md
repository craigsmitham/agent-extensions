# Codebase review

An outcome-centered, evidence-aware framework for reviewing a software product
through its repository and other available evidence. The ten pillar lists state
desired product qualities. Cross-cutting records preserve context,
specification, structure, lifecycle integrity, risk, assurance, feedback, and
evidence without turning methods or supporting artifacts into extra pillars.

The collection is a source-reviewed and design-reviewed candidate. It supports
bounded assessment and reporting; it does not certify product quality, release
readiness, security, safety, compliance, or fitness.

## Run a review

- [Reviewing a codebase](reviewing-a-codebase.md) - Use when a repository needs a bounded quality review; frame product claims, assess applicable pillar criteria, apply relevant cross-cutting concerns, and preserve evidence and uncertainty without treating checklist completion as assurance.

## The quality-outcome taxonomy

Read the pillar definitions first; the boundary and research concepts explain
what the ten deliberately exclude and why the set looks the way it does.

- [Software quality pillars](software-quality-pillars.md) - Defines the ten candidate product-quality outcomes used by codebase review — suitability through intelligibility — with each pillar's desired outcome, inclusions, exclusions, nearest-neighbor boundary tests, and applicability rules.
- [Quality layers outside the ten pillars](quality-layer-boundaries.md) - Explains where subqualities, supporting-artifact qualities, design principles, engineering-system capabilities, assurance mechanisms, and evidence properties belong once they are excluded from the ten product-quality pillars, using testing, reproducibility, delivery, observability, and a practitioner review system as worked routings.
- [Research basis for the quality pillars](quality-pillar-research-basis.md) - Records why the ten pillars depart from ISO/IEC 25010 and its predecessors, which alternative quality models were considered and rejected, what the synthetic design review settled, and which claims about the taxonomy remain unvalidated.

## The cross-cutting concern model

Four concepts, read in order: what qualifies as cross-cutting, what the eight
records mean, how they touch the pillars, and how the model itself is kept.

- [Cross-cutting concerns for software quality](cross-cutting-concerns.md) - Defines what makes a concern cross-cutting rather than an eleventh quality pillar, names the eight canonical records and their three presentation roles, and supplies the subject, role, and admission tests every candidate record must pass.
- [Cross-cutting concern records](cross-cutting-concern-records.md) - Definitions of the eight canonical cross-cutting records — claim context, specification, structure, lifecycle integrity, risk, assurance, feedback, and evidence — each with what it includes, what it excludes, and why it reaches across several quality pillars.
- [Cross-cutting relationships to the quality pillars](cross-cutting-pillar-relationships.md) - Supplies the seven directed relationship types that replace a bare "relates to" edge, the compact concern-by-pillar discovery matrix, and the placement of testing, testability, and test-suite quality across those edges.
- [Maintaining the cross-cutting concern model](cross-cutting-model-maintenance.md) - How the eight cross-cutting records should be stored, projected into views, trialled through classification, task, portability, and review-performance validation, and merged, split, or retired once observed use contradicts the current synthesis.

## Evolve and validate the collection

- [Maintaining codebase-review criteria](maintaining-codebase-review-criteria.md) - Use when adding, revising, evaluating, or retiring codebase-review criteria; preserve stable quality outcomes while evolving evidence aids, perspectives, and inspection methods independently.
- [Validating codebase-review criteria](validating-codebase-review-criteria.md) - Use when deciding whether the review criteria may carry stronger claims than candidate design coherence; design comparative trials, measure coverage and false assurance against bound conditions, read the existing design-review evidence for what it does not establish, and retire criteria that fail.
- [Codebase-review framework design review](framework-design-review.md) - Synthetic scenario and structural review of the ten-pillar outcome framework, its cross-cutting relationships, supporting test-suite assessment, and separation of criteria from review methods.

## Product-quality criteria

- [Product-quality criteria](criteria/) - Ten `reporting-review` checklists for
  judging desired qualities of the software product, with the working definition
  of a `reporting-review` checklist and the boundary between judging a product
  at a stated revision and sustaining the same outcomes in a running system.

These ten lists own product-quality judgments. Their order is stable reference,
not priority or weighting.

- [Suitability quality criteria](criteria/suitability.md) - Use when assessing whether the product's capability set is complete and appropriate for its intended stakeholder needs and operating context.
- [Correctness quality criteria](criteria/correctness.md) - Use when assessing whether product behavior conforms to applicable contracts and preserves declared invariants across relevant conditions and transitions.
- [Reliability quality criteria](criteria/reliability.md) - Use when assessing whether required service remains dependable through time, demand, faults, interruption, degradation, and recovery.
- [Security quality criteria](criteria/security.md) - Use when assessing whether the product preserves authorized protection of information, identity, authority, and operation against relevant threats.
- [Safety quality criteria](criteria/safety.md) - Use when assessing whether the product keeps the risk of unacceptable harm within declared tolerances across use, misuse, failure, and integration.
- [Efficiency quality criteria](criteria/efficiency.md) - Use when assessing whether required behavior meets applicable time, capacity, resource, and cost constraints under representative workloads.
- [Usability quality criteria](criteria/usability.md) - Use when assessing whether intended users can understand and operate the product to accomplish relevant goals with acceptable effort and error risk.
- [Compatibility quality criteria](criteria/compatibility.md) - Use when assessing whether the product can coexist and exchange meaning with required systems and environments without unacceptable interference.
- [Evolvability quality criteria](criteria/evolvability.md) - Use when assessing whether the product can accommodate required change over its lifetime without disproportionate risk, delay, or cost.
- [Intelligibility quality criteria](criteria/intelligibility.md) - Use when assessing whether qualified maintainers can form an accurate, coherent, and appropriately bounded mental model of the product.

## Supporting quality criteria

- [Supporting quality criteria](supporting/) - Checklists for subjects that can
  support a product-quality claim without being the software product, and the
  rule that a supporting verdict never substitutes for an applicable
  product-quality criterion.

- [Test-suite quality criteria](supporting/test-suite-quality.md) - Use when assessing automated tests as supporting artifacts; evaluate whether the suite provides valuable, sustainable, and appropriately bounded evidence for applicable product-quality claims.

## Review aids

- [Codebase-review aids](review-aids/) - Optional methods for locating,
  challenging, and interpreting evidence once a review has selected its
  criteria, with the rule for choosing which of them fit a given claim context.

These guides contain optional evidence and inspection methods. They do not add
quality criteria or prescribe one universal review sequence.

- [Repository evidence](review-aids/repository-evidence.md) - Use when locating and interpreting evidence across source, configuration, history, generated artifacts, and dependency relationships without treating proxies as findings.
- [Scenario analysis](review-aids/scenario-analysis.md) - Use when challenging product-quality claims with concrete stakeholder, workload, failure, threat, hazard, integration, and change scenarios.
- [Verification evidence](review-aids/verification-evidence.md) - Use when selecting and interpreting tests, analysis, proofs, scans, measurements, and reviews as evidence rather than product outcomes.
- [Runtime investigation](review-aids/runtime-investigation.md) - Use when a product-quality claim depends on execution, operational signals, representative workloads, degradation, interruption, or recovery.
- [Model-assisted review](review-aids/model-assisted-review.md) - Use when one or more frontier models assist a codebase review; preserve bounded claims, attributable evidence, counterevidence, uncertainty, and human decision authority.
