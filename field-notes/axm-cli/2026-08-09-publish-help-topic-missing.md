---
subject: axm-cli
key: publish-help-topic-missing
date: 2026-08-09
kind: gap
status: open
---

**Expected:** The repository instruction to read the relevant `axm help` topic
before acting, together with a need to validate publish guidance, suggested that
`axm help publish` would provide the publish-specific topic.
**Actual:** `axm help publish` exited nonzero and reported `Unknown help topic
'publish'`; the topic list includes `authoring`, while the AXM skill separately
directs unfamiliar commands to command-level `--help`.
**Gap:** Publish guidance has no same-named help topic, so the generic instruction
does not identify whether to use `axm help authoring` or `axm publish --help`.
**Suggests:** Name the publish help route explicitly wherever AXM requires a
relevant topic before publishing.

Evidence: `axm help publish` exited 1 and reported `not_found` at the repository
root.
