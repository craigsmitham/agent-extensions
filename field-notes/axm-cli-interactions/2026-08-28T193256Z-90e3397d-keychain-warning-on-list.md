---
id: 2026-08-28T193256Z-90e3397d
subject: axm-cli-interactions
key: keychain-warning-on-list
observed_at: "2026-08-28T19:32:56Z"
session: 90e3397d
kind: gap
status: open
---

**Expected:** `axm list --json` would report installed and enabled extension
state without credential diagnostics, as directed by the evaluator runner
selection guidance.
**Observed:** The command completed successfully but emitted `OS keychain
unavailable; using restricted credential file.` while checking deprecation
status.
**Impact:** The warning added diagnostic noise to an otherwise successful
read-only state check; progress was not blocked and no retry was needed.
**Recovery:** No recovery was required; the structured result was complete and
the task continued.
**Detected by:** The command's retained diagnostic output.
**Observed factors:** AXM CLI 0.28.1; project workspace; `axm list --json`;
deprecation checking occurred; exit status 0.
**Diagnostic evidence:** Warning level `warn`; message `OS keychain
unavailable; using restricted credential file.`; result `ok: true`; 54 items
returned.
**Hypothesis:** unknown

Evidence: The successful structured result and separate warning were both
retained from the original invocation.
