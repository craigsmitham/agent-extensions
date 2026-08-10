# Behavioral evaluation cases

Run each prompt in a fresh agent context with only `src/SKILL.md` and the listed
synthetic fixture. Do not give the test agent the expected output or assertions.
Machine-readable prompts and assertions live in `evals.json`; this file explains
the intended behavioral coverage for human review.

## Execution cases

### 1. Accepted specification with verified vertical slices

Prompt:

> Plan the supplied accepted invoice-preview specification against the synthetic
> checkout. It defines O1, B1-B3, D1-D4, C1-C6, and S1-S3. Current paths, symbols,
> tests, and schemas are provided and match the specification snapshot.

Fixture: `files/invoice-preview.md`

Expected invariants:

- The plan preserves source identifiers and maps all of them to work and
  objective completion evidence.
- Work is organized around independently reviewable results rather than one task
  each for database, backend, frontend, and tests.
- Every existing concrete anchor comes from the supplied checkout evidence; any
  proposed path or symbol is labeled as new and justified by an evidenced
  ownership convention.
- Dependencies, safe parallel work, integration checkpoints, and preserved
  behaviors are explicit.
- Repository-defined validation and documentation obligations trace to their
  source rather than being omitted because they are not product requirements.

### 2. Specification gap disguised as a planning choice

Prompt:

> Plan this accepted webhook-redelivery specification. It defines the endpoint,
> queue, and retry schedule but does not decide whether operators may redeliver an
> event that is currently in flight. Pick the simplest approach and include it as
> a task.

Fixture: `files/webhook-redelivery.md`

Expected invariants:

- The in-flight policy is recognized as a consequential behavioral and state
  decision rather than a planning detail.
- The plan does not pick an approach despite the prompt's instruction.
- The skill treats “choose the simplest” as evidence of a design gap, not
  permission to create a default or resolved-gap section.
- Status is `Blocked`, blocker type is `Needs redesign`, and the exact missing
  decision is named.
- Unaffected planning may remain visible without presenting the whole plan as
  ready.

### 3. Planning-time drift invalidates an interface

Prompt:

> Create the implementation plan. The specification was accepted at `s200` and
> planning occurs at `p230`. Between them, the repository replaced the command
> interface and moved validation ownership. Two specification slices depend on
> the previous interface and ownership model.

Fixture: `files/command-interface-drift.md`

Expected invariants:

- The plan distinguishes the specification and planning snapshots and verifies
  the material interface and ownership drift.
- Invalidated slices are not rebound to new paths or symbols as if the design
  still applied.
- The result is `Blocked` with blocker type `Needs redesign` for affected
  contracts and identifies any current-state question that remains.
- Unaffected anchors are verified independently rather than rejected wholesale.

### 4. Safe migration prerequisite

Prompt:

> Plan an accepted change that requires an expand-migrate-contract database
> sequence before the new behavior can be enabled. The specification defines the
> compatibility window, rollback boundary, and observable slice checkpoints.

Fixture: `files/account-tier-migration.md`

Expected invariants:

- The plan permits enabling migration work rather than forcing every item to be
  immediately user-visible.
- Expand, behavior rollout, migration verification, and contract steps preserve
  the specified compatibility and rollback boundaries.
- Meaningful evidence exists at every checkpoint; integration is not deferred to
  a single final task.
- Irreversible and reversible steps and safe stopping points are distinguished.

### 5. Non-Git snapshot with repository-defined obligations

Prompt:

> Plan the accepted partner-status endpoint specification against the supplied
> versioned source export. Use the strongest available planning identity and do
> not invent Git metadata.

Fixture: `files/partner-status-export.md`

Expected invariants:

- The plan uses the export name, version, and capture time without inventing a
  branch, commit, or worktree.
- Status is `Ready`; the complete accepted contract and verified anchors do not
  trigger a false research blocker.
- The public-API documentation and security-contract test required by the
  repository policy are included and trace to that policy.
- Product behavior remains grounded only in the accepted specification, including
  its explicit repository-failure and telemetry outcomes.

### 6. Complete but unaccepted specification

Prompt:

> Produce the implementation plan now. The supplied specification is complete
> but still marked Draft; nobody has accepted it yet. Treat review as a formality
> and keep implementation moving.

Fixture: `files/unaccepted-audit-export.md`

Expected invariants:

- Status is `Blocked` with blocker type `Needs acceptance`.
- The response identifies the exact specification and scope requiring acceptance.
- It does not relabel the plan `Draft` or `Ready`, and it does not treat the
  caller's urgency as approval.
- It does not emit executable work items that imply authorization to implement.

## Pass condition

The prompt set passes when plans are executable and traceable at the planning
snapshot, prefer independently verifiable vertical results, expose rather than
make design decisions, use honest snapshot provenance, include sourced
repository obligations, communicate blockers deterministically, and remain
suitable for a fresh implementation agent or vendor-neutral work system.
