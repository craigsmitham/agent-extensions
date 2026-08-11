# Synthetic feature-flag retirement plan gap

Assessment snapshot: repository revision `f88`, observed
2026-08-06T10:00:00Z. No relevant drift is reported.

## Accepted contract

- O1: the completed invoice-summary behavior becomes unconditional.
- B1: enabled and disabled tenants both receive the already accepted summary.
- C1: removing the flag must not change authorization, response schema, or
  telemetry labels.
- C2: until production equivalence is observed, rollback must be possible by
  restoring flag evaluation without a data or schema reversal. Production
  equivalence requires a 60-minute shadow comparison across enabled and disabled
  tenants with zero response-schema or authorization-decision mismatches and an
  identical telemetry label set; the comparison result must be recorded.

## Current evidence and plan

- Flag evaluation, both behavior branches, response snapshots, authorization
  tests, telemetry tests, the shadow comparator, and the rollback toggle are
  verified at `f88`.
- P1 removes the disabled branch and flag reads, then runs behavior, response,
  authorization, and telemetry tests covering O1/B1/C1.
- The plan does not preserve the rollback toggle, describe another C2 safeguard,
  define the production equivalence observation, or name evidence that rollback
  remains executable.

The accepted behavior and implementation anchors are otherwise sufficient.
