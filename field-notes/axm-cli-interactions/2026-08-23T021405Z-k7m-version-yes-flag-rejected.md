---
id: 2026-08-23T021405Z-k7m
subject: axm-cli-interactions
key: version-yes-flag-rejected
observed_at: "2026-08-23T02:14:05Z"
session: k7m
kind: gap
status: open
---

**Expected:** `axm version` would accept `--yes` for a non-interactive apply after a successful preview.
**Observed:** Each of three version commands rejected `--yes` with `Unrecognized flag: --yes in command axm version`.
**Impact:** Three version updates required one repeated invocation with the supported flag set; elapsed delay was not measured.
**Recovery:** Remove `--yes` and retain `--json --non-interactive`; progress resumed.
**Detected by:** AXM returned a usage error before applying any version change.
**Observed factors:** AXM previews had succeeded for all three targets; the apply commands used the same targets plus `--yes`.
**Hypothesis:** Confirmation behavior or accepted flags differ between `axm version` and commands such as pack dependency updates.

Evidence: The CLI emitted error code `usage` and the message `Unrecognized flag: --yes in command axm version` for the knowledge, skill, and pack targets.
