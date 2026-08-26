---
id: 2026-08-26T163633Z-a7n2
subject: axm-cli-interactions
key: sync-preview-reports-apply-mode
observed_at: "2026-08-26T16:36:33Z"
session: s8c3f
kind: gap
status: open
---

**Expected:** `axm sync --preview --fail-on-change --json` should identify the
result as a preview because the command was explicitly invoked with
`--preview`.
**Observed:** The command exited successfully with an `outcome` of `no-op`, but
the structured result reported `"mode": "apply"`.
**Impact:** The result mode could not be used as evidence that the command was a
preview; this work instead relied on the invoked command and zero planned or
committed units. No retry was performed.
**Recovery:** Continued using the unchanged projection state and separate
symlink inspection; the original task remained unblocked.
**Detected by:** Inspection of the complete JSON result after the preview.
**Observed factors:** AXM CLI version `0.28.1`; project scope; command
`axm sync --preview --fail-on-change --json`; outcome `no-op`; total, planned,
ready, committed, failed, and blocked counts all `0`; units was empty.
**Diagnostic evidence:** Process exit status `0`; result contract
`plan-result-v3`; result mode `apply`; message `Workspace materialization is up
to date`.
**Hypothesis:** unknown

Evidence: The retained command output contains the explicit preview invocation,
exit status `0`, and the contradictory structured mode value.
