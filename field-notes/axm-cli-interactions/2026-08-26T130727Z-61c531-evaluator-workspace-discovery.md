---
id: 2026-08-26T130727Z-61c531
subject: axm-cli-interactions
key: evaluator-workspace-discovery
observed_at: "2026-08-26T13:07:27Z"
session: 49cfe7f2
kind: workaround
status: open
---

**Expected:** The repository-prescribed Agent Skill evaluation validation
command, invoked without `--package` from the active AXM workspace root, should
discover and validate every workspace-authored Agent Skill.
**Observed:** The evaluator returned exit code `2`, an empty `packages` array,
and `No workspace-authored Agent Skill packages were discovered; pass
--package explicitly.`
**Impact:** Validation could not run once across the workspace; each affected
package had to be supplied explicitly. Elapsed cost was not measured.
**Recovery:** Validate each changed package with an explicit canonical
`--package` argument.
**Detected by:** The evaluator's machine-readable result and non-zero process
status.
**Observed factors:** Node `v24.13.1`; evaluator source under
`agent_extensions/agentxm/@agentxm/skills/agent-skill-evaluator/`; project AXM
workspace with workspace-authored skills under `skills/`.
**Diagnostic evidence:** Exit code `2`; `ok: false`; `packages: []`; one
finding requesting an explicit `--package`.
**Hypothesis:** Workspace discovery expects a different canonical authored-root
layout or scope state than this project exposes.
**Suggests:** Align no-argument evaluator discovery with AXM's project-authored
skill inventory or update repository instructions to pass explicit packages.

Evidence: The exact no-argument validation command prescribed by repository
instructions ran from the workspace root and returned the structured result
above without validating any package.
