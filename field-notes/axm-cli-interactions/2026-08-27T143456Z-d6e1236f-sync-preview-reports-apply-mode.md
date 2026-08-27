---
id: 2026-08-27T143456Z-d6e1236f
subject: axm-cli-interactions
key: sync-preview-reports-apply-mode
observed_at: "2026-08-27T14:34:56Z"
session: 28a43f14
kind: gap
status: open
---

**Expected:** `axm sync --preview --fail-on-change --json` should identify its result as preview mode while proving repository convergence without applying changes.
**Observed:** The successful no-op result reported `mode: "apply"` despite the explicit `--preview` flag.
**Impact:** Verification required inspecting the outcome, counts, and units rather than relying on the reported mode; no repository change occurred.
**Recovery:** Confirmed `outcome: "no-op"`, zero planned or committed units, and an empty `units` array, then continued.
**Detected by:** Inspection of the structured AXM sync result.
**Observed factors:** AXM CLI `0.28.1`; command `axm sync --preview --fail-on-change --json`; clean compatible workspace; no candidate extensions present.
**Diagnostic evidence:** Process exit status `0`; contract `plan-result-v3`; outcome `no-op`; mode `apply`; all counts `0`; units `[]`.
**Hypothesis:** The plan-result mode field reflects the sync engine's execution path instead of the requested preview policy.

Evidence: A preview-only convergence check completed successfully without changes but labeled the result as apply mode.
