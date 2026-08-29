---
id: 2026-08-29T193008Z-b7m2
subject: axm-cli-interactions
key: unknown-command-help-falls-back
observed_at: "2026-08-29T19:30:08Z"
session: wm8k2q
kind: workaround
status: open
---

**Expected:** `axm create --help` should reject the unknown command clearly or
route to the supported scaffolding commands.
**Observed:** The command printed global AXM help, so the unsupported surface
was not distinguishable from a successful help request in the combined probe.
**Impact:** One additional help lookup was required before using `axm knowledge
new`, `axm skills new`, and `axm packs new`; elapsed cost was not measured.
**Recovery:** Read the type-specific help and used the documented `new`
subcommands; implementation continued.
**Detected by:** The output described the global command surface rather than a
`create` command.
**Observed factors:** AXM CLI 0.28.2; the probe ran several help commands in one
shell invocation; the overall shell exit status was `0`, while the individual
unknown-command status was unavailable because a later command determined the
shell result.
**Diagnostic evidence:** Command surface `axm create --help`; result output was
global AXM help; individual exit status unavailable — the combined shell
reported `0`.
**Hypothesis:** Unknown command help falls back to the root help renderer.

Evidence: The direct output named the root `axm <command> [flags]` usage and
listed `skills`, `knowledge`, and `packs` rather than documenting `create`.
