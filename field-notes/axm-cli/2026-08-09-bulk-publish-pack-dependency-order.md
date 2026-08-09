---
subject: axm-cli
key: bulk-publish-pack-dependency-order
date: 2026-08-09
kind: gap
status: open
---

**Expected:** A successful authored-catalog preview would either order new pack
dependencies before their pack or block the plan before applying it.
**Actual:** The apply published two skills, one rule, and one knowledge bundle,
then failed the new pack because every dependency must resolve to a public,
installable registry version.
**Gap:** A bulk publish can partially apply a previewed plan even though the
pack's dependencies are members of the same selection and become available
during that operation.
**Suggests:** Topologically publish dependencies before packs and re-resolve
them, or flag the dependency-order problem during preview.

Evidence: `axm publish --authored --owner @craigsmitham --on-existing verify
--yes --json` exited 9 on 2026-08-09 with four successful publishes and one
failed `@craigsmitham/packs/harness-engineering@0.0.1` result.
