---
id: 2026-08-27T005226Z-a7k2
subject: axm-cli-interactions
key: managed-sibling-path-mismatch
observed_at: "2026-08-27T00:52:26Z"
session: unknown
kind: gap
status: open
---

**Expected:** The enabled Agent Engineering knowledge sibling and evaluation runner selection reference would be readable at the `.axm/extensions/...` paths prescribed by the installed `author-agent-skill` instructions.
**Observed:** Every prescribed `.axm/extensions/@agentxm/...` path was absent. `axm list --scope project --json` nevertheless reported `@agentxm/knowledge/agent-engineering` version `0.9.2` and `@agentxm/skills/evaluate-agent-skill` version `0.3.2` as installed, enabled, implicit, and active.
**Impact:** Skill-authoring guidance loading stopped for one extra state-resolution step before the Gen Stack skill could be revised.
**Recovery:** Use AXM's declared project canonical acquired-package location if the exact enabled identities are present there; otherwise leave skill authoring blocked. Task completion is not yet known.
**Detected by:** Direct reads of the instruction-prescribed paths returned `No such file or directory`.
**Observed factors:** AXM CLI `0.28.1`; `axm lint --json` exited `0` with no findings; the project inventory reports both dependencies active.
**Diagnostic evidence:** Missing paths were `.axm/extensions/@agentxm/knowledge/agent-engineering/src/...` and `.axm/extensions/@agentxm/skills/evaluate-agent-skill/src/references/runner-selection.md`; inventory command exit status `0`.
**Hypothesis:** The installed authoring instructions name a user-scope materialization path while this project exposes enabled acquired packages at the project canonical path.

Evidence: The prescribed files were absent while AXM's structured project inventory identified both exact package dependencies as active.
