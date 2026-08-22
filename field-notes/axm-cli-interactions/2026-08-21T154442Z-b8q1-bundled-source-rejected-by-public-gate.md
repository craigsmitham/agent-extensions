---
id: 2026-08-21T154442Z-b8q1
subject: axm-cli-interactions
key: bundled-source-rejected-by-public-gate
observed_at: "2026-08-21T15:44:42Z"
session: 01a024da-8386-7640-a9e3-92070912bb1f
kind: workaround
status: open
---

**Expected:** The AXM-prescribed bundled official-skill recovery would leave the public workspace in a releasable state once strict AXM lint passed.
**Observed:** Strict AXM lint passed, but `scripts/check-public-safety.sh` rejected the bundled workspace source as an unexpected package source.
**Impact:** The public gate stopped once and required another source-authority transition for the official AXM skill.
**Recovery:** Previewed and installed public Registry version `@agentxm/skills/axm@0.27.15`; this restored the source form allowed by the repository gate.
**Detected by:** `scripts/check-public-safety.sh` after clean strict AXM lint and sync convergence.
**Observed factors:** Settings represented the official skill as `workspace:@agentxm/skills/axm` with bundled origin; the public gate allows only sources beginning with `@agentxm/skills/axm`.
**Hypothesis:** AXM recovery validity and this repository's publication-source policy recognize different acceptable official-skill authorities.

Evidence: The public gate printed `The workspace contains an unexpected package owner or source`; the subsequent Registry install of `0.27.15` applied successfully.
