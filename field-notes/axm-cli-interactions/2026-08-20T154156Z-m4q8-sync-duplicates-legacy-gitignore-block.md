---
id: 2026-08-20T154156Z-m4q8
subject: axm-cli-interactions
key: sync-duplicates-legacy-gitignore-block
observed_at: "2026-08-20T15:41:56Z"
session: s9p4x2
kind: gap
status: open
---

**Expected:** `axm sync` would migrate or replace the existing AXM instruction-alias `.gitignore` block while reconciling it to the current marker format.
**Observed:** Sync added a versioned `region=instruction-aliases` block after the legacy `# >>> axm:instructions >>>` block, leaving two `**/CLAUDE.md` entries; subsequent lint and convergence preview reported no findings or changes.
**Impact:** Final review required one additional manual cleanup of duplicated generated ignore content.
**Recovery:** Remove only the obsolete legacy block and retain the current AXM-owned region, then rerun lint and convergence checks.
**Detected by:** Reviewing the `.gitignore` diff after AXM reported successful reconciliation.
**Observed factors:** AXM CLI and skill 0.27.13; the legacy and current blocks contained the same ignore pattern; AXM lint reported zero findings.
**Hypothesis:** Current reconciliation does not recognize the older banner-style instruction-alias ownership block as replaceable legacy state.

Evidence: `.gitignore` contained both `# >>> axm:instructions >>>` / `# <<< axm:instructions <<<` and `axm:start v=1 region=instruction-aliases` / `axm:end v=1 region=instruction-aliases`, each containing `**/CLAUDE.md`.
