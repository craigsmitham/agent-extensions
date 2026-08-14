---
subject: axm-cli-interactions
key: cli-skill-patch-lag-blocks-clean-index
date: 2026-08-13
kind: blocked
status: promoted
---

**Expected:** The installed official AXM skill should remain compatible with the active CLI so a clean repository can be evaluated at the Git-index boundary without an unrelated tool-version blocker.
**Actual:** With AXM CLI 0.26.7 and the official `@agentxm/skills/axm` skill at 0.26.6 with range `0.26.6`, both `axm status` and `axm lint --view git-index` reported `cli-version-incompatible`; lint suggested `axm skills install @agentxm/skills/axm --bundled --preview` as “Adopt an unmanaged skill.”
**Gap:** A patch-level CLI/skill release skew creates a blocking workspace finding, and the recovery label describes a provenance operation rather than the observed compatibility problem.
**Suggests:** Keep the bundled skill and CLI compatibility contract release-atomic, or make intentional patch skew non-blocking; report recovery in compatibility terms and verify that applying it reaches a lintable postcondition.

Evidence: Repository `agent-extensions` at Git commit `cd38511a78675120d871bd04825d3145f850a682` on 2026-08-13, initially with a clean worktree and index. `axm --version` returned 0.26.7. `axm status` reported the installed skill source as `@agentxm/skills/axm@0.26.6`, and `axm lint --view git-index` exited 1 with rule `workspace/axm-skill-compatible`.
