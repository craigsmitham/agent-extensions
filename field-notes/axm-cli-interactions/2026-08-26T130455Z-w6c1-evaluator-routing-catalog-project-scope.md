---
id: 2026-08-26T130455Z-w6c1
subject: axm-cli-interactions
key: evaluator-routing-catalog-project-scope
observed_at: "2026-08-26T13:04:55Z"
session: unknown
kind: blocked
status: open
---

**Expected:** The explicitly selected Agent Skill evaluator would run one routing authoring smoke against the validated workspace-authored `skills/research` package and its declared neighbors.
**Observed:** Preflight exited 2 with `missing-catalog-entry` for `research`; static inspection showed that routing catalog resolution reads only `<root>/.axm/extensions/<owner>/skills/...`, while AXM reports this project workspace's canonical authored package at `skills/research` and acquired packages under `agent_extensions/`.
**Impact:** The required representative routing smoke could not start for the changed project-authored package; no behavioral evidence was created.
**Recovery:** Preserved the reserved disposition and completed deterministic source validation and package inspection; the routing smoke remains open for a mechanism that can bind project-scope catalog entries.
**Detected by:** Evaluator `run` preflight for Research routing case 6, followed by static inspection of the exact failing catalog resolver.
**Observed factors:** Evaluator version 0.2.2; selection source `explicit`; proposed ignored workspace `.work/evals/@craigsmitham/skills/research/research-v2-explicit-selection-smoke`; `evidence_created: false`.
**Diagnostic evidence:** Process exit status 2; error code `missing-catalog-entry`; message `Routing catalog entry is unavailable: research`; disposition state `reserved`.
**Hypothesis:** The evaluator's catalog resolver currently assumes the user-scope `.axm/extensions` layout and does not resolve AXM project-workspace authored or acquired roots.
**Suggests:** Resolve routing catalog entries through active AXM scope state or accept explicit catalog source bindings.

Evidence: `catalogForCase` constructs catalog paths only under `<root>/.axm/extensions`, while current `axm help skills` documents `skills/` and `agent_extensions/` for this project scope.
