---
id: 2026-08-31T190836Z-b3k9
subject: axm-cli-interactions
key: keychain-warning-on-public-view
observed_at: "2026-08-31T19:08:36Z"
session: q8v4n2
kind: gap
status: open
---

**Expected:** A public `axm view` metadata read would complete without credential-storage diagnostics.
**Observed:** Both public `axm view` calls succeeded but emitted `OS keychain unavailable; using restricted credential file.`
**Impact:** The warning added diagnostic noise to two otherwise successful public read-only calls; progress was not blocked and no retry was needed.
**Recovery:** No recovery was required; both structured results were complete and the task continued.
**Detected by:** The retained warning event accompanying each command result.
**Observed factors:** AXM CLI version 0.28.2; project workspace; public extension visibility; two parallel `axm view --json` reads.
**Diagnostic evidence:** Both exit statuses 0; warning level `warn`; result `ok: true`; warning message `OS keychain unavailable; using restricted credential file.`
**Hypothesis:** Public registry reads still initialize the configured credential-storage path even when authorization is unnecessary.

Evidence: Each original invocation retained a successful structured result separately from the identical warning event.
