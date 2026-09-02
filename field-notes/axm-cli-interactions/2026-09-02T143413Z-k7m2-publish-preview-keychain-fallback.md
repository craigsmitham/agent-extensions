---
id: 2026-09-02T143413Z-k7m2
subject: axm-cli-interactions
key: publish-preview-keychain-fallback
observed_at: "2026-09-02T14:34:13Z"
session: k7m2
kind: workaround
status: open
---

**Expected:** The bounded publication preview would resolve its configured
registry authentication without a degraded-storage warning.
**Observed:** `axm packs publish ... --preview --json` warned that the OS
keychain was unavailable and used a restricted credential file.
**Impact:** Publication preflight continued successfully, but authentication
used a fallback storage path; no retry or extra command was required.
**Recovery:** AXM applied its own restricted-file fallback and completed the
preview with both intended candidates admitted. The task remains in progress.
**Detected by:** The retained structured publication-preview output.
**Observed factors:** AXM CLI 0.28.4; registry `agentxm`; preview only; explicit
selection of `@craigsmitham/packs/software-engineering` with workspace
dependencies; no credential value was emitted.
**Diagnostic evidence:** warning `OS keychain unavailable; using restricted
credential file.`; result `ok: true`; two pending candidates and zero blocked
or failed candidates.
**Hypothesis:** unknown

Evidence: The warning and successful result occurred in the same retained
preview output; no authentication material was exposed.
