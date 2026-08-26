---
id: 2026-08-26T140044Z-q4m8
subject: axm-cli-interactions
key: sync-preview-noop-mode-apply
observed_at: "2026-08-26T14:00:44Z"
session: unknown
kind: gap
status: open
---

**Expected:** `axm sync --preview --json` should identify the result as a
preview or otherwise avoid labeling its mode as an apply.
**Observed:** AXM 0.28.1 returned exit status 0 with `outcome: no-op` and
`mode: apply` for the preview command.
**Impact:** The result made preview semantics ambiguous and required manual
confirmation that no unit was committed; no artifact changed.
**Recovery:** Confirmed all plan counts were `0` and the message was `Workspace
materialization is up to date`; work continued without an apply.
**Detected by:** Inspection of the complete structured sync result.
**Observed factors:** Project workspace; AXM CLI 0.28.1; plan-result-v3;
`--preview`; no-op outcome; zero units.
**Diagnostic evidence:** Exit status `0`; `ok: true`; `outcome: no-op`;
`mode: apply`; `counts.total: 0`; `counts.committed: 0`;
`counts.failed: 0`.
**Hypothesis:** unknown

Evidence: The exact preview command returned a successful no-op result whose
mode field said `apply`, while every plan count was zero.
