---
subject: axm-cli-interactions
key: update-already-current-status
date: 2026-08-15
kind: gap
status: open
---

**Expected:** Updating an already-current extension would report that no update
was needed without first presenting it as an update to apply.
**Actual:** `axm update @agentxm/skills/axm --ignore-release-age
--non-interactive` reported “Would update 1 skill” and “1 to apply,” then
completed with “Already up to date.”
**Gap:** The planning and completion statuses describe different update
outcomes for the same successful invocation.
**Suggests:** Distinguish a resolution check from a material update in the plan,
or report the selected extension as unchanged when its installed content is
already current.

Evidence: AXM 0.27.5 in the project workspace; the command exited 0 on
2026-08-15 and selected `@agentxm/skills/axm` 0.27.5.
