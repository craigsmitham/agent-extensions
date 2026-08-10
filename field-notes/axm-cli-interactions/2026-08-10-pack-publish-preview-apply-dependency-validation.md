---
subject: axm-cli-interactions
key: pack-publish-preview-apply-dependency-validation
date: 2026-08-10
kind: gap
status: open
---

**Expected:** An exact pack publish preview would run the same registry
dependency validation as apply and report any dependency that would prevent the
release.

**Actual:** `axm publish
@craigsmitham/packs/codebase-change-workflow --preview --json` selected version
`0.0.4` with zero blocked or failed items, while the identical apply exited 9
with `Every pack dependency must resolve to a public, installable Registry
version. (validation)`.

**Gap:** Preview did not expose the apply-time registry dependency validation,
even though the five required skill versions had just published and were
subsequently visible through `axm view`.

**Suggests:** Run the same dependency validation during preview and name the
dependency, requested constraint, and registry status that prevents publishing.

Evidence: the rejected pack requires `frame-codebase-research@^0.0.4`,
`conduct-codebase-research@^0.0.3`, `workshop-codebase-design@^0.0.3`,
`specify-codebase-change@^0.0.2`, and `plan-codebase-change@^0.0.2`; `axm view`
reported each required version as the package's latest release immediately
after the failed apply.
