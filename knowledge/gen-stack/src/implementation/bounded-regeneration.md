---
type: Guide
title: Bounded regeneration
description: Use when considering regeneration of replaceable Implementation Units; make regeneration earn trust through conservation boundaries, operational memory, and rollback.
tags: [regeneration, replacement, deletion-test, data, contracts, rollback, operational-memory]
generated: { by: "codex/gpt-5.6", at: "2026-08-26T14:02:36Z" }
---

# Bounded regeneration

Treat regeneration as an earned property of a bounded Implementation Unit or
coordinated set of Units, not as a synonym for generating more code.

Before replacing or regenerating an Implementation Unit:

1. Identify the accepted Requirements, public contracts, persistent data,
   security and compliance boundaries, and operational envelope that must be
   conserved.
2. Extract knowledge that exists only in implementation behavior, incidents,
   runbooks, or experienced maintainers. Classify observations separately from
   accepted intent.
3. Establish diverse evaluations for the conserved behavior and failure modes.
4. Bound the writable scope and dependencies of the replacement mechanism.
5. Make the change observable, containable, and reversible; define rollback
   against durable state rather than only source files.
6. Compare the new Implementation with its Requirements, Architecture, and
   evaluation evidence.
7. Compact the superseded Unit only after the replacement and recovery path
   are established.

Use a deletion test as a diagnostic: if an Implementation Unit disappeared,
could the system be rebuilt from retained Requirements, Architecture, data,
contracts, decisions, operational memory, and Evaluations without
rediscovering critical behavior in production? A failed deletion test
identifies missing conservation knowledge; it does not authorize
reconstructing that knowledge as accepted Intent without review.
