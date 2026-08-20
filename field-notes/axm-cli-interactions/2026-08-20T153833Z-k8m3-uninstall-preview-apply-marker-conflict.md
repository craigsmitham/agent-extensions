---
id: 2026-08-20T153833Z-k8m3
subject: axm-cli-interactions
key: uninstall-preview-apply-marker-conflict
observed_at: "2026-08-20T15:38:33Z"
session: s9p4x2
kind: blocked
status: open
---

**Expected:** `axm uninstall @craigsmitham/knowledge/software-architecture` would apply the one-step candidate that its immediately preceding preview reported as ready with no warnings or errors.
**Observed:** Apply failed before changing the workspace with `AXM ownership marker is missing v: AGENTS.md (conflict)`.
**Impact:** Bundle removal was delayed by one failed apply and required additional instruction-marker diagnosis.
**Recovery:** In progress; no uninstall changes were applied.
**Detected by:** The structured apply result returned `ok: false`, `errorCode: conflict`, and one failed step.
**Observed factors:** AXM 0.27.11; project scope; preview and apply reported the same candidate ID; `AGENTS.md` contains unversioned Knowledge Base and Rules region markers.
**Hypothesis:** The uninstall preview does not validate the managed instruction marker ownership version that apply requires.

Evidence: Candidate `1eef58d8ac3d25c1d724d9b0203fa1ee293d6e9b7fcdfcd14e2cefdcec79d472` previewed with `readyCount: 1`, `warningCount: 0`, and `errorCount: 0`; apply failed on the missing marker version and reported `appliedCount: 0`.
