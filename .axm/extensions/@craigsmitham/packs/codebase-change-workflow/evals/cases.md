# End-to-end behavioral evaluation

Run this case as consecutive turns in one isolated agent session. Give the agent
the synthetic fixture, current turn, and named skill instructions. Withhold the
expected output and assertions in `evals.json` until grading.

## Turn 1 — Frame

> Use frame-codebase-research on the webhook redelivery request in the fixture.
> Treat the proposed worker-loop implementation as an assumption. Return only
> the research brief.

After verifying the brief is `Ready`, explicitly accept its question coverage.

## Turn 2 — Conduct

> The brief is accepted. Use conduct-codebase-research to answer it from the
> synthetic repository evidence at `w100`. Return only the research report.

## Turn 3 — Workshop

> Use workshop-codebase-design with the original change intent and completed
> report. The frame is confirmed. For the first decision choose worker-owned
> retry policy. For later decisions, after the skill presents each one, choose:
> three total attempts with the fixture schedule; stable delivery-key plus
> attempt-number idempotency; and `retrying` as the consumer-visible state.
> Record only explicitly chosen decisions and return no specification or plan.

After the complete record is presented, explicitly accept its in-scope design
against `w100`.

## Turn 4 — Specify

> The Codebase Design Record is explicitly accepted against `w100`. Use
> specify-codebase-change to produce the complete Change Specification. Return
> no implementation plan.

After reviewing the complete specification, explicitly accept it against
`w100` without changing its contracts.

## Turn 5 — Plan

> The specification is explicitly accepted. Use plan-codebase-change against
> planning snapshot `w110`; the fixture says the only intervening change is
> documentation. Produce the complete implementation plan.

The first planning attempt must block if the accepted response taxonomy does not
establish whether 1xx or 3xx responses can reach the worker. Only after that
precise question appears, reveal `evals/files/webhook-planning-supplement.md` and
ask the planner to resume against `w110` without reopening unaffected decisions.

Implementation now occurs outside this pack. Reveal
`evals/files/webhook-verification-supplement.md` as the resulting implementation
snapshot and reported checks.

## Turn 6 — Verify

> Use verify-codebase-change to verify the supplied implementation snapshot
> against the accepted contract. Return only the verification report and do not
> fix any finding.

The report should be `Not Verified`: the implementation classifies HTTP 429 as
terminal even though the accepted contract makes it retryable. Green reported
tests do not establish the missing 429 behavior.

## Pass condition

The case passes when every stage respects its authority boundary, provenance and
stable identifiers survive the handoffs, explicit acceptance gates every later
artifact, the planning evidence gap routes backward without invented behavior,
the accepted capability path and feasibility basis survive research, design,
specification, and planning, and verification detects a contract violation in
the actual implementation without repairing it.
