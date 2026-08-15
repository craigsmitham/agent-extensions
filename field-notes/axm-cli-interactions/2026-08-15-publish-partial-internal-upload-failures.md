---
subject: axm-cli-interactions
key: publish-partial-internal-upload-failures
date: 2026-08-15
kind: blocked
status: open
---

**Expected:** After a catalog-wide public publish preview admitted all 32
selected packages with no findings, applying the identical selection would
publish the six pending releases or return an actionable package-specific
validation error.
**Actual:** The apply published two releases, returned `upload_failed` with only
“An unexpected error occurred. (internal)” for three releases, and blocked the
docs pack because two failed uploads were its dependencies.
**Gap:** The admitted publication set applied only partially, and the registry
error did not identify whether retrying was safe or what condition caused the
failed uploads.
**Suggests:** Make catalog publication atomic when possible, or return a typed,
actionable failure with explicit retry safety and the resulting registry state
for every selected package.

Evidence: AXM 0.27.5 previewed the authored `@craigsmitham` catalog with public
visibility as 32 selected, 26 already published, six pending, and zero
findings. Applying the same selection published `author-docs@0.3.0` and
`software-engineering@0.1.0`; `audit-docs@0.1.0`, `docs@0.9.0`, and
`workflow-automation@0.1.1` failed with reason `upload_failed`; `docs@0.4.0`
was blocked by the two failed member uploads.
