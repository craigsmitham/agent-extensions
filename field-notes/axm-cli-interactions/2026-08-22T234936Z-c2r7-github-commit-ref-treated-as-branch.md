---
id: 2026-08-22T234936Z-c2r7
subject: axm-cli-interactions
key: github-commit-ref-treated-as-branch
observed_at: "2026-08-22T23:49:36Z"
session: audit-4f9c
kind: gap
status: open
---

**Expected:** A GitHub source locator with a full commit SHA in the documented final `@ref` position would resolve that immutable public revision during `--preview`.
**Observed:** AXM attempted a shallow clone using the SHA as a remote branch and failed because no branch had that name.
**Impact:** One preview failed and the downstream workspace could not be pinned to the unpublished AgentXM commit through that locator form.
**Recovery:** Keep the installed registry version explicit and bind the audit directly to the checked-out public Git commit; the task continued.
**Detected by:** The CLI network error envelope and nested Git error.
**Observed factors:** AXM CLI 0.27.15; locator `github:agentxm/agent-extensions//.axm/extensions/@agentxm/packs/agent-engineering@031a07d`; `--preview --non-interactive`; the commit exists on the remote `main` branch.
**Hypothesis:** Provider shorthand implements shallow branch or tag resolution and does not accept commit SHAs as refs.
**Suggests:** Support immutable commit refs or state the branch/tag-only restriction in install help.

Evidence: Git reported `Remote branch 031a07d not found in upstream origin` during the preview clone.
