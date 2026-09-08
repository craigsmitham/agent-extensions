---
type: Explainer
title: Cross-cutting concern records
description: Definitions of the eight canonical cross-cutting records — claim context, specification, structure, lifecycle integrity, risk, assurance, feedback, and evidence — each with what it includes, what it excludes, and why it reaches across several quality pillars.
tags: [codebase-review, cross-cutting-concerns, claim-context, specification, structure, lifecycle-integrity, risk, assurance, feedback, evidence]
status: draft
sources:
  - id: iso-25030
    resource: https://www.iso.org/standard/72116.html
    title: ISO/IEC 25030:2019 Systems and software Quality Requirements and Evaluation — Quality requirements framework
  - id: iso-25040
    resource: https://www.iso.org/standard/83467.html
    title: ISO/IEC 25040:2024 Systems and software Quality Requirements and Evaluation — Quality evaluation framework
  - id: iso-25020
    resource: https://www.iso.org/standard/72117.html
    title: ISO/IEC 25020:2019 Systems and software Quality Requirements and Evaluation — Quality measurement framework
  - id: iso-15939
    resource: https://www.iso.org/standard/71197.html
    title: ISO/IEC/IEEE 15939:2017 Systems and software engineering — Measurement process
  - id: iso-15026-1
    resource: https://www.iso.org/standard/73567.html
    title: ISO/IEC/IEEE 15026-1:2019 Systems and software assurance — Concepts and vocabulary
  - id: iso-15026-2
    resource: https://www.iso.org/standard/80625.html
    title: ISO/IEC/IEEE 15026-2:2022 Systems and software assurance — Assurance case
  - id: sacm
    resource: https://www.omg.org/spec/SACM/2.3/About-SACM
    title: OMG Structured Assurance Case Metamodel 2.3
  - id: parnas
    resource: https://www.cs.lafayette.edu/~gexia/cs301/resources/parnas.html
    title: On the Criteria To Be Used in Decomposing Systems into Modules
  - id: atam
    resource: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
    title: Architecture Tradeoff Analysis Method collection
  - id: swebok
    resource: https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf
    title: Guide to the Software Engineering Body of Knowledge, Version 4.0
  - id: nist-ssdf
    resource: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf
    title: NIST SP 800-218 Secure Software Development Framework 1.1
  - id: slsa
    resource: https://slsa.dev/spec/v1.2/verifying-artifacts
    title: SLSA 1.2 — Verifying artifacts
  - id: nasa-assurance
    resource: https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398RevB.pdf
    title: NASA-STD-8739.8B Software Assurance and Software Safety Standard
  - id: ieee-1012
    resource: https://standards.ieee.org/ieee/1012/7324/
    title: IEEE 1012-2024 Standard for System, Software, and Hardware Verification and Validation
  - id: opentelemetry
    resource: https://opentelemetry.io/docs/concepts/signals/
    title: OpenTelemetry signals
  - id: google-sre
    resource: https://sre.google/sre-book/monitoring-distributed-systems/
    title: Google SRE — Monitoring Distributed Systems
generated: { by: claude/opus-5, at: 2026-09-08T00:00:00Z }
---

# Cross-cutting concern records

This concept defines the eight canonical records named in
[Cross-cutting concerns for software quality](cross-cutting-concerns.md). Each
definition states one semantic head, what the record includes, what it
excludes, and the mechanism by which it reaches across several
[quality pillars](software-quality-pillars.md). Read the typed edges in
[Cross-cutting relationships to the quality pillars](cross-cutting-pillar-relationships.md);
this concept supplies the meaning those edges connect.

## `XC-01` — Claim context

**Definition:** the declared conditions that give a quality claim its subject,
meaning, applicability, required confidence, and limits.

It includes the target entity and version; stakeholders and intended uses;
operating and integration environments; lifecycle stage; workloads and
scenarios; consequence and criticality; risk tolerance; assumptions;
exclusions; and the distinction among `Not applicable`, `Not assessed`, and
insufficient evidence. It excludes the content of the specification, the
method of review, and the evidence used to justify the verdict.

