---
subject: axm-cli-interactions
key: source-runner-stale-core-dist
date: 2026-08-11
kind: gap
status: open
---

**Expected:** The AXM repository instructions describe `pnpm axm` and
`scripts/axm-local` as source entrypoints, so `scripts/axm-local --version
--json` from another workspace should start the anchored CLI without a separate
build step.
**Actual:** The source runner exited 1 before CLI startup because the current
source imports `decodeDesiredExtensionIdentity`, while the resolved
`packages/core/dist/src/unstable/extensions/index.js` did not export it.
**Gap:** The source entrypoint can resolve a stale built workspace dependency and
does not detect or repair that state before launching.
**Suggests:** Make the source runner consume current workspace source or fail with
an actionable dependency-build instruction when generated package output is
stale.

Evidence: From the clean AXM checkout at
`a8a528091979b017e3968501e7c1009ac76f14d8`, running
`AXM_TELEMETRY=0 NO_COLOR=1
<AXM_CHECKOUT>/scripts/axm-local --version --json` in the
`agent-extensions` workspace exited 1 with `SyntaxError: Export named
'decodeDesiredExtensionIdentity' not found in module
'<AXM_CHECKOUT>/packages/core/dist/src/unstable/extensions/index.js'`.
