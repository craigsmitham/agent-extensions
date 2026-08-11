# Full-suite cases 1–3

- Runtime: Codex collaboration subagents in separate fresh contexts
- Model: Inherited session model; exact public identifier unavailable
- Tested `src/` SHA-256: `6fa0f6007b293809ddde43359963d17d27e98de3e5843dac880e9119e49bf05c`
- Reference availability: Available; not needed by these responses
- State changed: None

## Case 1 — Relevant research-to-design drift

### Raw response

The retry-ownership decision cannot be responsibly workshopped from the r111 report because the relevant ownership changed before design began at d222.

Current frame:

- Evidence snapshot: `r111`; API process owned retry scheduling.
- Design snapshot: `d222`; scheduling reportedly moved into the worker.
- Material drift: ownership, control flow, failure recovery, and possibly timing/lifecycle contracts changed.
- Change intent and desired outcomes beyond “decide retry ownership” are not yet stated.

Decision ledger:

- **D1 — Which component should own retry scheduling?**
  - Type: Coupled functional/technical
  - Status: **Needs research**
  - Blocks specification: Yes
- **B1 — Observable retry behavior**
  - Status: **Needs research**
  - Includes retry timing, duplicate prevention, restart behavior, and terminal-failure handling.

Required scoped research question:

> At `d222`, what triggers retry scheduling, which component has authoritative retry state, how does work flow from failure through rescheduling, and what contracts govern persistence, concurrency, process restarts, duplicate attempts, and terminal failure?

The design record is therefore **Blocked**, not merely awaiting a preference. Once that boundary is revalidated at `d222` or a later exact revision, we can compare viable ownership options without relying on stale assumptions.

Please confirm this frame and provide or authorize refreshed evidence for that scoped question, along with the desired outcome or problem the ownership decision is meant to solve.

### Assertion grades

- Pass — The frame distinguishes `r111` from `d222` and names the ownership drift.
- Pass — The retry ownership decision is `Needs research`; no option is recommended or accepted.
- Pass — The research question is precise and scoped to the affected retry boundary.
- Pass — No unrelated area is used as grounds for broader research.

Result: **4/4**

## Case 2 — Irrelevant research-to-design drift

### Raw response

## Workshop frame

Status: **Discussing**

- **Intent:** Decide how invoice IDs should be exposed to consumers.
- **Research snapshot:** `r333`.
- **Design snapshot:** `d444`.
- **Drift assessment:** The intervening changes are irrelevant because they affect only the marketing site and do not touch the relevant interfaces, configuration, dependencies, deployment, or runtime behavior. The `r333` evidence therefore remains applicable at `d444`, based on your supplied drift classification.
- **O1:** Consumers can obtain the appropriate invoice identifier through a defined, stable contract.
- **B1:** Which consumers observe the ID, where they observe it, and its format, stability, and failure semantics remain unresolved.
- **D1:** What consumer-facing invoice-ID contract should be established? **Proposed; blocks specification.**

The material evidence limit is that the `r333` findings themselves were not included. I need their relevant contents before presenting viable options—particularly the current exposure paths, consumer types, existing identifier forms and ownership, compatibility constraints, and known failure or security boundaries.

Is this frame accurate? If so, please provide the `r333` research report or its relevant findings.

### Assertion grades

- Pass — Both snapshots and the basis for irrelevant drift are recorded.
- Pass — Refreshed research is not demanded merely because the repository advanced.
- Pass — The response asks for frame confirmation before resolving D1.
- Pass — No option is recommended or accepted from snapshot labels alone.

Result: **4/4**

## Case 3 — Snapshot changes before acceptance

### Raw response

The design cannot be accepted against `d666` yet. The persistence-schema change is material drift at a mixed boundary: it may affect stored data, compatibility with existing records, migration safety, and failure behavior.

Updated workshop state:

- Evidence snapshot used for discussion: `d555`
- Current design snapshot: `d666`
- Record status: `Blocked`
- Any persistence-dependent decision remains `Needs research`; prior discussion does not constitute acceptance.
- Unaffected decisions may remain `Proposed`, but must also be revalidated before final acceptance.

The precise current-state question is:

> At `d666`, what persistence schema, invariants, read/write ownership, versioning or migration behavior, compatibility requirements, and failure semantics now constrain the candidate design—and does the design still satisfy them for both existing and newly written data?

Please provide the scoped `d555`→`d666` evidence for that persistence boundary, including relevant schema/migration changes and tests or documented contracts. Once revalidated, we can determine whether the candidate remains viable, requires revision, or must be superseded. Final acceptance must record the exact revalidated `d666` identity—preferably the full commit hash—and validation time.

### Assertion grades

- Pass — A scoped drift check against `d666` is required before acceptance.
- Pass — Persistence-dependent decisions are reopened while unaffected decisions remain separable.
- Pass — The record remains `Blocked`, not `Accepted`.
- Pass — Later acceptance must record the exact validated snapshot and validation time.

Result: **4/4**
