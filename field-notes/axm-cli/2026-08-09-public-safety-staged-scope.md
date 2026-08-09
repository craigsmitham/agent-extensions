---
subject: axm-cli
key: public-safety-staged-scope
date: 2026-08-09
kind: blocked
status: open
---

**Expected:** Committing one staged field note could run the repository safety
gate against the exact proposed commit without requiring unrelated worktree
changes to be release-ready.
**Actual:** `scripts/check-public-safety.sh` reported six AXM findings from
unstaged, locally modified extension packages while the staged field note itself
was the only intended commit content.
**Gap:** The gate has no staged-only mode, so unrelated work in progress blocks
or obscures validation of an otherwise isolated commit.
**Suggests:** Add a documented staged-index gate, or make the safety script
accept a staged-only mode that preserves its public-safety checks.

Evidence: The staged diff contained one new field-note file; the gate reported
`workspace/desired-state-reconcilable`, `workspace/knowledge-state-valid`, and
four `workspace/authored-content-unpublished` findings for unstaged packages.
