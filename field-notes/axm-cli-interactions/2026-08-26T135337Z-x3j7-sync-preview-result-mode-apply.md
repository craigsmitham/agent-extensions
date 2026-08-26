---
id: 2026-08-26T135337Z-x3j7
subject: axm-cli-interactions
key: sync-preview-result-mode-apply
observed_at: "2026-08-26T13:53:37Z"
session: unknown
kind: gap
status: open
---

**Expected:** `axm sync --preview --fail-on-change --json` should identify its
result as a preview or otherwise avoid labeling the mode as an apply.
**Observed:** AXM 0.28.1 returned exit status 0 with `outcome: no-op` and
`mode: apply` for the preview command.
**Impact:** The structured result made preview semantics ambiguous and required
manual confirmation that no unit was planned or committed; no artifact changed.
**Recovery:** Confirmed `counts.total`, `counts.planned`, and `counts.committed`
were all `0`, with the message `Workspace materialization is up to date`; the
documentation task completed.
**Detected by:** Inspection of the complete structured sync result.
**Observed factors:** Project workspace; AXM CLI 0.28.1; plan-result-v3;
`--preview`; `--fail-on-change`; no-op outcome; zero units.
**Diagnostic evidence:** Exit status `0`; `ok: true`; `outcome: no-op`;
`mode: apply`; `counts.total: 0`; `counts.planned: 0`;
`counts.committed: 0`; `counts.failed: 0`.
**Hypothesis:** unknown

Evidence: The exact preview command returned a successful no-op structured
result whose mode field said `apply`, while every unit count was zero.
