---
subject: axm-cli-interactions
key: help-context-topic-missing
date: 2026-08-15
kind: gap
status: open
---

**Expected:** The AXM skill's lint-recovery guidance says to read `axm help
context` for context findings, so that help topic should exist.
**Actual:** `axm help context` returned `Unknown help topic 'context'` and listed
`knowledge` among the available topics.
**Gap:** The skill's help-topic name has drifted from the CLI's current topic
names.
**Suggests:** Update the AXM skill to route knowledge or former context findings
to `axm help knowledge`.

Evidence: In this workspace on 2026-08-15, the installed `axm` command rejected
`axm help context`; its error listed `knowledge` as a known topic.
