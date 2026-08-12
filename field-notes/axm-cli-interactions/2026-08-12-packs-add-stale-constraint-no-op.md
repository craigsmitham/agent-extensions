---
subject: axm-cli-interactions
key: packs-add-stale-constraint-no-op
date: 2026-08-12
kind: gap
status: open
---

**Expected:** `axm packs add <pack> <extension>@<newer-version> --replace-existing --preview --json` should preview a constraint update when an authored pack still references an older version and the workspace trust state already contains the newer version.
**Actual:** The command reported a no-op for each stale dependency constraint.
**Gap:** The authored pack remained on its older constraint even though the requested replacement version was present and trusted, so the supported pack-editing command could not express the intended repair.
**Suggests:** Compare an explicit replacement request with the authored manifest constraint and preview the requested constraint change whenever they differ.

Evidence: In a workspace-authority source repository, AXM 0.26.0 reported no changes for four explicit `--replace-existing` previews. The requested versions were visible in trust state, while `axm packs show` continued to display older desired dependency constraints.
