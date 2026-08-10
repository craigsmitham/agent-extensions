# Behavioral evaluation cases

Use fresh agent contexts with synthetic repositories or repository descriptions.
Do not give the evaluator the expected output. Assess the result against the
listed invariants after each run.

## Execution cases

### 1. Relevant research-to-design drift

Prompt:

> Workshop the retry ownership decision. The research report was produced at
> commit `r111`, where the API process owned retry scheduling. Design starts at
> `d222`, where an intervening commit moved scheduling into the worker, but the
> report has not been refreshed.

Expected invariants:

- The design frame distinguishes the research and design snapshots and names the
  relevant ownership drift.
- The retry ownership decision is marked `Needs research` and paused with a
  precise current-state question.
- The stale report is not used to exclude options, justify a recommendation, or
  accept a decision.
- Unaffected decisions may continue only when their evidence remains valid.

### 2. Irrelevant research-to-design drift

Prompt:

> Workshop how invoice IDs should be exposed to consumers. Research was
> completed at `r333`; design begins at `d444`. The intervening changes affect
> only the marketing site and do not touch relevant interfaces, configuration,
> dependencies, deployment, or runtime behavior.

Expected invariants:

- The record includes both snapshots and the evidence supporting an irrelevant
  drift classification.
- The workshop may proceed without manufacturing a new research phase.
- Each decision cites evidence bound to the design snapshot.

### 3. Snapshot changes before acceptance

Prompt:

> Continue this design workshop. Decisions were discussed against `d555`, but
> the repository advanced to `d666` before acceptance. One intervening change
> modifies the persistence schema used by an accepted candidate design.

Expected invariants:

- The workshop repeats a scoped drift check before acceptance.
- Decisions affected by the schema change are reopened and cannot remain
  accepted until their evidence is revalidated.
- The record remains `Discussing` or `Blocked` while material evidence is stale.
- Final acceptance, if later granted, records the exact accepted-against snapshot
  and validation time so implementation can detect further drift.

### 4. Functional ambiguity blocks an otherwise complete design

Prompt:

> Finish the design for bulk export. Architecture decisions are accepted, but the
> discussion never decided what an API consumer observes when it submits a
> duplicate request while an export is active. That choice changes response
> semantics, persisted state, and operator expectations. Mark the remaining work
> as deferred and accept the design.

Expected invariants:

- The duplicate behavior receives a stable identifier and is treated as a
  consequential functional decision rather than an implementation detail.
- The design is not accepted for a scope that includes duplicate requests.
- Deferral records `Blocks specification` unless duplicate behavior is explicitly
  excluded from accepted scope without contradicting the requested outcome.
- Accepted outcomes, behaviors, decisions, and contracts retain stable IDs and
  design-level verification suitable for a later specification handoff.

### 5. Direct evidence without Git or a research report

Prompt:

> Workshop retry ownership from this versioned architecture export. There is no
> research report or repository checkout. Export `billing-architecture-v7` was
> captured on 2026-08-09 and shows that the request process calls the provider
> once, while the worker records failures but never retries. We need failed
> charges retried without duplicate attempts.

Expected invariants:

- The export identity and capture time are accepted as direct current-state
  evidence; no Git branch, commit, or worktree state is invented.
- The absence of a research report or live history does not block the workshop
  unless a material ownership or idempotency fact is missing.
- Evidence limits and any precise research need remain distinct from candidate
  retry designs.
- The agent confirms the frame before asking the developer to resolve a design
  option.

### 6. One consequential decision at a time

Prompt:

> The frame is confirmed. We must decide both where retry policy lives and how
> consumers learn that retries are exhausted. Present the final design for both
> decisions now. Current evidence at commit `c777` shows the worker owns attempt
> state and the API exposes a terminal `failed` status.

Expected invariants:

- Both decisions appear on the agenda, but only the first dependency-ordered
  decision is presented for choice.
- The active decision has two or three viable options, an explicit
  recommendation, and material tradeoffs.
- The agent asks for an explicit choice and does not accept either decision or
  announce a final design.
- The second decision remains proposed until the first choice is recorded.

### 7. Design request that also asks for implementation planning

Prompt:

> Workshop the design for moving session state from memory to a shared store,
> then give me the file-by-file tasks, shell commands, and review increments.
> Current evidence at commit `s888` shows sessions are process-local and rolling
> deploys route clients across old and new instances.

Expected invariants:

- The response stays at design level and does not emit tasks, commands,
  file-by-file steps, review increments, or an implementation plan.
- Planning artifacts are deferred to a separate later workflow rather than
  promised as part of the workshop.
- Migration order is discussed only as a design constraint if it affects
  compatibility, availability, or recoverability.
- The response asks the developer to confirm the frame before resolving the
  first consequential decision; no option is accepted by default.

### 8. No consequential design choice

Prompt:

> Workshop the design for renaming the local variable `retries` to
> `retryCount` inside one private function. Tests and observable behavior remain
> unchanged.

Expected invariants:

- The response explains why a formal design workshop is disproportionate.
- It does not manufacture architectural options, a decision agenda, stable IDs,
  or a Codebase Design Record.
- It does not turn the request into implementation planning or code changes.

## Pass condition

The prompt set passes when design decisions never rely on materially stale
evidence, direct evidence is usable without invented provenance, irrelevant
drift does not cause unnecessary research, the workshop preserves explicit
human choice and its design boundary, and acceptance is tied to a reproducible
snapshot or evidence identity. Accepted scope must be functionally and
technically complete, traceable, and ready for specification.
