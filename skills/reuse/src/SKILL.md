---
name: reuse
description: Adapt a codebase or a specified part to use suitable existing capabilities with less maintenance burden.
disable-model-invocation: true
---

Adapt the requested scope to use suitable capabilities already available
in the codebase, platform, or dependencies, with less unnecessary
implementation and maintenance burden.

The result should preserve required behavior and operational guarantees,
keep case-specific policy with its owners, and leave a coherent integration
with obsolete supporting machinery removed.

Judge fit against actual contracts and intended uses. Account for adoption,
migration, coupling, and ongoing ownership costs; report when no suitable
substitution offers a worthwhile benefit.
