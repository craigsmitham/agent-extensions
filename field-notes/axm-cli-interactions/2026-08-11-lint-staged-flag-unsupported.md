---
subject: axm-cli-interactions
key: lint-staged-flag-unsupported
date: 2026-08-11
kind: gap
status: open
---

**Expected:** The publishing guide's `axm lint --staged` release gate should lint the staged extension changes.
**Actual:** AXM 0.25.8 rejected `--staged` as an unrecognized flag.
**Gap:** The repository's prescribed gate is unavailable in the workspace-installed CLI.
**Suggests:** Align the publishing guide with a released AXM command, or add staged-file support to `axm lint`.

Evidence: On 2026-08-11, after staging the prune-work release, `axm lint --staged --json` exited with a usage error stating `Unrecognized flag: --staged in command axm lint`; `axm lint --json` then completed with zero findings.
