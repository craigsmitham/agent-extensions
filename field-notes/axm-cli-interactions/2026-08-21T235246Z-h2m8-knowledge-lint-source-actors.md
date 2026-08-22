---
id: 2026-08-21T235246Z-h2m8
subject: axm-cli-interactions
key: knowledge-lint-source-actors
observed_at: "2026-08-21T23:52:46Z"
session: s-k7p3
kind: gap
status: open
---

**Expected:** `axm knowledge lint` would diagnose source `author` values that
do not truthfully follow OKF's actor convention.
**Observed:** AXM reported the bundle valid with zero diagnostics although
source authors include the undefined `team:` prefix and encode a person as a
tool/version actor.
**Impact:** The evaluation needed a separate metadata review to detect four
questionable author values; elapsed time was not measured.
**Recovery:** Treated the values as a bundle provenance finding and continued;
the evaluation remains in progress.
**Detected by:** Comparing source frontmatter to the OKF v0.2 actor convention
after AXM lint completed.
**Observed factors:** The affected files are `foundations/goal-oriented-behavior.md`
and `guides/reviewing-responsibilities-with-scenarios.md`; the accepted values
include `team:ivar-jacobson-and-alistair-cockburn` and
`alistair-cockburn/2026`.
**Hypothesis:** AXM checks the scalar's shape but cannot determine whether a
source author is a person, team, process, or versioned producer.

Evidence: `axm knowledge lint --path
./.axm/extensions/@craigsmitham/knowledge/software-architecture --json` exited
0 with `valid: true` and no diagnostics. OKF v0.2 defines `<producer>/<version>`
for agents and tools, `human:<id>` for people, and `process:<id>` for automated
processes.
