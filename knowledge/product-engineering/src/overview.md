---
type: Explanation
title: Product engineering overview
description: How this body of knowledge is organized as six practitioner questions, why that scheme was chosen over lifecycle or artifact schemes, how deep the scheme runs and what a subtree may be named for, which seventh question was tried and retired, where design fits, and what stays outside it.
tags: [product-engineering, body-of-knowledge, information-architecture, organizing-scheme, design, explanation]
status: draft
---

# Product engineering overview

This bundle collects the portable craft of building software products. It is
organized around the questions a practitioner is actually facing, because that
is how both people and agents reach for knowledge: by the problem in front of
them, not by the file a claim happens to live in.

## The six questions

| Question | Section | What it owns |
| --- | --- | --- |
| Where should we participate, and how do we win there? | Where to play | The organization-level choice of arena |
| Which problems are worth solving, and what outcome would tell us we succeeded? | What to solve | The problem, the outcome, and the evidence that the outcome occurred |
| Which solution concept do we commit to, and how do we state that commitment so others can dispute it? | What to build | The search across candidate forms and the commitment that ends it, stated so it can be disputed |
| How do we construct and verify what we committed to? | How to build it | Technical design, construction, and evidence of behavior |
| How does a change reach production safely and predictably? | How to ship it | The movement of change toward release |
| How does the product stay healthy, secure, and affordable in production? | How to run it | Production reality, including incident response and what an incident teaches |

The order is a value stream, but retrieval does not depend on it. Each section
index stands alone for a reader who arrives through search, and each names the
neighbor that owns the adjacent concern.

Sections are not equally developed. The map in [the discovery
index](index.md) says which ones hold concepts today and which hold only their
question, scope, and boundaries.

## Why questions rather than stages or artifacts

Several schemes could organize this material. Each was considered and set aside.

- **Lifecycle or activity**, in the manner of requirements, design, construction,
  testing, and maintenance. Familiar, but cross-cutting concerns such as
  security and evidence then repeat inside every stage, and the sequence reads
  as though the phases were separable in time.
- **Quality outcomes**, such as correctness, reliability, and evolvability.
  These make an excellent review rubric and a poor partition, because a single
  practice usually serves several outcomes at once.
- **Artifact type**, such as code, tests, specifications, and work items. Every
  item gets one obvious home, but practices that span artifacts have none, and
  the result drifts toward tool documentation.
- **Scale**, from statement through module to organization. Useful for design
  material, weak for everything about process and people.
- **Feedback loop**, such as sense, decide, act, verify, and learn. Elegant and
  stable, but almost all content lands under a single node.

Question-shaped sections avoid these failures. A concept belongs where a reader
would go looking for it, and the boundary between two sections is a difference
the reader already recognizes.

## The seventh question, tried and retired

An earlier shape had a seventh section, How to learn: how do we notice what
happened, keep what we learned, and retire what is stale? It has been retired,
and the reasoning is recorded here because knowing why a section was set aside
is as useful as knowing why the others were kept.

The section never found content it could own. Of its four planned areas, two
restated the separate `knowledge-management` bundle, one restated the separate
`field-notes` bundle, and the fourth was never written at all. Nothing was left
in the middle. The only candidate identity that was genuinely product
engineering, learning from what shipped, already had an owner: [Outcomes and
evidence](problem/outcomes-and-evidence.md) covers whether the expected outcome
occurred, and names production use as one link in that evidence chain.

Neither neighboring bundle should move in. Knowledge management stays outside on
exactly the argument this overview already accepts for documentation craft: it
governs agent instructions, skills, and knowledge bundles, none of which are
products, so its audience is wider than product engineering. Field-note practice
stays outside because it is the concept layer of a mechanism this repository
runs, coupled to a rule, a skill, and a pack, rather than portable craft that
travels on its own.

Every clause of the retired question now has an owner.

| Clause | Owner |
| --- | --- |
| Learning from production, including what an incident taught | [How to run it](operations/), as post-incident review |
| Learning whether the expected outcome occurred | [What to solve](problem/) |
| Noticing friction in how work actually goes | The `field-notes` bundle |
| Keeping a claim trustworthy and retiring it when stale | The `knowledge-management` bundle |

