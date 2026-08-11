---
subject: axm-cli-interactions
key: npm-exec-0262-startup-failure
date: 2026-08-11
kind: workaround
status: open
---

**Expected:** `npx -y axm.sh@0.26.2 --version` should run the official newer
CLI ephemerally so a publication can use its visibility preflight without
replacing the installed binary.
**Actual:** npm resolved the package, warned that `ini@7.0.0` does not support
the current Node 24.13.1 runtime, and AXM exited with `Cannot read properties of
undefined (reading 'get') (internal)` before printing its version.
**Gap:** The documented npm package cannot start under this otherwise supported
local Node runtime, so it cannot serve as a non-installing fallback for the
standalone AXM binary.
**Suggests:** Align the packaged dependency engine range with AXM's supported
Node runtime and cover `npm exec` startup on each supported Node line.

Evidence: `npm view axm.sh@0.26.2 version dist.integrity --json` resolved
version `0.26.2`; the immediately following `npx -y axm.sh@0.26.2 --version`
failed under Node `v24.13.1` after the `ini@7.0.0` engine warning.
