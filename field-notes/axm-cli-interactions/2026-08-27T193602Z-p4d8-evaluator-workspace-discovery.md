---
id: 2026-08-27T193602Z-p4d8
subject: axm-cli-interactions
key: evaluator-workspace-discovery
observed_at: "2026-08-27T19:36:02Z"
session: unknown
kind: workaround
status: open
---

**Expected:** The repository-prescribed evaluator validation command without a
package argument would discover workspace-authored Agent Skills.
**Observed:** The validator found no packages and required an explicit
`--package` argument.
**Impact:** Validation required one additional invocation; elapsed overhead was
not measured.
**Recovery:** Re-running the same validator with `--package skills/research`
completed successfully with no findings.
**Detected by:** The structured validator result returned `ok: false`.
**Observed factors:** Agent Skill evaluator `0.2.2`; repository root; first
command exit status `2`; recovery command exit status `0`.
**Diagnostic evidence:** Result output: `No workspace-authored Agent Skill
packages were discovered; pass --package explicitly.` The recovery result
identified `skills/research` and reported an empty findings array.
**Hypothesis:** unknown

Evidence: Workspace-wide discovery returned zero packages, while explicit
selection of the canonical Research package validated successfully.
