# Full-suite cases 13–14

- Runtime: Codex collaboration subagents in separate fresh contexts
- Model: Inherited session model; exact public identifier unavailable
- Tested `src/` SHA-256: `6fa0f6007b293809ddde43359963d17d27e98de3e5843dac880e9119e49bf05c`
- Reference availability: Available; case 14 read the supplied record shape
- State changed: None

## Case 13 — Missing operational objective remains a decision

### Raw response

I can’t mark the design accepted yet. The confirmed frame leaves consequential user-facing and operational policies undecided; accepting them implicitly would invent requirements.

Design record status: **Discussing**  
Evidence identity: confirmed direct evidence at commit `p130`; no later drift information supplied.

The agenda is:

- `D1` Delivery model — decide now.
- `D2` Latency and freshness objectives — depends on `D1`.
- `D3` Failure, retry, and availability behavior — depends on `D1`.
- `D4` Admission control and cost ceiling — depends on `D1`.
- `D5` Durable work coordination and recovery — depends on `D1–D4`.
- `D6` Report identity, persistence, and regeneration semantics.
- `D7` Compatibility and rollout behavior.

### D1 — How should users receive monthly reports?

The synchronous scan already has a four-second p95 against a ten-second gateway timeout. Fivefold event growth makes preserving the current path unsafe, although the evidence does not establish linear latency growth.

1. **Keep generation synchronous.** Preserve the current interaction and optimize or pre-aggregate enough to meet a later latency objective. This minimizes visible workflow change but retains request-time coupling and creates the greatest risk of unpredictable infrastructure cost.

2. **Generate asynchronously on demand.** A request creates durable work and immediately returns report status; users retrieve the report when ready. This bounds execution through admission control but introduces waiting whenever a report is requested.

3. **Publish monthly artifacts, with asynchronous fallback — recommended.** Generate a durable, versioned report after the reporting period closes. Normal requests serve the latest successful artifact; missing or explicitly regenerated reports enter durable asynchronous processing. This separates viewing availability from generation failures, avoids repeated full scans, and permits bounded concurrency and work quotas. It changes freshness and correction semantics, which subsequent decisions must define.

This is a mixed boundary change observable to report users and operators. The current synchronous response behavior would not be preserved under options 2 or 3.

`B1` remains unresolved: when a user requests a monthly report, whether they receive the completed artifact immediately or a visible pending state depends on `D1`. It blocks specification and design acceptance.

Please explicitly choose `D1` option 1, 2, or 3—or revise the alternatives. I recommend option 3.

### Assertion grades

- Pass — No latency, freshness, availability, or cost target is invented.
- Pass — Missing completion semantics and objectives have stable D/B identifiers and block acceptance.
- Pass — Technical delivery choices follow the visible objective gaps; a queue is not assumed mandatory.
- Pass — The design remains `Discussing` and only D1 is presented for choice.
- Pass — Performance, capacity, availability, and cost are treated as design forces.

Result: **5/5**

## Case 14 — Finalize a complete accepted design record

### Raw response

# Codebase Design Record: Optional-note response

Status: Accepted

## Inputs, Evidence, and Drift

- Change intent: Define the admin response contract so callers can distinguish an absent note from a present string.
- Evidence mode: Direct current-state evidence
- Current-state evidence: `admin-response-contract-v3`, captured 2026-08-11
- Design snapshot: `admin-response-contract-v3`, validated for acceptance at 2026-08-11T15:00:00Z
- Evidence limits: No repository revision was supplied; this design is bound to the named evidence source and capture date.
- Relevant drift: No later evidence identity was introduced before acceptance.

## Current State

Existing consumers distinguish field absence. The existing admin authorization and error boundary govern the response and remain unchanged.

## Desired Outcomes

| ID | Outcome, constraint, or non-goal | Observer | Verification |
| --- | --- | --- | --- |
| O1 | Callers can distinguish an absent note from a present string. | Admin response callers | Verify absent-note and present-string responses are observably distinct. |

## Decision Agenda

