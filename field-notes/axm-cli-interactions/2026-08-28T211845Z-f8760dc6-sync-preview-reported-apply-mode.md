---
id: 2026-08-28T211845Z-f8760dc6
subject: axm-cli-interactions
key: sync-preview-reported-apply-mode
observed_at: "2026-08-28T21:18:45Z"
session: 90e3397d
kind: gap
status: open
---

**Expected:** `axm sync --preview --fail-on-change --json` would identify its
result mode as preview, consistent with the command help's no-write contract.
**Observed:** The command returned a successful no-op `plan-result-v3`, but the
structured result identified `mode` as `apply` and reported atomicity as
applied.
**Impact:** No files changed, but the structured mode could not independently
prove that the requested preview boundary was honored.
**Recovery:** Confirm the workspace remained unchanged and retain the command,
no-op outcome, zero counts, and exit status together as the verification
evidence.
**Detected by:** Inspection of the complete structured sync result.
**Observed factors:** AXM CLI 0.28.1; `--preview`; `--fail-on-change`; outcome
`no-op`; all unit counts zero; exit status 0.
**Diagnostic evidence:** Contract `plan-result-v3`; mode `apply`; message
`Workspace materialization is up to date`; declared and applied atomicity
`closure-atomic`.
**Hypothesis:** The no-op result path may reuse the apply-mode label even when
the command was invoked as a preview.

Evidence: Live help described `--preview` as non-applying, the command line
included the flag, the result reported `mode: apply`, and the worktree showed
no projection changes.
