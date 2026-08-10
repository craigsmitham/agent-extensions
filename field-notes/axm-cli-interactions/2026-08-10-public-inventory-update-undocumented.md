---
subject: axm-cli-interactions
key: public-inventory-update-undocumented
date: 2026-08-10
kind: workaround
status: open
---

**Expected:** The documented new-package publishing workflow would identify all
repository state that must change for the public safety gate to remain valid.
**Actual:** After four packages published successfully, the gate failed because
its hard-coded package list and ownership count still described the prior
29-package inventory.
**Gap:** `docs/publishing.md` does not mention updating the safety script's
allowlist, diagnostic count, and workspace-owned package count when adding a
public package.
**Suggests:** Document this release step or derive the approved inventory and
count from one reviewable source.

Evidence: `scripts/check-public-safety.sh` reported four additions against the
approved 29-package set after the registry publish succeeded.