Claim context constrains every pillar. A codebase cannot by itself establish
whether a capability addresses the right stakeholder need, whether a workload
is representative, or how much assurance a safety-relevant decision requires.
Quality-requirements guidance is explicitly stakeholder- and purpose-aware and
does not prescribe one quality measure or development process.[^iso-25030]

## `XC-02` — Specification

**Definition:** the quality of the explicit intent, requirements, contracts,
invariants, bounds, and trace relationships that govern product judgments.

It includes functional and quality requirements; acceptance conditions;
interface and protocol contracts; data meaning; legal states; error and
recovery semantics; compatibility commitments; security and safety
constraints; and bidirectional traceability through changes and evidence. It
excludes whether the implemented product conforms, whether the requirement is
socially or commercially valuable, and any one notation or documentation
format.

Specification enables and can be evidence for every pillar, but only when the
specified claim is itself accepted and applicable. It is especially important
to preserve the difference between verifying conformance and validating
fitness for intended use. Current V&V guidance treats both as distinct reasons
for assessment and permits analysis, review, inspection, testing, and other
means.[^ieee-1012]

## `XC-03` — Structure

**Definition:** the discipline with which the product localizes changeable
decisions, responsibility, authority, state, dependency, and complexity into
coherent boundaries.

It includes information hiding; modular and package boundaries; cohesion and
coupling; dependency direction; interface size and stability; ownership of
state and effects; representation choices; concurrency boundaries; and
justified complexity. It excludes the product-level outcomes of
intelligibility and evolvability, prescriptive pattern catalogs, and
uncalibrated proxies such as file length or number of abstractions.

Structure can contribute to every pillar, but its effects are conditional and
tradeoff-bearing. A boundary that aids change can increase latency; isolation
that improves fault containment can complicate usability or deployment.
Parnas grounds modularity in hiding changeable design decisions, while ATAM
uses concrete scenarios to expose quality interactions and architectural
tradeoffs rather than assuming one structure is universally best.[^parnas][^atam]

## `XC-04` — Lifecycle integrity

**Definition:** the engineering system's ability to preserve the identity,
control, reproducibility, provenance, and recoverability of product states and
changes over time.

It includes configuration identification; dependency and toolchain
resolution; change control and status; reproducible construction; generated
artifact ownership; build and release lineage; source and artifact provenance;
migration, compatibility, and rollback paths; retirement; and recovery from a
partial lifecycle operation. It excludes the throughput of a delivery team,
the security or correctness of the resulting product, and a mandate for one
branching, packaging, or deployment method.

Configuration management is treated as a lifecycle knowledge area in SWEBOK,
while secure-development and supply-chain frameworks connect controlled
changes, protected artifacts, and verified provenance to security claims.[^swebok][^nist-ssdf][^slsa]
Those controls enable evidence and reduce threats; their presence does not
prove that a build is correct, safe, or suitable.

## `XC-05` — Risk

**Definition:** the explicit reasoning that connects uncertain faults,
threats, hazards, misuse, interactions, and tradeoffs to consequences and
declared tolerances.

It includes relevant failure and attack scenarios; hazard and abuse analysis;
fault propagation; exposure and consequence; uncertainty and sensitivity;
quality-attribute conflicts; risk acceptance; compensating controls; and
residual risk. It excludes the product-quality outcomes themselves, a generic
governance program, and a universal severity or probability scale.

Risk constrains and can threaten every pillar. It also prevents a review from
assuming that all desirable properties can be maximized at once. Assurance and
safety standards tailor rigor to consequence and integrity needs, and ATAM
elicits scenario-specific risks, sensitivity points, and tradeoffs.[^nasa-assurance][^ieee-1012][^atam]

## `XC-06` — Assurance

**Definition:** the proportionate portfolio of verification and validation
mechanisms used to produce grounds for believing applicable quality claims.

It includes tests, proofs, reviews, inspections, static and dynamic analysis,
benchmarks, simulations, security testing, safety analysis, operational
monitoring, audits, attestations, and appropriate independence or diversity.
It excludes the product quality being claimed, the intrinsic quality of each
supporting artifact, and the assumption that activity volume equals
confidence.

