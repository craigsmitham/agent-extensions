---
id: 2026-09-21T162039Z-k4m8v2
subject: axm-cli-interactions
key: v7-lockfile-blocked-cli
observed_at: "2026-09-21T16:20:39Z"
session: session-k4m8v2
kind: blocked
status: open
---

**Expected:** `axm lint --json` would validate the workspace before package revision.
**Observed:** AXM 0.32.2 rejected the workspace's lockfile version 7 because it supports version 8. After preserving the old lockfile, the first sync preview also found the configured bundled AXM skill as a missing workspace-authored package.
**Impact:** Validation was blocked and required one lockfile migration plus a bundled-skill reinstall before package work could continue. Elapsed overhead was not measured.
**Outcome:** The bundled AXM skill was reinstalled through its documented preview/apply path, and `axm sync` regenerated lockfile version 8 and restored the accepted agent-engineering pack.
**Recovery:** `axm skills install @agentxm/skills/axm --bundled`, followed by `axm sync`.
**Detected by:** `axm lint --json` and `axm sync --preview --json`.
**Observed factors:** CLI version 0.32.2; original lockfile version 7; desired AXM skill entry used bundled origin.
**Diagnostic evidence:** initial exit status 9; problem code `workspace-lockfile-version-unsupported`; observedVersion 7; supportedVersion 8; first sync preview blocked `skill:axm` because `skills/axm` was absent.
**Hypothesis:** unknown

Evidence: The structured results named the incompatible lockfile, the supported version, the missing canonical path, and the recovery operations. No mutation was rerun to recover evidence.
