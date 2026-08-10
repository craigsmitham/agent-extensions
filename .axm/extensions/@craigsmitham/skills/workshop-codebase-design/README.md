# Workshop Codebase Design

Workshop consequential functional and technical choices for a codebase change
with a developer, using current-state evidence rather than hidden assumptions.
The skill keeps recommendations distinct from accepted human decisions and
produces a traceable Codebase Design Record.

Use it after relevant current behavior is understood through a research report
or directly supplied evidence, when product behavior, responsibilities,
interfaces, state, failure handling, migration, or operational choices remain
open. Do not use it to research the codebase, generate a design unilaterally,
write a specification or implementation plan, review code, or implement a
change.

Install it with:

```sh
axm install @craigsmitham/skills/workshop-codebase-design
```

For example:

> Workshop whether duplicate bulk-export requests should join the active export,
> return a conflict, or create another export. Here is the current request flow,
> persistence behavior, and API contract captured from release 2.6.

The skill will confirm the evidence and desired outcome, present viable options
and a recommendation for one consequential decision at a time, wait for an
explicit choice, and preserve accepted decisions and unresolved blockers in the
record.
