---
subject: axm-cli-interactions
key: publish-lost-workspace-origin
date: 2026-08-12
kind: workaround
status: open
---

**Expected:** Publishing workspace-authored skills would preserve their
`workspace:` source and leave the workspace safety gate ready to validate.
**Actual:** Both successful publications were followed by
`canonical-wrong-origin` status problems requiring explicit adoption.
**Gap:** The publish operation completed remotely but did not preserve locally
usable workspace authorship for either published package.
**Suggests:** Make successful publication retain the workspace source and add a
post-publish status regression test for authored packages.

Evidence: On 2026-08-12, AXM 0.26.6 successfully published
`@craigsmitham/skills/refine-work@0.0.2` and
`@craigsmitham/skills/workshop-codebase-design@0.0.5`; the next
`scripts/check-public-safety.sh` run reported `canonical-wrong-origin` for both
and recommended `axm adopt <fqn> --preview`.
