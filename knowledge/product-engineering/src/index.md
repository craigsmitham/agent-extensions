---
okf_version: "0.2"
---
# Product engineering

A portable body of knowledge for building software products, organized as the
six questions a practitioner works through, from deciding where to compete to
keeping the result healthy in production. Each section owns exactly one
question. The order is a value stream, but no section depends on being read in
order: each one stands alone for a reader who arrives through search.

This bundle holds portable craft only. Technology bindings that churn with a
framework, and domain overlays that span several questions, stay in their own
bundles and are referenced here rather than restated. The
[overview](overview.md) states the one bounded exception: a dated comparative
mapping of named platforms onto a portable model may stay when the model would
otherwise be uncheckable, under a currency contract the overview sets.

## Start here

* [Product engineering overview](overview.md) - How this body of knowledge is organized as six practitioner questions, why that scheme was chosen over lifecycle or artifact schemes, which seventh question was tried and retired, where design fits, and what stays outside it.

## The six questions

* [Where to play](strategy/) - Where should we participate, and how do we win there?
* [What to solve](problem/) - Which problems are worth solving, and what outcome would tell us we succeeded?
* [What to build](solution/) - Which solution concept do we commit to, and how do we state that commitment so others can dispute it?
* [How to build it](engineering/) - How do we construct and verify what we committed to?
* [How to ship it](delivery/) - How does a change reach production safely and predictably?
* [How to run it](operations/) - How does the product stay healthy, secure, and affordable in production?

## How full each section is

The sections are at very different stages. Five hold concepts and one holds none
yet. Of the five, two are complete for their scope and three cover part of
theirs. A section with no concepts still carries its
question, its scope, and the boundaries that keep its neighbors honest, so it is
worth reading to find out where something belongs, not to find out how to do it.

| Section | What it holds today |
| --- | --- |
| [Where to play](strategy/) | Complete for its scope: strategic choice, advantage and value, Wardley mapping, and strategy as hypothesis |
| [What to solve](problem/) | Complete for its scope: value and demand, outcomes and evidence, product risk, teams, and cadence |
| [What to build](solution/) | Requirements craft in depth under [Requirements](solution/requirements/); the design half of the section is not yet written |
| [How to build it](engineering/) | Verification, [codebase review](engineering/codebase-review/), and the repository execution surface; architecture and construction are not yet written |
| [How to ship it](delivery/) | [Work items](delivery/work-items/) and [automation](delivery/automation/); delivery flow is not yet written |
| [How to run it](operations/) | Scope and boundaries only; no concepts yet |

## Deeper entry points

Four subtrees are large enough that a reader often wants to land in them
directly rather than through their section.

* [Requirements](solution/requirements/) - Discovering, analyzing, specifying, reviewing, changing, and maintaining requirements.
* [Codebase review](engineering/codebase-review/) - Outcome-centered review of an existing codebase against product-quality criteria.
* [Work items](delivery/work-items/) - Operational Incident Records, Defect Reports, and Changes as durable case records.
* [Automation](delivery/automation/) - Workflow automation as a field, including continuous integration, delivery, and deployment.

## Retrieval

`axm knowledge concepts query` filters by bundle and by tag, and bundle is its
only scope filter. Every concept file therefore carries a section tag matching
its directory, so that a query can be scoped to one question: `pe-strategy`,
`pe-problem`, `pe-solution`, `pe-engineering`, `pe-delivery`, and
`pe-operations`. Reserved `index.md` and `log.md` files carry no section tag,
and neither do concepts at the bundle root, such as the
[overview](overview.md), which belong to no section. The
[overview](overview.md) explains why section membership is carried in metadata
as well as in the path.
