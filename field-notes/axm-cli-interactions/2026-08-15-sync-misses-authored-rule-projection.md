---
subject: axm-cli-interactions
key: sync-misses-authored-rule-projection
date: 2026-08-15
kind: gap
status: open
---

**Expected:** `axm sync --preview` would report the managed instruction-region
update after the canonical bodies of enabled workspace-authored rules changed.
**Actual:** The preview reported “Workspace materialization is up to date,” and
`axm lint` reported no findings while `AGENTS.md` still contained both previous
rule bodies.
**Gap:** Canonical authored rule content and its managed instruction projection
can differ without sync or lint surfacing the drift.
**Suggests:** Include enabled workspace-authored rule content in sync planning
and projection-drift linting, or document the command that reconciles this
state.

Evidence: AXM 0.27.5; enabled workspace-authored rules
`@craigsmitham/rules/yagni@0.1.0` and
`@craigsmitham/rules/tidy-first@0.1.0`; observed on 2026-08-15 before versioning.
