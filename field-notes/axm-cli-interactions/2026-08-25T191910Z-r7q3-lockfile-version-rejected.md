---
id: 2026-08-25T191910Z-r7q3
subject: axm-cli-interactions
key: lockfile-version-rejected
observed_at: "2026-08-25T19:19:10Z"
session: unknown
kind: blocked
status: open
---

**Expected:** `axm list --json` would report installed and enabled extension state so the evaluation runner could be selected.
**Observed:** AXM exited before listing extensions because the workspace lockfile declares version 6 while this CLI expects version 5.
**Impact:** AXM-managed state inspection, runner activation proof, lint, versioning, and synchronization are unavailable through the current CLI.
**Recovery:** No AXM mutation was attempted; work continued against canonical workspace-authored sources, with AXM-dependent validation and versioning left for a compatible CLI.
**Detected by:** `axm list --json` returned a validation error.
**Observed factors:** CLI output reached 100% workspace loading before failure; the repository-root `axm-lock.yaml` begins with `lockfileVersion: 6`.
**Diagnostic evidence:** Exit code `9`; error code `validation`; cause tag `LockfileDecodeError`; cause message `lockfileVersion: Expected 5`.
**Hypothesis:** The workspace lockfile was produced by a newer AXM schema than the installed 0.27.18 CLI supports.

Evidence: The complete machine output returned `ok: false` with `Invalid Request`, and the inspected lockfile declares version 6.
