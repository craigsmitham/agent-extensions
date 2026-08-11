---
subject: axm-cli-interactions
key: pack-publish-preview-apply-dependency-validation
date: 2026-08-11
kind: blocked
status: open
---

**Expected:** A successful explicit publish preview for a new skill and a pack
that directly depends on it should either validate the public-dependency
condition or prevent any upload before the same apply can fail that condition.
**Actual:** The preview marked both packages pending with no blockers. Apply
published the skill, then rejected the pack with the generic message `Every
pack dependency must resolve to a public, installable Registry version.` A
pack-only preview again passed, while its apply again failed identically.
**Gap:** Preview and apply disagree on a release-blocking dependency condition,
and apply partially mutates the registry before reporting the failure without
naming the unavailable dependency or recovery action.
**Suggests:** Validate pack dependency visibility and installability during
preview, preflight the complete selection before uploads, and identify the
failing dependency plus an exact recovery command.

Evidence: AXM 0.25.8 previewed
`@craigsmitham/skills/prune-work@0.0.1` and
`@craigsmitham/packs/work-management@0.1.0` as two pending publications. The
matching apply published only the skill. Registry views then showed both
`prune-work@0.0.1` and the existing `refine-work@0.0.1`, but a second pack-only
preview/apply pair reproduced the mismatch.
