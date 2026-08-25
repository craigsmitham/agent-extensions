---
type: Explanation
description: Why a durable claim needs one canonical owner and how summaries, pointers, and local applications avoid competing definitions.
tags: [authority, ownership, source-of-truth, canonical-source, knowledge-governance]
status: draft
---

# Authority and ownership

A durable claim needs one canonical owner: the source whose change changes the
accepted meaning of the claim. Other sources may introduce it, apply it, or
point to it, but should not quietly become competing definitions.

Authority follows the information rather than a preferred document type. A
schema may own an exact data shape, tests may own supported observable behavior,
an architecture document may own a responsibility boundary, and an operational
system may own current runtime state. Calling one document the source of truth
for all four makes each claim less reliable.

Ownership includes responsibility for:

- deciding what the claim means;
- reconciling contradictions;
- keeping it current enough for its use; and
- naming a successor when its authority moves.

## Pointers, summaries, and applications

A pointer names the canonical source and adds no competing meaning. A summary
helps a local audience navigate but remains subordinate to its source. A local
application may add context-specific consequences while leaving the shared
definition untouched.

Duplication is dangerous when both copies appear authoritative. If a claim must
be repeated for usability, label the canonical source and keep the repeated
portion no more detailed than necessary.

## Moving authority

Move a claim by establishing the new source, updating its dependents, and then
removing or clearly deprecating the old definition. Leaving two current-looking
copies turns every later edit into an implicit choice between them.
