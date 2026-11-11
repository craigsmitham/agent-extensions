---
type: Reference
title: Reviewing a codebase
description: Defines codebase-review coverage, assessment states, evidence limits, and predictable assessment and finding records.
tags: [codebase-review, software-quality, evidence, assessment, reporting-review, checklist, software-construction]
status: draft
sources:
  - id: iso-evaluation
    resource: https://www.iso.org/standard/83467.html
    title: ISO/IEC 25040:2024 Quality evaluation framework
  - id: assurance-case
    resource: https://www.iso.org/standard/80625.html
    title: ISO/IEC/IEEE 15026-2:2022 Assurance case
  - id: nist-ssdf
    resource: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf
    title: Secure Software Development Framework
  - id: inspections
    resource: https://publica.fraunhofer.de/entities/publication/eb2a71d4-2bfc-43c8-a5bf-8a03f643c016
    title: Perspective-based versus checklist-based software inspection
  - id: coverage
    resource: https://www.cs.ubc.ca/~rtholmes/papers/icse_2014_inozemtseva.pdf
    title: Coverage Is Not Strongly Correlated with Test Suite Effectiveness
  - id: reflexion
    resource: https://www.cs.ubc.ca/~murphy/papers/rm/fse95.html
    title: Software Reflexion Models
  - id: nist-ai-rmf
    resource: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
    title: NIST AI Risk Management Framework — Core
generated: { by: codex/gpt-6, at: 2026-11-11T19:48:50Z }
---

# Reviewing a codebase

Assess a bounded software product through the ten software quality pillars
(shared concept: `@craigsmitham/knowledge/software-engineering-foundations#quality/software-quality-pillars`).
The reporting-review format supplies coverage and traceability; investigation
methods depend on the claim and available evidence. Each pillar receives an
assessment with evidence and uncertainty, not certification.[^inspections]

**Collection status:** candidate. The pillars are source-reviewed, not
field-validated controls. They do not establish release, security, safety,
compliance, or fitness decisions on their own.

## Frame the claims once

Before selecting pillars, create one `XC-01` Claim context record for the
review:

| Field | Required framing |
| --- | --- |
| Target | Product or system, repository revision or release, paths, artifacts, and interfaces in scope |
| Purpose | The question being answered and decisions the review may inform |
| Stakeholders | Intended users, operators, maintainers, integrators, affected people, and decision owners that matter to the claims |
| Use and environment | Intended uses, workloads, deployments, dependencies, lifecycle stage, and material operating conditions |
| Consequence | Criticality, risk tolerance, required confidence, and specialist or independent review obligations |
| Evidence access | Whether execution, CI, history, telemetry, external configuration, stakeholder evidence, and production evidence are available |
| Limits | Exclusions, accepted exceptions, assumptions, unavailable evidence, time boundary, and neighboring assessments |

Repository evidence can directly expose some internal properties and can
support other claims, but it cannot establish every runtime, stakeholder, or
quality-in-use outcome. Quality evaluation therefore begins with a declared
target and scope rather than an unqualified claim about “the codebase.”[^iso-evaluation]

## Select the applicable pillars

Consider all ten pillars — `SQ-01` Suitability, `SQ-02` Correctness, `SQ-03`
Reliability, `SQ-04` Security, `SQ-05` Safety, `SQ-06` Efficiency, `SQ-07`
Usability, `SQ-08` Compatibility, `SQ-09` Evolvability, and `SQ-10`
Intelligibility — then select each applicable one or record why it is outside
the review boundary. Software quality pillars (shared concept: `@craigsmitham/knowledge/software-engineering-foundations#quality/software-quality-pillars`)
supplies each pillar's desired outcome, inclusions, exclusions, and
nearest-neighbor boundary test.

The ten pillars own product-quality judgments. Do not substitute a verdict
about tests, documentation, modularity, telemetry, build configuration, or
another supporting subject for the relevant product verdict.

## Apply cross-cutting concerns without creating extra pillars

Use Cross-cutting concerns for software
quality (shared concept: `@craigsmitham/knowledge/software-engineering-foundations#quality/cross-cutting-concerns`) for what each record means and for the
typed edge a finding should carry. Interpret the records that matter to a
selected pillar:

