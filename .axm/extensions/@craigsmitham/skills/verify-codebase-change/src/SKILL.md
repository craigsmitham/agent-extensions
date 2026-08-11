---
name: verify-codebase-change
description: Verifies an implemented codebase change against its accepted outcomes, behaviors, contracts, specification, repository obligations, and named implementation snapshot using objective evidence. Use when asked to verify, validate, audit, or confirm that a completed change is correct, complete, or ready to close. Not for pre-implementation readiness, ordinary code review, designing or planning a change, implementing fixes, or validating a deployment without an accepted change contract.
---

# Verify a codebase change

Determine whether the implemented change satisfies its accepted contract at a
named snapshot. Inspect and test; do not fix the implementation or revise the
contract.

## Verification boundary

Treat accepted outcomes, behaviors, decisions, contracts, constraints, and
applicable repository obligations as normative. A plan is supporting evidence
for intended work and completion claims, not a requirement by itself. A plan
deviation is a finding only when it violates accepted scope, an applicable
obligation, or the evidentiary basis for the change.

Accept equivalent caller-supplied artifacts and identifiers. Do not require a
particular workflow or another skill. Apply verification depth in proportion to
failure impact, irreversibility, exposure, novelty, and uncertainty.

Remain read-only. Do not edit code, generate missing tests, approve waivers,
reinterpret failed behavior, or turn the report into a remediation plan. A check
is safe only when its target and material side effects are known and confined to
disposable local state. Do not run a check that may mutate shared or external
systems, update snapshots, or rewrite implementation artifacts; use an existing
non-mutating mode or report the limitation. Record any state created by probing.
Separate observed facts, declarations, and inferences; do not treat passing tests
or an implementation summary as proof of uncovered behavior.

## Inputs and disposition

Require:

- an accepted change contract with stable intended outcomes and obligations;
- the implementation snapshot and comparison boundary needed to identify the
  actual change;
- access to relevant code, configuration, tests, and other material evidence;
  and
- any required runtime, migration, rollout, security, or operational evidence.

Use one overall disposition:

- `Verified` — every material applicable obligation is satisfied with objective
  evidence, required outcomes have been exercised at the appropriate level, and
  no material unaccepted scope or contradictory behavior remains.
- `Not Verified` — an obligation is unsatisfied, required evidence remains
  absent after available checks, or material unaccepted scope is present.
- `Blocked` — missing contract authority, snapshot identity, comparison boundary,
  access, or provenance prevents a defensible assessment. Name the exact
  unblocking input.

Classify each obligation `Satisfied`, `Unsatisfied`, `Unverified`, or `Not
Applicable`. A material `Unverified` obligation makes the change `Not Verified`
unless the missing boundary prevents the assessment as a whole, in which case
use `Blocked`.

## Workflow

### 1. Bind contract and implementation snapshots

Identify the accepted scope and strongest available acceptance identity. Bind
the implementation to a commit, revision, named export, patch, or other supplied
snapshot plus observation time; never invent Git provenance. Establish the base
or comparison boundary and record material worktree, configuration, dependency,
schema, deployment, and runtime state. Revalidate evidence affected by drift.

### 2. Determine the actual change set

Inspect the implementation and its tests rather than relying on completion
claims. Account for modified, added, generated, configuration, schema,
documentation, migration, and operational surfaces within scope. Identify
unplanned work and distinguish harmless implementation detail from unaccepted
behavior or scope.

### 3. Build the verification matrix

Trace every accepted outcome, behavior, decision, contract, slice, preservation
constraint, and applicable repository obligation to implementation evidence and
a verification method. Preserve supplied identifiers. Use plan items only to
locate intended surfaces or claimed evidence; do not fail conforming code merely
for differing from the plan.

### 4. Inspect and exercise evidence

Inspect relevant control and data flow, boundary handling, state transitions,
failure and concurrency behavior, authorization, compatibility, and preserved
behavior. Evaluate whether tests prove the claimed behavior, then run the
smallest risk-appropriate set of tests, static checks, builds, and safe runtime
observations. Before execution, establish the target and expected writes. Record
commands, target and environment, observation time, results, evidence locators,
limitations, and probe-created state without exposing secrets.

Requirements tests show conformance only for exercised cases. Add independent
weakness and failure-mode discovery where security or operational risk warrants
it. Do not infer absence of defects from green tests.

### 5. Verify transitions and outcomes

Where applicable, inspect migration safety, staged compatibility, rollout and
rollback evidence, observability, recovery, and cleanup. Attribute runtime
evidence to the verified artifact and environment. Report contract conformance
separately from evidence that the user or operational outcome is achieved; do
not claim outcome validation when only structural or unit evidence exists.

### 6. Classify findings and disposition

For each `Unsatisfied` or `Unverified` obligation, cite the expected contract,
actual implementation or missing evidence, consequence, affected scope, and a
reproduction or observation path. Note unplanned scope and material plan
deviations separately. Do not prescribe implementation details unless needed to
make a failed obligation reproducible.

## Verification Report

Read `references/verification-report.md` and adapt its shape. Keep the report
snapshot-bound and reproducible. State limitations and independence explicitly;
verification by the implementer can still be useful but is not independent
assurance.

Set `Verified` only when the matrix covers all material obligations, evidence is
current and attributable, required checks pass, preservation and adverse cases
are addressed in proportion to risk, and no material finding remains
`Unsatisfied` or `Unverified`.
