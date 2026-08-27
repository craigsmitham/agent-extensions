---
id: 2026-08-27T192729Z-k7m2
subject: axm-cli-interactions
key: list-keychain-fallback
observed_at: "2026-08-27T19:27:29Z"
session: unknown
kind: gap
status: open
---

**Expected:** `axm list --json` would inspect project extension state without
credential diagnostics for this local read.
**Observed:** The command completed successfully but warned that the OS keychain
was unavailable and that AXM used a restricted credential file.
**Impact:** The local inventory remained usable; the command added an unrelated
credential warning. No retry was required.
**Recovery:** AXM's automatic fallback preserved progress and the task continued.
**Detected by:** The structured command stream emitted a warning before the final
successful result.
**Observed factors:** AXM CLI `0.28.1`; command `axm list --json`; project scope;
exit status `0`.
**Diagnostic evidence:** Diagnostic output: `OS keychain unavailable; using
restricted credential file.` Result output reported `ok: true` and 48 items.
**Hypothesis:** unknown

Evidence: A read-only project inventory checked deprecation state, emitted the
keychain fallback warning, and still returned a complete successful list.
