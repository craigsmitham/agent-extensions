---
id: 2026-08-26T180532Z-q7m2
subject: axm-cli-interactions
key: registry-view-missing-published-extension
observed_at: "2026-08-26T18:05:32Z"
session: q7m2
kind: blocked
status: open
---

**Expected:** Registry preflight for `@craigsmitham/skills/reconcile-gen-stack` should return the published extension metadata needed to deprecate the package; local source identifies version `2.0.0`, and retained publication evidence identifies earlier published versions.
**Observed:** `axm view @craigsmitham/skills/reconcile-gen-stack --json` exited `3` with `code: not_found` and reported that the extension was not found on registry `agentxm`.
**Impact:** Registry deprecation could not proceed because AXM could not select a published candidate. Local workspace removal remained available.
**Recovery:** Preserved the failed preflight and continued only the independently authorized local removal workflow; registry deprecation remains unapplied.
**Detected by:** Required exact-target registry preflight before `axm deprecate`.
**Observed factors:** AXM CLI `0.28.1`; workspace lint compatible and clean; registry `agentxm`; local authored manifest version `2.0.0`.
**Diagnostic evidence:** Process exit `3`; error code `not_found`; affected identity `@craigsmitham/skills/reconcile-gen-stack`; retryability and request identifier were not supplied.
**Hypothesis:** unknown
