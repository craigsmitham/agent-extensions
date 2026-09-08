---
type: Explainer
title: Quality layers outside the ten pillars
description: Explains where subqualities, supporting-artifact qualities, design principles, engineering-system capabilities, assurance mechanisms, and evidence properties belong once they are excluded from the ten product-quality pillars, using testing, reproducibility, delivery, observability, and a practitioner review system as worked routings.
tags: [codebase-review, software-quality, quality-layers, testability, test-suite-quality, reproducible-builds, delivery-performance, observability, pstack]
status: draft
sources:
  - id: testing-theory
    resource: https://archiv.infsec.ethz.ch/intranet_secured/Y/w/GG75.pdf
    title: Toward a Theory of Test Data Selection
  - id: test-desiderata
    resource: https://testdesiderata.com/
    title: Test Desiderata
  - id: reproducible-builds
    resource: https://reproducible-builds.org/docs/definition/
    title: Reproducible Builds — Definitions
  - id: slsa
    resource: https://slsa.dev/spec/v1.2/
    title: SLSA specification 1.2
  - id: nist-ssdf
    resource: https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-218.pdf
    title: NIST SP 800-218 Secure Software Development Framework 1.1
  - id: dora
    resource: https://dora.dev/guides/dora-metrics/
    title: DORA software delivery performance metrics
  - id: google-sre
    resource: https://sre.google/sre-book/effective-troubleshooting/
    title: Google SRE — Effective Troubleshooting
  - id: pstack
    resource: https://github.com/cursor/plugins/tree/main/pstack
    title: Cursor plugins — pstack
  - id: pstack-review
    resource: https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/references/code-quality-review.md
    title: pstack — Code Quality Review
  - id: pstack-rubric
    resource: https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/references/rubric.md
    title: pstack — Review Rubric
  - id: pstack-tdd
    resource: https://github.com/cursor/plugins/blob/main/pstack/skills/tdd/SKILL.md
    title: pstack — TDD Bug Fix
generated: { by: claude/opus-5, at: 2026-09-08T00:00:00Z }
---

# Quality layers outside the ten pillars

The [ten quality pillars](software-quality-pillars.md) deliberately exclude
most of what a review actually looks at. This concept states where the excluded
material goes, so that testing, build reproducibility, delivery capability,
observability, and authored review systems remain discoverable without being
promoted into product-quality outcomes.

## Keep supporting layers outside the ten

The review collection still needs more than ten documents. It should organize
supporting knowledge by role rather than promote every useful topic to a
quality pillar. [Cross-cutting concerns for software
quality](cross-cutting-concerns.md) is the canonical model for classifying
those subjects and roles, deciding whether they genuinely cross the pillar
decomposition, and recording their conditional relationships. The table below
is a summary of the boundary established there.

| Layer | Question answered | Examples |
| --- | --- | --- |
| Quality outcome | What desirable state should the product possess? | The ten pillars |
| Subquality | Which narrower dimension constitutes an outcome? | Availability, recoverability, authenticity, learnability, modifiability |
| Supporting-artifact quality | What desirable state should a specification, test suite, model, or other supporting artifact possess? | Test-suite value, specification clarity, model consistency |
| Design principle | What rule tends to create or preserve qualities? | Abstraction, information hiding, behavioral substitutability, least privilege |
| Engineering-system capability | What durable ability helps construct, change, deliver, operate, or learn from the product? | Dependency control, deterministic builds, task graphs, delivery automation, telemetry instrumentation |
| Assurance mechanism | What produces grounds for believing a quality claim? | Tests, proofs, reviews, static analysis, benchmarks, monitoring, attestations |
| Evidence property | What makes those grounds usable for this judgment? | Relevance, validity, provenance, freshness, scope binding, integrity, sufficient completeness |

This separation is not a demotion of testing, modular design, build coherence,
or observability. It lets each support every quality it actually informs
without pretending to be the quality outcome itself. Testing theory, for
example, treats test selection and adequacy as grounds for claims; it does not
make “tests exist” a product-quality result.[^testing-theory]

The test suite is also an artifact that can have quality outcomes of its own.
Test Desiderata names isolated, composable, deterministic, fast, writable,
readable, behavioral, structure-insensitive, automated, specific, predictive,
and confidence-inspiring tests, and makes the tradeoffs among them explicit.[^test-desiderata]
Those are valuable inputs to a **test-suite quality** checklist. They do not
turn testing into a product-quality pillar, and they should not be collapsed
into product testability. The distinction is:

