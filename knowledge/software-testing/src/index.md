---
okf_version: "0.2"
---
# Software testing

Test design, execution, evidence, suite quality, and defect reporting.

This bundle contains existing material migrated from product-engineering. Coverage is partial.


Shared definitions and guidance are supplied by `@craigsmitham/knowledge/software-engineering-foundations`, included in this discipline’s pack.

Companion readings in other discipline bundles are optional. Resolve a named concept by its bundle identity and concept ID with `axm knowledge concepts get`.

- [Choosing browser-dependent interface tests](choosing-browser-dependent-interface-tests.md) — Use when an interface claim may depend on real browser rendering, interaction, accessibility, or platform behavior; state the observable claim, name the browser capability that alone reveals it, and admit the narrowest scope — from DOM-emulated component to deployed journey — that keeps the risk visible.
- [Choosing the narrowest effective test](choosing-the-narrowest-effective-test.md) — Use when a change needs executable evidence and no material risk yet requires a real cross-boundary or browser world; admit the test deliberately, choose the narrowest level that observes the claim, substitute collaborators through explicit seams, and keep repository conventions out of tests.
- [Designing cross-boundary and end-to-end tests](designing-cross-boundary-and-end-to-end-tests.md) — Use when a material risk spans components, processes, services, storage, artifacts, or deployment configuration; separate claim scope from boundary reality and execution distance, then select the smallest representative test world and observation surface that still discriminates the claim.
- [Operating cross-boundary test suites](operating-cross-boundary-test-suites.md) — Use once a cross-boundary test world is chosen and the suite has to live somewhere; place the harness with one accountable owner, design seed state, readiness, and cleanup, bind execution to the decision point it can honestly serve, and keep failures attributable.
- [Test-suite quality criteria](test-suite-quality.md) — Use when assessing automated tests as supporting artifacts; evaluate whether the suite provides valuable, sustainable, and appropriately bounded evidence for applicable product-quality claims.
- [Writing browser test evidence](writing-browser-test-evidence.md) — Use once a browser test is admitted and the question is how to write it; choose locators and readiness conditions that survive churn, isolate browser and application state, size the environment matrix to real risk, and keep visual and accessibility conclusions inside what their methods support.
- [Defects](defects/index.md) — Existing material about defects.
