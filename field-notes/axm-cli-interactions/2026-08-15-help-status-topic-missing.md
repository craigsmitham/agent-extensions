---
subject: axm-cli-interactions
key: help-status-topic-missing
date: 2026-08-15
kind: gap
status: open
---

**Expected:** The repository publishing gate relies on AXM status and lint, so
`axm help status` should explain the status check or route to its current help
topic.
**Actual:** `axm help status` returned `Unknown help topic 'status'` and listed
`workspace-state` among the available topics.
**Gap:** The CLI exposes a status command or concept without a matching help
topic or alias.
**Suggests:** Add a `status` help topic or alias, or document
`workspace-state` as the help route for status checks.

Evidence: In this workspace on 2026-08-15, the installed `axm` command rejected
`axm help status`; its error listed `workspace-state` as a known topic.
