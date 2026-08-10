---
subject: axm-cli-interactions
key: packs-add-replace-existing-no-op
date: 2026-08-10
kind: gap
status: open
---

**Expected:** After a workspace pack member moved from `0.0.1` to `0.0.2`, the
`axm packs add --replace-existing --preview` workflow would preview replacing
the pack's stale `^0.0.1` declaration with a constraint derived from the
member's current version.
**Actual:** The command returned `outcome: no-op`, `totalSteps: 0`, and "No
extensions added to pack," while `axm packs show codebase-change-workflow
--json` still reported the desired constraint and version as `^0.0.1` and
`0.0.1`.
**Gap:** The documented `--replace-existing` option does not refresh an existing
member declaration when its workspace version changes, and the no-op result
does not explain that the constraint remains stale.
**Suggests:** Replace the existing dependency constraint from the current
workspace version, or report why the declaration cannot be refreshed and name
the supported command sequence.

Evidence: AXM 0.25.8; `axm packs add codebase-change-workflow
@craigsmitham/skills/frame-codebase-research --replace-existing --preview
--json` exited 0 with a no-op result after the member manifest changed from
`0.0.1` to `0.0.2`.
