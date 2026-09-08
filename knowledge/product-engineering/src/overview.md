---
type: Explanation
title: Product engineering overview
description: How this body of knowledge is organized as seven practitioner questions, why that scheme was chosen over lifecycle or artifact schemes, where design fits, and what stays outside it.
tags: [product-engineering, body-of-knowledge, information-architecture, organizing-scheme, design, explanation]
status: draft
---

# Product engineering overview

This bundle collects the portable craft of building software products. It is
organized around the questions a practitioner is actually facing, because that
is how both people and agents reach for knowledge: by the problem in front of
them, not by the file a claim happens to live in.

## The seven questions

| Question | Section | What it owns |
| --- | --- | --- |
| Where should we participate, and how do we win there? | Where to play | The organization-level choice of arena |
| Which problems are worth solving, and what outcome would tell us we succeeded? | What to solve | The problem and the outcome |
| Which solution concept do we commit to, and how do we state that commitment so others can dispute it? | What to build | The search across candidate forms and the commitment that ends it, stated so it can be disputed |
| How do we construct and verify what we committed to? | How to build it | Technical design, construction, and evidence of behavior |
| How does a change reach production safely and predictably? | How to ship it | The movement of change toward release |
| How does the product stay healthy, secure, and affordable in production? | How to run it | Production reality |
| How do we notice what happened, keep what we learned, and retire what is stale? | How to learn | The feedback loop over every other section |

The order is a value stream, but retrieval does not depend on it. Each section
index stands alone for a reader who arrives through search, and each names the
neighbor that owns the adjacent concern.

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

## Where design fits

Design is choosing the form a solution will take, at a deliberate resolution,
from alternatives that were genuinely considered. A statement becomes design
the moment it constrains form; until then it describes a problem. That test is
what separates What to solve from What to build.

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

The guidance here is technology-agnostic. Anything that churns with a specific
language, framework, or vendor lives in its own bundle and is referenced rather
than restated, because it ages on a different clock than the practice does.

Documentation craft also stays outside, in its own bundle. Expressing knowledge
for a reader is a discipline in its own right, with an audience wider than
product engineering.

Because knowledge bundles cannot declare dependencies on one another, a concept
here must be readable by someone who installed only this bundle. Where a section
borrows a term another bundle owns, it gives the term a short working definition
and names the owner, rather than relying on a link that may not resolve. A
section that cannot be read without another bundle installed is a sign that a
concept has been placed in the wrong section.
