---
id: 2026-08-20T155203Z-w3c9
subject: axm-cli-interactions
key: registry-demote-recreates-materialization-marker
observed_at: "2026-08-20T15:52:03Z"
session: s9p4x2
kind: workaround
status: open
---

**Expected:** Returning the official AXM skill from bundled authority to Registry authority would leave the workspace ready for its public commit without an untracked package-internal marker.
**Observed:** Successful `axm demote` to `@agentxm/skills/axm@0.27.13` recreated `.axm/extensions/@agentxm/skills/axm/.axm-materialization.json` after the workspace's materialization files had been removed earlier in the session.
**Impact:** Pre-commit cleanup required deleting one newly generated untracked file.
**Recovery:** Remove the package-internal materialization marker and verify it remains absent after read-only lint and safety checks.
**Detected by:** Explicit `find .axm -name .axm-materialization.json` during post-demotion verification.
**Observed factors:** Demotion succeeded; registry source, lock, and AXM 0.27.13 compatibility were valid; the marker was untracked by Git.
**Hypothesis:** Registry materialization always creates the private completion marker, but this workspace does not ignore it.

Evidence: `find` returned exactly `.axm/extensions/@agentxm/skills/axm/.axm-materialization.json`; `git status --short` reported it as untracked.
