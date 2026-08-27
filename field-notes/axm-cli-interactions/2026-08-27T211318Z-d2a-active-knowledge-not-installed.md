---
id: 2026-08-27T211318Z-d2a
subject: axm-cli-interactions
key: active-knowledge-not-installed
observed_at: "2026-08-27T21:13:18Z"
session: 3764bb
kind: gap
status: open
---

**Expected:** The active authoring workflow's required
`@agentxm/knowledge/agent-engineering` sibling would resolve through AXM; the
repository instructions also list that bundle as available.
**Observed:** `axm knowledge show @agentxm/knowledge/agent-engineering --json`
exited `3` with code `not_found` and reported that the knowledge bundle was not
installed.
**Impact:** Canonical knowledge resolution required one fallback to the
repository-authoritative bundle path before Agent Skill authoring could
continue; elapsed cost was not measured.
**Recovery:** Continued with the bundle source explicitly indexed by the
repository instructions; the original task remained in progress.
**Detected by:** AXM preflight while resolving the canonical `/plan` package
and its required authoring guidance.
**Observed factors:** AXM CLI `0.28.1`; workspace lint reported compatible and
clean; the `plan` skill resolved as enabled project-workspace source version
`0.1.0`.
**Diagnostic evidence:** command exit `3`; error code `not_found`; suggested
recovery command `axm knowledge list`.
**Hypothesis:** unknown

Evidence: The structured AXM result explicitly reported the bundle as not
installed while repository instructions exposed its source as available.
