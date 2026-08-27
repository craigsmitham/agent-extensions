---
id: 2026-08-27T234939Z-676f
subject: axm-cli-interactions
key: publish-upload-timeout
observed_at: "2026-08-27T23:49:39Z"
session: unknown
kind: workaround
status: open
---

**Expected:** The admitted recovery publication would upload Gen Stack
Knowledge 0.25.0 within the configured deadline and then publish its dependent
Gen Stack pack.
**Observed:** The upload timed out after one attempt; AXM refused automatic
replay as unsafe, reported the pack blocked, and emitted an exact two-package
recovery command using `--on-existing verify`.
**Impact:** Publication required one exact Registry read, another preview, and
one explicit recovery command before the release could complete.
**Recovery:** Registry readback confirmed Knowledge 0.25.0 absent. The emitted
recovery selection then published Knowledge 0.25.0 and Gen Stack pack 4.2.0;
AXM exited 0 with two successes and no failed, blocked, pending, or unknown
items.
**Detected by:** Structured `publish-result-v3` apply output.
**Observed factors:** AXM 0.28.1; Gen Stack Knowledge archive 529,581 ZIP bytes,
146 included files, 15 excluded files; Registry `agentxm`; public visibility.
**Diagnostic evidence:** Exit status 16; cause code `timeout`; class `external`;
`retryable: true`; `attemptCount: 1`; `maxAttempts: 1`;
`attemptsExhausted: true`; `retryStoppedBy: replay-unsafe`; blocked dependent
`@craigsmitham/packs/gen-stack`; emitted recovery selected that dependency and
pack with `--on-existing verify`.
**Hypothesis:** The knowledge archive upload exceeded the configured Registry
request deadline on that attempt.

Evidence: The first recovery apply preserved explicit timeout and replay-safety
fields; exact Registry readback showed the version absent; the bounded emitted
recovery completed both exact versions.
