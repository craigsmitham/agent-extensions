---
id: 2026-08-26T171033Z-r4k8
subject: axm-cli-interactions
key: agent-engineering-sibling-path
observed_at: "2026-08-26T17:10:33Z"
session: 01a03ef4-7b39-7b60-9aa1-d9fa07e72092
kind: gap
status: open
---

**Expected:** The installed `author-agent-skill` would route project-scope AXM work to the current canonical location of its required Agent Engineering sibling.
**Observed:** The skill requires `.axm/extensions/@agentxm/knowledge/agent-engineering/src/`, while AXM 0.28.1 project help identifies acquired project packages under `agent_extensions/`; the required sibling is present at `agent_extensions/agentxm/@agentxm/knowledge/agent-engineering/src/` and `.axm/extensions/` is absent.
**Impact:** Resolving the authoring guidance required one additional reconciliation between the skill text and live AXM project-scope help before work could continue.
**Recovery:** Used the compatible AXM 0.28.1 project-scope authority and the acquired canonical sibling under `agent_extensions/`; the original task continued.
**Detected by:** Reading the required authoring workflow after `axm lint --json` and `axm skills show author-okf --json` established clean project state.
**Observed factors:** AXM CLI 0.28.1; project scope; `author-okf` workspace source version 0.1.3; lint exit category `clean`; author-agent-skill acquired through the Agent Engineering pack.
**Diagnostic evidence:** `axm lint --json` exited 0 with compatibility `compatible` and zero findings; `axm skills show author-okf --json` exited 0 and reported `source: workspace`, `scope: project`, `enabled: true`.
**Hypothesis:** The authoring skill still encodes a user-scope canonical path while current project scope uses `agent_extensions/`.
**Suggests:** Express the sibling route through the active AXM scope model or document both project and user canonical locations.

Evidence: The required literal path is absent in this project, current AXM help names `agent_extensions/` for acquired project skills, and the required Agent Engineering knowledge files are available there.
