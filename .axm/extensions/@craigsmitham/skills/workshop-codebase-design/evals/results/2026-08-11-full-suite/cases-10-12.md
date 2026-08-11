# Full-suite cases 10–12

- Runtime: Codex collaboration subagents in separate fresh contexts
- Model: Inherited session model; exact public identifier unavailable
- Tested `src/` SHA-256: `6fa0f6007b293809ddde43359963d17d27e98de3e5843dac880e9119e49bf05c`
- Reference availability: Available; not needed by these responses
- State changed: None

## Case 10 — Technical incompleteness blocks design acceptance

### Raw response

I can’t mark this design accepted. “Shared job state” selects a mechanism, but leaves consequential concurrency contracts unresolved. These are observable through incorrect terminal status, duplicate exports, and recovery behavior—not mere implementation details.

Status: **Discussing**  
Evidence: caller-supplied description, observed 2026-08-11; no repository revision or runtime identity supplied.  
Specification readiness: **Blocked**

Decision agenda:

- **D1 — State-transition authority:** Decide now; blocks specification.
- **D2 — Atomic consistency and duplicate-suppression boundary:** Decide after D1; blocks specification.
- **B1 — Concurrent/post-enqueue outcome:** The state ultimately observed by consumers and operators must trace to D1 and D2.

For D1, choose one:

1. **Phase ownership — recommended:** The API owns state until durable enqueue; the worker owns it afterward. The handoff boundary and permitted recovery transitions must be explicit.
2. **Shared conditional state machine:** Both may update state, but only through atomic, version-checked transitions governed by an explicit transition matrix.
3. **Single coordinator:** API and worker submit intents; one component exclusively applies state transitions.

I recommend phase ownership because it gives the simplest authority rule and prevents an API-side failure after enqueue from overwriting legitimate worker progress. Its handoff still needs an explicit atomicity contract, which D2 will address.

Please choose option 1, 2, or 3—or revise the authority rule. Until D1 and D2 are explicitly accepted, the design cannot be accepted.

### Assertion grades

- Pass — State authority and duplicate suppression are consequential design, not implementation details.
- Pass — D1 and D2 appear on the agenda and block specification.
- Pass — No ownership or consistency rule is silently added or accepted.
- Pass — The design remains `Discussing`, not `Accepted`.

Result: **4/4**

## Case 11 — Do not manufacture technical alternatives

### Raw response

The confirmed frame leaves one coupled contract decision.

**D1 — How is an absent optional note represented?**  
Evidence basis: `u100`. The caller is the observer; the existing handler, schema validation, and error boundary remain unchanged.

- **Omit `note`** — Absence is represented by no property. This matches ordinary optional-field semantics and avoids conflating “not provided” with an explicit null value. Clients must tolerate a variable object shape.
- **Return `"note": null`** — The property is always present, giving clients a stable shape. However, the schema must define the field as nullable, and callers may interpret null as an explicitly supplied empty value.

Recommendation: **omit `note`**. “Optional” most directly means the property may be absent. Moving later between omission and null would still be an observable contract change, so the choice should be fixed now.

Decision ledger:

- **B1 — Proposed:** When the note has no value, the caller observes the representation selected in D1.
- **D1 — Proposed, blocks specification:** Omit the property or serialize it as null.
- **C1 — Constrained by `u100`:** Existing handler ownership, validation, error behavior, and all persistence and operational boundaries remain unchanged.
- Classification: **mixed/boundary**—the internal serialization choice changes the caller-visible response contract.
- Verification: exercise a response with an absent note and assert the exact serialized JSON and successful schema validation; existing present-note and error scenarios must remain unchanged.

Please explicitly choose **omit** or **null**, or revise the recommendation.

### Assertion grades

- Pass — The agenda contains only the functional response-shape decision.
- Pass — Existing technical boundaries are represented by evidenced C1, not manufactured D decisions.
- Pass — Options are presented and explicit human choice is requested.
- Pass — The response stays at design level.

Result: **4/4**

## Case 12 — Authorization boundary and stakeholder visibility

### Raw response

Workshop status: **Discussing**, bound to the caller-confirmed evidence at commit `a120`. No later revision is part of the supplied frame, so material drift must be revalidated before design acceptance.

The outcomes are:

- **O1:** An assigned support agent can replay an eligible failed delivery.
- **O2:** The affected tenant’s customers can observe replay activity.
- **O3:** No caller-controlled value can enable cross-tenant replay.
- **O4:** Replay records identify the employee and capture the replay reason.

The confirmed frame establishes these constraints:

- **C1 — Constrained:** A delivery’s tenant comes from its persisted row, never from request data.
- **C2 — Constrained:** Authorization requires a current server-side assignment between the authenticated employee and that persisted tenant.
- **C3 — Constrained:** Only failed deliveries are replay-eligible.
- **C4 — Constrained:** Any tenant ID retained in the endpoint is an untrusted assertion; it cannot grant or broaden authority.

