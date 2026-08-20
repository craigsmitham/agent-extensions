---
type: Explanation
title: Domain context views
description: How bounded contexts model semantic, policy, authority, and state boundaries without becoming a synonym for services, modules, or teams.
tags: [domain-driven-design, bounded-contexts, context-map, authority, state-ownership, ubiquitous-language]
status: draft
generated:
  by: codex/gpt-5.6
  at: 2026-08-20T19:56:11Z
---

# Domain context views

A bounded context identifies where a domain model, language, policy, and source
of authority are internally consistent. It answers who decides what terms mean,
who owns consequential rules and state, and how those decisions cross into
another context.

Bounded contexts are not automatically services, deployables, packages, teams,
or database schemas. Those structures can align with a context when the
boundary is valuable, but equating them by default confuses semantic ownership
with current implementation.

## Describe a context

Record the durable distinctions that make the boundary matter:

- the responsibility and outcomes the context owns;
- its local language and any terms that differ from neighboring contexts;
- the policy and state for which it is authoritative;
- what it deliberately does not own;
- upstream facts it accepts and downstream promises it makes; and
- translation, validation, consistency, and failure obligations at each
  material relationship.

A context map is a relationship view across contexts. Name direction and
meaning rather than drawing untyped lines. Useful relationships include an
upstream model consumed downstream, a published language, a translation or
anti-corruption boundary, and a shared model whose coordination cost is
accepted explicitly.

## Connect contexts to other views

Features may be governed by one context while being available through several
surfaces and realized by several containers. A container may host parts of
several contexts, and one context may span several containers. These are
possible architectural consequences, not contradictions.

When alignment matters, state the intended relationship and why. For example,
a context may require an independent persistence authority without requiring an
independent deployment unit, or a container boundary may isolate trust even
though the domain language remains shared.

Use context documents for semantic and authority boundaries that are expensive
to infer. Keep exact schemas, endpoint contracts, table inventories, and
current module placement with their executable owners.
