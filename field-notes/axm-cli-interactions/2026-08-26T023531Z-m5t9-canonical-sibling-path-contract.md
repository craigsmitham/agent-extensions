---
id: 2026-08-26T023531Z-m5t9
subject: axm-cli-interactions
key: canonical-sibling-path-contract
observed_at: "2026-08-26T02:35:31Z"
session: codex-q8r4
kind: workaround
status: open
---

**Expected:** The installed Author Agent Skill instructions said its required same-pack knowledge and runner references would resolve beneath `.axm/extensions/@agentxm/`.
**Observed:** `.axm/extensions/` was absent. AXM 0.28.1 listed the extensions as installed and enabled with canonical paths beneath `agent_extensions/agentxm/@agentxm/`, where all required references existed.
**Impact:** Required guidance reads initially failed for six files and had to be repeated against the AXM-reported canonical package path; no managed state was changed.
**Recovery:** Used `axm skills list --json`, `axm knowledge list --json`, and the reported canonical `agent_extensions/agentxm/@agentxm/` paths to resolve the installed siblings.
**Detected by:** File read failures followed by AXM installed-state output and successful reads at the reported paths.
**Observed factors:** AXM CLI version 0.28.1; project scope; `.axm/` contained only `build/`; acquired canonical packages were under `agent_extensions/agentxm/`.
**Diagnostic evidence:** Six `sed` reads returned `No such file or directory` under `.axm/extensions`; AXM reported the relevant skills `installed: true`, `enabled: true`, and canonical paths under `agent_extensions/agentxm/@agentxm/`.
**Hypothesis:** The skill guidance retains a canonical-path convention from an earlier AXM workspace layout.

Evidence: The failed `.axm/extensions` reads, AXM list results, and successful canonical-path reads were observed in the same session.
