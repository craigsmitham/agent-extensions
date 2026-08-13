---
type: Explanation
description: How routing layers, stable concepts, and search metadata make knowledge findable without duplicating it at every entry point.
tags: [discovery, progressive-disclosure, information-architecture, indexes, findability]
status: draft
sources:
  - id: fair-principles
    resource: https://doi.org/10.1038/sdata.2016.18
    title: The FAIR Guiding Principles for scientific data management and stewardship
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Open Knowledge Format specification
---

# Discovery and structure

Knowledge is useful only when a reader can reach the right source at the moment
of need. Findability therefore belongs to the knowledge itself, not merely to a
separate search tool.[^fair]

Progressive disclosure separates routing from explanation:

1. A catalog or instruction entry says whether a corpus is relevant.
2. An index groups and distinguishes destinations.
3. Search metadata helps a reader select a concept.
4. The concept owns the substantive knowledge.

Each layer should contain only enough information to make the next decision.
Putting explanations into an index makes the route slower and creates a second
place to maintain the meaning. An overview is a concept, not an oversized
index.

Structure should follow distinctions readers actually use. Begin flat. Add a
section only when several independently useful concepts share a coherent
subject and the new route makes selection easier. Avoid directories created
for symmetry, mirrors of implementation structure, and a document for every
possible intersection of two taxonomies.

Descriptions and tags should distinguish neighboring concepts using vocabulary
readers are likely to search. Links express navigation and relationships;
metadata should add retrieval value rather than repeat titles mechanically.

[^fair]: The FAIR principles identify findability and rich metadata as
    prerequisites for reuse. Their original domain is research data; the
    discovery concern generalizes to durable digital knowledge.
