---
subject: axm-cli-interactions
key: axm-skill-context-help-topic
date: 2026-08-14
kind: gap
status: open
---

**Expected:** The installed AXM skill directs lint findings for context extensions to `axm help context`, so that help topic should exist.
**Actual:** `axm help context` exited with a `not_found` error; `axm help` lists `knowledge` as the current topic for Knowledge bundles.
**Gap:** The installed skill's lint-routing table uses a removed or renamed AXM help topic.
**Suggests:** Update the AXM skill to route Knowledge findings to `axm help knowledge`.

Evidence: On 2026-08-14 in this workspace, `axm help context` reported “Unknown help topic 'context'”; `axm help` listed `knowledge` and did not list `context`.
