---
name: modularize
description: Modularize a codebase or a specified part around cohesive responsibilities that can evolve independently.
disable-model-invocation: true
---

Modularize the requested scope around cohesive responsibilities, so changes
to one concern have limited effects on unrelated concerns.

Keep knowledge and decisions that change for the same reasons together,
and allow independently changing policies to evolve separately.
Responsibilities should have clear owners and simple interfaces that expose
only what collaborators need.

The result should preserve required behavior and make representative changes
more local, without unnecessary layers or fragmentation. Let intended uses
and reasons for change determine the appropriate boundaries.
