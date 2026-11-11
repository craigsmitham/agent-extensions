---
type: Pattern
title: Repository task interface
description: Resolves competing repository commands through canonical task meaning, bounded entrypoints, and one workflow membership authority.
tags: [repository-task-interface, task-runner, ci, workflow, engineering-environment]
status: draft
generated: { by: codex/gpt-6, at: 2026-11-11T19:47:25Z }
sources:
- id: fowler-ci
  resource: https://www.martinfowler.com/articles/continuousIntegration.html
  title: Continuous Integration
- id: build-systems-a-la-carte
  resource: https://simon.peytonjones.org/assets/pdfs/build-systems-original.pdf
  title: "Build Systems \xE0 la Carte"
- id: nx-project-configuration
  resource: https://nx.dev/docs/reference/project-configuration
  title: "Nx \u2014 Project Configuration"
- id: turborepo-configuring-tasks
  resource: https://turborepo.dev/docs/crafting-your-repository/configuring-tasks
  title: "Turborepo \u2014 Configuring tasks"
- id: just-manual
  resource: https://just.systems/man/en/
  title: Just Programmer's Manual
- id: prior-repository-task-interface
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/engineering-environment/src/repository-task-interface.md
  title: Designing a coherent repository task interface
- id: prior-adopting-a-repository-task-interface
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/engineering-environment/src/adopting-a-repository-task-interface.md
  title: Adopting a repository task interface
---

# Repository task interface

## Problem and context

Developers, agents, hooks, and CI can encounter several plausible commands for
the same intent. When scripts, wrappers, and CI paths independently define
prerequisites, selection, arguments, environment, caching, outputs, or success,
callers must reconstruct which result to trust. A clean-checkout build with a
single supported command reduces this ambiguity.[^fowler-ci]

Several physical declarations can form one contract. Nx can compose inferred
and declared tasks; Turborepo combines task metadata and package scripts.
Multiplicity alone is not competing semantics.[^nx-project-configuration][^turborepo-configuring-tasks]

## Forces

Actors need a discoverable vocabulary and consistent evidence, while runners
have different models and capabilities. Small repositories may need only a
command interface; bootstrap, approvals, external state, and privileged
operations can have owners outside a task graph. Cache reuse saves work only
when a prior result still answers the present question.

## Response

Give each supported intent one canonical resolved contract and explicit
entrypoints. The operation identifies the requested action; the subject or
selection identifies its scope. The invocation binds these to configuration and
options. The resolved contract owns effective action, prerequisites,
dependencies, inputs, outputs, environment, cache policy, and result meaning.

A task implementation performs the work. A launcher provisions or selects the
runner without redefining the task. An alias adds convenience; a declared
composite or adapter spans work the runner cannot faithfully express. Host-owned
workflows retain their lifecycle authority. Direct underlying-tool invocation
can be useful diagnostics without establishing supported repository evidence.

Stable workflows have one membership authority or derivation rule. Different
selectors and presentation for humans and automation can share the same
semantics. The [Repository task contract](../repository-task-contract.md)
defines dependency kinds, freshness, cache trust, entrypoint boundaries, and
resolved-behavior checks.

## Local binding

Keep a short repository policy or executable binding that names:

- the orchestrator and how its native concepts map to operation, subject,
  invocation, and resolved contract;
- the supported version-pinned launcher and bootstrap boundary;
- declared prerequisites, environment provisioning and injection boundaries,
  and supported platforms;
- task vocabulary and semantic owners, including workspace- and host-owned
  work;
- dependency kinds, cache trust policy, freshness controls, and result meaning;
- admitted aliases, composites, host adapters, diagnostic paths, and migration
  exceptions;
- workflow membership authorities; and
- enforcement and behavioral-test locations.

Keep repository-specific syntax and inventories in that binding or executable
configuration, not in portable guidance.


## Consequences and limits

One semantic owner reduces synchronization and makes failures and success easier
to interpret. Adoption still costs migration and conformance work; unsupported
runner capabilities need explicit boundaries, not layers of wrappers. A
migration gap retains its safe path and retirement condition. A legitimate
host or bootstrap boundary need not be migrated into the graph.

The intended gains are faster discovery, fewer wrong-path invocations and lost
arguments, clean-checkout success, consistent local and CI results, correct
cache restores, and fewer authored locations for workflow membership. Neat
configuration alone establishes none of these. Observe those outcomes and the
age and number of exceptions.

## Evidence and variation

The cited sources establish tool capabilities and design guidance, not universal
outcome improvements. This pattern is a draft synthesis. A command runner can
provide a coherent interface without a build graph; tool choice and native
terminology remain local.[^build-systems-a-la-carte][^just-manual]

## Worked example

A repository lists its validation work in two package scripts, a Git hook, and
a CI workflow. Adding a check requires four edits, and affected validation can
omit it when the lists drift. A coding agent sees several plausible commands
and cannot determine which one supplies release-candidate evidence.

In this illustrative case, consider how the repository's orchestrator represents validation. In Nx,
the effective task may combine inferred or package-script behavior with task
defaults; in Turborepo, the package script may implement the registered task.
Those runner-native sources can remain as long as they resolve to one contract.

Give validation one membership authority: a faithful graph-native lifecycle
task when available, or one derived inventory otherwise. Make the hook and CI
invoke that identity through the supported launcher instead of listing its
members. If a commit-range security scan cannot be expressed faithfully in the
graph, admit one composite that invokes the canonical validation task and the
host-aware scan. Each child keeps its own dependency, cache, freshness, and
evidence policy.

The technical result is one semantic task contract and one validation
inventory rather than four competing definitions. The valuable result is that
a developer or agent can discover the validation intent, invoke it through a
supported entrypoint, distinguish execution from replay, trust what success
means, and add a future check in one authoritative place.

## Apply the example to a product change

In Northbank's engineering-system episode (shared concept: `@craigsmitham/knowledge/software-engineering-foundations#cases/northbank-engineering-system`),
one copied CI inventory omits a new allocation-concurrency check. The worked
change resolves membership, shows an intentional failure propagating through
the supported workflow, and distinguishes source validation, artifact build,
migration rehearsal, and current deployed assessment. Use that case to follow
the contract into CI/CD and infrastructure while keeping orchestration separate
from each task's meaning.

[^fowler-ci]: Martin Fowler, *Continuous Integration*.
[^nx-project-configuration]: Nx, *Project Configuration*.
[^turborepo-configuring-tasks]: Turborepo, *Configuring tasks*.
[^build-systems-a-la-carte]: Mokhov, Mitchell, and Peyton Jones, *Build Systems à la Carte*.
[^just-manual]: *Just Programmer's Manual*.
