---
id: 2026-08-21T230130Z-p9x
subject: axm-cli-interactions
key: public-safety-missing-agents-projection
observed_at: "2026-08-21T23:01:30Z"
session: unknown
kind: blocked
status: open
---

**Expected:** `scripts/check-public-safety.sh` should assess the public safety of the current extension changes.
**Observed:** The check stopped with `workspace/projections-current` because the AXM-owned projection at the workspace-root `AGENTS.md` was missing.
**Impact:** Repository-wide public-safety validation did not reach its content checks; one narrower validation path was required. Elapsed cost was not measured.
**Recovery:** Continued with package-local validation and left the unrelated missing projection unchanged.
**Detected by:** Nonzero output from `scripts/check-public-safety.sh`.
**Observed factors:** AXM reported one manual-attention issue and listed all knowledge contributors as affected; the software-architecture knowledge lint passed separately.
**Hypothesis:** unknown

Evidence: `scripts/check-public-safety.sh` exited 1 and reported `The AXM-owned projection at /Users/craig/Code/craigsmitham/agent-extensions/AGENTS.md is missing.`
