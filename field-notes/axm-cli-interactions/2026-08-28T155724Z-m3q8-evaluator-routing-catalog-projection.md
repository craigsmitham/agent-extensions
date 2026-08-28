---
id: 2026-08-28T155724Z-m3q8
subject: axm-cli-interactions
key: evaluator-routing-catalog-projection
observed_at: "2026-08-28T15:57:24Z"
session: codex-8f2c
kind: workaround
status: open
---

**Expected:** After `axm sync --preview --fail-on-change --json` reported that
workspace materialization was up to date, the enabled evaluator could discover
the workspace skill catalog needed for a routing smoke run.
**Observed:** The evaluator reserved the run with exit status 2 and
`missing-catalog-entry` for `shape` because it looked only under
`.axm/extensions`, while current workspace skill projections are under
`.agents/skills`.
**Impact:** The routing smoke could not start until a bounded ignored catalog
projection was prepared.
**Recovery:** Copied only the required canonical `SKILL.md` descriptors into an
ignored `.axm/extensions/@craigsmitham/skills/...` projection, then reran the
same bounded smoke successfully.
**Detected by:** The evaluator's structured preflight result and filesystem
inspection after AXM's no-op convergence result.
**Observed factors:** AXM CLI 0.28.1; Agent Skill evaluator 0.2.2; project scope;
AXM sync exit status 0; first evaluator run exit status 2; recovered Shape run
exit status 0.
**Diagnostic evidence:** Preflight error code `missing-catalog-entry`; message
`Routing catalog entry is unavailable: shape`; `.agents/skills/shape` resolved
to the canonical package while `.axm/extensions` was absent before recovery.
**Hypothesis:** The evaluator's routing-catalog discovery still assumes a
legacy AXM projection layout rather than resolving the current host projection.
**Suggests:** Resolve routing entries through active AXM workspace state or
accept the current `.agents/skills` projection as a catalog source.

Evidence: AXM reported `outcome: no-op` and “Workspace materialization is up to
date”; the first evaluator preflight created no run evidence, and the bounded
projection allowed the selected routing cases to complete.
