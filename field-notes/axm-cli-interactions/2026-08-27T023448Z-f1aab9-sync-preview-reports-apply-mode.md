---
id: 2026-08-27T023448Z-f1aab9
subject: axm-cli-interactions
key: sync-preview-reports-apply-mode
observed_at: "2026-08-27T02:34:48Z"
session: d0fbda7e
kind: gap
status: open
---

**Expected:** `axm sync --preview --fail-on-change --json` should identify its
result as a preview, based on the requested `--preview` mode.
**Observed:** The successful no-op result reported `"mode": "apply"`.
**Impact:** The verification output was ambiguous about whether the command had
used preview semantics; no retry or mutation occurred, and work continued using
the no-op outcome and zero planned changes.
**Recovery:** Confirmed the result was `no-op` with all change counts zero and
continued; the original documentation task completed.
**Detected by:** Inspection of the command's complete structured JSON result.
**Observed factors:** AXM CLI `0.28.1`; command
`axm sync --preview --fail-on-change --json`; exit status `0`; clean lint result
before the preview.
**Diagnostic evidence:** Result `ok: true`; contract `plan-result-v3`; outcome
`no-op`; mode `apply`; total, planned, ready, committed, failed, blocked, and
warning counts all `0`; message `Workspace materialization is up to date`.
**Hypothesis:** unknown
**Suggests:** Make the result mode reflect preview execution, or document why a
no-op preview reports apply mode.

Evidence: A preview request completed successfully without planned or applied
changes, while its machine-readable result labeled the mode as apply.
