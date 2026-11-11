---
type: Reference
title: Repository task contract
description: Defines canonical task ownership, dependencies, cache meaning, entrypoint roles, and observable conformance.
tags: [task-contract, dependencies, cache, entrypoints, conformance, engineering-environment]
status: draft
generated: { by: codex/gpt-6, at: 2026-11-11T19:56:05Z }
sources:
- id: nx-run-tasks
  resource: https://nx.dev/docs/features/run-tasks
  title: "Nx \u2014 Run Tasks"
- id: nx-task-pipeline
  resource: https://nx.dev/docs/concepts/task-pipeline-configuration
  title: "Nx \u2014 Task pipeline configuration"
- id: nx-caching
  resource: https://nx.dev/docs/concepts/how-caching-works
  title: "Nx \u2014 How caching works"
- id: turborepo-configuring-tasks
  resource: https://turborepo.dev/docs/crafting-your-repository/configuring-tasks
  title: "Turborepo \u2014 Configuring tasks"
- id: turborepo-environment
  resource: https://turborepo.dev/docs/crafting-your-repository/using-environment-variables
  title: "Turborepo \u2014 Using environment variables"
- id: turborepo-caching
  resource: https://turborepo.dev/docs/crafting-your-repository/caching
  title: "Turborepo \u2014 Caching"
- id: turborepo-remote-cache
  resource: https://turborepo.dev/docs/core-concepts/remote-caching
  title: "Turborepo \u2014 Remote Caching"
- id: gradle-task-practices
  resource: https://docs.gradle.org/current/userguide/best_practices_tasks.html
  title: "Gradle \u2014 Best Practices for Tasks"
- id: gradle-build-cache
  resource: https://docs.gradle.org/current/userguide/build_cache.html
  title: "Gradle \u2014 Build Cache"
- id: bazel-dependencies
  resource: https://bazel.build/concepts/dependencies
  title: "Bazel \u2014 Dependencies"
- id: bazel-hermeticity
  resource: https://bazel.build/concepts/hermeticity
  title: "Bazel \u2014 Hermeticity"
- id: gradle-organizing-tasks
  resource: https://docs.gradle.org/current/userguide/organizing_tasks.html
  title: "Gradle \u2014 Organizing Tasks"
- id: gradle-wrapper
  resource: https://docs.gradle.org/current/userguide/gradle_wrapper.html
  title: Gradle Wrapper
- id: turborepo-running-tasks
  resource: https://turborepo.dev/docs/crafting-your-repository/running-tasks
  title: "Turborepo \u2014 Running tasks"
- id: nx-conformance
  resource: https://nx.dev/docs/reference/conformance/overview
  title: "Nx \u2014 Conformance"
- id: moon-tasks
  resource: https://moonrepo.dev/docs/concepts/task
  title: "moon \u2014 Tasks"
- id: prior-resolved-task-contract-principles
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/engineering-environment/src/resolved-task-contract-principles.md
  title: Resolved task contract principles
- id: prior-task-invocation-and-conformance-principles
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/engineering-environment/src/task-invocation-and-conformance-principles.md
  title: Task invocation and conformance principles
---

# Repository task contract

Reference semantics for the [Repository task interface](patterns/repository-task-interface.md) pattern.

## One resolved contract owns each supported intent

Each repeatable unit has one canonical identity and one resolved contract for
what executes, under which prerequisites, with which dependencies, inputs,
outputs, environment, cache behavior, and interpretation of success.

The physical declarations may be composed, inferred, or inherited when the
orchestrator natively supports that model. A package script consumed as an Nx
task or Turborepo task implementation is part of the canonical contract, not
automatically a competing interface.[^nx-run-tasks][^turborepo-configuring-tasks]
What must not happen is for callers to restate or alter semantic behavior
independently.

## Intent and lifecycle determine name and ownership

Name operations for actor intent, not the tool or historical implementation.
Use one verb for one kind of work across the scope where actors transfer
knowledge. Qualifiers narrow the intent rather than repeat the subject or
configuration file.

Assign the narrowest stable semantic owner that controls the outcome and its
lifecycle:

- a project or package for a capability it builds, verifies, runs, or changes;
- the workspace for cross-cutting work with no honest project subject;
- an environment, release unit, or operational system for shared state and
  privileged mutations; or
- the host platform for lifecycle events it controls.

Root or workspace tasks are legitimate when work has no useful package scope;
Turborepo explicitly supports this case.[^turborepo-configuring-tasks]
Do not force ownership onto a project merely because its files contain the
implementation.

