# Diagnostic case 5 — Direct evidence without Git or a research report

- Runtime: Codex collaboration subagent
- Model: Inherited session model; exact public identifier unavailable
- Tested `src/` SHA-256: `9635ad7ea8154f3ffdd4b3134217c1da152988deef7c04aef4bc78a2b66db3dd`
- Reference availability: Available; not needed by the response
- State changed: None

## Prompt

> Workshop retry ownership from this versioned architecture export. There is no research report or repository checkout. Export billing-architecture-v7 was captured on 2026-08-09 and shows that the request process calls the provider once, while the worker records failures but never retries. We need failed charges retried without duplicate attempts.

## Raw response

### Workshop frame

**Evidence snapshot:** `billing-architecture-v7`, captured **2026-08-09**.

There is no repository checkout or revision history, so I cannot check for changes after that date. I’ll treat the export as the design-time evidence until a newer source is supplied.

**Current state established by the export**

- The request process invokes the payment provider once.
- The worker records failed charges.
- The worker does not retry them.
- The export does not establish the persistence model, provider idempotency capabilities, concurrency controls, or handling of ambiguous provider responses.

**Proposed outcomes**

- **O1:** Eligible failed charges are retried.
- **O2:** A charge cannot acquire overlapping or independently duplicated retry execution.
- **O3:** Retries cannot produce duplicate financial effects at the provider.
- **O4:** Every charge reaches an observable state such as succeeded, retry-scheduled, terminally failed, or awaiting reconciliation.

“Without duplicate attempts” is materially ambiguous. It could mean no concurrent retry executions, no repeated provider calls with different identities, or no duplicate financial charges. Sequential retries necessarily involve additional provider calls, so we should define this precisely before assigning ownership.

**Material unknowns**

- Whether the provider supports idempotency keys and status lookup.
- Whether failure records distinguish definitive rejection from timeout or unknown outcome.
- Which component owns the authoritative charge lifecycle.
- Whether workers can process the same charge concurrently or recover work after crashing.
- Retry eligibility, limits, backoff, cancellation, and terminal-failure policy.
- Whether the request process’s current one-call behavior must remain unchanged.

**Tentative decision agenda**

1. **D1 — Coupled, Decide now:** What exactly must be prevented as a “duplicate attempt”?
2. **D2 — Technical:** Which component owns retry initiation and completion?
3. **D3 — Coupled:** What durable state machine and idempotency invariant govern attempts?
4. **D4 — Functional:** Which failures are retryable, under what limits and timing?
5. **D5 — Coupled:** How are timeouts and other ambiguous provider outcomes reconciled?
6. **D6 — Technical:** What operational visibility and recovery controls are required?

The design record remains **Discussing**; no decisions are accepted yet.

Please confirm or correct this frame, especially whether “no duplicate attempts” means preventing duplicate provider calls, duplicate concurrent executions, duplicate financial effects, or some combination.

## Grade

- Pass — Direct evidence mode preserves the export identity and capture time.
- Pass — No Git or research-report provenance is invented.
- Pass — Evidence limits and precise unknowns remain distinct from candidate designs.
- Pass — The response requests frame confirmation before resolving an option.

Result: **4/4**
