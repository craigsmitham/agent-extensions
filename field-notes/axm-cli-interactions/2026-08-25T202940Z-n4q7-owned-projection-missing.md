---
id: 2026-08-25T202940Z-n4q7
subject: axm-cli-interactions
key: owned-projection-missing
observed_at: "2026-08-25T20:29:40Z"
session: s8f2n
kind: gap
status: open
---

**Expected:** The lockfile-compatible AXM CLI should lint the workspace and confirm its managed projections are current.
**Observed:** Lint loaded the workspace but reported that the AXM-owned root `AGENTS.md` projection was missing.
**Impact:** Package lifecycle preflight remains incomplete until desired and projected state are reconciled; no AXM-owned package mutation has started.
**Recovery:** Progress continued through canonical authored-source inspection. Projection reconciliation remains required before package lifecycle mutation.
**Detected by:** Required AXM preflight for the `gen-stack` pack migration.
**Observed factors:** Clean local `agentxm/axm` main checkout at `b57f99f7a39ebcd8fc75575ad7c3f70317c6c4de`; CLI reported `0.27.18`; project lockfile version `6`; command `lint --json` against the agent-extensions workspace.
**Diagnostic evidence:** Process exit status `1`; rule `workspace/projections-current`; severity `error`; subject `.`; affected projection `AGENTS.md`; AXM skill compatibility `compatible` for CLI `0.27.18` and installed skill `0.27.15`.
**Hypothesis:** unknown

Evidence: The structured result returned `ok: false`, one error finding, and no warnings or informational findings. No workspace mutation was attempted.
