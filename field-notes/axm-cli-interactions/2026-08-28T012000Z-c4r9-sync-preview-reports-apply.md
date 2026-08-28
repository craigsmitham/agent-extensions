---
id: 2026-08-28T012000Z-c4r9
subject: axm-cli-interactions
key: sync-preview-reports-apply
observed_at: "2026-08-28T01:20:00Z"
session: 9284d25c-de46-47d1-91e2-500437eda0c9
kind: gap
status: open
---

**Expected:** `axm sync --preview --fail-on-change --json` would report its
mode as `preview`.
**Observed:** The no-op preview result reported `mode: "apply"`.
**Impact:** The structured result could not independently demonstrate that the
verification was non-mutating; the original command invocation had to be
retained with the result.
**Recovery:** Retained the exact preview command and confirmed the result was a
no-op with zero committed units.
**Detected by:** Comparing the invoked flags with the structured result.
**Observed factors:** AXM 0.28.1; outcome `no-op`; zero total and committed
units; process exit status `0`; no diagnostic output was supplied.
**Diagnostic evidence:** Primary result fields included `mode: "apply"`,
`message: "Workspace materialization is up to date"`, and an empty `units`
array. Diagnostic output: none supplied.
**Hypothesis:** The no-op sync result may use the apply-mode label regardless
of the requested preview flag.
**Suggests:** Preserve `mode: "preview"` in no-op results from preview
invocations.

Evidence: The exact command included both `--preview` and `--fail-on-change`,
and it exited successfully without planned or committed changes.
