---
id: 2026-08-26T130320Z-v2n8
subject: axm-cli-interactions
key: evaluator-validate-needs-package
observed_at: "2026-08-26T13:03:20Z"
session: unknown
kind: workaround
status: open
---

**Expected:** The repository instruction `node agent_extensions/agentxm/@agentxm/skills/agent-skill-evaluator/src/scripts/agent-skill-eval.mjs validate` would discover and validate workspace-authored Agent Skill suites.
**Observed:** The command exited 2 and reported `No workspace-authored Agent Skill packages were discovered; pass --package explicitly.`
**Impact:** Evaluation-source validation required one corrected invocation with the package path supplied; elapsed impact was not measured.
**Recovery:** Used the command's documented `validate --package PATH` form for `skills/research`; the original task remained in progress.
**Detected by:** Direct execution of the repository-required validator command.
**Observed factors:** Evaluator source was the repository-bound `@agentxm/skills/agent-skill-evaluator` package; the target was the workspace-authored `skills/research` package.
**Diagnostic evidence:** Process exit status 2; complete diagnostic: `No workspace-authored Agent Skill packages were discovered; pass --package explicitly.`
**Hypothesis:** Automatic discovery does not recognize this repository's authored package layout or current workspace state.
**Suggests:** Include `--package skills/<name>` in the repository validation instruction, or make discovery cover the configured authoring root.

Evidence: Evaluator help explicitly lists `validate [--package PATH]`, and the no-argument validation required that flag at runtime.