| ID | Decision question or constraint | Type | Status | Depends on | Basis or why consequential |
| --- | --- | --- | --- | --- | --- |
| D1 | Should an absent note be represented by omission or `null`? | Functional | Decide now — resolved | O1, C1, C2 | The representation is caller-visible, and existing consumers already distinguish field absence. |
| C1 | Preserve the existing admin authorization and error boundary. | Technical | Constrained | — | Established by `admin-response-contract-v3`. |
| C2 | Permit an absent or string note and reject `null`. | Technical | Constrained | — | Established by `admin-response-contract-v3`; this is evidence-constrained rather than developer-chosen. |

## Functional Behavior and Acceptance Scenarios

### B1 — Optional-note response behavior

- Observer: Admin response callers.
- Preconditions and trigger: An admin response is produced through the existing authorization and error boundary.
- Result and state transition: When no note is present, the response omits `note`. When a note is present, the response includes `note` with its string value. No persisted-state transition is introduced.
- Boundary and failure scenarios: A `null` note is rejected by the response schema. Existing authorization failures and other error behavior remain governed by C1.
- Behavior preserved: Existing consumers may continue distinguishing absence through field presence, and the existing admin authorization and error boundary remain unchanged.
- Design-level verification: Verify that an absent note produces no `note` field, a present note returns the supplied string, `null` fails schema validation, and existing authorization and error cases are unchanged.

## Change Model

### Behavioral Changes

| ID | Element | Current behavior | Desired behavior | Observer | Verification |
| --- | --- | --- | --- | --- | --- |
| D1 / B1 | Optional-note representation | Existing consumers distinguish field absence. | Omit `note` when absent and return its string when present. | Admin response callers | Exercise absent and present cases and inspect field presence and value. |

### Mixed or Boundary Changes

| ID | Element | Structural aspect | Observable effect | Affected observer |
| --- | --- | --- | --- | --- |
| C2 | Admin response schema | The schema defines `note` as absent-or-string. | Absent and string values are accepted; `null` is rejected. | Response producers, validators, and callers |

## Proposed End State

The existing admin authorization and error boundary continues to own access control and failure handling (C1). For an authorized response, the optional note is represented according to D1 and B1: the response omits `note` when no note exists and includes the exact string when one does. The response schema enforces the same boundary contract by permitting absence or a string and rejecting `null` (C2). This satisfies O1 while remaining compatible with consumers that already use field absence.

## Decision Log

### D1 — Represent an absent note by omission

- Status: Accepted
- Decision type: Functional
- Change kind: Behavioral
- Context, evidence, and supporting identity: Existing consumers already distinguish field absence, as established by `admin-response-contract-v3`, captured 2026-08-11.
- Forces and constraints: O1 requires absent and present notes to be distinguishable; C1 preserves the surrounding boundary; C2 rejects `null`.
- Affected boundaries or contracts: Admin response shape and optional-note behavior.
- Options considered: Omit `note` when absent; include `note: null` when absent.
- Decision: Omit `note` when absent and return the string when present.
- Rationale and consequences: Omission preserves the field-presence distinction already used by consumers. Callers receive a string only when the field is present, and `null` is not a valid representation.
- Revisit when: The admin response contract or consumer compatibility requirements materially change.
- Specification impact: Non-blocking

## Interfaces and Invariants

| ID | Interface, invariant, or rule | Preserve or establish | Verification |
| --- | --- | --- | --- |
| C1 | Existing admin authorization and error boundary | Preserve | Verify authorization and error scenarios remain unchanged. |
| C2 | The response schema permits `note` to be absent or a string and rejects `null`. | Establish | Validate absent, string, and `null` cases against the schema. |

## Compatibility, Migration, and Operations

Omission is compatible with existing consumers that distinguish field absence. Producers must not emit `note: null`. No migration, rollout, persisted-data, or operational change is included in the accepted scope.

## Design Acceptance

The developer accepted the complete scope—O1, B1, D1, C1, and C2—against direct evidence source `admin-response-contract-v3`, captured 2026-08-11, at 2026-08-11T15:00:00Z. There are no unresolved decisions or exclusions.

Specification readiness: Ready

### Assertion grades

- Pass — Direct evidence source, capture date, and exact acceptance time are recorded without invented Git provenance.
- Pass — O1, B1, D1, C1, and C2 trace through the applicable record sections and verification.
- Pass — C2 is a constrained agenda item with evidence basis and is not logged as a human D decision.
- Pass — The record is `Accepted` and specification readiness is `Ready`.
- Pass — The record shape is selective, complete, and contains no implementation work.

Result: **5/5**
