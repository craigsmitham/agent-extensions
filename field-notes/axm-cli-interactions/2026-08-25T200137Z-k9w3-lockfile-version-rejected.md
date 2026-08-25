---
id: 2026-08-25T200137Z-k9w3
subject: axm-cli-interactions
key: lockfile-version-rejected
observed_at: "2026-08-25T20:01:37Z"
session: s8f2n
kind: gap
status: open
---

**Expected:** `axm lint --json` should load and validate the project workspace so a read-only pack inspection can resolve AXM-managed identity and composition.
**Observed:** AXM loaded the workspace, then rejected `axm-lock.yaml` because its `lockfileVersion` did not match the expected version.
**Impact:** AXM-managed canonical-state inspection could not proceed; this work continued using repository manifests and source content directly. One diagnostic retry was needed to retain the process exit status.
**Recovery:** Continued with read-only repository inspection. AXM workspace validation remains unresolved.
**Detected by:** Required AXM preflight for a pack-composition review.
**Observed factors:** AXM CLI `0.27.18`; command `axm lint --json`; project-root `axm-lock.yaml`; two attempts, with the second retaining the exit status.
**Diagnostic evidence:** Process exit status `9`; error code `validation`; title `Invalid Request`; detail reported `lockfileVersion: Expected 5`.
**Hypothesis:** unknown

Evidence: `axm lint --json` emitted progress through workspace loading, then returned `ok: false` with validation code and exit status `9`. No workspace mutation was attempted.
