---
id: 2026-08-26T192710Z-5df5
subject: axm-cli-interactions
key: sync-rejects-yes
observed_at: "2026-08-26T19:27:10Z"
session: q7m2
kind: workaround
status: open
---

**Expected:** The ordinary AXM confirmation flag `--yes` would allow a
previously previewed workspace sync to run non-interactively.
**Observed:** `axm sync --yes --json` exited with a usage error because `sync`
does not accept `--yes`; its help lists `--non-interactive` as the only relevant
global interaction flag and shows plain `axm sync` for application.
**Impact:** Applying the already-previewed managed rule projection required one
additional help lookup and command retry.
**Recovery:** Inspected `axm sync --help` and continued with the supported plain
sync form.
**Detected by:** AXM CLI structured diagnostic output.
**Observed factors:** AXM CLI `0.28.1`; project scope; the prior preview had one
ready instruction-reconciliation unit and no warnings or blocks.
**Diagnostic evidence:** Process exit `1`; error code `usage`; message
`Unrecognized flag: --yes in command axm sync`; rejected command
`axm sync --yes --json`.
**Hypothesis:** Mutation confirmation is command-specific and `sync` applies
its computed plan without the flag used by other AXM operations.
