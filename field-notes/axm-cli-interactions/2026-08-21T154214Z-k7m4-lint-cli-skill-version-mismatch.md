---
id: 2026-08-21T154214Z-k7m4
subject: axm-cli-interactions
key: lint-cli-skill-version-mismatch
observed_at: "2026-08-21T15:42:14Z"
session: 01a024da-8386-7640-a9e3-92070912bb1f
kind: blocked
status: open
---

**Expected:** `axm lint --strict --json` would validate the workspace after the running AXM CLI had created and synchronized packages.
**Observed:** Lint stopped with `workspace/axm-skill-compatible`; CLI `0.27.15` was outside the installed official AXM skill's declared `0.27.13` range.
**Impact:** Strict workspace validation was blocked once and required a separate official-skill recovery boundary.
**Recovery:** Previewed and installed the `0.27.15` skill bundled with the running CLI; validation then resumed.
**Detected by:** `axm lint --strict --json`.
**Observed factors:** The workspace skill source was `@agentxm/skills/axm@0.27.13`; the running CLI reported `0.27.15` and prescribed an official-skill update.
**Hypothesis:** The CLI advanced independently of the workspace-pinned official skill.

Evidence: The lint result reported `reasonCode: cli-version-incompatible`, target CLI and skill version `0.27.15`, and recovery action `update-registry-skill`.
