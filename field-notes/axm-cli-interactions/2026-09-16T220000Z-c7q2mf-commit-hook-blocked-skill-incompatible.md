---
id: 2026-09-16T220000Z-c7q2mf
subject: axm-cli-interactions
key: commit-hook-blocked-skill-incompatible
observed_at: "2026-09-16T22:00:00Z"
session: 76c596d8-0a1f-4563-8ba9-65ac5787063d
kind: observation
status: open
---

**Expected:** `git commit` of the staged `spec` skill addition would succeed after the pre-commit AXM check.
**Observed:** The pre-commit hook ran an AXM check against view `git-index`, returned `ok: false` with one error, `workspace/axm-skill-compatible`, and the commit was not created. There were no findings about the staged changes.
**Impact:** Blocking. A workspace-wide compatibility advisory unrelated to the staged content prevents every commit until the bundled AXM skill is refreshed.
**Outcome:** The first commit attempt failed. After user approval, the recovery was applied; `axm lint --json` then reported compatibility `compatible` with 0 errors, and the commit was retried. The hook was not bypassed.
**Recovery:** `axm skills install @agentxm/skills/axm --bundled` (previewed first)
**Detected by:** Pre-commit hook output during `git commit`.
**Observed factors:** axm 0.31.1; bundled AXM skill 0.29.4; the same incompatibility was recorded earlier today in note `2026-09-16T214850Z-8wh946` as non-blocking lint output.
**Diagnostic evidence:** ruleId `workspace/axm-skill-compatible`; severity `error`; kind `advisory`; reasonCode `cli-version-incompatible`; summary `exitCategory: errors`; nextAction `axm skills install @agentxm/skills/axm --bundled --preview`.

Evidence: the pre-commit hook's JSON output from one `git commit` attempt in this session.