## Supported tasks are self-sufficient within a declared boundary

A supported task invocation produces correct behavior from a clean shell once
its declared prerequisites are met. Hermetic systems go further by isolating
actions from undeclared host tools and services, which improves reproducibility
and cache safety.[^bazel-hermeticity]

Self-sufficiency does not mean the task owns every value or external system.
Separate:

- **declaration** — required files, tools, services, environment variable
  names, and permissions;
- **provisioning** — acquisition of the runner, toolchain, or local services;
- **injection** — host- or secret-manager delivery of environment-specific
  values; and
- **hashing** — which values and runtime facts can change task outputs.

Keep values such as credentials outside repository configuration. Account for
every behavior-changing environment value in the cache contract; Turborepo
documents how an omitted variable can restore output for the wrong
environment.[^turborepo-environment]

## Dependencies are explicit and typed

Every actual dependency the orchestrator can model must be represented in the
resolved contract. Bazel frames correctness as requiring actual dependencies
to be included in the declared graph.[^bazel-dependencies] Caller-side
sequencing hides that information from affected selection, parallel execution,
and caching; use the runner's dependency model instead, such as Nx task-pipeline
relationships, when it expresses the required semantics.[^nx-task-pipeline]

Choose the relationship that expresses why it exists:

| Relationship | Use when |
| --- | --- |
| **Data or artifact dependency** | The consumer reads an output; prefer this over generic sequencing when the runner can infer execution from dataflow. |
| **Required execution dependency** | Another task must complete successfully even without a direct artifact edge. |
| **Order-only relationship** | Selected work must be ordered but neither task causes the other to be selected. |
| **Lifecycle or aggregate membership** | A no-op intent groups independently useful work. |
| **Continuous or service relationship** | A long-running process must become ready without being treated as a completed prerequisite. |
| **Optional relationship** | Absence or failure is explicitly tolerated by the workflow. |
| **External prerequisite** | A service, permission, approval, or host state is required but not owned by the graph. |

Gradle specifically recommends connecting actionable tasks through inputs and
outputs rather than using coarse `dependsOn` relationships, reserving the
latter primarily for lifecycle tasks.[^gradle-task-practices]

## Cache policy preserves result meaning

A cache replay is a prior result for the computed input identity. It answers
the current question only if execution was deterministic enough, the declared
identity was complete, the stored result is trusted, and the restored evidence
is fit for the caller's purpose. Nx, Turborepo, and Gradle all make cache
correctness depend on accurate task inputs and outputs.[^nx-caching][^turborepo-caching][^gradle-build-cache]

| Task behavior | Default direction |
| --- | --- |
| Deterministic build or verification with complete declared inputs | Cache when outputs are complete and relocatable. |
| Evidence-producing work | Cache only when restored evidence, metadata, and logs remain coherent and answer the caller's question. |
| Observation or measurement, such as a benchmark | Execute when the question concerns current conditions. |
| Aggregate or no-op orchestration | Rely on child-task correctness; do not treat an aggregate cache hit as independent evidence. |
| Interactive, continuous, privileged, or mutating work | Do not cache. |
| Very fast work or work with very large artifacts | Measure whether caching costs more than execution. |

For each cacheable task, establish:

- complete file, dependency, argument, environment, runtime, and toolchain
  inputs;
- complete, non-overlapping, and relocatable outputs;
- repeatability for the same declared identity;
- visible distinction between execution and replay;
- trusted remote-cache readers and writers, artifact integrity, and safe
  treatment of captured logs; Turborepo, for example, offers signed remote
  artifacts and warns that logs are artifacts too;[^turborepo-remote-cache]
- whether cache reads, writes, or both are allowed in each context; and
- whether cache lookup and transfer are economically useful.

Document one runner-native freshness route for each supported observation and
state its scope. `--skip-nx-cache`, Turborepo's `--force`, and Gradle rerun
controls do not have identical read, write, task, and dependency semantics.
Every admitted entrypoint must preserve the selected freshness behavior or
fail loudly.

[^nx-run-tasks]: Nx, *Run Tasks*.
[^nx-task-pipeline]: Nx, *Task pipeline configuration*.
[^nx-caching]: Nx, *How caching works*.
[^turborepo-configuring-tasks]: Turborepo, *Configuring tasks*.
[^turborepo-environment]: Turborepo, *Using environment variables*.
[^turborepo-caching]: Turborepo, *Caching*.
[^turborepo-remote-cache]: Turborepo, *Remote Caching*.
[^gradle-task-practices]: Gradle, *Best Practices for Tasks*.
[^gradle-build-cache]: Gradle, *Build Cache*.
[^bazel-dependencies]: Bazel, *Dependencies*.
[^bazel-hermeticity]: Bazel, *Hermeticity*.

