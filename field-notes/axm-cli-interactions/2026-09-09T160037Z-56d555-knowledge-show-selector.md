---
id: 2026-09-09T160037Z-56d555
subject: axm-cli-interactions
key: knowledge-show-selector
observed_at: "2026-09-09T16:00:37.748414+00:00"
session: brooks-56d555
kind: gap
status: open
---

**Expected:** Resolve the workspace bundle after identifying it as `@craigsmitham/knowledge/product-engineering`; the AXM skill calls for fully qualified identity resolution, while `knowledge show --help` describes its argument only as a bundle name.
**Observed:** `axm knowledge show @craigsmitham/knowledge/product-engineering --json` reported that the bundle was not installed. `axm knowledge list --json` listed `product-engineering` at `knowledge/product-engineering/src`; `axm knowledge show product-engineering --json` succeeded.
**Impact:** One failed read and two follow-up reads during source resolution; elapsed delay not measured. No mutation was attempted.
**Recovery:** Used the short inventory name; canonical source resolved and authoring proceeded.
**Detected by:** CLI exit status and structured result, compared with the subsequent local inventory.
**Observed factors:** CLI 0.28.12; workspace-authored project bundle version 2.0.0; no per-agent knowledge projection.
**Diagnostic evidence:** Failure exit 3; diagnostic error code `not_found`, message `knowledge bundle "@craigsmitham/knowledge/product-engineering" is not installed`, suggestion `axm knowledge list`. Primary JSON result: `ok: false`, `code: not_found`, `title: Not Found`, same detail and suggestion. Recovery reads both exited 0; show returned `source: workspace`, `scope: project`, `enabled: true`, `locked: false`.
**Hypothesis:** The show selector uses the local inventory name rather than the fully qualified extension identity.
