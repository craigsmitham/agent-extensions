# Product engineering knowledge

A portable body of knowledge for building software products, organized as the
six questions a practitioner works through, from deciding where to compete to
keeping the result healthy in production.

Start at the [discovery map](src/index.md).

| Section | Question |
| --- | --- |
| [Where to play](src/strategy/) | Where should we participate, and how do we win there? |
| [What to solve](src/problem/) | Which problems are worth solving, and what outcome would tell us we succeeded? |
| [What to build](src/solution/) | Which solution concept do we commit to, and how do we state that commitment so others can dispute it? |
| [How to build it](src/engineering/) | How do we construct and verify what we committed to? |
| [How to ship it](src/delivery/) | How does a change reach production safely and predictably? |
| [How to run it](src/operations/) | How does the product stay healthy, secure, and affordable in production? |

The guidance here is technology-agnostic. Anything that churns with a specific
language, framework, or vendor stays in its own bundle, such as `effect-v4`,
and is referenced rather than restated. One bounded exception is stated in the
[overview](src/overview.md): a dated comparative mapping of named platforms onto
a portable model may stay when the model would otherwise be uncheckable.
[Workflow model](src/delivery/automation/workflow-model-explainer.md) is the
only one, and it lives under the currency contract the overview sets.

Every concept file carries a section tag matching its directory, because
`axm knowledge concepts query` can scope a search to a bundle but not to a
folder. The tags are `pe-strategy`, `pe-problem`, `pe-solution`,
`pe-engineering`, `pe-delivery`, and `pe-operations`. Reserved `index.md` and
`log.md` files carry none, and neither do concepts at the bundle root, such as
the [overview](src/overview.md), which belong to no section.

## Boundaries

Four neighboring disciplines stay in their own bundles.

| Outside | Bundle | Why |
| --- | --- | --- |
| Documentation craft | `docs` | Expressing knowledge for a reader is its own discipline, and it applies well beyond product engineering |
| Knowledge management | `knowledge-management` | It governs agent instructions, skills, and knowledge bundles, none of which are products |
| Field-note practice | `field-notes` | It is the concept layer of a mechanism this repository runs, coupled to a rule, a skill, and a pack |
| Agent engineering | `agent-engineering` | The design of goal-directed model-driven systems is its own discipline; this bundle owns the workflow that surrounds an agent step, not the model-directed choice inside it |

The second and third were once candidates for a seventh section, How to learn.
That section has been retired; the [overview](src/overview.md) records the
reasoning and shows where each clause of its question now lives.

## Status

Five of the six sections hold concepts. They arrived from six standalone bundles
that have been retired into this one, so the material is migrated rather than
newly written, and its depth varies by where it came from.

| Section | Source | State |
| --- | --- | --- |
| Where to play | `strategy`, `product-management` | Migrated; both bundles retired |
| What to solve | `product-management` | Migrated; that bundle retired |
| What to build | `requirements-engineering`, `product-management` | Requirements migrated and that bundle retired; the design half is unwritten |
| How to build it | `software-engineering` | Migrated and that bundle retired; two of five areas are unwritten |
| How to ship it | `work-management`, `workflow-automation` | Both migrated and retired; delivery flow is unwritten |
| How to run it | None | No concepts; scope and boundaries only |

Three sections carry more than one source, and each resolved it differently. In
"Where to play", the eight concepts of the `strategy` bundle and
[Product strategy](src/strategy/product-strategy.md) from `product-management`
sit together at the section's top level, because product strategy is the rung of
the choice cascade that turns an arena choice into product direction rather than
a separate body of craft. In "What to build", the requirements concepts sit in a
[Requirements](src/solution/requirements/) subtree, keeping the section's own
top level for design concepts.
[Product meaning and requirements](src/solution/product-meaning-and-requirements.md)
arrived separately with `product-management` because it explains where product
meaning stops and a requirement begins; it cites
[Requirements and neighboring artifacts](src/solution/requirements/foundations/requirements-and-neighboring-artifacts.md)
directly rather than by URL, and the two accounts must not diverge. In "How to
ship it", [work items](src/delivery/work-items/) and
[automation](src/delivery/automation/) arrived as separate bundles and remain
separate subtrees, because one is a record contract and the other is a field of
systems.

### What is still unsourced

No bundle exists behind any of the following, and none of it has been written.

| Unsourced area | Section |
| --- | --- |
| Architecture and technical design | How to build it |
| Construction | How to build it |
| Delivery flow: batch size, branching, review gates, and cadence | How to ship it |
| Everything: observability, reliability, incident practice, operational security, and sustainment | How to run it |

The design half of "What to build" is a fifth gap of the same kind. Solution
concept, resolution and fidelity, interaction design, and constraint as design
input have no existing bundle behind them and will be written from scratch.
Build and release in "How to ship it" is a partial gap rather than a whole one:
pipelines, quality gates, and artifact promotion arrived with
[automation](src/delivery/automation/), while versioning, environment topology,
and rollout strategy did not.

A section with no concepts still states its question, its scope, and its
boundaries. That is enough to place a concept and to keep neighboring sections
from claiming the gap, and it is not a claim that the guidance exists.

The knowledge package is licensed under CC-BY-SA-4.0.
