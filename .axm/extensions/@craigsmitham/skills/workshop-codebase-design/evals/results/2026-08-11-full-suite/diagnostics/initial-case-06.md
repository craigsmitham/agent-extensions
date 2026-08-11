# Diagnostic case 6 — One consequential decision at a time

- Runtime: Codex collaboration subagent
- Model: Inherited session model; exact public identifier unavailable
- Tested `src/` SHA-256: `9635ad7ea8154f3ffdd4b3134217c1da152988deef7c04aef4bc78a2b66db3dd`
- Reference availability: Available; not needed by the response
- State changed: None

## Prompt

> The frame is confirmed. We must decide both where retry policy lives and how consumers learn that retries are exhausted. Present the final design for both decisions now. Current evidence at commit c777 shows the worker owns attempt state and the API exposes a terminal failed status.

## Raw response

The design cannot yet be marked final because both consequential choices require explicit acceptance. We’ll resolve them in dependency order against the supplied evidence at commit `c777`; later drift remains unverified.

## Decision agenda

| ID | Question | Status |
| --- | --- | --- |
| D1 | Which component owns retry policy and the transition to exhausted? | Decide now |
| D2 | How do consumers distinguish retry exhaustion from other terminal failures? | Pending D1 |

### D1 — Retry-policy ownership

Evidence: at `c777`, the worker owns attempt state. This makes retry evaluation consequential to the worker’s state-transition and failure contracts.

Options:

1. **Worker owns retry policy — recommended.** The worker evaluates retry eligibility, records each attempt, schedules or requests the next attempt, and atomically transitions the job to terminal failure when the limit is reached. Policy values may be supplied through configuration, but the worker remains authoritative.
   - Preserves existing state ownership.
   - Avoids split-brain decisions between attempt state and retry scheduling.
   - Can later move to a coordinator if policy becomes global, provided the policy boundary is explicit.

2. **API owns retry policy.** The API determines whether and when another attempt occurs.
   - Centralizes client-facing policy, but splits authority from worker-owned attempt state.
   - Introduces coordination and partial-failure risks when API decisions and worker state updates diverge.

3. **A separate scheduler/coordinator owns retry policy.**
   - Appropriate if retries require global admission control, fleet-wide scheduling, or sophisticated orchestration.
   - Adds a new authority, lifecycle, and consistency boundary unsupported by the supplied requirements.

Recommendation: **Option 1.** Establish the invariant that the worker is the sole authority for attempt accounting, retry eligibility, and the exhausted transition. The API remains an observer of persisted job state.

D1 remains `Proposed` and blocks D2 and specification. Please explicitly choose **Option 1, 2, or 3**, or revise the decision.

## Grade

- Pass — Both decisions appear in dependency order, but only D1 is resolved.
- Pass — D1 has three viable options, tradeoffs, and a recommendation.
- Pass — The response requests explicit choice and accepts neither decision.
- Pass — It does not announce a final design.

Result: **4/4**
