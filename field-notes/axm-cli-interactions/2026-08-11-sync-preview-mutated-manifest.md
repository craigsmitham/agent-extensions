---
subject: axm-cli-interactions
key: sync-preview-mutated-manifest
date: 2026-08-11
kind: gap
status: open
---

**Expected:** `axm sync @craigsmitham/rules/field-notes --preview --json`
would report its proposed changes without writing canonical package content.

**Actual:** After the preview reported a proposed rule version of `0.1.4`, the
canonical `rule.json` contained `"version": "0.1.4"` even though the preceding
version apply had written `0.1.3`.

**Gap:** The scoped preview changed the authored manifest while reporting an
`outcome` of `previewed`, violating the expected read-only preview boundary.

**Suggests:** Make scoped sync preview transactions read-only and add a
regression check that hashes canonical package content before and after every
preview path.

Evidence: AXM 0.25.8; `axm version
@craigsmitham/rules/field-notes patch --json` reported an applied transition
from `0.1.2` to `0.1.3`; the subsequent targeted sync preview reported
`proposed version=0.1.4`; validation immediately afterward found version
`0.1.4` in `.axm/extensions/@craigsmitham/rules/field-notes/rule.json`.