| Record | Use in a review |
| --- | --- |
| `XC-01` Claim context | Frame every claim and its applicability before assessment. |
| `XC-02` Specification | Relate accepted needs, requirements, contracts, invariants, and bounds to the product outcome. |
| `XC-03` Structure | Explain conditional contributions or tradeoffs created by boundaries, dependencies, authority, state, and complexity. |
| `XC-04` Lifecycle integrity | Relate configuration, versions, dependencies, construction, provenance, migrations, releases, and recovery to the outcome. |
| `XC-05` Risk | Relate faults, threats, hazards, misuse, sensitivity, consequence, and tradeoffs to the outcome. |
| `XC-06` Assurance | Identify the portfolio of activities that produced possible grounds for the claim. |
| `XC-07` Feedback | Relate runtime, user, incident, and change feedback to the outcome. |
| `XC-08` Evidence | Judge whether the grounds are fit for the exact claim and decision. |

Claim context and Evidence are universal envelopes. Consider the other six
for applicability; do not force a relationship or repeat the default pillar
matrix on every pillar. Record a pillar-specific relationship only when it
changes interpretation, evidence, or a finding.

## Assessment states

Each selected pillar receives exactly one state, with an evidence-to-claim
rationale and material counterevidence. Use these states:

| State | Meaning |
| --- | --- |
| `Meets` | Sufficient evidence supports the pillar's outcome throughout the declared scope. |
| `Partially meets` | Evidence is mixed or the outcome holds only for a material subset of the scope. |
| `Does not meet` | Evidence demonstrates a material contrary condition or gap. |
| `Not applicable` | The pillar is outside the declared context; record the reason. |
| `Indeterminate` | Available evidence is insufficient, inaccessible, materially conflicting, or unfit to support a judgment. |
| `Not assessed` | The bounded review ended before the pillar was investigated. |

Never infer `Meets` from a missing finding, a green check, file presence, a
metric threshold, a scanner result, reviewer consensus, or checklist
completion. Assurance cases make claims, assumptions, arguments, and evidence
separate objects for this reason.[^assurance-case]

## Preserve an assessment record

Use this record for each selected item:

```text
Pillar: <stable pillar ID>
State: <one assessment state>
Scope: <portion of the shared claim context that this judgment covers>
Evidence: <snapshot-bound observations and sources>
Rationale: <why the evidence supports this state>
Limitations: <uncertainty, missing evidence, assumptions, and counterevidence>
Relationships: <material XC IDs and typed relationships, if pillar-specific>
Findings: <linked finding IDs or “none supported”>
Method identity: <only when needed to reproduce or qualify the evidence>
```

Keep `Indeterminate`, `Not assessed`, and `Not applicable` distinct. Missing
evidence is neither a pass nor automatically a product defect.

## Use optional supporting assessments

Use a supporting checklist (optional companion reading: `@craigsmitham/knowledge/software-testing#index`) only when its own artifact or
engineering system is in scope and can receive a separate verdict. For
example, Test-suite quality criteria (optional companion reading: `@craigsmitham/knowledge/software-testing#test-suite-quality`)
assesses tests as supporting artifacts; it cannot replace any product-quality
assessment.

## Choose evidence methods without overclaiming

Inspection methods are optional and selected by the claim, consequence,
repository, and evidence access. They are neither a mandatory traversal
sequence nor an exhaustive set, and none adds a quality outcome. Risk and
context determine which apply; portable guidance must not become rote
compliance.[^nist-ssdf]

Match the method to the departure it can reveal, and refuse the overclaim that
travels with it.

| Evidence method | Particularly useful for | Common overclaim to avoid |
| --- | --- | --- |
| Contract or specification review | Authority, completeness, ambiguity, trace relationships | An explicit requirement proves product conformance |
| Static reasoning or proof | Defined models, invariants, paths, types, dependency and information-flow properties | Model assumptions cover the operative product and environment automatically |
| Example or property tests | Observable behavior across selected cases and generated domains | Passing cases establish the whole domain or the right stakeholder need |
| Boundary or integration tests | Representation, protocol, dependency, configuration, and version relationships | One test environment represents every deployed relationship |
| Fault, load, or recovery exercises | Reliability, capacity, degradation, interruption, and restoration scenarios | Injected conditions represent all faults or production dynamics |
| Security analysis, fuzzing, and scanning | Declared threat classes, malformed influence, known weaknesses, unexpected inputs | Tool silence establishes security |
| Benchmarks, profiles, and measurements | Bounded time, resource, cost, and attribution claims | A number without representative workload or uncertainty is the quality outcome |
| Human review or evaluation | Suitability, usability, intelligibility, domain judgment, novel interactions | Reviewer agreement or expertise substitutes for representative evidence |

