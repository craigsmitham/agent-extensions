---
subject: axm-cli-interactions
key: sync-preview-additional-version-bump
date: 2026-08-11
kind: gap
status: open
---

**Expected:** After `axm version @craigsmitham/rules/field-notes patch`
reported `0.1.2 -> 0.1.3`, a targeted sync preview would materialize version
`0.1.3` without introducing another version change.

**Actual:** `axm sync @craigsmitham/rules/field-notes --preview --json`
proposed previous version `0.1.2`, proposed version `0.1.4`, with reason
`locally-modified`.

**Gap:** The scoped sync inferred an additional version bump beyond the
explicitly applied authoring version, so its proposed version did not match the
reviewed version transition.

**Suggests:** Preserve an explicit authoring version through scoped sync, or
explain why sync will advance it and identify the baseline used to derive the
new version.

Evidence: AXM 0.25.8; the version preview and apply each reported
`0.1.2 -> 0.1.3` with one successful step; the subsequent targeted sync preview
reported `previous version=0.1.2; proposed version=0.1.4;
reason=locally-modified` with one ready step and no warnings or errors.
