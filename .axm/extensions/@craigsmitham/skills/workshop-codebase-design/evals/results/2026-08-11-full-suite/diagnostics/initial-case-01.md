# Case 1 — Relevant research-to-design drift

- Runtime: Codex collaboration subagent
- Model: Inherited session model; exact public identifier unavailable
- Tested `src/` SHA-256: `9635ad7ea8154f3ffdd4b3134217c1da152988deef7c04aef4bc78a2b66db3dd`
- Reference availability: Available; not needed by the response
- State changed: None

## Prompt

> Workshop the retry ownership decision. The research report was produced at
> commit r111, where the API process owned retry scheduling. Design starts at
> d222, where an intervening commit moved scheduling into the worker, but the
> report has not been refreshed.

## Raw response

# Codebase Design Record: Retry scheduling ownership

Status: Blocked

## Frame

- Change intent: decide which component owns retry scheduling.
- Evidence snapshot `r111`: the API process owned retry scheduling.
- Design snapshot `d222`: an intervening change reportedly moved scheduling into the worker.
- Relevant drift: material. It changes the exact responsibility under discussion, so the `r111` report cannot safely constrain this decision.
- Evidence limit: “moved scheduling into the worker” does not establish whether the worker owns retry policy and durable authority, or only executes scheduling mechanics.

Assumed outcome `O1`: establish one unambiguous authority for retries while preserving or deliberately redefining eligibility, backoff, attempt limits, deduplication, and restart recovery.

## Decision ledger

`D1` — Which component should own retry scheduling authority at `d222`?

- Type: Coupled functional/technical
- Change kind: Mixed/boundary; ownership can affect timing, availability, recovery, deployment compatibility, and operational observability.
- Status: Needs research
- Specification impact: Blocks specification
- Affected boundaries: API-to-worker handoff, retry state, scheduling trigger, dispatch, duplicate prevention, and process-restart recovery.

## Required scoped evidence

Refresh only the affected flow at `d222`:

1. Trace a failed attempt through retry eligibility, delay calculation, durable state, wake-up, and redispatch.
2. Identify which process has authority versus which merely performs mechanics.
3. Establish the source of truth for retry state and duplicate suppression.
4. Confirm behavior when either API or worker restarts or is temporarily unavailable.
5. Check compatibility if API and worker versions can be deployed independently.
6. Determine whether the move was an intended behavioral change or a behavior-preserving restructuring.

I’m pausing before presenting ownership options because their viability and tradeoffs depend on those facts. Please confirm or correct this frame and provide a scoped `d222` evidence refresh; then we can resolve `D1` explicitly.

## Grade

- Pass — The frame distinguishes `r111` from `d222` and names the ownership drift.
- Pass — `D1` is `Needs research`; no option is recommended or accepted.
- Pass — The requested evidence is confined to the affected retry flow.
- Pass — No unrelated area is used to justify broader research.

Result: **4/4**
