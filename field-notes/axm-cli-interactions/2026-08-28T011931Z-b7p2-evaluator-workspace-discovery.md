---
id: 2026-08-28T011931Z-b7p2
subject: axm-cli-interactions
key: evaluator-workspace-discovery
observed_at: "2026-08-28T01:19:31Z"
session: 9284d25c-de46-47d1-91e2-500437eda0c9
kind: workaround
status: open
---

**Expected:** The repository-prescribed workspace validation command would
discover and validate workspace-authored Agent Skill suites.
**Observed:** The evaluator exited before validation and reported that no
workspace-authored Agent Skill packages were discovered.
**Impact:** The required validation needed one additional package-specific
invocation instead of the documented workspace-wide command.
**Recovery:** Used the runner's documented explicit `--package skills/research`
route to validate the changed package.
**Detected by:** The evaluator process exit status and primary error output.
**Observed factors:** Node.js v24.13.1; evaluator source
`agent_extensions/agentxm/@agentxm/skills/agent-skill-evaluator`; process exit
status `2`; no diagnostic output was supplied separately.
**Diagnostic evidence:** Primary output: `No workspace-authored Agent Skill
packages were discovered; pass --package explicitly.` Diagnostic output: none
supplied.
**Hypothesis:** The workspace discovery route may not recognize this
repository's configured authored skill root.
**Suggests:** Make workspace discovery honor the repository's AXM-authored
skill roots or update the prescribed command to pass those packages explicitly.

Evidence: `skills/research/evals/` exists and contains an evaluation contract
and cases, but the no-argument validator discovered no workspace-authored
packages.
