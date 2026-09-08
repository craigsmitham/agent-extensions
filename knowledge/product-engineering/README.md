# Product engineering knowledge

A portable body of knowledge for building software products, organized as the
seven questions a practitioner works through, from deciding where to compete to
learning from what shipped.

Start at the [discovery map](src/index.md).

| Section | Question |
| --- | --- |
| [Where to play](src/strategy/) | Where should we participate, and how do we win there? |
| [What to solve](src/problem/) | Which problems are worth solving, and what outcome would tell us we succeeded? |
| [What to build](src/solution/) | Which solution concept do we commit to, and how do we state that commitment so others can dispute it? |
| [How to build it](src/engineering/) | How do we construct and verify what we committed to? |
| [How to ship it](src/delivery/) | How does a change reach production safely and predictably? |
| [How to run it](src/operations/) | How does the product stay healthy, secure, and affordable in production? |
| [How to learn](src/learning/) | How do we notice what happened, keep what we learned, and retire what is stale? |

The guidance here is technology-agnostic. Anything that churns with a specific
language, framework, or vendor stays in its own bundle, such as `effect-v4`,
and is referenced rather than restated.

## Boundaries

Documentation craft stays in the separate `docs` bundle. Expressing knowledge
for a reader is its own discipline with its own audience, and it applies well
beyond product engineering.

## Status

Version 0.3.0 holds two migrated sections and part of a third.
[Where to play](src/strategy/) carries the eight concepts of the retired
standalone `strategy` bundle plus product strategy, and
[What to solve](src/problem/) carries the rest of the retired
`product-management` bundle. The remaining sections carry their question,
scope, and boundaries and hold no concepts yet, except for the single
requirements concept now in [What to build](src/solution/).

| Section | Source | State |
| --- | --- | --- |
| Where to play | `strategy`, `product-management` | migrated; both bundles are retired |
| What to solve | `product-management` | migrated; that bundle is retired |
| What to build | `requirements-engineering`; design material is new | partial |
| How to build it | `software-engineering` | pending |
| How to ship it | `work-management`, `workflow-automation` | pending |
| How to run it | none; new material | pending |
| How to learn | none committed; see below | pending |

"What to build" holds one migrated concept,
[Product meaning and requirements](src/solution/product-meaning-and-requirements.md),
which arrived with `product-management` because it explains where product
meaning stops and a requirement begins. Reconcile it with
`requirements-engineering` when that bundle migrates: that bundle still owns
the portable boundary between requirements and neighboring artifacts, and the
two accounts should not diverge.

"What to build" also carries a second, unsourced half. `requirements-engineering`
supplies elicitation, specification, review, and traceability, but the solution
concept, fidelity, and interaction design areas have no existing bundle behind
them and will be written from scratch. Architecture and technical design under
"How to build it" is likewise new material.

The `knowledge-management` and `field-notes` bundles plausibly belong under
"How to learn", but neither is ready to migrate. Their purposes need to be
clearer, and their current content sits closer to tactics than to the durable
practice this section is meant to hold. Treat the section's scope as the
statement of intent and decide the sourcing separately.

The knowledge package is licensed under CC-BY-SA-4.0.
