---
id: 2026-08-27T212412Z-f3b
subject: axm-cli-interactions
key: sync-preview-reports-apply
observed_at: "2026-08-27T21:24:12Z"
session: 3764bb
kind: gap
status: open
---

**Expected:** `axm sync --preview --fail-on-change --json` would identify the
result mode as preview while reporting whether reconciliation would change the
workspace.
**Observed:** The command exited `0` with outcome `no-op` and message
`Workspace materialization is up to date`, but its structured result reported
`mode: apply`.
**Impact:** The no-change convergence result required separate interpretation
from its reported mode; no file change was observed and elapsed cost was not
measured.
**Recovery:** Used the no-op outcome, zero counts, subsequent projection byte
comparison, and workspace status as convergence evidence without claiming that
an apply occurred.
**Detected by:** Final AXM convergence verification for the Plan skill update.
**Observed factors:** AXM CLI `0.28.1`; command included `--preview` and
`--fail-on-change`; result counts were all zero.
**Diagnostic evidence:** process exit `0`; contract `plan-result-v3`; outcome
`no-op`; reported mode `apply`; warnings `0`.
**Hypothesis:** unknown

Evidence: The preserved structured result contains both the preview invocation
and the contradictory apply-mode label while reporting no planned or committed
units.
