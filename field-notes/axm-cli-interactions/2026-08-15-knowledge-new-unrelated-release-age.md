---
subject: axm-cli-interactions
key: knowledge-new-unrelated-release-age
date: 2026-08-15
kind: workaround
status: open
---

**Expected:** After `axm knowledge new software-engineering --preview --json`
reported one ready step that only created the new package and AXM state, running
the same command with `--yes --json` should have applied that plan.
**Actual:** The apply failed before creating any files because the unrelated
configured package `@agentxm/knowledge/skill-engineering@0.1.0` was held by
`minimumReleaseAge`.
**Gap:** A scoped authoring command resolved release-age policy for a package
that was absent from its reported candidate plan, and the command exposes no
`--ignore-release-age` flag.
**Suggests:** Keep `knowledge new` resolution scoped to the authored package and
state files, or include every release-age-sensitive dependency in preview and
provide the applicable policy override.

Evidence: AXM 0.27.4 produced candidate
`2dc1f8b9668d60f8f13f19463f04c466b0497c54e34817b657f0e24b034a69d8` with
one ready creation step and no warning or error. Applying that candidate failed
with `conflict` and the message that
`@agentxm/knowledge/skill-engineering@0.1.0` was held until
`2026-08-15T23:08:02.255Z`; the result reported `appliedCount: 0`.
