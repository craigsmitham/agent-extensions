---
id: 2026-08-21T234452Z-91787b
subject: axm-cli-interactions
key: workspace-lint-agents-projection-missing
observed_at: "2026-08-21T23:44:52Z"
session: d33b0f14590a
kind: gap
status: open
---

**Expected:** `axm lint --json` would validate the current workspace, including
the existing `AGENTS.md` projection.
**Observed:** The command exited 1 with `workspace/projections-current`, saying
the AXM-owned projection at `AGENTS.md` was missing even though the file was
present in the worktree.
**Impact:** Full-workspace lint could not provide a clean completion signal for
this documentation change; one additional help lookup and scoped validation
path were required. Elapsed delay was not measured.
**Recovery:** Continued with `axm knowledge lint` for the affected bundle and
the OKF validator; both passed. The original task continued.
**Detected by:** The JSON result and exit status from `axm lint --json`.
**Observed factors:** The worktree already contained unrelated changes to
`AGENTS.md` and AXM-managed extension state. The task changed one canonical
skill source and an untracked knowledge bundle.
**Hypothesis:** unknown

Evidence: `axm lint --json` reported one error with rule ID
`workspace/projections-current`; the focused knowledge lint and OKF validator
reported zero findings for the software-architecture bundle.
