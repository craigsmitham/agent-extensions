---
subject: axm-cli-interactions
key: single-selector-publish-preview-symbol-error
date: 2026-08-12
kind: blocked
status: dropped
---

**Dropped:** Resolved by the current publish selection implementation and its explicit-selector coverage; current previews no longer reproduce the Symbol conversion failure.

**Expected:** Previewing one explicitly selected skill would report that
package's publish plan without uploading it.
**Actual:** Each single-skill preview stopped during candidate preparation with
`Cannot convert a Symbol value to a string`.
**Gap:** Reducing the publish selection to one documented explicit selector did
not avoid the candidate-preparation failure.
**Suggests:** Cover single explicit skill previews in the same candidate-
preparation regression fix as multi-selector previews.

Evidence: On 2026-08-12, authenticated as `@craigsmitham` with AXM 0.26.4,
separate `axm publish <skill-fqn> --preview --json` commands for
`@craigsmitham/skills/refine-work` and
`@craigsmitham/skills/workshop-codebase-design` each returned error code
`internal` with detail `Cannot convert a Symbol value to a string`.
