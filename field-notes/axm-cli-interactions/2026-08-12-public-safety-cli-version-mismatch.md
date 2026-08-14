---
subject: axm-cli-interactions
key: public-safety-cli-version-mismatch
date: 2026-08-12
kind: workaround
status: promoted
---

**Expected:** The installed AXM CLI would match the version required by the
repository's public-safety gate.
**Actual:** `axm --version` reported 0.26.5 after upstream `main` adopted and
required 0.26.4.
**Gap:** Ordinary AXM authoring commands could run, but the final safety gate
required a separate pinned 0.26.4 executable.
**Suggests:** Provide or document a repository-local way to invoke the pinned
AXM version independently of the globally installed version.

Evidence: On 2026-08-12, `docs/publishing.md` and
`scripts/check-public-safety.sh` on `origin/main` required AXM 0.26.4, while
`axm --version` returned 0.26.5.
