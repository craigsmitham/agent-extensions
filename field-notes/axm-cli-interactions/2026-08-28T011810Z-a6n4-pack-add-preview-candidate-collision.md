---
id: 2026-08-28T011810Z-a6n4
subject: axm-cli-interactions
key: pack-add-preview-candidate-collision
observed_at: "2026-08-28T01:18:10Z"
session: 9284d25c-de46-47d1-91e2-500437eda0c9
kind: gap
status: open
---

**Expected:** Previewing two different `axm packs add` operations against the
same pack would identify different manifest candidates and expose which member
and constraint each candidate would add.
**Observed:** The skill and subagent previews both returned candidate
`aa6dd6193d56cbe831b381aa0aeeee125364559a0f5cbed48b124dba0e8ea585`, and
neither result identified the proposed dependency or constraint.
**Impact:** The previews could not be bound to their distinct proposed manifest
changes from result data alone; application and manifest readback had to remain
strictly sequential.
**Recovery:** Preserved both complete results and continued with one bounded
apply followed by manifest inspection before the next apply.
**Detected by:** Comparing the two structured preview results.
**Observed factors:** AXM 0.28.1; commands targeted
`@craigsmitham/skills/research` and
`@craigsmitham/subagents/researcher`; both outcomes were `previewed`; both
process exit statuses were `0`; no diagnostic output was supplied.
**Diagnostic evidence:** Each primary result contained one ready unit with
`id: "research"` and the same candidate ID; dependency identity and proposed
constraint were not supplied. Diagnostic output: none supplied.
**Hypothesis:** The candidate identity may be derived from the unchanged pack
state rather than the proposed dependency-specific manifest.
**Suggests:** Include the proposed dependency and constraint in each result and
derive the candidate identity from the full proposed manifest.

Evidence: The two commands differed only in the extension argument, and their
complete structured results were otherwise identical apart from the suggestion
commands.
