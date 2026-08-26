---
type: Guide
title: Designing a system evaluation approach
description: Use when establishing or revising how a system's evaluations are organized, traced, navigated, reported, and maintained across methods and repositories.
tags: [evaluations, testing, traceability, reporting, architecture, requirements]
status: draft
sources:
  - resource: evaluation-as-bounded-evidence.md
    title: Evaluation as bounded evidence
  - resource: ../profile/gen-stack-application-profile.md#system-evaluation-approach
    title: Gen Stack application profile — System Evaluation Approach
  - resource: ../architecture/requirements/one-authority-many-witnesses.md
    title: One authority, many witnesses
  - resource: ../architecture/requirements/easy-approach-to-requirements-syntax.md
    title: Easy Approach to Requirements Syntax (EARS)
generated:
  by: codex/gpt-5.6
  at: 2026-08-26T19:12:18Z
---

# Designing a system evaluation approach

> **Authority:** This Guide applies the canonical meaning in the [Gen Stack
> vocabulary and relationship model](/glossary.md). When it authors a
> profile-governed corpus concept, the [Gen Stack application
> profile](/profile/gen-stack-application-profile.md) owns its required
> representation. This Guide supports action and adds neither semantic authority
> nor profile-conformance rules.

## Goal

Create a coherent evaluation portfolio whose Definitions and Results remain at
their repository-native authorities while people can find evidence by
Architecture subject, Requirement, and Evaluation Role.

## Representation

Use the OKF envelope, the profile's exact `System Evaluation Approach` type and
path, and its five required second-level headings in their required order:
scope and objectives, evaluation portfolio, navigation and reporting, evidence
and lifecycle, then gaps and maintenance. Inside them, link repository-native
Definitions, Suites, Executions, Results, and Reports by their stable native
identities; do not copy their fields or current results into the governed
concept. Exact headings come from the profile; any lower-level organization is
proportional authoring guidance.

## 1. Bound the approach

Name the System, realized-state boundary, environments, decisions supported,
and material exclusions. Link the root System Assurance concept and explain
which confidence questions the portfolio supports; do not turn the approach
into an approval policy.

## 2. Inventory claims before methods

For each maintained Definition, record a stable identity, one primary role,
the assessed subject, criteria authority, method, conditions, oracle or
judgment procedure, and provenance needs. Use:

- `requirement-satisfaction` with stable Requirement IDs;
- `architecture-realization` with canonical Architecture subjects or ADRs; or
- `other-bounded-claim` with a named criteria authority.

Choose method and lifetime for the claim and consequence. Combine economical
implementation-local checks, durable boundary evaluations, and operational
evaluations where their different blind spots matter.

For a Requirement expressed with [EARS](../architecture/requirements/easy-approach-to-requirements-syntax.md),
use its clauses as inputs to Definition design without treating the syntax as
an executable test specification:

| Requirement element | Evaluation Definition concern |
| --- | --- |
| Optional-feature clause | Applicable configuration or product variant |
| Continuing-state clause | Setup and maintained preconditions |
| Desired or unwanted trigger | Stimulus, observed event, or sampled condition |
| Obligated subject | Canonical Architecture subject being evaluated |
| Required response | Expected outcome, oracle, or judgment criterion |
| Bounds in the response | Threshold, tolerance, population, or observation window |

The Definition still owns its method, cases or sampling, oracle, environment,
and uncertainty. Deriving those details requires evaluation judgment; EARS
only helps preserve the Requirement's applicability and expected response.

## 3. Organize suites for execution, not authority

Keep Suites where their tooling, ownership, fixtures, lifecycle, and execution
dependencies make them maintainable. Do not force physical suite paths to
mirror Architecture. A Suite may span subjects, and one subject may depend on
several Suites. Preserve Definition-level subject and criteria traceability so
navigation can be projected independently.

## 4. Publish navigable projections

Provide routes from every claimed-covered Requirement and Architecture subject
to its Definitions and current Results. At minimum, readers must be able to
navigate:

- Architecture subject hierarchy and cross-view mappings;
- stable Requirement ID and its canonical subject;
- Evaluation Role; and
- Definition, Execution, Result, revision, environment, and observation window.

Generate indexes, dashboards, or reports from traceability metadata when
practical. Architecture has several overlapping views, not one universal tree;
preserve canonical Surface and C4 hierarchies while exposing cross-links
instead of duplicating evidence.

## 5. Keep reports claim-specific

Publish distinct reports for Requirement satisfaction and Architecture
realization. A report declares its audience, scope, filter, generation time,
underlying evidence, and roll-up policy. Never allow a missing Result, skipped
Execution, or harness error to become a pass. Parent roll-ups must expose
`unknown` and failing descendants; a child pass does not prove its parent.

## 6. Govern provenance and gaps

Bind each Result to its Definition version, realized revision, material inputs,
environment, evaluator, time or observation window, and outcome. Record known
coverage gaps, stale Definitions, unsupported environments, responsible
stewardship route, and review triggers. Route disagreements through the Gen
Stack control loop rather than silently changing a Requirement or evaluator.

## Final check

- Definitions own criteria; Suites only group them; Reports only project Results.
- Every Definition has one primary Evaluation Role.
- Requirement and Architecture evidence are separately navigable and reported.
- Physical runner layout is free to differ from subject navigation.
- Provenance, `unknown`, and harness errors survive aggregation.
- The approach links, but does not copy, repository-native authorities.

## Related

- [Evaluation as bounded evidence](evaluation-as-bounded-evidence.md)
- [Designing evaluations for Surfaces](designing-evaluations-for-surfaces.md)
- [Designing evaluations for C4 structure](designing-evaluations-for-c4-structure.md)
- [One authority, many witnesses](../architecture/requirements/one-authority-many-witnesses.md)
