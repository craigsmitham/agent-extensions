---
type: Reference
title: Harness classification
description: Independent axes and applied profiles for classifying agent harnesses without confusing domains, ownership, topology, scope, or product labels.
tags: [harness, taxonomy, classification, coding-harness, repository-harness, archetypes]
status: stable
sources:
  - id: harness-properties
    resource: https://arxiv.org/abs/2606.10106
    title: What Makes a Harness a Harness? Evaluating Agentic Scaffold Properties
  - id: scaffold-taxonomy
    resource: https://arxiv.org/abs/2604.03515
    title: Inside the Scaffold — A Taxonomy of Agentic Coding System Architectures
  - id: ai-harness-runtime
    resource: https://arxiv.org/abs/2605.13357
    title: AI Harness Engineering — A Runtime Substrate for Foundation-Model Software Agents
generated:
  by: codex/gpt-5.6
  at: 2026-08-14T21:42:14Z
stale_after: 2027-02-14
---

# Harness classification

Harness categories become inconsistent when one label names the work, another
names the deployment, and a third names the owner. Classify a concrete system
along independent axes before assigning it a convenient profile name.

## Classification axes

| Axis | Question | Representative values |
| --- | --- | --- |
| Application domain | What kind of work is supported? | software engineering, research, personal assistance, business operations, computer use |
| Adaptation locus | Where is agent-specific adaptation primarily implemented? | agent host, working environment, shared platform, evaluation system |
| Ownership and adaptation scope | Who owns the adaptation, and where does it apply? | user, repository, subtree/package, workspace/monorepo, team, organization |
| Interaction mode | How is work initiated and supervised? | interactive copilot, delegated task, event-driven, scheduled, autonomous service |
| Execution location | Where does work run? | local, remote, browser, container, VM, managed service |
| Continuity | How long does identity and state persist? | single turn, session, resumable task, long-lived agent |
| Coordination topology | How many actors coordinate, and how? | single agent, supervisor/worker, peer agents, workflow graph, shared queue |
| Authority and environment reach | What may be observed or changed? | read-only, repository-scoped, workstation, SaaS accounts, production systems |
| Evaluation role | Is this the operating target or the system measuring it? | production harness, evaluation target, evaluation harness |

“Runtime topology” is useful shorthand, but it often bundles execution
location, continuity, interaction mode, and coordination. Keep those values
separate when the distinction affects design or evaluation. Current scaffold
research likewise finds meaningful variation in control flow, planning,
memory, tool use, coordination, and verification rather than one size axis.
[^harness-properties][^scaffold-taxonomy]

## Applied profiles combine axes

**Coding harness** and **repository harness** are both useful terms, but they
answer different questions:

| Profile | Primary classification |
| --- | --- |
| Coding harness | Software-engineering application domain |
| Coding-agent harness | Agent-host adaptation for software-engineering work |
| Repository harness | Environment-side adaptation owned and scoped by a repository |
| Organization coding harness | Software-engineering domain with organization-wide ownership and policy |
| Coding evaluation harness | Evaluation-side system administering software-engineering cases and trials |
| Repository coding system | Composition of a coding-agent harness, repository harness, execution environment, and applicable user or organization policy |

A profile is not a new foundational discipline or necessarily a separate
package. It is a stable, recognizable combination of axis values. This keeps
one harness-engineering body of knowledge while allowing domain and
environment profiles to carry specialized guidance.

## Product archetypes are another view

Market categories usually combine several axes:

| Archetype | Typical combination |
| --- | --- |
| Interactive copilot | User-scoped, interactive, short-lived, usually single-agent |
| Background worker | Delegated, remote, task-persistent, isolated execution |
| Persistent personal agent | User-owned, long-lived, multi-channel, broad personal environment reach |
| Collaborative work agent | Team or organization scope, business-system integrations, shared state and governance |
| Multi-agent service | Coordinated agents or workflows behind a service boundary |
| Enterprise agent platform | Shared runtime, orchestration, governance, observability, and integration facilities for many agent systems |

Named products are changing examples of these combinations, not definitions of
the categories. Classify the deployed configuration: the same product can move
between archetypes as channels, persistence, tools, or authority change.

## Treat overloaded labels as claims to unpack

Terms such as **AI OS**, **agent OS**, **framework**, **platform**,
**assistant**, **copilot**, **digital worker**, and **scaffold** do not have
stable architectural meanings. Translate them into explicit responsibilities
and axis values. In particular, an “AI OS” may mean a personal-agent host, an
enterprise control plane, a multi-agent platform, or simply an application
suite; the name alone should not determine bundle boundaries.

[^harness-properties]: What Makes a Harness a Harness? Evaluating Agentic Scaffold Properties
[^scaffold-taxonomy]: Inside the Scaffold — A Taxonomy of Agentic Coding System Architectures
[^ai-harness-runtime]: AI Harness Engineering — A Runtime Substrate for Foundation-Model Software Agents
