---
name: plan-codebase-change
description: Converts an accepted functional and technical codebase change specification into a snapshot-validated, traceable implementation plan organized as independently verifiable vertical slices and work items. Use when asked to plan, decompose, sequence, task, or prepare an approved codebase change for an implementation agent or work management system. Not for researching current behavior, choosing or specifying a design, estimating delivery, writing code, or implementing the plan.
---

# Plan a codebase change

Produce a tactical handoff that another agent or work system can execute without
rediscovering the design or making hidden product and architecture choices.

## Non-negotiable planning boundary

Never choose a missing product behavior, interface semantic, state transition,
compatibility rule, failure policy, ownership boundary, or other consequential
technical behavior while planning. This remains true when the specification is
labeled accepted and when the caller asks to “pick the simplest,” use a default,
make a reasonable assumption, or keep the plan moving. Those requests expose a
design gap; they do not authorize the planner to resolve it.

Independently check the accepted input for such gaps before deriving work. If an
in-flight, duplicate, empty, failure, authorization, concurrency, migration, or
other material case lacks an accepted outcome, set the plan to `Blocked` with
blocker type `Needs redesign` and identify the exact decision. Do not create
tasks, tests, exclusions, or “resolved gaps” that imply an answer. A plan
containing an invented consequential choice must never be `Ready`.

## Inputs and readiness

Require:

- an explicitly accepted functional and technical change specification or an
  equivalent approved contract with stable outcomes, behaviors, decisions,
  interfaces, invariants, slices, and verification obligations; and
- access to the relevant codebase snapshot and evidence needed to verify concrete
  implementation anchors.

Accept these inputs in any caller-supplied format. Do not require another skill
or a particular artifact name. Preserve the specification's identifiers and
acceptance boundary.

Use one plan status:

- `Blocked` when planning cannot proceed without new acceptance, research, or
  redesign. Add one or more blocker types and identify their affected scope:
  - `Needs acceptance` when the governing specification or contract is not
    explicitly accepted;
  - `Needs research` when a current ownership, flow, interface, test surface,
    path, or material drift fact cannot be established; and
  - `Needs redesign` when accepted scope lacks a consequential behavior or
    contract, a task would decide one, or drift invalidates an accepted decision.
- `Draft` only when no blocker exists and the complete plan is intentionally
  awaiting a caller-requested or repository-required plan review. Do not use it
  for unfinished work or unresolved blockers.
- `Ready` when no blocker exists, no plan review remains, and every readiness
  condition below is satisfied.

Do not reopen a settled choice merely because another implementation seems
preferable. Name the violated decision or constraint when redesign is required.
An `Accepted` label is necessary but not sufficient evidence that the supplied
specification is complete.

## Planning workflow

### 1. Establish the planning snapshot

Read the complete accepted specification and applicable repository instructions.
Bind planning evidence to the strongest available identity: repository and
commit or revision when available, otherwise a named snapshot, version, and
observation time. Never invent Git provenance. Record branch, worktree state,
configuration, dependency, deployment, and runtime versions only when they
materially constrain the plan. Compare this snapshot with the specification and
evidence snapshots only across affected boundaries.

Verify every existing material path, symbol, test surface, configuration point,
schema, and operational anchor before putting it in the plan. Label an intended
new path or symbol as proposed and justify its ownership and placement from a
verified repository convention; do not present it as existing evidence. If drift
is harmless, record the evidence. If current-state facts are uncertain, state a
precise research question. If drift invalidates an accepted decision or contract,
route the affected work back to design.

### 2. Derive the work graph from vertical slices

Start with the specification's slice boundaries. Refine each into the smallest
work items that retain a meaningful integration or verification checkpoint.
Assign stable plan IDs (`P<n>`) and explicit dependencies.

Prefer work that delivers a narrow end-to-end behavior over work grouped only by
database, backend, frontend, or test layer. Permit enabling prerequisites such as
safe schema expansion, compatibility bridges, or test infrastructure when their
own completion evidence is clear and later slices consume them. Do not manufacture
parallelism or verticality that violates sequencing, migration, or safety
constraints.

### 3. Detail each work item

For each item, specify:

- the independently reviewable purpose and observable result;
- covered outcome, behavior, decision, contract, and slice IDs;
- concrete change surfaces: verified existing paths, symbols, interfaces,
  schemas, configuration, tests, and operational assets, plus clearly labeled
  proposed additions grounded in an established ownership convention;
- intended structural and behavioral changes, including behavior that must remain
  unchanged;
- implementation actions at enough precision to remove rediscovery, without
  writing code or prescribing incidental line-level mechanics;
- tests, static checks, runtime observations, migrations, rollout checks,
  observability, recovery, and rollback work needed for completion;
- dependencies, safe parallel work, and the integration checkpoint; and
- objective completion evidence an implementer can return.

Keep tests and operational work with the behavior they verify unless a genuine
shared prerequisite warrants its own item. Do not defer all integration, cleanup,
documentation, or verification to an undifferentiated final phase.

### 4. Cover cross-cutting and final verification

Account for repository documentation, compatibility windows, staged migrations,
feature flags, data backfills, security review, performance evidence, deployment,
monitoring, and cleanup when required by the accepted specification or by
applicable repository instructions and evidenced conventions. Trace each
repository-defined obligation to its source; do not turn a convention into a new
product or architecture choice. Separate reversible rollout steps from
irreversible transitions and state the safe stopping points.

Define final verification as confirmation that all slice checkpoints compose and
that preserved behaviors still hold—not as the first time components integrate.

### 5. Validate traceability and handoff

Map every in-scope outcome, behavior, decision, contract, and specification slice
to implementation work and completion evidence. Every work item must trace back
to accepted scope or an applicable repository-defined obligation; mark optional
improvements separately and exclude them from the required plan.

Keep the plan vendor-neutral. Use stable hierarchy, IDs, dependencies, and
acceptance evidence that a caller can translate into an agent queue, issue
tracker, or other work management system. Do not add time estimates, assignees,
sprints, or vendor fields unless the caller supplies the governing method and
explicitly requests that separate adaptation.

## Implementation Plan

Read `references/implementation-plan.md` and adapt its shape rather than leaving
empty boilerplate.

Set `Ready` only when all required specification identifiers and repository
obligations have implementation and verification coverage, all anchors are
verified at the planning snapshot, no work item contains an unresolved
consequential choice, dependencies form a coherent executable graph, no required
plan review remains, and another agent or work system can determine what evidence
completes each item.
