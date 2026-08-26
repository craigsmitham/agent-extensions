---
id: 2026-08-26T185741Z-j6r4
subject: axm-cli-interactions
key: agent-engineering-sibling-path
observed_at: "2026-08-26T18:57:41Z"
session: q7m2
kind: workaround
status: open
---

**Expected:** The author-agent-skill dependency would be available at its prescribed direct sibling path `.axm/extensions/@agentxm/knowledge/agent-engineering/src/`.
**Observed:** The prescribed path was absent, while the same acquired package was available at `agent_extensions/agentxm/@agentxm/knowledge/agent-engineering/src/`.
**Impact:** Loading the required skill-maintenance and evaluation guidance required one additional canonical-path resolution step.
**Recovery:** Read the required guidance from the available canonical acquired-package path without changing AXM state.
**Detected by:** Filesystem existence check before loading the author-agent-skill knowledge dependency.
**Observed factors:** AXM CLI `0.28.1`; project scope; `axm lint --json` reported a compatible clean workspace; the acquired package exists under `agent_extensions/agentxm/`.
**Diagnostic evidence:** Prescribed path existence check failed; canonical acquired-package path existence check succeeded; all five required reference files were present there.
**Hypothesis:** The authoring skill assumes a user-scope sibling layout while this project uses the project-scope acquired-package layout documented by AXM.
