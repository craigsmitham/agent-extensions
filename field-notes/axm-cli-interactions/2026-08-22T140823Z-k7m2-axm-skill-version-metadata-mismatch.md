---
id: 2026-08-22T140823Z-k7m2
subject: axm-cli-interactions
key: axm-skill-version-metadata-mismatch
observed_at: "2026-08-22T14:08:23Z"
session: codex-20260822-k7m2
kind: gap
status: open
---

**Expected:** The AXM skill instructions exposed at the declared available-skill path should describe the active AXM skill and its CLI compatibility.
**Observed:** The user-scoped available-skill file for AXM declared skill and CLI version `0.27.11`, while `axm lint --strict --json` reported CLI `0.27.15`, installed official skill `0.27.15`, and a compatible `>=0.27.0 <0.28.0` range.
**Impact:** The authoring workflow required an extra comparison between loaded instructions and live CLI evidence; elapsed cost was not measured. The target skill revision was not blocked.
**Recovery:** Used live `axm help` output and strict lint as current CLI evidence, then continued the authorized revision.
**Detected by:** Comparing the loaded AXM skill frontmatter with the strict-lint compatibility result.
**Observed factors:** The available-skill catalog pointed to a user-scoped AXM skill file; the project workspace lint completed successfully with no findings.
**Hypothesis:** unknown
**Suggests:** Keep the available AXM skill projection aligned with the active installed official skill version.

Evidence: The loaded file named exact version `0.27.11`; the same session's strict-lint result named CLI and skill version `0.27.15` and reported `status: compatible`.
