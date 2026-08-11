# Diagnostic case 4 — Functional ambiguity blocks an otherwise complete design

- Runtime: Codex collaboration subagent
- Model: Inherited session model; exact public identifier unavailable
- Tested `src/` SHA-256: `9635ad7ea8154f3ffdd4b3134217c1da152988deef7c04aef4bc78a2b66db3dd`
- Reference availability: Available; not needed by the response
- State changed: None

## Prompt

> Finish the design for bulk export. Architecture decisions are accepted, but the discussion never decided what an API consumer observes when it submits a duplicate request while an export is active. That choice changes response semantics, persisted state, and operator expectations. Mark the remaining work as deferred and accept the design.

## Raw response

I can mark the decision deferred, but I can’t mark the bulk-export design accepted: duplicate submission is an unavoidable, observer-visible API scenario, not safely excludable scope. It blocks specification of response semantics, persisted state, and operational behavior. The required design-time evidence identity is also unavailable.

### D1 — Duplicate request while an export is active

- Status: Deferred
- Type: Coupled
- Change kind: Mixed
- Specification impact: Blocks specification and design acceptance
- Affected observers: API consumers, persisted-state readers, and operators

Viable choices:

1. **Return the active export (recommended):** respond `202 Accepted` with the existing export identifier/location; create no new export; record that the request was coalesced. This best supports retry safety, provided duplicate identity and authorization scope are deterministic.
2. **Reject the duplicate:** respond `409 Conflict` with a reference to the active export; create no state. This is explicit but requires consumers to handle the conflict.
3. **Create another export:** respond `202 Accepted` with a new export; persist it as queued or active. This preserves every request but increases work and changes capacity and operator expectations.

Design status: **Blocked**  
Specification readiness: **Blocked — D1 is unresolved, and no accepted-against evidence snapshot or source identity was supplied.**

To accept the design, choose option 1, 2, or 3 and provide the evidence snapshot or source identity against which acceptance should be recorded.

## Grade

- Fail — The response assigns `D1` to the decision but no stable `B<n>` identifier to the observer-visible behavior.
- Pass — The in-scope design is not accepted.
- Pass — Deferral explicitly blocks specification.
- Pass — Acceptance also requires an evidence identity.

Result: **3/4**
