---
type: Explainer
title: Research basis for the quality pillars
description: Records why the ten pillars depart from ISO/IEC 25010 and its predecessors, which alternative quality models were considered and rejected, what the synthetic design review settled, and which claims about the taxonomy remain unvalidated.
tags: [codebase-review, software-quality, quality-model, research, alternatives, iso-25010, mccall, boehm, furps, dromey, validation, pe-engineering]
status: draft
sources:
  - id: mccall
    resource: https://www.scribd.com/document/418348872/Factors-in-Software-Quality-Concept-and-Definitions-of-Software-Quality-Jim-A-McCall-Paul-K-Richard-Gene-F-Walters
    title: Factors in Software Quality — Volume I, Concept and Definitions of Software Quality
  - id: iso-25010
    resource: https://www.iso.org/standard/78176.html
    title: ISO/IEC 25010:2023 Systems and software Quality Requirements and Evaluation — Product quality model
  - id: iso-25010-preview
    resource: https://www.en-standard.eu/publicdoc/iec_previews/3440529.pdf
    title: ISO/IEC 25010:2023 public preview
  - id: iso-9126
    resource: https://www.iso.org/standard/22749.html
    title: ISO/IEC 9126-1:2001 Software engineering — Product quality — Part 1, Quality model
  - id: boehm
    resource: https://citeseerx.ist.psu.edu/document?doi=b79adbdb51a0be5f9d9fdbf731bc31d1ff43747d&repid=rep1&type=pdf
    title: Quantitative Evaluation of Software Quality
  - id: furps
    resource: https://public.dhe.ibm.com/software/rational/docs/v2003/unix_solutions/pdf/reqpro/reqpro_user.pdf
    title: IBM Rational RequisitePro User's Guide
  - id: dromey
    resource: https://research-repository.griffith.edu.au/bitstream/10072/15682/1/3476.pdf
    title: A Model for Software Product Quality
  - id: dijkstra
    resource: https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html
    title: Notes on Structured Programming
  - id: hoare
    resource: https://sites.cs.ucsb.edu/~kemm/courses/cs266/acmhoare69.pdf
    title: An Axiomatic Basis for Computer Programming
  - id: parnas
    resource: https://www.cs.lafayette.edu/~gexia/cs301/resources/parnas.html
    title: On the Criteria To Be Used in Decomposing Systems into Modules
  - id: brooks
    resource: https://soloway.pbworks.com/f/The.Mythical.Man.Month.F.Brooks.pdf
    title: The Mythical Man-Month — Essays on Software Engineering, Anniversary Edition
  - id: lehman
    resource: https://users.ece.utexas.edu/~perry/education/SE-Intro/lehman.pdf
    title: Programs, Life Cycles, and Laws of Software Evolution
  - id: dependability
    resource: https://www.landwehr.org/2004-aviz-laprie-randell.pdf
    title: Basic Concepts and Taxonomy of Dependable and Secure Computing
  - id: dora
    resource: https://dora.dev/guides/dora-metrics/
    title: DORA software delivery performance metrics
generated: { by: claude/opus-5, at: 2026-09-08T00:00:00Z }
---

# Research basis for the quality pillars

The [ten quality pillars](software-quality-pillars.md) are a design synthesis.
This concept records what that synthesis drew on, what it rejected, what its
design review settled, and what it still cannot claim. Read it before arguing
that a pillar should be added, merged, or renamed.

## Why this is a synthesis, not a vote

Influential models repeatedly recognize behavioral fitness, dependability,
resource efficiency, human interaction, environmental fit, protection, and
change capacity. They do not agree on assessment subject, hierarchy, or the
status of testing, portability, security, and constraints.

| Model | Organizing idea | Category lesson for this taxonomy |
| --- | --- | --- |
| McCall | Product operation, revision, and transition | A lifecycle grouping does not prove that every named factor is an independent peer.[^mccall] |
| Boehm | General utility decomposed through present use, maintenance, and portability | A hierarchy helps relate qualities but does not validate weights or an aggregate score.[^boehm] |
| FURPS/FURPS+ | Requirements classes plus design, implementation, interface, and physical constraints | Required behavior, qualities, and imposed constraints must not be flattened into one quality list.[^furps] |
| Dromey | Concrete product properties carry or contribute to higher-level qualities | Reviewable structures should be related to outcomes rather than mistaken for them.[^dromey] |
| ISO/IEC 9126 | Six product characteristics plus a separate quality-in-use model | Security, safety, testability, and portability have changed level across generations of the model.[^iso-9126] |
| ISO/IEC 25010:2023 | Nine product characteristics with subordinate characteristics | A current reference model is a strong anchor, but it remains tailorable and does not establish that nine is the natural number.[^iso-25010][^iso-25010-preview] |

The candidate starts from ISO/IEC 25010:2023's product-quality scope, then
makes three source-supported changes:

1. It separates **suitability** from **correctness**. A product can implement a
   stated contract correctly while the contract is incomplete or inappropriate
   for the intended need. Hoare explicitly distinguishes satisfying a formal
   specification from accomplishing the user's intention.[^hoare]
2. It groups maintainability and flexibility beneath **evolvability**, the
   singular capacity to accommodate change over the product's lifetime.
   Lehman's work makes continuing change intrinsic for software coupled to a
   changing environment.[^lehman]
3. It recognizes **intelligibility** separately from change capacity. Dijkstra,
   Parnas, and Brooks treat manageable structure, comprehensibility, and
   conceptual integrity as direct goods rather than only as proxies for the
   cost of a future edit.[^dijkstra][^parnas][^brooks]

These are design judgments informed by the sources. They are not categories
asserted by ISO or a consensus result from counting appearances in historical
models.

## Alternatives deliberately not selected

