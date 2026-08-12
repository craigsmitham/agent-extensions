---
subject: axm-cli-interactions
key: public-safety-cli-version-mismatch-recurrence
date: 2026-08-12
kind: blocked
status: open
---

**Expected:** The AXM CLI used for ordinary extension authoring would also run
the repository's required public-safety gate before commit.
**Actual:** After AXM successfully applied a package version bump, the safety
gate stopped because the same CLI was version 0.26.5 instead of required 0.26.4.
**Gap:** The repository pins a different AXM version from the active authoring
CLI, so the required commit gate cannot use the CLI that performed the work.
**Suggests:** Provide a repository-local pinned AXM invocation that both
authoring commands and the public-safety gate use.

Evidence: On 2026-08-12, `axm version
@craigsmitham/skills/refine-work patch --json` completed with AXM 0.26.5, then
`scripts/check-public-safety.sh` reported `AXM 0.26.4 is required; found
0.26.5`.
