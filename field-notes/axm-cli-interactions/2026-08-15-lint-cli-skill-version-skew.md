---
subject: axm-cli-interactions
key: lint-cli-skill-version-skew
date: 2026-08-15
kind: blocked
status: open
---

**Expected:** Workspace-wide `axm lint` would validate the extension changes
against the installed AXM skill.
**Actual:** Lint stopped with one manual-attention issue because AXM CLI
`0.27.5` is outside the official AXM skill range `0.27.4`.
**Gap:** The installed CLI and its governing skill have patch-version skew, so
workspace lint cannot produce a clean result even though the changed docs
bundle passes its focused validators.
**Suggests:** Publish or install an AXM skill release whose compatibility range
includes CLI `0.27.5`.

Evidence: `axm lint` reported exactly one issue at
`.axm/extensions/@agentxm/skills/axm`, rule `workspace/axm-skill-compatible`;
the same run reported CLI `0.27.5` and official skill range `0.27.4`.
