# Synthetic encryption-key migration case

Assessment snapshot: repository revision `k300`, observed
2026-08-07T18:00:00Z. No relevant drift is reported.

## Accepted contract

The security and service owners accepted:

- O1: stored customer export credentials are encrypted with key version K2.
- B1: new writes use K2 while reads support K1 and K2 during migration.
- B2: a resumable backfill re-encrypts K1 records with K2 without exposing
  plaintext outside the existing process boundary.
- C1: no credential may become unreadable during deployment, interruption, or
  rollback.
- C2: K1 retirement is irreversible and may occur only after migration safety is
  established.

The accepted sources do not define what evidence establishes migration safety or
who authorizes the irreversible K1 retirement.

## Current evidence and plan

- K1/K2 crypto adapters, credential storage, version tags, and the resumable
  batch framework are verified at `k300`.
- P1 implements dual reads and K2 writes with compatibility and failure tests.
- P2 runs the resumable backfill with batch-level counts.
- P3 retires K1 after P2 reports no batch failures.
- The plan has no complete-record reconciliation against the source population,
  unreadable-record probe, recovery exercise, partial-failure invariant, or
  rollback boundary before P3.

Authorization and deployment ordering are fully specified and covered.
