# Accepted specification and snapshot: account-tier migration

Specification status: Accepted at revision `m700` on 2026-08-09T18:00:00Z.
Planning snapshot: `m700`; all anchors below are verified.

- O1: Account reads use normalized tier records without downtime or lost updates.
- B1: During migration, old and new application versions read the same effective tier.
- B2: Writes remain accepted throughout the compatibility window.
- D1: Use expand, dual-write, backfill, read-switch, and contract stages.
- D2: Contract only after two consecutive 24-hour observation windows after the
  read switch show zero legacy reads and the reconciliation query reports no
  mismatches. Then deploy the normalized-only writer and require one further
  24-hour window with zero legacy writes and a complete, non-null normalized row
  for every account before dropping the trigger and legacy column. Cross-column
  equality is not required after the normalized-only writer starts. Any legacy
  access or incomplete telemetry resets the applicable window count.
- D3: `AccountRepository` is the single tier-read boundary for application and
  background processes and emits `account_tier_legacy_read_total` on every
  fallback to `accounts.tier`. Before the read switch, a missing normalized row or
  a null normalized tier falls back; null is never an authoritative tier.
- C1: Expand creates `account_tier(account_id PRIMARY KEY REFERENCES accounts(id)
  ON DELETE CASCADE, tier NULL)`. Null is permitted only through expand and
  backfill. After backfill reconciliation reaches zero, set `tier NOT NULL`
  before the read switch. Account creation and deletion therefore retain one
  normalized row per account without a separate lifecycle policy.
- C2: The expand migration installs `mirror_account_tier`, a database trigger that
  transactionally upserts `account_tier.tier` for every insert or update of
  `accounts.tier`, covering old versions. The first new repository release writes
  both locations in one transaction and continues doing so through the read
  switch. After D2's two clean read windows prove old versions are absent, a
  contract-ready release writes only `account_tier`. It may roll back to the
  preceding dual-write release while the legacy column remains because that
  release reads the current normalized value before writing both locations. The
  trigger and legacy column are removed only after D2's final clean-write window;
  rollback across that removal is not supported.
- C3: Backfill scans ascending immutable `account_id` values and inserts with
  `ON CONFLICT DO NOTHING`, so a concurrent dual-write always wins. Each batch
  and its exclusive high-water mark commit in one transaction. A partial batch
  failure rolls back the whole batch and leaves the mark unchanged. Changes below
  the mark are covered by dual-write and the reconciliation gate. Durable state
  lives in `account_tier_backfill_checkpoint(job_name PRIMARY KEY,
  last_account_id NULL, completed_at NULL)`. The job initializes one named row,
  locks it `FOR UPDATE` for each batch so only one runner advances, treats null as
  “before the first account,” and sets `completed_at` only after a final empty
  scan commits.
- C4: Read-switch is reversible while the legacy column remains.
- C5: Dropping `accounts.tier` is irreversible by ordinary application rollback.
- C6: While dual-write is active,
  `ops/queries/tier-reconciliation.sql` counts a mismatch when a normalized row
  is missing, null, or unequal to `accounts.tier`. The trigger increments
  `account_tier_legacy_write_total` for every legacy-column write. After the
  normalized-only writer starts, the final gate uses
  `ops/queries/tier-completeness.sql` to require exactly one non-null normalized
  row per account and monitors the legacy-write counter; it does not compare tier
  values across the two locations.
- S1: Expand schema and verify old-version compatibility.
- S2: Enable trigger-owned dual-write and verify old-version and new-version writes
  plus reconciliation under live-shaped test traffic.
- S3: Run and verify the resumable backfill.
- S4: Switch reads and observe two clean deploy windows.
- S5: Deploy the normalized-only writer, verify its accepted clean-write gate,
  then remove the trigger and legacy column at the irreversible boundary.

Verified anchors: `db/migrations/`, `src/accounts/repository.ts`,
`src/accounts/tier-backfill.ts`, `test/accounts/tier-migration.test.ts`,
`ops/queries/tier-reconciliation.sql`,
`ops/queries/tier-completeness.sql`,
`ops/dashboards/account-tier-migration.json`, and
`ops/deployments/completed-deployments.json`. The dashboard already derives
24-hour windows from the deployment record, reads both accepted legacy-access
counters, and treats absent series as incomplete telemetry. Repository policy RP1
requires migration runbooks under
`docs/runbooks/` and rehearsal with `npm run test:migrations`.
