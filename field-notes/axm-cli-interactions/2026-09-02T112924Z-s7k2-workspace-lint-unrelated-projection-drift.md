---
id: 2026-09-02T112924Z-s7k2
subject: axm-cli-interactions
key: workspace-lint-unrelated-projection-drift
observed_at: "2026-09-02T11:29:24Z"
session: s7k2m
kind: workaround
status: open
---

**Expected:** `axm lint --json` would complete the AXM preflight for the
software-engineering knowledge edit so the chained target-authority checks
could continue.
**Observed:** Workspace lint exited `1` for an unrelated stale `researcher`
subagent projection, so the shell stopped before the target-authority checks.
**Impact:** The target checks required a separate command; elapsed cost was not
measured.
**Recovery:** Preserve the lint finding and run the read-only knowledge help
and local authority checks separately; the semantic documentation task can
continue without repairing the unrelated projection.
**Detected by:** The structured `axm lint --json` result and process exit code.
**Observed factors:** AXM CLI `0.28.4`; AXM skill `0.28.1`; compatibility
status `compatible`; workspace lint scope; one unrelated stale projection.
**Diagnostic evidence:** Exit code `1`; rule
`workspace/projections-current`; severity `error`; subject `subagent:researcher`;
affected contributor `workspace:@craigsmitham/subagents/researcher`; summary
`total=1`, `errors=1`, `warnings=0`, `infos=0`, exit category `errors`.
**Hypothesis:** Workspace-wide projection freshness is evaluated even when the
requested mutation concerns an unrelated canonical knowledge package.
**Suggests:** Consider a documented target-scoped preflight or an explicit
non-blocking disposition for unrelated projection drift during canonical
package authoring.

Evidence: The failure occurred during the required AXM preflight from the
repository root before editing `knowledge/software-engineering`; the lint
result reported compatible CLI and skill versions and only the stale
`researcher` projection.