Assurance enables and produces potential evidence for every pillar. The
portfolio should respond to claim type, context, consequence, uncertainty, and
the failure modes of its own methods. Assurance-case standards make the
relationship explicit by connecting claims through argument and assumptions
to evidence, while SACM provides a shared model for representing those
relationships.[^iso-15026-1][^iso-15026-2][^sacm]

## `XC-07` — Feedback

**Definition:** the engineering system's ability to detect and interpret
product behavior and effects, connect them to decisions, and support timely
correction or learning.

It includes runtime observability and diagnosability; traces, metrics, logs,
profiles, and health signals; user and operator feedback; incident and defect
learning; change-impact feedback; escalation; and the latency and reach of
feedback loops. It excludes reliability itself, telemetry volume as a proxy
for insight, and a requirement that every product use production monitoring.

Feedback provides operational evidence across the pillars and especially
enables reliability, security, safety, evolvability, and intelligibility when
runtime behavior matters. OpenTelemetry distinguishes signals and their
correlation, while SRE guidance emphasizes actionable, symptom-oriented
monitoring and the cost of noisy signals.[^opentelemetry][^google-sre]

## `XC-08` — Evidence

**Definition:** the fitness of information to support a specific quality claim
and decision within a declared context.

It includes claim binding; relevance; construct validity; representativeness;
measurement reliability; provenance and integrity; scope and version
identity; freshness; independence; completeness; uncertainty; contradictory
results; and limitations. It excludes the assurance activity that generated
the information, the verdict it informs, and any assumption that a metric or
majority opinion is intrinsically authoritative.

Evidence governs judgments across every pillar. Measurement frameworks require
measures to answer stated information needs and explicitly address validity
and reliability.[^iso-15939][^iso-25020] Quality evaluation is a process for
declared target entities and does not supply a universal test method.[^iso-25040]
Therefore evidence can be strong, weak, conflicting, insufficient, or
inapplicable without silently changing the quality outcome being assessed.

[^iso-25030]: ISO, [ISO/IEC 25030:2019 quality requirements framework](https://www.iso.org/standard/72116.html).
[^iso-25040]: ISO, [ISO/IEC 25040:2024 quality evaluation framework](https://www.iso.org/standard/83467.html).
[^iso-25020]: ISO, [ISO/IEC 25020:2019 quality measurement framework](https://www.iso.org/standard/72117.html).
[^iso-15939]: ISO, [ISO/IEC/IEEE 15939:2017 measurement process](https://www.iso.org/standard/71197.html).
[^iso-15026-1]: ISO, [ISO/IEC/IEEE 15026-1:2019 assurance concepts and vocabulary](https://www.iso.org/standard/73567.html).
[^iso-15026-2]: ISO, [ISO/IEC/IEEE 15026-2:2022 assurance case](https://www.iso.org/standard/80625.html).
[^sacm]: OMG, [Structured Assurance Case Metamodel 2.3](https://www.omg.org/spec/SACM/2.3/About-SACM).
[^parnas]: Parnas, [On the Criteria To Be Used in Decomposing Systems into Modules](https://www.cs.lafayette.edu/~gexia/cs301/resources/parnas.html).
[^atam]: Software Engineering Institute, [Architecture Tradeoff Analysis Method collection](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/).
[^swebok]: IEEE Computer Society, [Guide to the Software Engineering Body of Knowledge, Version 4.0](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf).
[^nist-ssdf]: NIST, [Secure Software Development Framework 1.1](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf).
[^slsa]: SLSA, [Verifying artifacts](https://slsa.dev/spec/v1.2/verifying-artifacts).
[^nasa-assurance]: NASA, [Software Assurance and Software Safety Standard](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398RevB.pdf).
[^ieee-1012]: IEEE, [IEEE 1012-2024 Standard for System, Software, and Hardware Verification and Validation](https://standards.ieee.org/ieee/1012/7324/).
[^opentelemetry]: OpenTelemetry, [Signals](https://opentelemetry.io/docs/concepts/signals/).
[^google-sre]: Google, [Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/).
