# Software engineering knowledge

Portable engineering craft for reviewing codebases, designing test
architecture, and shaping repository execution surfaces. It is intended for
engineers and agents who need a bounded, evidence-backed review of a
repository, representative cross-boundary and browser-dependent test worlds,
or a coherent invocation contract for build, test, and automation work.

Use the codebase-review collection for ten outcome-centered software-product
quality lists: Suitability, Correctness, Reliability, Security, Safety,
Efficiency, Usability, Compatibility, Evolvability, and Intelligibility. Eight
typed cross-cutting records preserve context, specification, structure,
lifecycle integrity, risk, assurance, feedback, and evidence without turning
methods or supporting artifacts into extra pillars. Test-suite quality has a
separate supporting assessment, and optional review aids hold repository,
scenario, verification, runtime, and model-assisted inspection guidance. The
pillar taxonomy, the layers it deliberately excludes, and its research basis
are separate concepts, as are the cross-cutting admission gate, the record
definitions, the typed pillar relationships, and the model's maintenance and
validation plan.

Use the repository task-interface guide to make repository work discoverable,
safe to invoke, and trustworthy to interpret. It frames the competing-semantics
problem and the portable vocabulary; companion concepts hold the resolved
contract principles (ownership, self-sufficiency, typed dependencies, cache
semantics), the invocation and conformance principles (entrypoint roles,
workflow membership, canonical actor semantics, resolved-behavior checks), and
the adoption sequence with its local binding and worked example.

Use the narrowest-effective-test guide when a change needs executable evidence
and no material risk yet requires a real cross-boundary or browser world: admit
the test deliberately, prove each behavior once at the cheapest trustworthy
level, substitute collaborators through explicit seams, and keep repository
conventions in lint and build checks rather than test runners. Use the
cross-boundary and end-to-end testing guide to start with a material risk and
choose the smallest test world that preserves the necessary components,
processes, services, storage, artifacts, or deployment boundaries. Use the
complementary browser-dependent interface guide when real rendering,
interaction, accessibility, or platform behavior determines the observable
outcome. Together the three keep test scope independent from browser use and
admit expensive evidence only when a cheaper observer would erase the risk.
Once a test is admitted, separate concepts cover operating a cross-boundary
suite — harness ownership, state and readiness, decision points, attributable
failure — and writing browser evidence: locators, synchronization, isolation,
the environment matrix, and bounded visual and accessibility conclusions. Use
the executable-specifications guide on the separate axis of authority and
audience: which decided rules earn a human-readable statement of intent that
non-authors can dispute, what that text may contain, and how to bind automation
below it so implementation change never edits a specification. A companion
guide keeps an accepted specification trustworthy: acceptance and verification
as separate properties, evidence for obligations that cannot run on every
change, failure triage before either side is edited, retirement, and generated
change gated on reviewed intent.
This bundle is not a software-change method, requirements or architecture
lifecycle, work-item guidance, documentation craft, or a language or framework
reference.

The review framework is a source-reviewed and synthetic-design-reviewed
candidate, not a field-validated control. It supports coverage and traceability
but does not certify the reviewed product.

Earlier versions of this bundle (through 1.1.0) held design-change and
work-item guidance. Version 2.0.0 re-established the package around repository
execution surfaces; version 2.1.0 added the bounded codebase-review collection;
version 2.2.0 refactors that collection around product-quality outcomes without
reclaiming the retired change-method or work-item scope; version 2.3.0 reframes
command execution as a coherent repository task interface for developers,
agents, and automation; version 2.4.0 adds portable cross-boundary and
browser-dependent test architecture; version 2.4.1 marks those guides stable
after source reconciliation; version 2.5.0 adds the narrowest-effective-test
guide as a draft pending its own source reconciliation; version 2.6.0 adds
executable specifications as an axis of authority separate from test level;
version 2.7.0 splits every concept over 300 lines into reader-recognizable
siblings and brings the bundle into OKF conformance; version 2.8.0 revises
the executable-specifications guide around what is incidental to the
obligation, separates its lifecycle guidance into "Keeping specifications
authoritative", and marks both stable; and version 2.8.1 corrects that guide's
claims about what supporting coverage establishes and about which refund-window
details the rule must settle.

Install the pack with:

```bash
axm packs install @craigsmitham/packs/software-engineering
```

Or install the standalone knowledge bundle directly:

```bash
axm install @craigsmitham/knowledge/software-engineering
```

Then browse its discovery index or search installed concepts, for example:

```bash
axm knowledge concepts search '"repository task interface"'
axm knowledge concepts search '"codebase review"'
axm knowledge concepts search '"narrowest effective test"'
axm knowledge concepts search '"cross-boundary"'
axm knowledge concepts search '"browser-dependent"'
axm knowledge concepts search '"cross-cutting concern"'
```

This knowledge package is licensed under the Creative Commons
Attribution-ShareAlike 4.0 International license (`CC-BY-SA-4.0`). The
reciprocal license applies to the package content; it does not automatically
apply to unrelated output created while using the package.
