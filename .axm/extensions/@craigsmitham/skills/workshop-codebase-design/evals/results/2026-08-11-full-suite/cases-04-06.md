# Full-suite cases 4–6

- Runtime: Codex collaboration subagents in separate fresh contexts
- Model: Inherited session model; exact public identifier unavailable
- Tested `src/` SHA-256: `6fa0f6007b293809ddde43359963d17d27e98de3e5843dac880e9119e49bf05c`
- Reference availability: Available; not needed by these responses
- State changed: None

## Case 4 — Functional ambiguity blocks an otherwise complete design

### Raw response

I can defer unrelated remaining work, but I cannot accept the design while duplicate-request behavior remains unresolved. It governs an in-scope API behavior, persisted state, and operational interpretation, so deferring it blocks specification.

Assuming the accepted design already defines what constitutes a duplicate, choose one:

1. **Return the active export (recommended).** Treat the duplicate as an idempotent retry, return the existing export identifier/status, and create no new export record or work. Operators observe one logical export.
2. **Reject it as a conflict.** Return a conflict response referencing the active export, with no new export state. Operators can distinguish duplicate submissions from ordinary retries.
3. **Create another export.** Accept and persist a separate export. This preserves independent request semantics but permits duplicate work, records, and operator noise.

Recommendation: option 1, because it gives retry-safe semantics and keeps persisted and operational state aligned around one active export.

Decision ledger:

- **D1 — Active duplicate semantics:** Proposed; coupled behavioral/boundary decision; blocks specification and acceptance.
- **B1 — Duplicate submission while an export is active:** Unresolved; API consumer, stored-state, and operator-visible behavior depend on D1.
- **D2 — All other remaining design work:** Deferred and explicitly excluded from the accepted scope; non-blocking only if it does not alter the chosen duplicate contract.

Record status: **Discussing**, not Accepted. Please choose option 1, 2, or 3. Final acceptance must also identify the repository revision or other material evidence snapshot against which the design was validated.

### Assertion grades

- Pass — The duplicate-request behavior receives stable identifier `B1` and is not treated as an implementation detail.
- Pass — The design is not accepted with the in-scope behavior unresolved.
- Pass — D1 blocks specification; unrelated work is non-blocking only when coherently excluded.
- Pass — Final acceptance also requires a material evidence identity.

Result: **4/4**

## Case 5 — Direct evidence without Git or a research report

### Raw response

Design record status: `Discussing`

Evidence is bound to `billing-architecture-v7`, captured 2026-08-09. There is no repository, revision history, or research report, so I cannot check whether the system changed between that export and this workshop on 2026-08-11.

My current frame is:

- `O1`: Failed charges are retried.
- `O2`: One logical charge must not produce duplicate provider attempts.
- Current behavior: the request process invokes the provider once; the worker records failures but performs no retry.
- Scope: decide which component owns retry initiation and completion, including the handoff and deduplication boundary.
- Preserved behavior: the initial charge request should still result in a single logical charge.
- `B1` (`Proposed`): After a retryable provider failure, the system eventually makes another attempt according to an explicit retry policy.
- `B2` (`Proposed`): Repeated delivery, worker restarts, concurrency, or uncertain provider outcomes do not create duplicate logical charges.
- `D1` (`Proposed`, blocks specification): Which component owns retry orchestration?
- No retry limit, delay/backoff policy, terminal-failure behavior, or operator-facing behavior has yet been supplied; these remain later functional decisions.
- Material unknowns include whether the provider supports idempotency keys, what durable charge/attempt state exists, how the worker is triggered, and whether “duplicate attempt” means no duplicate provider API calls at all or no duplicate financial charge. That distinction materially affects the available design.

Please confirm or correct this frame. In particular, does “without duplicate attempts” prohibit repeated provider calls, or is repeating a call acceptable when the provider guarantees the same logical charge through idempotency?

### Assertion grades

- Pass — Direct evidence mode preserves the export identity and capture time.
- Pass — No Git branch, commit, worktree, or research report is invented.
- Pass — Evidence limits and research needs remain distinct from candidate designs.
- Pass — The response asks for frame confirmation before resolving an option.

Result: **4/4**

## Case 6 — One consequential decision at a time

### Raw response

Evidence identity for this decision is commit `c777`; no later drift evidence was supplied. Two coupled decisions remain:

- `D1` — retry-policy ownership
- `D2` — consumer-visible retry-exhaustion semantics, dependent on `D1`

`C1`: the worker currently owns attempt state.  
`C2`: the API currently exposes a terminal `failed` status.

### D1 — Where does retry policy live?

Type: Coupled  
Change kind: Mixed/boundary  
Status: Proposed — blocks specification

**Option A — Worker-owned policy and enforcement**

The worker is the sole authority for attempt eligibility, retry limits, backoff, and exhaustion. Policy parameters may enter through worker configuration, but neither the API nor consumers count or schedule attempts.

- Fits the existing attempt-state ownership at `c777`.
- Keeps retry decisions and their state in one consistency boundary.
- Avoids competing authorities during failures or concurrent processing.
- Requires the worker to communicate the terminal result clearly to the API.

**Option B — API-owned policy, worker executes attempts**

The API decides whether another attempt is allowed and instructs the worker accordingly.

- Centralizes externally visible workflow policy.
- Moves authority away from the component that currently owns attempt state.
- Introduces coordination and partial-failure risks between counting, scheduling, and execution.
- Requires a substantially stronger API–worker retry protocol.

**Recommendation: Option A.** The worker should remain the single retry authority because it already owns the state needed to make consistent retry decisions. `D2` can then define how the worker’s exhaustion decision crosses the API boundary without duplicating retry logic.

Please explicitly choose `D1-A`, `D1-B`, or a revision. I’ll then resolve `D2` and present the complete design record; neither decision can be marked accepted or the design called final before that choice.

### Assertion grades

- Pass — Both decisions appear in dependency order, but only D1 is actively resolved.
- Pass — D1 has two viable options, tradeoffs, and a recommendation.
- Pass — The response asks for explicit choice and accepts neither decision.
- Pass — It does not announce a final design for both decisions.

Result: **4/4**
