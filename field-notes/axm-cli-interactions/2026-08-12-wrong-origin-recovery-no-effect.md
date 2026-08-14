---
subject: axm-cli-interactions
key: wrong-origin-recovery-no-effect
date: 2026-08-12
kind: blocked
status: dropped
---

**Dropped:** Superseded by the v4 authority model; the trust-derived wrong-origin predicate and adopt/status recovery loop were removed rather than retained as recovery authority.

**Expected:** Applying the recovery reported by `axm status` would restore
workspace origin and clear each `canonical-wrong-origin` blocker.
**Actual:** Adoption and scoped sync both reported successful application, but
subsequent workspace and Git-index status checks retained both blockers.
**Gap:** AXM's successful recovery results do not satisfy the postcondition
that prompted those recoveries.
**Suggests:** Make adoption and scoped sync verify that wrong-origin state is
cleared before reporting success, and roll back or return an error otherwise.

Evidence: On 2026-08-12 with AXM 0.26.6, `axm adopt` and `axm sync` were applied
to `@craigsmitham/skills/refine-work` and
`@craigsmitham/skills/workshop-codebase-design`. Repeating adoption for
`refine-work` also reported success. `axm status` and
`scripts/check-public-safety.sh --view git-index` continued to report
`canonical-wrong-origin` for both skills.
