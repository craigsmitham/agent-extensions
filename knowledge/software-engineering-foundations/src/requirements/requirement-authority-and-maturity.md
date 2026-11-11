---
type: Reference
title: Requirement authority and maturity
description: Separates candidate and normative requirements from independent decision, persistence, realization, and evidence states.
tags: [requirement, authority, maturity, candidate, normative, evidence, software-engineering-foundations]
generated: { by: codex/gpt-6, at: 2026-11-11T19:45:59Z }
sources:
- id: prior-eliciting-and-inventorying-requirement-sources
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/requirements-engineering/src/development/eliciting-and-inventorying-requirement-sources.md
  title: Eliciting and inventorying requirement sources
- id: prior-developing-candidate-requirements
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/requirements-engineering/src/development/developing-candidate-requirements.md
  title: Developing candidate requirements
- id: prior-resolving-conflicts-and-open-decisions
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/requirements-engineering/src/development/resolving-conflicts-and-open-decisions.md
  title: Resolving conflicts and open decisions
---

# Requirement authority and maturity

A **requirement candidate** is a proposed obligation whose meaning, support,
conflicts, feasibility, or authority may still be unresolved. A **normative
requirement** is an obligation accepted as authoritative under the project's
declared decision policy.

Do not infer acceptance from polished wording, a document location, an issue
status, implementation, or passing tests. Record the applicable authority and
decision evidence.

Track these dimensions independently:

| Dimension | Typical states or questions |
| --- | --- |
| Maturity | observation, need, candidate, refined, normative, retired |
| Normative force | informative, recommended, required, prohibited |
| Decision | undecided, proposed, accepted, rejected, deferred, superseded |
| Persistence | transient note, durable record, authoritative source |
| Realization | unknown, planned, implemented, partially implemented, removed |
| Evidence | unsupported, linked, assessed, satisfied, failed, unknown |

A project may use other names. Map them explicitly rather than treating a
single workflow status as proof of every dimension.

## Sources, candidates, and unresolved decisions

Provenance connects evidence to a need and proposed obligation. Relevant sources
may include stakeholders and affected people, goals and policies, contracts and
external obligations, observed behavior and incidents, interfaces and lifecycle
events, prior requirements, designs, and decisions. Source identity, version or
observation date, applicability, confidence, and interpretation or access gaps
keep observations distinguishable from inference. No elicitation technique or
source inventory proves completeness or acceptance.

A candidate identifies its obligated subject, context, intended or prohibited
outcome, source, and unresolved decisions. Missing quantities, regulatory
versions, priorities, stakeholder agreement, or architecture decisions remain
unknown; polished wording cannot supply them.

A conflict record preserves the competing claims and sources, affected outcomes,
exact decision, viable options and their evidence, consequences and tradeoffs,
authority, due point, result, rationale, and superseded candidates when known.
Research, modeling, measurement, negotiation, or explicit risk acceptance may
resolve uncertainty. Until then, keep the candidate status or normative
requirement's unresolved field visible rather than smoothing away disagreement.

The [Northbank commitment case](../cases/northbank-commitment-requirements.md)
illustrates why “appropriate substitute” cannot resolve disagreement about
machine size, site compatibility, and secured capacity.
