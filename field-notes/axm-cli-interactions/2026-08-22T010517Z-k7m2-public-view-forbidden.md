---
id: 2026-08-22T010517Z-k7m2
subject: axm-cli-interactions
key: public-view-forbidden
observed_at: "2026-08-22T01:05:17Z"
session: s8d4q1
kind: gap
status: open
---

**Expected:** `axm view @agentxm/packs/agent-engineering version --json` should return public Registry metadata, as described by `axm help basic-usage`.
**Observed:** The command requested the package visibility endpoint and returned HTTP 403 with `forbidden` because the active credential lacked `extensions:admin`.
**Impact:** The package-version inspection was prevented; this work required one alternate read through `axm list --outdated --json`.
**Recovery:** Used the successful outdated assessment and continued with update and uninstall previews; task completion was not yet known at capture time.
**Detected by:** The command's JSON error envelope and Registry response metadata.
**Observed factors:** AXM CLI 0.27.15; project scope; public `@agentxm/packs/agent-engineering`; an active credential granted publish scopes but not `extensions:admin`; update discovery succeeded immediately before this command.
**Hypothesis:** The view path performs an authorization-sensitive visibility lookup even when only public version metadata was requested.

Evidence: `axm view @agentxm/packs/agent-engineering version --json` returned `code: forbidden`, `requiredScope: extensions:admin`, and HTTP status 403; `axm list --outdated --json` reported latest version 0.5.0 for the same package.
