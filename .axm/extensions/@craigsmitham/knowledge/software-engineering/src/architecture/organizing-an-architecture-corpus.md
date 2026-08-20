---
type: Guide
title: Organizing an architecture corpus
description: How to organize a view-oriented architecture corpus with progressive disclosure, descriptive subject files, navigational indexes, and explicit cross-view relationships.
tags: [architecture-corpus, information-architecture, progressive-disclosure, index, filenames, relationships]
status: draft
generated:
  by: codex/gpt-5.6
  at: 2026-08-20T19:56:11Z
---

# Organizing an architecture corpus

Organize an architecture corpus so readers can begin with the system as a
whole, choose a question, scan recognizable subject names, and follow explicit
relationships into other views. The directory tree is a discovery aid; it is
not the architecture model itself.

## Start with useful views

A mature corpus may contain collections for:

- strategic position and evolution;
- capabilities and features;
- actor-facing surfaces;
- domain contexts and their relationships;
- structural C4 views, runtime dynamics, deployment, shared modules, and
  structural principles;
- cross-context concerns and external boundaries; and
- experience concerns.

Create only collections that contain current, consequential material. Do not
scaffold an empty taxonomy for symmetry or future completeness.

## Give collections and subjects different shapes

Every major collection that earns a directory uses `index.md` as a navigation
surface. The index states the collection's scope briefly and lists annotated
links to immediate subjects or narrower collections. It does not own the
collection's model or rationale.

Give each substantive subject a descriptive filename such as
`subscription-access.md` or `billing.md`. When one subject grows into several
documents, expand it without changing its conceptual identity:

```text
billing.md

# becomes

billing/
  index.md       # navigation within billing
  overview.md    # meaning of billing as a whole
  ...            # cohesive subordinate subjects
```

`overview.md` earns its place when readers need a mental model,
responsibilities, boundaries, or relationships at that level. It is not a
mandatory partner for every index.

## Preserve one canonical home

Each capability, feature, surface, context, container, component, module, or
other maintained element has one canonical document. A stable primary grouping
may determine its directory, but relationships to other views are links, not
duplicate files or nested ownership claims.

Use descriptive, actor- or domain-recognizable filenames. Avoid numeric
prefixes, generic names such as `feature-1.md`, and filenames that encode a
temporary status. Index annotations should make neighboring subjects
distinguishable without requiring every file to be opened.

## Model relationships explicitly

State relationship types in prose, tables, frontmatter understood by an actual
consumer, or diagrams. Common relationships include contributes to, available
through, governed by, realized by, depends on, upstream of, deployed to, and
constrained by. Folder ancestry alone cannot represent the many-to-many
relationships among architecture views.

For C4 structure, retain its real containment: components live beneath their
owning container. Do not use this exception to turn every other view into a
structural subtree.

## Keep the corpus selective

Apply the architecture admission test before creating any subject file. Prefer
a small corpus with individually useful documents over an exhaustive mirror of
applications, features, packages, services, or deployment resources. Link to
code, schemas, tests, generated references, work tracking, and live systems for
the precise or current facts they own.

Review navigation whenever a subject is added, moved, expanded, merged, or
removed. A finished change leaves every maintained subject reachable from the
corpus root and updates inbound links in the same change.
