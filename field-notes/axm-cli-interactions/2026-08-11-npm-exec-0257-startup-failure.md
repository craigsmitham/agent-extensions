---
subject: axm-cli-interactions
key: npm-exec-0257-startup-failure
date: 2026-08-11
kind: gap
status: open
---

**Expected:** `npm exec --package=axm.sh@0.25.7 -- axm --version` and the
public-safety lint invocation should start successfully because `0.25.7`
supports Node `>=22.19.0` and the repository's Ubuntu/Node 24 workflow has
successful runs with that pin.
**Actual:** On macOS, the published package failed before both commands on Node
22.23.1 and Node 24.19.0 with `Cannot read properties of undefined (reading
'get')`.
**Gap:** The published CLI's local startup behavior differs from the successful
workflow evidence, and the current error does not identify the platform-specific
precondition.
**Suggests:** Make startup failure diagnostics identify the failing service or
platform boundary so a published-version reproduction can distinguish an
environment mismatch from workspace incompatibility.

Evidence: `npm exec --yes --package=axm.sh@0.25.7 -- axm --version` and
`npm exec --yes --package=axm.sh@0.25.7 -- axm lint --strict --json --quiet
--non-interactive` failed with the same internal error under Node 22.23.1;
repeating through `mise x node@24.19.0 --` produced the same result.
