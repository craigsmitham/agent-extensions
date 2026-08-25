---
id: 2026-08-25T194510Z-p6x2
subject: axm-cli-interactions
key: lockfile-version-rejected
observed_at: "2026-08-25T19:45:10Z"
session: sess-p6x2
kind: workaround
status: open
---

**Expected:** `axm list --json` should report the workspace's managed extension state after the documented AXM authoring preflight.
**Observed:** The command returned a `validation` error and did not list extensions because the workspace lockfile decoder expected lockfile version 5.
**Impact:** One read-only package-resolution command was unusable, so canonical authored package paths had to be inspected directly. The added cost was one failed command and one manual resolution step; elapsed delay was not measured.
**Recovery:** Continued from the documented project-authored roots and direct repository evidence; the original documentation task was still in progress when this note was captured.
**Detected by:** The structured `axm list --json` result.
**Observed factors:** The command ran at the repository root. AXM emitted progress for loading the project workspace before returning the validation error.
**Diagnostic evidence:** Command `axm list --json`; process exit status not supplied by the tool result; error code `validation`; title `Invalid Request`; cause tag `LockfileDecodeError`; cause message `lockfileVersion: Expected 5`.
**Hypothesis:** The observed workspace lockfile does not satisfy the decoder's version-5 contract.

Evidence: AXM completed workspace-loading progress, then returned `ok: false` with a lockfile decode cause and no extension inventory.
