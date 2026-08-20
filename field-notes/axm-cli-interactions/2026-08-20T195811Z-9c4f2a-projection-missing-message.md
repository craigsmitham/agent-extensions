---
id: 2026-08-20T195811Z-9c4f2a
subject: axm-cli-interactions
key: projection-missing-message
observed_at: "2026-08-20T19:58:11Z"
session: codex-architecture-corpus-20260820
kind: gap
status: open
---

**Expected:** `axm lint` should describe an existing but stale instruction
projection as needing reconciliation.
**Observed:** `workspace/projections-current` said the AXM-owned projection at
the root `AGENTS.md` path was missing, while `ls` and `axm instructions` showed
the path present and healthy; `axm sync --preview` described the actual change
as an update to Knowledge discovery in `AGENTS.md`.
**Impact:** The release gate required extra inspection to distinguish a stale
managed region from a missing file; elapsed time was not measured.
**Recovery:** `axm instructions` and `axm sync --preview` exposed the applicable
reconciliation action; release work continued.
**Detected by:** Comparing `axm lint`, filesystem state, `axm instructions`, and
the sync preview.
**Observed factors:** AXM CLI 0.27.13; project scope; the description of a
workspace-authored Knowledge bundle had changed before lint.
**Hypothesis:** The projection-current finding uses one generic missing message
for stale managed-region content.

Evidence: `axm lint` reported `The AXM-owned projection at .../AGENTS.md is
missing`; `ls -la AGENTS.md` showed a regular file; `axm instructions` reported
all five instruction targets `ok`; `axm sync --preview` proposed `Knowledge
discovery (updated AGENTS.md)`.
