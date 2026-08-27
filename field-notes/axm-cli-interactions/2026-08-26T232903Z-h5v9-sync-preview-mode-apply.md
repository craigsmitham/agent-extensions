---
id: 2026-08-26T232903Z-h5v9
subject: axm-cli-interactions
key: sync-preview-mode-apply
observed_at: "2026-08-26T23:29:03Z"
session: w3p9
kind: gap
status: open
---

**Expected:** `axm sync --preview --fail-on-change --json` would report preview mode while confirming workspace convergence.
**Observed:** The command performed no writes and returned `outcome: no-op`, but the structured result reported `mode: apply`.
**Impact:** The result's mode field could not be used as evidence that the command was a preview; no task delay was measured.
**Recovery:** Confirm preview semantics from the invoked flags, zero committed units, and unchanged workspace state.
**Detected by:** Comparison of the invoked flags with the structured result.
**Observed factors:** AXM CLI 0.28.1; project workspace; `--preview`; `--fail-on-change`; JSON output; workspace already converged.
**Diagnostic evidence:** Command exit status `0`; result `ok: true`; contract `plan-result-v3`; outcome `no-op`; mode `apply`; message `Workspace materialization is up to date`; total units `0`; committed units `0`.
**Hypothesis:** The no-op result uses a default apply-mode label even when resolution was requested as a preview.

Evidence: The command line included `--preview`, while its successful no-op result explicitly reported `mode: apply` and no committed work.
