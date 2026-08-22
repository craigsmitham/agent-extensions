---
id: 2026-08-21T203121Z-k7p
subject: axm-cli-interactions
key: parallel-mutations-stale-candidate
observed_at: "2026-08-21T20:31:21Z"
session: s-7m2q
kind: workaround
status: open
---

**Expected:** Two independent `axm skills new` commands for different skill
names could apply concurrently after both previews reported ready candidates.

**Observed:** One command created `maintain-architecture-docs`; the concurrent
`setup-architecture-docs` command failed with `stale-candidate` and instructed
the caller to rerun it.

**Impact:** Creating the second skill required one additional sequential AXM
invocation; elapsed delay was not measured.

**Recovery:** Rerun the failed creation sequentially against fresh workspace
state; the original implementation task continued.

**Detected by:** The failed command's JSON envelope returned `ok: false`,
`reason: stale-candidate`, and `errorCode: conflict`.

**Observed factors:** Both commands mutated the same project AXM workspace and
were launched concurrently for distinct new skill names.

**Hypothesis:** Applying either candidate changes shared AXM workspace state and
invalidates a candidate resolved before that mutation.

**Suggests:** Document that AXM workspace mutations should be serialized even
when their target extensions differ.

Evidence: Both previews completed with one ready step and no warnings or
errors. During concurrent apply, `maintain-architecture-docs` succeeded and
`setup-architecture-docs` returned `stale-candidate`.
