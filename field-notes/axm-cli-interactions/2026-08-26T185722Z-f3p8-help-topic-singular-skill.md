---
id: 2026-08-26T185722Z-f3p8
subject: axm-cli-interactions
key: help-topic-singular-skill
observed_at: "2026-08-26T18:57:22Z"
session: q7m2
kind: workaround
status: open
---

**Expected:** The singular `axm help skill` topic would provide the type-specific help needed before revising a managed skill package.
**Observed:** `axm help skill` exited `1` with `not_found` and directed the user to list available help topics; that list exposed the actual topic as plural `skills`.
**Impact:** Canonical skill-package resolution required one additional help-discovery command before work could continue.
**Recovery:** Used `axm help` to discover the supported plural `skills` topic and continued with `axm help skills`.
**Detected by:** AXM CLI diagnostic output during managed-skill preflight.
**Observed factors:** AXM CLI `0.28.1`; project scope; workspace lint was compatible and clean immediately before the help lookup.
**Diagnostic evidence:** Process exit `1`; error class `not_found`; rejected topic `skill`; recovery guidance `axm help`; discovered topic `skills`.
**Hypothesis:** The type name is singular in common authoring language while the AXM help topic is plural.
