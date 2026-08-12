---
subject: axm-cli-interactions
key: multi-selector-publish-preview-symbol-error
date: 2026-08-12
kind: workaround
status: open
---

**Expected:** An exact publish preview naming two skill selectors would preflight
both packages as one selection before upload.
**Actual:** AXM stopped during candidate preparation with `Cannot convert a
Symbol value to a string` and returned an internal-error envelope.
**Gap:** The documented multi-selector publish path failed before it could
report the reviewed package selection.
**Suggests:** Make publish candidate preparation handle multiple explicit
selectors and add a regression test for the two-selector preview path.

Evidence: On 2026-08-12, authenticated as `@craigsmitham` with AXM 0.26.4,
`axm publish @craigsmitham/skills/refine-work
@craigsmitham/skills/workshop-codebase-design --preview --json` failed before
upload with error code `internal` and detail `Cannot convert a Symbol value to
a string`.
