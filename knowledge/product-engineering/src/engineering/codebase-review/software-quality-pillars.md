---
type: Explainer
title: Software quality pillars
description: Defines the ten candidate product-quality outcomes used by codebase review — suitability through intelligibility — with each pillar's desired outcome, inclusions, exclusions, nearest-neighbor boundary tests, and applicability rules.
tags: [codebase-review, software-quality, quality-model, taxonomy, outcomes, pillar-boundaries, applicability, pe-engineering]
status: draft
sources:
  - id: dijkstra
    resource: https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html
    title: Notes on Structured Programming
  - id: hoare
    resource: https://sites.cs.ucsb.edu/~kemm/courses/cs266/acmhoare69.pdf
    title: An Axiomatic Basis for Computer Programming
  - id: parnas
    resource: https://www.cs.lafayette.edu/~gexia/cs301/resources/parnas.html
    title: On the Criteria To Be Used in Decomposing Systems into Modules
  - id: liskov-wing
    resource: https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf
    title: A Behavioral Notion of Subtyping
  - id: dependability
    resource: https://www.landwehr.org/2004-aviz-laprie-randell.pdf
    title: Basic Concepts and Taxonomy of Dependable and Secure Computing
  - id: protection
    resource: https://web.cs.wpi.edu/~cs557/f14/papers/saltzer1975_alt.html
    title: The Protection of Information in Computer Systems
  - id: slsa
    resource: https://slsa.dev/spec/v1.2/
    title: SLSA specification 1.2
  - id: nist-ssdf
    resource: https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-218.pdf
    title: NIST SP 800-218 Secure Software Development Framework 1.1
generated: { by: claude/opus-5, at: 2026-09-08T00:00:00Z }
---

# Software quality pillars

This concept proposes ten foundational quality outcomes for codebase review.
It is a research-grounded candidate taxonomy, not a universal model, scorecard,
or claim that software quality naturally has ten dimensions.

The design prioritizes conceptual coherence, peer-level boundaries, durable
meaning, and source support over familiar repository-review groupings.

Two companion concepts carry the rest of the argument.
[Quality layers outside the ten pillars](quality-layer-boundaries.md) explains
where testing, build reproducibility, delivery performance, observability, and
practitioner review systems belong instead.
[Research basis for the quality pillars](quality-pillar-research-basis.md)
records which historical models informed the synthesis, which alternatives were
rejected, and what remains unvalidated.

## Decision in brief

Use the repository as an **evidence surface** for judging the quality of a
software product. Keep the ten pillars at the **quality-outcome layer**:

| ID | Pillar | Core question |
| --- | --- | --- |
| `SQ-01` | Suitability | Does the product provide a complete and appropriate capability set for its intended needs and operating context? |
| `SQ-02` | Correctness | Does the product's behavior conform to its applicable contracts and preserve its declared invariants? |
| `SQ-03` | Reliability | Does required service remain dependable over time, faults, load, interruption, and recovery? |
| `SQ-04` | Security | Does the product preserve authorized protection of information, authority, identity, and operation against relevant threats? |
| `SQ-05` | Safety | Does the product keep the risk of unacceptable harm within its declared tolerances across use, misuse, failure, and integration? |
| `SQ-06` | Efficiency | Does required behavior meet its time, capacity, resource, and cost constraints for representative workloads? |
| `SQ-07` | Usability | Can intended users understand and operate the product to accomplish relevant goals with acceptable effort and error risk? |
| `SQ-08` | Compatibility | Does the product coexist and exchange meaning with required systems and environments without unacceptable interference? |
| `SQ-09` | Evolvability | Can the product accommodate required change over its lifetime without disproportionate risk, delay, or cost? |
| `SQ-10` | Intelligibility | Can qualified maintainers form an accurate, coherent, appropriately bounded mental model of the product? |

The names are singular semantic heads. Each can contain multiple subordinate
dimensions without becoming a compound pillar. The list order is for stable
reference, not priority.

## Assessment universe

The assessed entity is the **software product**, including its source,
configuration, data definitions, generated elements, and externally observable
behavior where they are in scope. The **repository** is the principal evidence
surface. It can expose internal product properties, intended contracts,
engineering history, and the systems used to construct and verify the product.

