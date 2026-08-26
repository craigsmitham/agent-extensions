---
id: 2026-08-26T200537Z-b8n2
subject: axm-cli-interactions
key: agent-engineering-installed-sibling-path
observed_at: "2026-08-26T20:05:37Z"
session: s-r4k7
kind: workaround
status: open
---

**Expected:** The author-agent-skill route's direct `.axm/extensions/@agentxm/...` sibling path would resolve after AXM reported the agent-engineering pack installed and enabled.
**Observed:** That path did not exist in the project workspace; the installed sibling content was available under `agent_extensions/agentxm/@agentxm/...`.
**Impact:** Reading the required authoring references required one failed path lookup and one alternate repository lookup.
**Recovery:** Used the canonical installed package tree named by the repository's managed Knowledge index and continued.
**Detected by:** `rg` reported an I/O error for the prescribed `.axm/extensions` path.
**Observed factors:** AXM 0.28.1 reported `@agentxm/packs/agent-engineering` version `0.10.6` installed and enabled in project scope.
**Diagnostic evidence:** Initial `rg` exit status `1`, `No such file or directory`; recovery `rg` exit status `0` under `agent_extensions/agentxm/@agentxm/`.
**Hypothesis:** The path convention in the skill assumes a different canonical-root projection than this project workspace uses.

Evidence: The failed and successful path lookups occurred consecutively while resolving the required maintenance, evaluation, and AXM-profile references.
