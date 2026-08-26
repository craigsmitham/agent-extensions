---
id: 2026-08-26T151040Z-k7p9
subject: axm-cli-interactions
key: projected-research-skill-path-missing
observed_at: "2026-08-26T15:10:40Z"
session: s8f3k2
kind: gap
status: open
---

**Expected:** The installed `researcher` role instructed the caller to read `.axm/extensions/@craigsmitham/skills/research/src/SKILL.md` before delegating execution, so that path should have resolved from the active workspace.
**Observed:** Reading the instructed path failed because it does not exist; the source was available instead at `skills/research/src/SKILL.md`.
**Impact:** Research delegation was delayed by one failed read and two discovery reads; no research evidence or workspace authority was lost.
**Recovery:** Located the repository-owned skill with `rg --files`, read `skills/research/src/SKILL.md` and its referenced evidence/report contracts, and continued the task.
**Detected by:** `sed` returned a missing-file diagnostic while following the installed role instructions.
**Observed factors:** The workspace had been loaded successfully by `axm knowledge concepts`; the projected `researcher` file exists under `.agents/skills/`, while the referenced `.axm/extensions/.../research/` path does not.
**Diagnostic evidence:** command `sed -n '1,420p' .axm/extensions/@craigsmitham/skills/research/src/SKILL.md`; exit status `2`; diagnostic `sed: .axm/extensions/@craigsmitham/skills/research/src/SKILL.md: No such file or directory`.
**Hypothesis:** The managed researcher projection retained a source-layout path that is not projected into this workspace.
**Suggests:** Project the sibling research skill at the referenced path or emit a workspace-resolvable canonical path in the researcher instructions.

Evidence: The failed path and exit status were preserved from the original read. `rg --files -uu` returned `skills/research/src/SKILL.md`, which restored progress.
