---
subject: axm-cli-interactions
key: removed-lint-rule-blocks-axm-update
date: 2026-08-14
kind: blocked
status: dropped
---

**Dropped:** This is the accepted v3-to-v4 hard break; compatibility migration for removed lint-rule configuration is intentionally out of scope.

**Expected:** Following `docs/publishing.md`, `axm update @agentxm/skills/axm --ignore-release-age` should update the workspace skill to match the already-current AXM 0.27.3 CLI.
**Actual:** AXM rejected the workspace before resolving the update because `.axm/settings.json` configures the no-longer-known `workspace/authored-content-unpublished` lint rule.
**Gap:** The release workflow requires upgrading first, but the new CLI cannot load the prior committed workspace configuration needed to perform that upgrade.
**Suggests:** Make the AXM upgrade path migrate removed lint-rule settings, or document a versioned settings migration that runs before the workspace-skill update.

Evidence: In a clean worktree at `origin/main` (`877f8ad`), AXM CLI 0.27.3 exited 9 with `SettingsDecodeError`: `lint.rules: Unknown lint rule IDs in lint.rules: workspace/authored-content-unpublished`.
