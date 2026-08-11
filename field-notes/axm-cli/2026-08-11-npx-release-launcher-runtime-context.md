---
subject: axm-cli
key: npx-release-launcher-runtime-context
date: 2026-08-11
kind: gap
status: open
---

**Expected:** `npx --yes axm.sh@0.26.2 --version` and other read-only commands
should run the exact published CLI version, consistent with the verified npm
release.
**Actual:** every attempted command exited 10 before dispatch with
`Cannot read properties of undefined (reading 'get')`.
**Gap:** the published npm entry point depends on runtime context that is absent
under this npm-exec invocation, while the installed CLI and release binaries
remain usable.
**Suggests:** add a clean npm-exec smoke to release CI and make entry-point
runtime construction independent of package-runner context.

Evidence: `npx --yes axm.sh@0.26.2 --version`, `lint --help`,
`help git-hooks`, `update --help`, and `whoami --json` all failed identically on
Node 24 with exit 10.
