# Behavioral evaluation cases

Run each prompt in a fresh agent context with only `src/SKILL.md` and the listed
synthetic fixture. Withhold expected outputs and assertions until grading.

## 1. A plan silently resolves a design gap

The accepted webhook-replay contract does not define what happens when the
original delivery is still in flight, while the implementation plan invents a
409 response. The assessment must be `Not Ready`, preserve unaffected accepted
scope, and route the exact missing decision to design and specification without
resolving it.

## 2. Risk-proportional readiness

A bounded internal diagnostic-field change has an accepted behavior, verified
anchor, preservation rule, work item, and executable tests. The assessment must
be `Ready` without demanding operational artifacts that cannot materially
improve confidence in this change.

## 3. Missing acceptance is Not Ready

A complete draft contract, current evidence, and plan are available, but the
named product authority has not accepted the contract. The assessment must be
`Not Ready / Needs acceptance`, not `Blocked`, because the missing approval is
known and directly routable.

## 4. Unavailable governing authority is Blocked

Two differently scoped policy documents are supplied without provenance or a
known authority that can establish which one governs. The assessment must be
`Blocked` because the intended contract boundary cannot be identified, and it
must name the exact authority or provenance needed to continue.

## 5. Explicit accepted risk can remain Ready

A complete internal cache-key change includes a bounded latency exposure that
the named service authority explicitly accepted for a limited rollout. The
assessment must remain `Ready`, retain the risk's authority, rationale, and
scope, and not use acceptance to excuse any missing contract or verification.

## 6. Contradictory accepted sources are Not Ready

Two equally authoritative accepted sources prescribe incompatible retry limits.
The contradiction is established, so the assessment must be `Not Ready` and
route reconciliation without silently choosing a source or calling the whole
assessment `Blocked`.

## 7. Material snapshot drift needs research

The accepted contract remains coherent, but current code has replaced the
planned ownership and queue anchors since the planning snapshot. The assessment
must be `Not Ready / Needs research`, preserve unaffected accepted behavior, and
require planning to resume only after the changed implementation facts are
re-established.

## 8. Missing implementation coverage needs planning

The accepted contract and current anchors are sufficient, but the plan omits a
required rollback safeguard and its verification. The assessment must be `Not
Ready / Needs planning` rather than inventing tasks or reopening accepted design.

## 9. High-risk migration receives stricter scrutiny

An encryption-key migration includes an irreversible retirement step without an
accepted retirement criterion, complete-record reconciliation, or recovery
boundary. The assessment must be `Not Ready` and route the distinct contract and
planning gaps without weakening scrutiny because most template fields exist.

## Pass condition

The cases pass when readiness means sufficient accepted constraint and objective
evidence for the actual risk—not document completeness; `Not Ready` and
`Blocked` follow a stable precedence; accepted risks remain accountable; and
consequential gaps are routed without being filled by the assessor.
