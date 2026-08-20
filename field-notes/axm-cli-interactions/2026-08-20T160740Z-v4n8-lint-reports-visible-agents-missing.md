---
id: 2026-08-20T160740Z-v4n8
subject: axm-cli-interactions
key: lint-reports-visible-agents-missing
observed_at: "2026-08-20T16:07:40Z"
session: q7d2f9
kind: gap
status: open
---

**Expected:** Workspace-wide `axm lint --details` would validate the visible root `AGENTS.md` projection or report a content-level mismatch.
**Observed:** Lint returned `workspace/projections-current` and said the repository-root `AGENTS.md` was missing even though that file existed and had just been read.
**Impact:** Workspace-wide skill validation could not complete; package-level validation and other read-only checks were required. Delay was not measured.
**Recovery:** Continue with targeted Knowledge validation and independent package checks; leave unrelated projection state unchanged.
**Detected by:** `axm lint --details` after targeted Knowledge validation passed.
**Observed factors:** AXM's current working directory was the public agent-extensions repository; `AGENTS.md` was a tracked regular file; the error named that exact root file.
**Hypothesis:** unknown

Evidence: `axm knowledge lint --path ./.axm/extensions/@craigsmitham/knowledge/software-engineering` passed immediately before workspace lint reported the root `AGENTS.md` projection missing.