That distinction prevents three common overclaims:

- repository evidence can support but cannot alone establish every runtime or
  quality-in-use outcome;
- the presence of a test, scan, pipeline, metric, or document does not prove
  the quality it is intended to support; and
- a quality of the development or delivery system is not automatically a
  quality of the product.

If a future collection needs to assess the engineering system itself, give it
a separately named outcome model. Do not silently mix product qualities,
delivery performance, evidence quality, and development practices in one flat
set of ten.

## Pillar boundaries

Every pillar owns one desired product quality, not a review method or a bundle
of unrelated concerns.

### `SQ-01` — Suitability

**Desired outcome:** the product's capability set is complete and appropriate
for the intended stakeholders, goals, and operating context.

It includes missing, unnecessary, and ill-fitted capabilities. It excludes
whether implemented behavior faithfully conforms to an already accepted
contract; that belongs to correctness. Repository evidence may be insufficient
when stakeholder needs or real usage are unavailable.

### `SQ-02` — Correctness

**Desired outcome:** observable behavior conforms to applicable contracts, and
defined invariants hold across applicable conditions and state transitions.

It includes computations, control flow, data meaning, boundary behavior,
state, concurrency, and error semantics. It excludes whether the governing
contract is the right one. Proofs, tests, type checks, and review are evidence
mechanisms, not correctness itself. Dijkstra and Hoare ground correctness in
specification, assumptions, and reasoning rather than successful samples
alone.[^dijkstra][^hoare]

### `SQ-03` — Reliability

**Desired outcome:** the product delivers required service with acceptable
continuity and predictability across time, demand, faults, interruption, and
recovery.

It includes faultlessness, availability, tolerance, recoverability, and
bounded degradation. It excludes protection against adversaries and avoidance
of unacceptable harm as primary judgments. Dependability research is
especially useful here because it separates attributes, threats, and means
such as fault prevention, tolerance, removal, and forecasting.[^dependability]

### `SQ-04` — Security

**Desired outcome:** the product resists unauthorized or malicious action while
preserving the authorized confidentiality, integrity, authenticity,
accountability, and availability of relevant assets and operations.

It includes protection across trust boundaries and can include source-to-
artifact integrity when that chain is in product scope. Least privilege,
fail-safe defaults, complete mediation, signatures, scans, and provenance are
principles or evidence—not the outcome itself.[^protection][^slsa][^nist-ssdf]

### `SQ-05` — Safety

**Desired outcome:** product behavior keeps the risk of unacceptable harm
within declared tolerances.

It includes harm arising from intended use, reasonably foreseeable misuse,
failure, and integration. Safety can conflict with availability: stopping
service may be the safe result. It is context-dependent and may legitimately
be `Not applicable`, but hiding it inside reliability or security would erase
that distinct consequence.

### `SQ-06` — Efficiency

**Desired outcome:** the product delivers required behavior within justified
time, capacity, resource, and economic constraints.

It includes latency, throughput, capacity, computational work, memory,
storage, network use, and cost per useful result. A benchmark, profile, or
complexity metric is evidence about a bounded property, not efficiency as a
whole.

### `SQ-07` — Usability

**Desired outcome:** intended users can recognize, learn, control, and use the
product to achieve their relevant goals with acceptable effort and error risk.

It includes operability, learnability, inclusivity, assistance, and protection
from user error. It concerns the product's intended users, not maintainer
comprehension of source; the latter belongs to intelligibility. Its
applicability and evidence differ for an internal library, command-line tool,
public interface, and autonomous service.

### `SQ-08` — Compatibility

**Desired outcome:** the product coexists and exchanges meaning with required
systems and environments without unacceptable interference.

It includes interoperability, protocol and data agreement, coexistence, and
behavioral substitutability at shared boundaries. It excludes the future
capacity to adapt to a new environment, which belongs to evolvability. Static
type compatibility alone does not establish behavioral substitution.[^liskov-wing]

### `SQ-09` — Evolvability

**Desired outcome:** the product can accommodate required internal and
environmental change over its lifetime at sustainable risk, delay, and cost.

It includes modifiability, adaptability, installability, replaceability,
scalability, migration capacity, and sustainable dependency evolution.
Modular boundaries and information hiding are design contributors, while
change history and representative change exercises are evidence. Parnas shows
why the number of modules or a visually layered structure is not itself the
outcome.[^parnas]

