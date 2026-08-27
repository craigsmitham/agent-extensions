---
id: 2026-08-27T000930Z-q8m2
subject: axm-cli-interactions
key: authoring-sibling-paths-absent
observed_at: "2026-08-27T00:09:30Z"
session: g1b7
kind: gap
status: open
---

**Expected:** The `author-agent-skill` workflow said its required knowledge and
runner references were available beneath `.axm/extensions/@agentxm/` in the
active AXM scope.
**Observed:** All nine directly stated knowledge, runner-selection, and runner
reference paths returned `No such file or directory` with process exit status
`1`.
**Impact:** Skill-authoring preflight required an additional canonical-package
resolution step; elapsed delay was not measured.
**Recovery:** Continue through the AXM-resolved canonical acquired-package
paths and existing agent projections; task completion remained in progress.
**Detected by:** Direct reads of every required path failed.
**Observed factors:** AXM CLI `0.28.1`; project scope; workspace lint clean;
skill compatibility compatible; current repository uses project-authored and
acquired extension storage.
**Diagnostic evidence:** Nine `sed` invocations each exited `1` and reported
`No such file or directory` for a path beneath `.axm/extensions/@agentxm/`.
**Hypothesis:** The skill documents a user-scope-style sibling path that is not
the active project-scope canonical layout.

Evidence: Every required direct path named by the workflow was absent in the
active project, while AXM preflight had already established a valid project
workspace.
