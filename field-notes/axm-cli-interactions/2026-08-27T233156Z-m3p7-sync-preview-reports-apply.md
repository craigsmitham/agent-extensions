---
id: 2026-08-27T233156Z-m3p7
subject: axm-cli-interactions
key: sync-preview-reports-apply
observed_at: "2026-08-27T23:31:56Z"
session: s-m3p7
kind: gap
status: open
---

**Expected:** `axm sync --preview --fail-on-change --json` would identify its
result mode as preview.
**Observed:** The command exited 0 with outcome `no-op` and zero counts but
reported `mode: apply`.
**Impact:** Projection convergence required interpreting the no-op outcome and
counts separately from the contradictory mode field.
**Recovery:** Use the no-op outcome, zero planned and committed units, and
subsequent workspace checks as convergence evidence; do not claim an apply.
**Detected by:** The structured synchronization result.
**Observed factors:** AXM 0.28.1; invocation included both `--preview` and
`--fail-on-change`; warnings were zero.
**Diagnostic evidence:** Contract `plan-result-v3`; outcome `no-op`; mode
`apply`; total, planned, committed, and warnings all `0`; exit status `0`.
**Hypothesis:** unknown

Evidence: Workspace materialization was already up to date and no unit was
planned or committed despite the apply-mode label.
