---
type: Reference
title: Maintaining requirement identity and lineage
description: Preserves requirement identity and evidence meaning through revision, split, merge, supersession, and retirement.
tags: [identity, lineage, split, merge, supersession, retirement, requirements-engineering]
generated: { by: codex/gpt-6, at: 2026-11-11T20:03:45Z }
---

# Maintaining requirement identity and lineage

Keep an identity when edits clarify wording without changing the obligation's
meaning. Create successor identities when meaning, obligated subject, or
independent decision boundaries materially change.

- **Revision**: retain identity; record the semantic or editorial change.
- **Split**: create independently authoritative successors, link each to the
  source, and retire or narrow the source deliberately.
- **Merge**: create a successor only if one atomic obligation genuinely replaces
  the sources; preserve all predecessor links.
- **Supersession**: keep historical text and decision evidence discoverable.
- **Retirement**: record why and when the obligation ceased, plus residual impacts.

Evidence does not transfer automatically. Reassess whether a prior test,
analysis, or validation result supports each successor and its revision. A link
preserves lineage; it is not proof of satisfaction.

Work-item and requirement lineages remain separate. Merging duplicate work items does not merge the
requirements they cite, and retiring a requirement does not close the item that
retired it.
