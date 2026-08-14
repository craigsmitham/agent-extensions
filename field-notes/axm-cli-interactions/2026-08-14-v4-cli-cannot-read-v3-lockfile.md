---
subject: axm-cli-interactions
key: v4-cli-cannot-read-v3-lockfile
date: 2026-08-14
kind: blocked
status: dropped
---

**Dropped:** This is the accepted v3-to-v4 hard break; legacy lockfile migration and backward compatibility are intentionally out of scope.

**Expected:** After removing the obsolete lint-rule setting, the current CLI should be able to perform the publishing guide's required workspace-skill update and migrate accepted resolution as needed.
**Actual:** AXM loaded settings but rejected the committed lockfile as invalid and hard-blocked the update because accepted external resolutions could not be reconstructed from observation.
**Gap:** The current CLI requires v4 accepted-resolution state but provides no usable upgrade path from the prior committed lockfile once the older CLI has been replaced.
**Suggests:** Provide a lossless lockfile migration command or make the targeted AXM-skill update migrate the last supported lockfile format before enforcing v4 validity.

Evidence: In a clean worktree at `origin/main` (`877f8ad`) with the obsolete lint rule removed, AXM CLI 0.27.3 exited 6 with `workspace:lockfile-invalid` while running `axm update @agentxm/skills/axm --ignore-release-age`.
