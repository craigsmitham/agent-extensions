---
id: 2026-08-28T155043Z-k7m2
subject: axm-cli-interactions
key: evaluator-runner-canonical-path
observed_at: "2026-08-28T15:50:43Z"
session: codex-8f2c
kind: workaround
status: open
---

**Expected:** The enabled evaluator's runner guide would exist at the pack-default path `.axm/extensions/@agentxm/skills/agent-skill-evaluator/src/references/runner.md` stated by runner-selection guidance.
**Observed:** Reading that path failed because it does not exist; the enabled evaluator is materialized at `agent_extensions/agentxm/@agentxm/skills/agent-skill-evaluator/src/references/runner.md`.
**Impact:** One failed read and one bounded file search were required before evaluation validation could continue.
**Recovery:** Read the runner guide from the canonical acquired-package tree; the original task continued.
**Detected by:** `cat` returned exit status 1 with `No such file or directory` for the documented path.
**Observed factors:** AXM CLI 0.28.1; project scope; evaluator installed and enabled through `@agentxm/packs/agent-engineering`.
**Diagnostic evidence:** Failed path `.axm/extensions/@agentxm/skills/agent-skill-evaluator/src/references/runner.md`; recovered path `agent_extensions/agentxm/@agentxm/skills/agent-skill-evaluator/src/references/runner.md`.
**Hypothesis:** The runner-selection reference assumes a user-scope materialization path rather than resolving the active project-scope canonical package.
**Suggests:** Describe runner resolution through active AXM state or include the project-scope canonical acquired-package form.

Evidence: The initial read failed with exit status 1, and `rg --files` found the exact runner guide under the canonical acquired-package tree.