## Decision agenda

| ID | Decision | Type | Status | Why it matters |
|---|---|---|---|---|
| **D1** | How should the replay boundary derive tenant scope and address the delivery? | Coupled | Decide now | Establishes the security authority and endpoint contract. |
| **D2** | What response should an unauthorized or tenant-mismatched request receive? | Coupled | Decide after D1 | Balances support usability, information disclosure, and consistent failure semantics. |
| **D3** | What replay lifecycle prevents duplicate or stale replays under concurrency? | Coupled | Decide after D1 | Defines eligibility rechecks, idempotency, assignment revocation, and state transitions. |
| **D4** | Is a replay reason mandatory, and which audiences may see it? | Functional | Decide after D1 | The current audit record lacks the reason; customer visibility may require redaction or separate text. |
| **D5** | Which replay stages must customers observe: requested, started, succeeded, failed? | Functional | Decide after D3–D4 | Defines **B3**, the customer-visible behavior and failure experience. |
| **D6** | Which existing customer-visible surface and persistence boundary owns replay activity? | Technical | Needs research | The supplied `a120` evidence does not identify an existing customer activity contract or its transactional guarantees. This blocks technical specification of O2, but not D1. |
| **D7** | What consistency guarantee joins replay acceptance, audit history, and customer-visible activity? | Coupled | Decide after D3–D6 | Determines partial-failure recovery and whether activity can disappear while a replay proceeds. |

## First choice — D1: authority and request addressing

**Question:** How should the system identify a delivery while ensuring tenant authority is derived exclusively from server-owned state?

The affected boundary is the admin endpoint → authorization decision → replay command. This is consequential because the current endpoint authenticates an employee but trusts a request-supplied tenant ID, while the delivery row is the authoritative tenant owner.

### Option A — Delivery-first, resource-derived scope

The request identifies the delivery, not its tenant. The replay boundary loads the delivery’s persisted tenant, checks the authenticated employee’s current assignment to that tenant, and passes only server-derived tenant context downstream.

- Best fit for C1–C4 and O3.
- Removes the misleading tenant authority input.
- Makes one boundary responsible for authorization.
- Likely changes the endpoint contract, although a temporary compatibility adapter could validate and discard the old tenant assertion.
- Moderately reversible because a tenant-qualified route could be added later.

### Option B — Retain tenant-qualified addressing with conjunctive checks

Keep tenant ID plus delivery ID in the request, but require all three facts to agree: request tenant, persisted delivery tenant, and the employee’s assigned tenants. Downstream replay still uses only the persisted tenant.

- Preserves more of the existing endpoint shape.
- Makes the tenant context explicit to clients.
- Retains redundant, attacker-controlled input and requires every future path to preserve the three-way invariant.
- Easy to migrate later to Option A, but carries more long-term confused-deputy risk.

### Option C — Require a scoped replay capability

An assigned-tenant workflow issues a short-lived capability bound to employee, tenant, and delivery; replay consumes it and revalidates the assignment.

- Strongly scopes each replay request and can support deliberate approval workflows.
- Adds issuance, expiry, revocation, and workflow coupling not justified by the current outcomes.
- Most expensive option to change or remove later.

**Recommendation: Option A.** It gives the persisted delivery row and employee-assignment store sole authority, minimizes security-critical inputs, and makes the “cross-tenant replay is impossible” invariant easiest to verify. This recommendation remains **Proposed**, not accepted.

Under Option A, the observable and boundary behavior would be:

- **B1:** An authenticated employee assigned to the persisted tenant may request replay of a failed delivery.
- **B2:** An employee without that assignment cannot enqueue or cause the replay, even if they know the delivery or tenant identifier.
- **Mixed/boundary change:** The endpoint request contract and tenant provenance change.
- **Preserved behavior:** Employee authentication and persisted delivery ownership remain authoritative inputs.

Design-level verification must demonstrate:

- Assigned employee + failed delivery is accepted.
- Unassigned employee is denied despite supplying or guessing a valid tenant.
- A mismatched tenant assertion, if temporarily retained, never expands access.
- Assignment removal before authorization causes denial.
- No downstream replay step consumes caller-supplied tenant authority.

Choose **A**, **B**, or **C**, or revise the options.

### Assertion grades

- Pass — Support agents, customers, and the security boundary are all represented.
- Pass — Tenant authority, enforcement, and auditability choices are derived explicitly.
- Pass — No mechanism is silently accepted and employee authentication is not treated as tenant authority.
- Pass — Only D1 is resolved, with three options, tradeoffs, and a recommendation.
- Pass — The response remains at design level.

Result: **5/5**
