---
id: 2026-08-26T212652Z-p4n8
subject: axm-cli-interactions
key: sync-preview-reports-apply-mode
observed_at: "2026-08-26T21:26:52Z"
session: p4n8
kind: gap
status: open
---

**Expected:** `axm sync --preview --fail-on-change --json` would identify its
result as preview mode.
**Observed:** The command exited `0` with `ok: true`, `outcome: no-op`, and
`mode: apply`.
**Impact:** The result's mode was ambiguous during the convergence check; no
retry or work delay was required.
**Recovery:** The zero exit status, `no-op` outcome, “Workspace materialization
is up to date” message, and zero planned or committed counts established that
no workspace change occurred, so verification continued.
**Detected by:** Inspection of the complete structured command result.
**Observed factors:** AXM CLI `0.28.1`; command included both `--preview` and
`--fail-on-change`; every result count was zero.
**Diagnostic evidence:** Exit status `0`; contract `plan-result-v3`; outcome
`no-op`; mode `apply`; failed `0`; blocked `0`; committed `0`.
**Hypothesis:** unknown
**Suggests:** Report preview mode explicitly even when the outcome is a no-op.

Evidence: A successful no-op preview response labeled its mode as `apply`.
