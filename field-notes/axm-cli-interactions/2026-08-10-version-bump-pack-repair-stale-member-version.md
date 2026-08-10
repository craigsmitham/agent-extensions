---
subject: axm-cli-interactions
key: version-bump-pack-repair-stale-member-version
date: 2026-08-10
kind: blocked
status: open
---

**Expected:** After `axm version` successfully bumped three workspace-authored
skills, pack repair would resolve those canonical workspace versions when
reviewing dependency constraints updated to the new versions.

**Actual:** `axm packs repair
@craigsmitham/packs/codebase-change-workflow --accept-current` rejected
`@craigsmitham/skills/conduct-codebase-research: ^0.0.2` because trusted
workspace state still reported version `0.0.1`.

**Gap:** The version command updated canonical manifests without updating the
workspace version state used by authored-pack repair, leaving no recovery step
in the command output for accepting the intended member version bumps.

**Suggests:** Make `axm version` update the authored workspace version baseline,
or make pack repair resolve reviewed canonical workspace member versions and
report the exact command when another trust transition is required.

Evidence: `axm version @craigsmitham/skills/conduct-codebase-research patch`
reported `0.0.1 -> 0.0.2`; the subsequent pack repair exited with conflict:
`requires ^0.0.2, but trusted workspace state has 0.0.1`.
