---
id: 2026-09-09T174346Z-k9v3
subject: axm-cli-interactions
key: keychain-fallback
observed_at: "2026-09-09T17:43:46.339413+00:00"
session: release-r7c2
kind: gap
status: open
---

**Expected:** Registry identity preflight can use the OS keychain.
**Observed:** AXM whoami warned that the OS keychain was unavailable and used a restricted credential file; identity verification succeeded.
**Impact:** No blocked operation or manual retry; release preparation continued.
**Recovery:** Automatic restricted-file fallback; exit 0, ok true, intended publisher verified.
**Detected by:** Structured diagnostic warning separate from the successful primary result.
**Observed factors:** AXM 0.28.12 on macOS; registry identity preflight during product-engineering 2.1.0 release.
**Diagnostic evidence:** Warning message: OS keychain unavailable; using restricted credential file. No failure code or keychain cause supplied.
**Hypothesis:** unknown