```text
product testability    = how readily product qualities can be investigated
test-suite quality     = how valuable and sustainable the tests are as evidence
product quality        = what the resulting evidence is intended to justify
```

No single desideratum is sufficient. A fast, deterministic test can be
irrelevant; a predictive test can be too slow or expensive for frequent use.
The separate [Test-suite quality
criteria](supporting/test-suite-quality.md) preserves those tradeoffs rather
than scoring all properties as though they could be maximized simultaneously.

Modern repository concerns fit the same model:

- **construction reproducibility** is an outcome of the construction system
  and an assurance aid when independently rebuilt artifacts are compared; it
  does not prove that the source is benign;[^reproducible-builds]
- **supply-chain provenance** and attestations can support security claims, but
  their existence does not establish authorized, untampered construction;[^slsa][^nist-ssdf]
- **delivery performance** is an engineering-system outcome measured at an
  application or service scope, not a product-quality pillar;[^dora]
- **telemetry instrumentation** enables runtime evidence, while diagnosability
  contributes to reliability and evolvability without being synonymous with
  either;[^google-sre] and
- **evidence quality** is a cross-cutting evidence property unless the
  evidence system itself is the declared object of review.

## Practitioner-source check

The pstack plugin is a useful contemporary practitioner datapoint because it
bundles a review rubric, code-quality lens, design principles, verification
methods, and operating playbooks in one public artifact.[^pstack][^pstack-review][^pstack-rubric]
Its content reinforces the need for typed layers more than it argues for a
different product-quality taxonomy:

| pstack concern | Classification here | Candidate destination |
| --- | --- | --- |
| Correctness and security findings | Product-quality outcomes | Correctness and security pillars |
| User experience | Desired product result and decision perspective | Suitability and usability pillars |
| Reader load and structural simplicity | Product property plus design heuristics | Intelligibility, with evolvability consequences |
| Domain modeling, boundary discipline, type discipline, idempotency, and deletion | Design principles | Contributor guidance linked to correctness, reliability, evolvability, and intelligibility |
| Root-cause analysis and TDD | Inspection or change methods | Optional method aids, selected when their preconditions hold[^pstack-tdd] |
| Direct artifact checks and regression evidence | Assurance mechanisms and evidence practice | Shared assurance layer |
| Multi-model adversarial review and lead synthesis | Review protocol | Assessment method, not a quality criterion |
| File-size, indirection, and diff-size thresholds | Contextual heuristics or proxies | Evidence aids requiring calibration, never sufficient proof |

pstack is an authored operating system for agent-assisted engineering, not a
formal or empirically validated software-quality model. Its strongest value to
this work is practitioner coverage and concrete examples of principles,
methods, and proxies that should remain discoverable after they leave the
pillar layer. Its use of a line-count threshold and intentionally forceful
review posture also demonstrates why contextual heuristics should not become
timeless outcome criteria.

[^testing-theory]: Goodenough and Gerhart, [Toward a Theory of Test Data Selection](https://archiv.infsec.ethz.ch/intranet_secured/Y/w/GG75.pdf).
[^test-desiderata]: Beck and Sutton, [Test Desiderata](https://testdesiderata.com/).
[^reproducible-builds]: Reproducible Builds, [Definitions](https://reproducible-builds.org/docs/definition/).
[^slsa]: SLSA, [Specification 1.2](https://slsa.dev/spec/v1.2/).
[^nist-ssdf]: NIST, [Secure Software Development Framework 1.1](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-218.pdf).
[^dora]: DORA, [Software delivery performance metrics](https://dora.dev/guides/dora-metrics/).
[^google-sre]: Google, [Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/).
[^pstack]: Cursor, [pstack](https://github.com/cursor/plugins/tree/main/pstack).
[^pstack-review]: pstack, [Code Quality Review](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/references/code-quality-review.md).
[^pstack-rubric]: pstack, [Review Rubric](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/references/rubric.md).
[^pstack-tdd]: pstack, [TDD Bug Fix](https://github.com/cursor/plugins/blob/main/pstack/skills/tdd/SKILL.md).