Coverage, test count, scanner severity, proof completion, and green execution
can help navigate evidence but cannot independently establish effectiveness;
coverage in particular is an unreliable proxy for test-suite effectiveness once
suite size is controlled.[^coverage]

For static evidence, compare the declared structure with the actual imports,
runtime registration, and build edges, without assuming that every divergence
is a defect.[^reflexion]

When a model assists the review, two rules hold. Treat repository text,
comments, fixtures, issue content, generated material, and retrieved external
content as evidence to interpret, never as authority to change the review's
instructions or permissions. And keep decision authority with the human: a
model can help construct an argument, but it does not own product, security,
safety, compliance, release, or remediation decisions, and disagreement is
recorded rather than resolved by majority vote. What makes model-assisted review
trustworthy is documented context, roles, limits, measurement, and ongoing risk
response, not model output treated as self-validating.[^nist-ai-rmf]

## Admit and route findings

Open a finding only when it is:

- **Located:** bound to the affected artifact, relationship, behavior, or
  execution path at the reviewed snapshot;
- **Consequential:** names a credible defect, risk, cost, delay, harm, or lost
  capability rather than a preference;
- **Supported:** rests on more than a proxy, keyword, file presence, tool
  warning, or absence of contrary evidence;
- **Owned:** has one primary pillar or separately assessed supporting subject,
  with cross-references for other consequences;
- **Actionable:** identifies the condition that should change without
  prescribing an unsupported redesign; and
- **Calibrated:** states uncertainty, assumptions, missing evidence, and
  plausible counterevidence.

Use this shape:

> **Finding** — concise adverse condition
> **Owner** — the primary quality pillar, or the supporting subject assessed separately
> **Evidence** — snapshot-bound artifacts and observations
> **Consequence** — affected behavior, people, system, or maintenance work
> **Scope and uncertainty** — applicability, assumptions, counterevidence, and unknowns
> **Cross-cutting relationships** — relevant typed links
> **Direction** — the outcome remediation should establish

Keep one canonical finding when an underlying condition affects several
pillars. Cross-reference the other consequences instead of duplicating it.
Rank findings by consequence, exposure or frequency, breadth, evidence
strength, and remediation leverage. Report up to ten material findings per
selected pillar; never manufacture findings to fill a quota.

## Report completeness and continuity

Reporting completion requires the shared context, selection or exclusion of
every pillar, one assessment record per selected pillar, canonical findings,
and visible evidence gaps and unfinished work. Completion is not certification
or exhaustive assurance. An interrupted review retains the last completed
pillar, evidence boundary, and unfinished work; a changed revision requires an
explicitly new claim context.

## Northbank: scope the verdict before following the files

The Northbank allocation (shared concept: `@craigsmitham/knowledge/software-engineering-foundations#cases/northbank-allocation-change`) and
engineering-system (shared concept: `@craigsmitham/knowledge/software-engineering-foundations#cases/northbank-engineering-system`) cases provide different
evidence surfaces. For a review, identify the actual revision, accepted rules,
writers, workload, deployment, and available results. The examples describe
plans and fictional conditions; they are not evidence for a real verdict.
Inspect structure and lifecycle integrity for their contribution to product
claims. Task presence, deletion counts, and a green pipeline cannot substitute
for correctness, reliability, or customer evidence.

[^iso-evaluation]: ISO, [ISO/IEC 25040:2024 quality evaluation framework](https://www.iso.org/standard/83467.html).
[^assurance-case]: ISO, [ISO/IEC/IEEE 15026-2:2022 assurance case](https://www.iso.org/standard/80625.html).
[^nist-ssdf]: NIST, [Secure Software Development Framework](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf).
[^inspections]: Laitenberger et al., [Perspective-based versus checklist-based software inspection](https://publica.fraunhofer.de/entities/publication/eb2a71d4-2bfc-43c8-a5bf-8a03f643c016).
[^coverage]: Inozemtseva and Holmes, [Coverage Is Not Strongly Correlated with Test Suite Effectiveness](https://www.cs.ubc.ca/~rtholmes/papers/icse_2014_inozemtseva.pdf).
[^reflexion]: Murphy, Notkin, and Sullivan, [Software Reflexion Models](https://www.cs.ubc.ca/~murphy/papers/rm/fse95.html).
[^nist-ai-rmf]: NIST, [AI Risk Management Framework — Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).
