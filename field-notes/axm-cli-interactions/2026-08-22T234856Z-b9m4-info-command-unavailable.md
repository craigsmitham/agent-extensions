---
id: 2026-08-22T234856Z-b9m4
subject: axm-cli-interactions
key: info-command-unavailable
observed_at: "2026-08-22T23:48:56Z"
session: audit-4f9c
kind: gap
status: open
---

**Expected:** A read-only `axm info <extension> --json` command would expose the current registry identity for a named extension.
**Observed:** AXM rejected `info` as an unknown subcommand and returned a usage error.
**Impact:** Three registry-identity queries were not run; discovery required one additional help lookup and a different supported command.
**Recovery:** Read `axm help` and continue with the listed discovery and update surfaces; the task continued.
**Detected by:** The CLI error envelope and command output.
**Observed factors:** AXM CLI 0.27.15; project scope; the requested operation was read-only extension discovery.
**Hypothesis:** The installed CLI exposes extension state through other commands and has no generic `info` alias.

Evidence: `axm info @agentxm/packs/agent-engineering --json` returned `Unknown subcommand "info" for "axm"`; the top-level help output did not list an `info` command.
