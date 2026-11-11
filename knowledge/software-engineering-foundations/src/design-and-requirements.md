---
type: Explanation
title: Design and requirements
description: The existing account of design choices, design altitudes, and requirements as disputable commitments.
tags:
- software-engineering-foundations
status: draft
generated:
  by: codex/gpt-6
  at: '2026-11-11T18:36:09Z'
sources:
- id: migration-source
  resource: https://github.com/craigsmitham/agent-extensions/blob/c56a54cb5cdb2c14c0d71801709c2b38968c99dd/knowledge/product-engineering/src/overview.md
  title: Existing product-engineering material before the discipline migration
---

# Design and requirements

Design is choosing the form a solution will take, at a deliberate resolution,
from alternatives that were genuinely considered. A statement becomes design
the moment it constrains form; until then it describes a problem. That test is
what separates problem framing from choosing a solution's form.

This passage is the definition of record. A section that needs it cites this
one rather than repeating it, on the requirement principle [One authority, many
witnesses](requirements/one-authority-many-witnesses.md):
a second copy of a definition becomes a second authority the moment one of the
two is edited, and the bundle would then hold two accounts of design without
anyone having decided to change it.

Design is an activity that recurs at several altitudes.

| Altitude | Question answered | Discipline |
| --- | --- | --- |
| Solution concept | Which shape of solution do we commit to, and what will we not do? | Architecture and design |
| Interaction | What does a person encounter, and how do they operate it? | Architecture and design |
| Technical | How is the system structured so it can be built and changed? | Architecture and design |
| Operational | How is the running system arranged so it can be observed and recovered? | Software operations |

Naming the altitudes distinguishes the design questions.

A requirement is not a rival to design. It is the form a design choice takes
once it must survive being disputed, traced through change, and bound to
verification, which connects requirements engineering with design. Requirements
are chosen rather than discovered, and the choosing is design work.

Design and construction do not form a one-way handoff. What crosses that
boundary is a commitment, not a finished specification, and technical design
regularly sends it back.
