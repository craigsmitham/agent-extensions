---
okf_version: "0.2"
---

# Software engineering

Portable engineering craft for reviewing software products through repository
and other available evidence, designing test architecture, and shaping
repository execution surfaces.
Use this bundle for outcome-centered assessment of suitability, correctness,
reliability, security, safety, efficiency, usability, compatibility,
evolvability, and intelligibility; for explicit treatment of cross-cutting
context and evidence; for selecting representative cross-boundary and
browser-dependent test worlds; and for tool-neutral guidance on task graphs
and invocation contracts. It is not a software-change method, requirements or
architecture lifecycle, work-item system, documentation-craft guide, or
language and framework reference.

## Review codebases

- [Codebase review](codebase-review/) - An outcome-centered review framework with ten product-quality criteria lists, eight typed cross-cutting records, separate supporting-artifact assessments, optional evidence and method aids, and explicit uncertainty and lifecycle guidance.

## Design repository task interfaces

Read the entry guide first for the vocabulary and boundaries; the two principle
concepts and the adoption guide assume it.

- [Designing a coherent repository task interface](repository-task-interface.md) - Use when repository tasks, scripts, launchers, wrappers, or CI paths compete, or when placing new repeatable work; name the competing-semantics problem, the outcomes one task interface must deliver, and the portable vocabulary that the contract, invocation, and adoption guides build on.
- [Resolved task contract principles](resolved-task-contract-principles.md) - Use when deciding what a single repository task means — who owns it, what it guarantees from a clean shell, which dependencies it declares, and when a cache replay still answers the caller's question; the five principles that define a canonical resolved contract.
- [Task invocation and conformance principles](task-invocation-and-conformance-principles.md) - Use when wrappers, aliases, hooks, agents, or CI steps have accumulated around a repository's tasks; the five principles that bound each entrypoint's role, keep one membership authority per workflow, hold actors to canonical semantics, and check resolved rather than declared behavior.
- [Adopting a repository task interface](adopting-a-repository-task-interface.md) - Use when converting the task-interface principles into an actual repository change; a twelve-step design or repair sequence, the local binding that records runner-specific decisions, the signals that show whether the interface helped, and a worked example of collapsing four validation inventories into one.

## Choose a test level

Levels are chosen on one axis and authority on another: these three guides
decide where a claim is proved, and the specification guide below decides which
behaviors earn an authoritative, human-readable statement of intent.

- [Choosing the narrowest effective test](choosing-the-narrowest-effective-test.md) - Use when a change needs executable evidence and no material risk yet requires a real cross-boundary or browser world; admit the test deliberately, choose the narrowest level that observes the claim, substitute collaborators through explicit seams, and keep repository conventions out of tests.
- [Designing cross-boundary and end-to-end tests](designing-cross-boundary-and-end-to-end-tests.md) - Use when a material risk spans components, processes, services, storage, artifacts, or deployment configuration; separate claim scope from boundary reality and execution distance, then select the smallest representative test world and observation surface that still discriminates the claim.
- [Choosing browser-dependent interface tests](choosing-browser-dependent-interface-tests.md) - Use when an interface claim may depend on real browser rendering, interaction, accessibility, or platform behavior; state the observable claim, name the browser capability that alone reveals it, and admit the narrowest scope — from DOM-emulated component to deployed journey — that keeps the risk visible.

## Build and operate the admitted tests

Each guide above admits a test and fixes its scope. These two take over once
that decision is made and the suite has to be written, owned, and run.

- [Operating cross-boundary test suites](operating-cross-boundary-test-suites.md) - Use once a cross-boundary test world is chosen and the suite has to live somewhere; place the harness with one accountable owner, design seed state, readiness, and cleanup, bind execution to the decision point it can honestly serve, and keep failures attributable.
- [Writing browser test evidence](writing-browser-test-evidence.md) - Use once a browser test is admitted and the question is how to write it; choose locators and readiness conditions that survive churn, isolate browser and application state, size the environment matrix to real risk, and keep visual and accessibility conclusions inside what their methods support.

## Give behavior an authoritative statement

- [Designing executable specifications](designing-executable-specifications.md) - Use when intended behavior needs an authoritative, human-readable, continuously verified statement that non-authors can dispute; choose which rules earn a specification, keep incidental mechanics out of the specification text, and bind automation below the readable layer.
- [Keeping specifications authoritative](keeping-specifications-authoritative.md) - Use once an executable specification is accepted and must stay trustworthy; separate acceptance from verification, record evidence for obligations that cannot run on every change, triage a failure before editing either side, retire dead rules, and gate generated change on reviewed intent.
