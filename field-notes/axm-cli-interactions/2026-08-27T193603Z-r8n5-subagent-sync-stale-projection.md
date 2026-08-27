---
id: 2026-08-27T193603Z-r8n5
subject: axm-cli-interactions
key: subagent-sync-stale-projection
observed_at: "2026-08-27T19:36:03Z"
session: unknown
kind: gap
status: open
---

**Expected:** `axm sync --type subagent` would re-render the managed Codex
Researcher file after its workspace source changed, as described by
`axm help subagents`.
**Observed:** Sync reported a no-op while the managed file still contained the
prior prompt. A scoped local reinstall preview was ready, but apply refused to
install over workspace source authority and restored state atomically.
**Impact:** The canonical Researcher package is current, but the ignored local
Codex projection remains stale. The package change itself was not blocked.
**Recovery:** No projection workaround was applied; the managed file was left
untouched and canonical source remains authoritative.
**Detected by:** A direct content inspection after successful sync differed
from `subagents/researcher/src/researcher.md`.
**Observed factors:** AXM CLI `0.28.1`; project scope; workspace-sourced
Researcher `0.1.0`; sync exit status `0`; scoped reinstall exit status `6`.
**Diagnostic evidence:** Sync result: outcome `no-op`, total units `0`. Reinstall
failure: code `conflict`, disposition `restored`, message `Cannot install over
workspace-sourced subagent "researcher" with local:subagent:researcher
(conflict)`.
**Hypothesis:** unknown

Evidence: AXM reported the subagent projection current despite observable old
prompt content, then preserved workspace authority by rolling back the attempted
local-source reinstall.
