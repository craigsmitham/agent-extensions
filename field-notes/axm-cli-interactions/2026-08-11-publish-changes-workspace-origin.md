---
subject: axm-cli-interactions
key: publish-changes-workspace-origin
date: 2026-08-11
kind: gap
status: open
---

**Expected:** Publishing a workspace-authored skill should preserve its local
workspace origin, as documented by `axm help settings`.
**Actual:** After `workshop-codebase-design@0.0.4` published successfully,
`axm status --json` reported its canonical content as `wrong-origin` and
recommended adopting it again.
**Gap:** A successful publish left the authored workspace in a blocked local
reconciliation state.
**Suggests:** Preserve or restore workspace source authority when publishing an
authored package, and cover the post-publish status in a regression test.

Evidence: `scripts/check-public-safety.sh` passed immediately before the exact
three-skill publish. The publish result reported success for
`@craigsmitham/skills/workshop-codebase-design@0.0.4`. Immediately afterward,
the safety gate failed on `workspace/desired-state-reconcilable`; `axm status
--json` reported `canonical-wrong-origin` for that skill and the recovery action
`axm adopt @craigsmitham/skills/workshop-codebase-design --preview`.