| Alternative | Strength | Reason not selected for the candidate |
| --- | --- | --- |
| Adopt ISO/IEC 25010:2023 unchanged | Current, recognized, and already hierarchical | It does not make the need-versus-contract distinction explicit, and its treatment of comprehension remains subordinate to maintainability. |
| Use dependability as an umbrella | Compact treatment of reliability, safety, integrity, availability, and maintainability | It is too broad beside the other proposed pillars and would create parent-child overlap with security and reliability.[^dependability] |
| Make testability or verifiability a pillar | Keeps assurance highly visible | It mixes an assurance affordance with the desired product qualities that assurance supports. |
| Make reproducibility a pillar | Makes modern repository construction risk explicit | It changes the assessed subject from the software product to the construction system and still does not establish authenticity or correctness. |
| Make delivery capability a pillar | Recognizes that repository changes must reach use safely | It is a quality of the delivery system and combines throughput with instability unless carefully decomposed.[^dora] |
| Make observability a pillar | Reflects distributed operational practice | Instrumentation is an enabler; diagnosability is a narrower contributor to reliability and evolvability. |
| Organize around repository topics | Retains familiar review lenses | The topics mix outcomes, principles, enablers, mechanisms, and compound subjects. |

These alternatives can become separate engineering-system, assurance, or
domain-extension collections. Their exclusion from the ten is a boundary
decision, not a judgment that they are unimportant. Where each excluded subject
belongs instead is stated in
[Quality layers outside the ten pillars](quality-layer-boundaries.md).

## Current disposition

The framework refactor proceeded after its synthetic design review addressed
these conditions:

- accepted the product-versus-engineering-system boundary;
- confirmed that each pillar can receive one meaningful judgment without
  depending on another pillar's verdict;
- challenged the definitions with representative library, service,
  interactive, data-processing, safety-relevant, and multi-package scenarios;
- classified a sample of findings without persistent overlap or missing
  outcome families;
- agreed that supporting principles, enablers, mechanisms, and evidence remain
  discoverable after leaving the top-level ten;
- accepted or revised the typed cross-cutting-concern model used to preserve
  those relationships without creating additional product pillars;
- confirmed that Test Desiderata and pstack concerns can be routed without
  promoting test artifacts, workflow rules, or code-shape heuristics into
  product-quality pillars; and
- recorded unresolved tradeoffs and domain-specific extensions rather than
  hiding them in compound criteria.

The [Codebase-review framework design
review](framework-design-review.md) records the scenario and boundary trials,
revisions, and unresolved risks. It supports candidate design coherence only;
comparative repository and reviewer trials remain required before claims of
effectiveness or stability.

## Research limits and lifecycle

This synthesis used influential historical models, foundational primary works,
and current authoritative engineering-system sources. Public access to the
full normative ISO texts and the original FURPS publication was unavailable;
the detailed ISO category review used a public preview, and FURPS used IBM's
Rational descendant documentation. Similar labels across sources were not
treated as proof of equivalent meaning.

No located source establishes that these ten pillars are independent,
collectively exhaustive, or optimal for repository review. The cardinality of
ten is an editorial constraint. The candidate remains `status: draft` until
classification trials establish that its boundaries improve review coverage
and agreement without concealing material concerns; the trial design is in
[Validating codebase-review criteria](validating-codebase-review-criteria.md).

[^iso-25010]: ISO, [ISO/IEC 25010:2023 product quality model](https://www.iso.org/standard/78176.html).
[^iso-25010-preview]: ISO/IEC, [ISO/IEC 25010:2023 public preview](https://www.en-standard.eu/publicdoc/iec_previews/3440529.pdf).
[^iso-9126]: ISO, [ISO/IEC 9126-1:2001 lifecycle page](https://www.iso.org/standard/22749.html).
[^mccall]: McCall, Richards, and Walters, [Factors in Software Quality, Volume I](https://www.scribd.com/document/418348872/Factors-in-Software-Quality-Concept-and-Definitions-of-Software-Quality-Jim-A-McCall-Paul-K-Richard-Gene-F-Walters).
[^boehm]: Boehm, Brown, and Lipow, [Quantitative Evaluation of Software Quality](https://citeseerx.ist.psu.edu/document?doi=b79adbdb51a0be5f9d9fdbf731bc31d1ff43747d&repid=rep1&type=pdf).
[^furps]: IBM Rational, [RequisitePro User's Guide](https://public.dhe.ibm.com/software/rational/docs/v2003/unix_solutions/pdf/reqpro/reqpro_user.pdf).
[^dromey]: Dromey, [A Model for Software Product Quality](https://research-repository.griffith.edu.au/bitstream/10072/15682/1/3476.pdf).
[^dijkstra]: Dijkstra, [Notes on Structured Programming](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html).
[^hoare]: Hoare, [An Axiomatic Basis for Computer Programming](https://sites.cs.ucsb.edu/~kemm/courses/cs266/acmhoare69.pdf).
[^parnas]: Parnas, [On the Criteria To Be Used in Decomposing Systems into Modules](https://www.cs.lafayette.edu/~gexia/cs301/resources/parnas.html).
[^brooks]: Brooks, [The Mythical Man-Month, anniversary edition](https://soloway.pbworks.com/f/The.Mythical.Man.Month.F.Brooks.pdf).
[^lehman]: Lehman, [Programs, Life Cycles, and Laws of Software Evolution](https://users.ece.utexas.edu/~perry/education/SE-Intro/lehman.pdf).
[^dependability]: Avizienis, Laprie, Randell, and Landwehr, [Basic Concepts and Taxonomy of Dependable and Secure Computing](https://www.landwehr.org/2004-aviz-laprie-randell.pdf).
[^dora]: DORA, [Software delivery performance metrics](https://dora.dev/guides/dora-metrics/).
