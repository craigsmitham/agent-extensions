---
id: 2026-08-25T212915Z-h7r3
subject: axm-cli-interactions
key: batch-publish-timeout-left-ambiguous-results
observed_at: "2026-08-25T21:29:15Z"
session: s8f2n
kind: workaround
status: open
---

**Expected:** An admitted eight-package publication set would either complete with authoritative per-package outcomes or fail without leaving package state ambiguous.
**Observed:** The apply result was `partial`: four outcomes were successful and four reported `upload_failed` because the Registry request exceeded the configured deadline. Exact Registry readback showed that two of those four timed-out uploads had actually completed and two had not.
**Impact:** Publication could not safely continue from the command result alone. Eight package identities required readback, followed by a second preview and bounded recovery publication for the two versions confirmed absent.
**Recovery:** Read every affected package from the Registry, selected only `@craigsmitham/skills/reconcile-architecture-docs@0.5.0` and `@craigsmitham/knowledge/software-architecture@4.1.0`, then used a fresh preview and `--on-existing verify` so any late completion would become an integrity-checked no-op. Both exact versions subsequently published successfully.
**Detected by:** The publish result contract and exact Registry version readback.
**Observed factors:** AXM CLI `0.28.0`; eight-package explicit selection; publication set status `admitted`; execution status `partial`; client command completed in about 24 seconds; all candidates used preserved public visibility.
**Diagnostic evidence:** Initial counts were `published: 4`, `failed: 4`, `blocked: 0`; failed outcomes used phase `upload_execution`, reason `upload_failed`, and message `Registry request did not complete within the configured deadline. (timeout)`. Readback found the expected versions for `author-architecture-docs` and `author-software-work-items` despite their failed outcomes, while `reconcile-architecture-docs` remained at `0.3.0` and `software-architecture` at `3.1.0`. The two-package recovery completed with `published: 2`, `failed: 0`.
**Hypothesis:** Per-package upload requests can complete server-side after the client deadline, but the batch result has no authoritative late-result reconciliation before it reports failure.
**Suggests:** After a timeout, automatically perform exact-version readback and classify the outcome as published, absent-and-safe-to-retry, or unknown; include an explicit safe recovery command in the result.

Evidence: The final Registry audit confirmed all intended component versions exactly, and no immutable version was overwritten.
