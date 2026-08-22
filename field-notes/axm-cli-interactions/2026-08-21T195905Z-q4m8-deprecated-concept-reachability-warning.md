---
id: 2026-08-21T195905Z-q4m8
subject: axm-cli-interactions
key: deprecated-concept-reachability-warning
observed_at: "2026-08-21T19:59:05Z"
session: codex-s9k2
kind: gap
status: open
---

**Expected:** A deprecated OKF compatibility stub omitted from active indexes would validate without a discovery warning because normal concept search excludes deprecated concepts.
**Observed:** Both the OKF validator and `axm knowledge lint` reported the deprecated concept as unreachable from the root index.
**Impact:** Validation required one additional index edit and rerun; elapsed time was not measured.
**Recovery:** Added a clearly labeled deprecated route to the foundations index; the original documentation task continued.
**Detected by:** `validate_okf.py --info` and `axm knowledge lint --path`.
**Observed factors:** The concept had `status: deprecated`, linked to its successor, and was intentionally absent from active root navigation.
**Hypothesis:** Reachability validation applies uniformly to ordinary and deprecated concepts.
**Suggests:** Document whether deprecated compatibility stubs should remain indexed and show a recommended migration-index pattern.

Evidence: Both validators named `capabilities-features-and-surfaces.md` and reported that it was not reachable from the bundle-root index.
