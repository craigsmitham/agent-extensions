---
id: 2026-08-26T200633Z-928b7c
subject: axm-cli-interactions
key: project-acquired-source-path
observed_at: "2026-08-26T20:06:33Z"
session: 928b7c
kind: workaround
status: open
---

**Expected:** Authoring guidance should identify the project-acquired canonical
dependency path used by this workspace.
**Observed:** The guidance referenced `.axm/extensions/@agentxm/...`, which did
not exist; the same resources were present under
`agent_extensions/agentxm/@agentxm/...`.
**Impact:** The required source read needed one failed path check and one
repository search before authoring could continue.
**Recovery:** Used the project-acquired canonical path documented by
`axm help skills`; the adoption task continued.
**Detected by:** A file-existence check failed before reading the required
resources.
**Observed factors:** AXM version 0.28.1; project-scoped acquired dependencies;
the affected resources were agent-engineering knowledge and the evaluation
runner-selection reference.
**Diagnostic evidence:** The initial file-existence command exited 1 with no
result or diagnostic output. A subsequent `rg --files` search exited 0 and
returned the resources beneath `agent_extensions/agentxm/@agentxm/`.
**Hypothesis:** The authoring guidance describes a different AXM storage layout
than the project-scoped acquired layout in this workspace.
**Suggests:** Express dependency references through AXM-resolved package roots
or document both supported layouts.

Evidence: `axm help skills` identifies `agent_extensions/<scope>/<package>` as
the acquired project package path, and all required resources were found there.
