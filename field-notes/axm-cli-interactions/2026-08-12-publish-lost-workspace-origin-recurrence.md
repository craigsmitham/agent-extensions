---
subject: axm-cli-interactions
key: publish-lost-workspace-origin-recurrence
date: 2026-08-12
kind: workaround
status: open
---

**Expected:** Publishing workspace-authored skills would preserve their
`workspace:` source, leaving the workspace safety gate no worse than before the
release.
**Actual:** Two skills that had no origin problem before the release acquired
`canonical-wrong-origin` immediately after a successful publication, doubling
the gate's blocking findings.
**Gap:** Publication still rewrites canonical origin for authored packages, so
every release enlarges the set of packages the gate blocks on, and the
recommended recovery does not shrink it.
**Suggests:** Make publication preserve workspace authorship for authored
packages, and fail the release rather than leaving the workspace in a state its
own recovery command cannot clear.

Evidence: On 2026-08-12 with AXM 0.26.6, `axm status` reported
`canonical-wrong-origin` for `@craigsmitham/skills/refine-work` and
`@craigsmitham/skills/workshop-codebase-design` only. After
`axm publish` succeeded for `@craigsmitham/skills/frame-codebase-research@0.0.5`,
`@craigsmitham/skills/conduct-codebase-research@0.0.4`, and
`@craigsmitham/skills/workshop-codebase-design@0.0.6`, the same command reported
four blocking `canonical-wrong-origin` problems, adding the two research skills.
Earlier in the same session, `axm adopt --yes` had applied successfully to both
originally affected skills without clearing either blocker.