### `SQ-10` — Intelligibility

**Desired outcome:** qualified maintainers can form an accurate, coherent, and
appropriately bounded mental model of the product's concepts, responsibilities,
behavior, and structure.

It includes conceptual integrity, comprehensibility, localized meaning, and
controlled accidental complexity. Naming, abstraction, documentation, and
module design are contributors. A small file, low cyclomatic-complexity value,
or absence of duplication is not sufficient evidence of intelligibility.

## High-risk boundary tests

Use these distinctions when a concern appears to fit more than one pillar.
Record cross-pillar consequences, but give the underlying condition one
canonical owner.

| Neighbors | Canonical distinction |
| --- | --- |
| Suitability / correctness | Suitability asks whether the accepted capability set addresses the right need; correctness asks whether behavior conforms to the accepted contract. |
| Correctness / reliability | Correctness is contract conformance for applicable behavior; reliability concerns continuity and recovery over time and faults. A consistently wrong result can be reliable. |
| Reliability / safety | Reliability favors continued required service; safety favors bounded harm and may require service to stop. |
| Reliability / security | Reliability includes accidental faults and service continuity; security includes adversarial action and authorization. Availability can be relevant to both, but the threat and claim differ. |
| Security / safety | Security protects authorized assets and operation against threats; safety bounds unacceptable harm regardless of whether its cause is malicious. |
| Efficiency / reliability | Efficiency owns resource and timing constraints; reliability owns continuity and recovery. Resource exhaustion can create a linked finding in both. |
| Suitability / usability | Suitability asks whether the product provides the needed capability; usability asks whether intended users can successfully operate it. |
| Usability / intelligibility | Usability concerns intended product users; intelligibility concerns qualified maintainers reasoning about the product. |
| Compatibility / correctness | Correctness owns conformance to the product's declared behavior; compatibility owns successful coexistence and exchange across an external relationship. |
| Compatibility / evolvability | Compatibility is fit with required present environments; evolvability is capacity to accommodate future change. |
| Evolvability / intelligibility | Evolvability is sustainable change capacity; intelligibility is accurate comprehension. Each contributes to the other but neither guarantees it. |

The pillars are related rather than statistically independent. Record
`contributes-to`, `evidences`, `threatens`, and `trades-off-with` relationships
instead of forcing every observation into a single causal story;
[Cross-cutting relationships to the quality pillars](cross-cutting-pillar-relationships.md)
defines those edge types.

## Applicability and use

Apply all ten as candidate questions, but allow `Not applicable`,
`Indeterminate`, and `Not assessed` as defined in
[Reviewing a codebase](reviewing-a-codebase.md). A reusable library, interactive
application, embedded controller, data pipeline, and network service will
produce different applicability and evidence profiles.

Do not publish a summed quality score. The pillars have no justified universal
weights, can conflict, and can have veto-like importance in particular
contexts. Record scope, stakeholder, scenario, evidence, uncertainty, and
cross-pillar tradeoffs with each judgment.

[^dijkstra]: Dijkstra, [Notes on Structured Programming](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html).
[^hoare]: Hoare, [An Axiomatic Basis for Computer Programming](https://sites.cs.ucsb.edu/~kemm/courses/cs266/acmhoare69.pdf).
[^parnas]: Parnas, [On the Criteria To Be Used in Decomposing Systems into Modules](https://www.cs.lafayette.edu/~gexia/cs301/resources/parnas.html).
[^liskov-wing]: Liskov and Wing, [A Behavioral Notion of Subtyping](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf).
[^dependability]: Avizienis, Laprie, Randell, and Landwehr, [Basic Concepts and Taxonomy of Dependable and Secure Computing](https://www.landwehr.org/2004-aviz-laprie-randell.pdf).
[^protection]: Saltzer and Schroeder, [The Protection of Information in Computer Systems](https://web.cs.wpi.edu/~cs557/f14/papers/saltzer1975_alt.html).
[^slsa]: SLSA, [Specification 1.2](https://slsa.dev/spec/v1.2/).
[^nist-ssdf]: NIST, [Secure Software Development Framework 1.1](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-218.pdf).
