# Synthetic cache-key change with accepted risk

Assessment snapshot: repository revision `c72`, observed
2026-08-03T16:00:00Z. No relevant drift is reported.

## Accepted contract and risk

The service owner accepted:

- O1: internal profile-cache keys distinguish tenant and profile identifiers.
- B1: reads and writes use the same versioned key format.
- B2: cache misses retain current database fallback behavior.
- C1: keys contain no user-provided text or secret.
- C2: the old key format remains readable during the bounded rollout and is
  removed only after two complete cache-TTL windows report zero old-key
  fallbacks, no error-rate increase, and no more than the accepted 4 ms p95
  latency increase.

The service owner also accepted a possible increase of up to 4 ms in p95 profile
lookup latency during the first 10% rollout because dual reads occur only on old
entries, the service has 35 ms of SLO headroom, and rollback remains available.
The acceptance applies only to the 10% rollout and expires at its observation
gate.

## Current evidence and plan

- Revision `c72` verifies the key builder, read-through cache, rollout flag,
  latency metric, and rollback control.
- P1 adds the versioned writer and dual-read fallback with table-driven key
  separation and collision tests for O1 plus unit and integration tests for
  B1/B2/C1.
- P2 rolls out to 10%, observes two complete cache-TTL windows, and verifies p95
  latency, error rate, and old-key fallback counts against C2. It rolls back on
  any failed criterion and removes old-key reads only after every criterion
  passes.
- Completion evidence includes focused tests, the rollout metric query, the
  recorded two-window observation gate with each criterion, and a rollback
  exercise.
