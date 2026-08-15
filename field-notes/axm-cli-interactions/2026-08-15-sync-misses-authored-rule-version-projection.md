---
subject: axm-cli-interactions
key: sync-misses-authored-rule-version-projection
date: 2026-08-15
kind: workaround
status: open
---

**Expected:** After AXM versioned the workspace-authored field-notes rule and
`axm sync` reconciled the workspace, the managed rule marker in `AGENTS.md`
would identify the canonical `0.2.0` version.
**Actual:** `axm sync` updated Knowledge discovery but left the managed rule
marker at `0.1.4`; disabling and re-enabling the rule regenerated it as
`0.2.0`.
**Gap:** Sync does not reconcile the rendered version marker of an enabled
workspace-authored rule after its manifest version changes.
**Impact:** Completing the extension update required one preview and two extra
AXM lifecycle mutations; elapsed time was not measured.
**Suggests:** Include enabled workspace-authored rule manifest versions in sync
planning and projection-drift linting.

Evidence: With canonical `@craigsmitham/rules/field-notes@0.2.0`, `axm lint`
reported no findings and `axm sync --preview` planned only Knowledge discovery;
the `AGENTS.md` marker remained `0.1.4` until `axm rules disable field-notes`
followed by `axm rules enable field-notes`.
