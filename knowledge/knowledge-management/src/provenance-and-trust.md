---
type: Explanation
description: How source, transformation, evidence, currency, and review determine what confidence a knowledge consumer should place in a claim.
tags: [provenance, trust, evidence, verification, knowledge-quality]
status: draft
sources:
  - id: w3c-prov-overview
    resource: https://www.w3.org/TR/prov-overview/
    title: W3C PROV Overview
  - id: fair-principles
    resource: https://doi.org/10.1038/sdata.2016.18
    title: The FAIR Guiding Principles for scientific data management and stewardship
---

# Provenance and trust

Provenance explains where knowledge came from and what happened to it before a
reader encountered it. The W3C PROV model distinguishes entities, activities,
and agents so a result can be traced to its inputs and production.[^prov]

Useful provenance answers the questions that change reliance:

- Is this a primary source, an observation, or a later synthesis?
- Who or what produced and reviewed it?
- What evidence supports a current-state claim?
- Has the subject changed since the evidence was gathered?
- What license or use conditions apply?

Metadata cannot certify truth. A citation may be irrelevant, a review may be
shallow, and recent content may still be wrong. Provenance makes judgment
possible; accountable review supplies the judgment.

Trust is contextual. A draft synthesis may be adequate for exploration but not
for a contractual decision. An old source may remain authoritative for a
historical claim but unsafe for current behavior. State, confidence, and
currency should therefore be exposed when they materially affect use, not added
as decorative fields.

Public visibility is also not a trust level. Publication describes access;
authority and evidence describe warranted reliance.

[^prov]: W3C PROV provides a general model for representing the origins and
    transformations of digital information.
