---
subject: axm-cli-interactions
key: uninstall-preview-apply-conflict
date: 2026-08-15
kind: gap
status: open
---

**Expected:** An uninstall apply performed immediately after a clean preview
should execute the reviewed candidate or explain during preview why execution
will be blocked.
**Actual:** Preview reported one ready step with no warnings or errors, but the
immediate apply of the same candidate ID failed because the desired pack graph
was incomplete.
**Gap:** Preview and apply disagreed about whether the unchanged candidate was
executable.
**Suggests:** Validate pack-graph completeness while building the preview so a
blocked uninstall cannot be reported as ready.

Evidence: On 2026-08-15, preview and apply both reported candidate ID
`84d389858d8c0b07b8c17726037ebfaba264fa147f5ce6e8dd0097434c546c5c`;
preview had `readyCount: 1`, while apply failed with `conflict` and “Cannot
decide pack retention because the desired pack graph is incomplete.”
