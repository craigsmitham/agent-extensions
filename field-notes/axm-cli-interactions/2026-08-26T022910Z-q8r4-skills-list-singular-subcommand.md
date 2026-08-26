---
id: 2026-08-26T022910Z-q8r4
subject: axm-cli-interactions
key: skills-list-singular-subcommand
observed_at: "2026-08-26T02:29:10Z"
session: codex-q8r4
kind: workaround
status: open
---

**Expected:** `axm skill list --json` would report installed Agent Skills while resolving an authored skill package.
**Observed:** AXM returned a usage error with `code: usage`, reported `Unknown subcommand "skill" for "axm"`, and suggested `skills`.
**Impact:** One read-only command attempt was repeated with the plural subcommand; no mutation occurred.
**Recovery:** `axm skills list --json` succeeded and restored progress.
**Detected by:** The structured AXM error response and non-success result.
**Observed factors:** AXM CLI version 0.28.1; project workspace; read-only list operation.
**Diagnostic evidence:** Failing command: `axm skill list --json`; result `ok: false`; error code `usage`; suggested command surface `skills`; recovery command: `axm skills list --json`.
**Hypothesis:** The list surface uses the plural extension-type noun while the singular form is not an alias.

Evidence: The failed structured result and successful corrected invocation were observed in the same session.