## Every entrypoint has one bounded role

| Entrypoint role | Contract |
| --- | --- |
| **Runner-native task declaration or implementation** | May contain real behavior when the orchestrator consumes it into the resolved contract; direct use is supported only when the local binding says so. |
| **Launcher or bootstrap** | Pins or provisions the orchestrator and forwards its task vocabulary without redefining it. Gradle recommends its checked-in Wrapper for reliable execution across developers and CI.[^gradle-wrapper] |
| **Alias** | Adds only convenience or presentation, preserves one canonical task mapping, and forwards additional arguments unchanged or fails loudly. |
| **Composite or host adapter** | Owns a stable cross-boundary workflow the orchestrator cannot faithfully express; keep it explicit and allowlisted. |
| **Diagnostic invocation** | Runs an underlying tool for investigation and is not represented as supported repository evidence. |

The task implementation can remain a command or a script when that is native
to the orchestrator; moon, for example, supports both forms.[^moon-tasks]
A wrapper that silently injects required behavior above an otherwise
documented task, or a caller that reimplements dependencies and selection, is
a competing interface. The test is semantic duplication, not whether the path
is physically a script.

## Stable workflows have one membership authority

When a workflow means “run this set of work,” its membership has one authored
inventory or one derivation rule. Scripts, hooks, and CI do not maintain copies.

Prefer a graph-native lifecycle or aggregate task when it faithfully preserves
project and affected selection; Gradle recommends lifecycle tasks as accessible
entrypoints for users and CI.[^gradle-organizing-tasks] Otherwise use a single
generated inventory, repository policy, or host-owned definition and make
callers refer to it. The invariant is one authority, not one mandatory storage
mechanism.

## Actors use canonical semantics through supported entrypoints

Agents and CI invoke canonical task identities through the repository's
supported, preferably version-controlled launcher. Turborepo recommends direct
`turbo run` use in CI while also recommending package scripts for frequent
human invocations; both can share the same registered tasks.[^turborepo-running-tasks]

Humans and machines may use different selectors, output modes, or lifecycle
tasks. They must not receive different prerequisites, cache meaning, or result
semantics for the same stated intent. Durable automation does not depend on a
convenience alias whose mapping or argument behavior is undocumented.

When a supported task exists, invoke the underlying CLI directly only for a
clearly identified diagnostic or for work outside the task's contract. Do not
present that result as equivalent repository verification.

## Conformance examines resolved behavior

The pattern or local policy owns the reasons; executable checks own stable and
observable rules. Inspect the orchestrator's resolved task model rather than
assuming one source file contains the whole truth. Nx, for example, exposes a
resolved project graph to conformance rules.[^nx-conformance]

Combine structural checks with behavioral contract tests:

- invoke supported tasks from a clean checkout through the pinned launcher;
- verify canonical and admitted convenience paths resolve to the same task;
- verify arguments and freshness controls reach the intended layer;
- change declared file, environment, runtime, and tool inputs and observe
  invalidation;
- restore from cache in another directory or worker and verify every output;
- verify affected selection includes newly added work;
- detect copied workflow inventories and unsupported automation paths; and
- check that failures identify the task or unmet prerequisite.

No static check proves every dependency or environmental assumption. Preserve
unknowns and exceptions rather than treating an incomplete checker as proof of
conformance.

## Boundaries and gaps are explicit

Classify every path outside the canonical task contract:

- A **legitimate boundary** remains with its launcher, host, operational
  system, or diagnostic context and is documented as such.
- A **migration gap** preserves the currently safe path, records why the
  canonical task is incomplete, and names its retirement condition.
- A **duplicate interface** is removed or redirected because it independently
  owns semantics already represented elsewhere.

Do not label intentional tool boundaries as defects. Do not normalize actual
gaps into folklore or add another wrapper around them.

[^gradle-organizing-tasks]: Gradle, *Organizing Tasks*.
[^gradle-wrapper]: Gradle, *Gradle Wrapper*.
[^turborepo-running-tasks]: Turborepo, *Running tasks*.
[^nx-conformance]: Nx, *Conformance*.
[^moon-tasks]: moon, *Tasks*.
