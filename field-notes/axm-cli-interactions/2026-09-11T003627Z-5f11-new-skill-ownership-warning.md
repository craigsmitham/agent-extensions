---
id: 2026-09-11T003627Z-5f11
subject: axm-cli-interactions
key: new-skill-ownership-warning
observed_at: "2026-09-11T00:36:27.232049+00:00"
session: devops-docs-01a08dcc
kind: gap
status: open
---

**Expected:** A skill created by AXM would have resolvable ownership in AXM lint, based on the successful managed creation result.
**Observed:** After `axm skills new devops-docs --json` reported applied, lint reported `workspace/managed-file-unowned` for `./skills/devops-docs`, as it already did for nine existing authored skills.
**Impact:** The new package could not receive a warning-free lint result. Additional scoped convergence verification was needed; elapsed cost not measured.
**Recovery:** Continued canonical authoring. Scoped FQN sync preview reported no-op and materialization up to date.
**Detected by:** Post-authoring `axm lint --json`.
**Observed factors:** AXM 0.28.12; project-authored `@craigsmitham/skills/devops-docs`; compatible bundled skill; source manifest updated from scaffold 0.0.1 to 0.1.0.
**Diagnostic evidence:** Creation process exit 0, `ok: true`, `outcome: applied`, unit `skill:devops-docs` committed. Lint `ok: true`, rule `workspace/managed-file-unowned`, severity warning, observed “Agent skill artifact has no AXM ownership proof.” Lint summary errors 0, warnings 10. Scoped sync process exit 0, `outcome: no-op`.
**Hypothesis:** unknown