There is an irony worth stating. The feedback loop was rejected above as an
organizing scheme because almost all content would land under a single node. As
a section rather than a scheme, the inverse happened: almost none did. The test
this overview sets under [What stays outside](#what-stays-outside) settles it. A
section that cannot be read without another bundle installed means a concept has
been placed in the wrong section, and a section that is nothing but routing to
other bundles fails that test in its entirety.

## Facets, not folders

Some distinctions are real but must not become sections, because a concept can
carry several of them at once. These belong in concept metadata and in section
prose:

- the quality outcome a practice serves;
- the artifact it touches;
- its knowledge form, such as principle, pattern, practice, or reference; and
- whether it is portable craft or a technology binding.

Promoting any of these to a folder would force the same concept to exist in
several places, which is how a corpus starts contradicting itself.

## Depth: sections ask, subtrees hold

Sections are named for questions. Within a section, a subtree may be named for
the artifact whose craft it holds, as [Requirements](solution/requirements/) and
[Work items](delivery/work-items/) are.

That is not artifact type readmitted as an organizing scheme. Artifact type
fails as a partition because a reader arriving at the top of the corpus would
have to guess which artifact their question is about, and because practices that
span artifacts would have no home. A reader who has reached a section has already
chosen the question, and at that depth the artifact is the thing they came for.
The rule is a rule about depth: the question names the section, the artifact may
name the subtree, and no artifact ever names a section.

Two conditions keep the depth rule from becoming a loophole. A subtree earns an
artifact name only where it holds that artifact's craft in enough depth that a
reader wants to land in it directly rather than through the section. And a
concept that spans artifacts stays at the section's top level, because copying
it into each subtree is exactly the failure the facet rule above forbids.

A subtree may equally be named for the body of craft it holds rather than for an
artifact, as [Codebase review](engineering/codebase-review/) and
[Automation](delivery/automation/) are. What a subtree may never be named for is
knowledge form. Form is a facet of every concept rather than a body of craft, so
naming a folder for it would force a concept that is both a pattern and a
practice to exist twice. Where a subtree wants to group its concepts as
patterns, practices, or principles, it does so with headings in its index and
tags on its concepts, which is what [Automation](delivery/automation/) does.

The test is what the folder is named for, not what it happens to contain. A
subtree named for a body of craft may turn out to be uniform in form without
being partitioned by it: every list under
[Criteria](engineering/codebase-review/criteria/) is a checklist and every
concept under [Review aids](engineering/codebase-review/review-aids/) is a
guide, because that craft happens to be expressed one way, not because form
drew the boundary. The signal that form has become the partition is a sibling
folder that holds the same subject in a different form.

The same reasoning runs the other way for section membership, which is a folder
already. Retrieval does not see folders: `axm knowledge concepts query` filters
by bundle and by tag, and bundle is the only scope filter it offers. Without
help, a query cannot ask for the requirements material without also pulling the
codebase-review material. So section membership is carried as a facet too. Every
concept file gets one section tag appended to its existing tags, matching the
directory it sits in.

| Directory | Section tag |
| --- | --- |
| `src/strategy/` | `pe-strategy` |
| `src/problem/` | `pe-problem` |
| `src/solution/` | `pe-solution` |
| `src/engineering/` | `pe-engineering` |
| `src/delivery/` | `pe-delivery` |
| `src/operations/` | `pe-operations` |

Two kinds of file carry no section tag. Reserved `index.md` and `log.md` files
carry none because they are navigation and history rather than retrievable
claims. Concepts at the bundle root carry none because they belong to no
section: this overview is one, and a query that wants it is asking about the
bundle rather than about a question. Every other concept file carries exactly
one. The tag is derived from
the path and adds no meaning of its own; when a concept moves between sections,
its tag moves with it. Treat a section tag that disagrees with the directory as
a defect in the file, not as a second opinion about where the concept belongs.

## Where design fits

Design is choosing the form a solution will take, at a deliberate resolution,
from alternatives that were genuinely considered. A statement becomes design
the moment it constrains form; until then it describes a problem. That test is
what separates What to solve from What to build.

This passage is the definition of record. A section that needs it cites this
one rather than repeating it, on the requirement principle [One authority, many
witnesses](solution/requirements/foundations/one-authority-many-witnesses.md):
a second copy of a definition becomes a second authority the moment one of the
two is edited, and the bundle would then hold two accounts of design without
anyone having decided to change it.

Design is not a section, because it is an activity that recurs at several
altitudes. Sections own altitudes; no section owns the word.

| Altitude | Question answered | Owning section |
| --- | --- | --- |
| Solution concept | Which shape of solution do we commit to, and what will we not do? | What to build |
| Interaction | What does a person encounter, and how do they operate it? | What to build |
| Technical | How is the system structured so it can be built and changed? | How to build it |
| Operational | How is the running system arranged so it can be observed and recovered? | How to run it |

Naming the altitudes is what lets two sections do design work without
colliding, and it is why the sections are named for questions rather than for
the activity.

A requirement is not a rival to design. It is the form a design choice takes
once it must survive being disputed, traced through change, and bound to
verification, which is why What to build owns both. Requirements are chosen
rather than discovered, and the choosing is design work.

Naming What to build and How to build it as a pair does not make them a
handoff. What crosses that boundary is a commitment, not a finished
specification, and technical design regularly sends it back.

## What stays outside

Five things are deliberately not here. Each is real craft; none of it is owned
by a product-engineering question.

| Outside | Why |
| --- | --- |
| Technology bindings | A language, framework, or vendor specific ages on a different clock than the practice does, so it lives in its own bundle and is referenced rather than restated |
| Documentation craft | Expressing knowledge for a reader is a discipline in its own right, with an audience wider than product engineering |
| Knowledge management | It governs agent instructions, skills, and knowledge bundles, none of which are products, so its audience is wider too |
| Field-note practice | It is the concept layer of a mechanism this repository runs, coupled to a rule, a skill, and a pack, rather than portable craft that travels alone |
| Agent engineering | The design of goal-directed model-driven systems is its own discipline, owned by the separate `agent-engineering` bundle; this bundle owns the workflow that surrounds an agent step, not the model-directed choice inside it |

The last row is the youngest and the least obvious, so the sections that touch
it say where the line falls rather than leaving it to this table. [How to ship
it](delivery/) and its [automation](delivery/automation/) subtree both name the
boundary, and [Agents and agentic
workflows](delivery/automation/agents-and-agentic-workflows.md) exists to mark
it, stating for each form of system which concerns delivery automation owns and
which it does not.

### A binding is not a mapping

The first row rules out technology bindings, and one concept in this bundle
looks like a violation of it. The rule is narrower than it reads, and this is
where it is stated exactly.

A **binding** is guidance that only works on one platform: how to configure this
runner, which flag this framework wants, what this vendor calls its own feature.
It ages with the product, it is useless to a reader on a different platform, and
it stays out.

A **mapping** is a dated, comparative statement of how several named platforms
line up against a portable model. It teaches nobody how to operate a platform.
It exists so that the portable model can be checked rather than taken on faith.
[Workflow model](delivery/automation/workflow-model-explainer.md) is the only
one here: its claim is that vendor nouns such as pipeline, job, and step do not
form one hierarchy, and a reader cannot test that claim without seeing the
platforms disagree.

A mapping may stay only under a currency contract, and every condition has to
hold.

| Condition | What it requires |
| --- | --- |
| It serves a portable claim | The mapping makes a portable model checkable, rather than telling a reader how to use a platform |
| It is severable | Removing the mapping leaves the portable model standing and the concept still readable |
| It is dated | The concept carries a `stale_after` date and cites the platform documentation each row rests on |
| It is findable | The concept carries the `vendor-mapping` tag, so every dated mapping in the bundle can be listed in one query |
| It is announced | The owning subtree index names the dated concept and says what a maintainer should do when the date arrives |
| It is rare | A second mapping in one subtree is a sign the bundle is drifting toward vendor documentation, not a precedent |

A mapping past its date is worse than no mapping, because it invites a reader to
trust a hierarchy that has since moved. On the date, refresh the table against
the cited documentation and move the date forward, or delete the table and keep
the model.

A `stale_after` date is not exclusive to mappings. Any concept resting on
material that moves faster than the craft around it may carry one, and
[Agents and agentic workflows](delivery/automation/agents-and-agentic-workflows.md)
does without being a mapping. The contract above adds its remaining conditions
only when the dated material is a vendor mapping. The subtree that holds a dated
concept states what a maintainer does when the date arrives.

Because knowledge bundles cannot declare dependencies on one another, a concept
here must be readable by someone who installed only this bundle. Where a section
borrows a term another bundle owns, it gives the term a short working definition
and names the owner, rather than relying on a link that may not resolve. A
section that cannot be read without another bundle installed is a sign that a
concept has been placed in the wrong section.
