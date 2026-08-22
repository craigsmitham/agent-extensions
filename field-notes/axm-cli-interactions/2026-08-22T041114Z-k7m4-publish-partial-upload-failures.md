---
id: 2026-08-22T041114Z-k7m4
subject: axm-cli-interactions
key: publish-partial-upload-failures
observed_at: "2026-08-22T04:11:14Z"
session: codex-root-20260821-evals
kind: gap
status: open
---

**Expected:** An exact 13-skill publication set admitted by `axm publish
--preview --json` should publish each selected version, or return an actionable
preflight finding before applying.
**Observed:** The apply returned `status: partial`: six versions succeeded and
seven returned `reason: upload_failed` after the same exact selection had been
admitted with no findings.
**Impact:** Publication and the dependent pack release were delayed; seven
skill identities require failure-detail inspection and a bounded retry.
**Recovery:** In progress; preserve the six successful immutable versions and
retry only after inspecting the failed outcomes.
**Detected by:** The structured apply result reported `published: 6` and
`failed: 7`.
**Observed factors:** AXM CLI and installed skill were both 0.27.15; publisher
identity was `@craigsmitham`; the Registry preview immediately before apply was
admitted with 13 pending items and no findings.
**Hypothesis:** unknown

Evidence: The failed identities were author-architecture-docs 1.1.1,
author-docs 0.3.2, author-okf 0.1.1, author-software-work-items 0.1.3,
improve-whatever 0.0.7, maintain-architecture-docs 0.2.1, and question 0.1.1.
