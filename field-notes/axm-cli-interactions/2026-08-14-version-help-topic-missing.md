---
subject: axm-cli-interactions
key: version-help-topic-missing
date: 2026-08-14
kind: gap
status: open
---

**Expected:** `axm help version` would describe the `axm version` command named
by the repository publishing guide, consistent with the instruction to read the
relevant AXM help before a package mutation.
**Actual:** AXM 0.27.4 returned `Unknown help topic 'version'` and listed no
versioning topic.
**Gap:** A supported release command has no discoverable corresponding help
topic in the local CLI's help catalog.
**Suggests:** Add a `version` help topic or route the unknown-topic response to
the authoritative versioning documentation.

Evidence: From this workspace on 2026-08-14, `axm help version` exited after
reporting the topic unknown; `docs/publishing.md` invokes `axm version` and
requires relevant help to be read before package mutations.
