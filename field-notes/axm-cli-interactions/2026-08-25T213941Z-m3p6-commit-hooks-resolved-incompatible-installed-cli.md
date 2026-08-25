---
id: 2026-08-25T213941Z-m3p6
subject: axm-cli-interactions
key: commit-hooks-resolved-incompatible-installed-cli
observed_at: "2026-08-25T21:39:41Z"
session: s8f2n
kind: workaround
status: open
---

**Expected:** Repository commit hooks would validate a lockfile already accepted by the AXM CLI used to perform and verify the migration.
**Observed:** The hooks resolved the installed `axm` CLI `0.27.18`, which rejected the v6 workspace lockfile with `LockfileDecodeError: lockfileVersion: Expected 5`, even though the migration and explicit validation used the compatible source CLI `0.28.0`. In one consumer repository, lint-staged restored the old tree and left the complete migration only in an automatic backup stash.
**Impact:** Commits failed after migration validation, one clean-looking working tree concealed the uncommitted migration, and recovery required inspecting stashes and controlling the hook's CLI resolution.
**Recovery:** Put a temporary `axm` wrapper first on `PATH` so the unchanged hooks execute the already-validated `0.28.0` source CLI, then recover the exact lint-staged backup with its index before recommitting.
**Detected by:** Commit exit status, structured hook output, working-tree and log comparison, and `git stash list` inspection.
**Observed factors:** AXM CLI `0.27.18` installed at `/Users/craig/.local/bin/axm`; workspace lockfile version 6; compatible AXM source CLI `0.28.0`; commit hooks invoke `axm` from `PATH`; lint-staged automatic backup enabled in the Vineyard repository.
**Diagnostic evidence:** The root commit exited 1 after `Failed to read the workspace lockfile` and `lockfileVersion: Expected 5`; Vineyard remained at its prior commit with old pack declarations while `stash@{0}` contained the complete gen-stack migration and field note.
**Hypothesis:** Hook configuration assumes the globally installed AXM remains compatible with the repository lockfile and does not pin or resolve the workspace-compatible CLI.
**Suggests:** Make validation hooks resolve a repository-declared AXM version, or fail preflight before lint-staged hides a valid migration in its automatic backup.

Evidence: Direct validation with the `0.28.0` source CLI had already reported zero lint findings and a no-change sync preview for each migrated workspace.
