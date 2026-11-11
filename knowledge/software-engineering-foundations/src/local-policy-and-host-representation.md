---
type: Reference
title: Local policy and host representation
description: Preserves artifact meaning across local policy, native fields, derived views, and external persistence.
tags: [authority, local-policy, host, mapping, native-fields, provenance, software-engineering-foundations]
generated: { by: codex/gpt-6, at: 2026-11-11T19:45:59Z }
sources:
- id: prior-applying-project-specific-considerations
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/software-engineering-foundations/src/work-items/applying-project-specific-considerations.md
  title: Applying repository-specific work-item considerations
- id: prior-mapping-to-work-item-hosts
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/software-engineering-foundations/src/work-items/mapping-to-work-item-hosts.md
  title: Mapping work items to native hosts
- id: prior-applying-project-specific-requirements-policy
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/requirements-engineering/src/adaptation/applying-project-specific-requirements-policy.md
  title: Applying project-specific requirements policy
- id: prior-mapping-to-requirements-hosts
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/requirements-engineering/src/adaptation/mapping-to-requirements-hosts.md
  title: Mapping to requirements hosts
---

# Local policy and host representation

Portable artifact contracts define meaning. Repository, project, and
organizational instructions establish applicable local policy: terminology,
fields, decision authority, rigor, lifecycle rules, confidentiality, retention,
and access. Apply documented obligations where their conditions hold; generic
good practice does not establish a local requirement.

Local content belongs in the corresponding contract slot, with a separate
section only for meaning no existing slot carries. An API compatibility rule,
for example, may contribute constraints, migration context, completion
conditions, and verification without creating a new work-item role.

When policy changes a portable semantic assumption, make the conflict visible
and follow the higher-precedence authority. Labels must not silently become
proof of acceptance, diagnosis, verification, or closure.

## One authoritative representation

[One authority, many witnesses](requirements/one-authority-many-witnesses.md)
distinguishes governing content from its representations. A host record or
export is a witness unless explicitly designated as authoritative.

Use native structured fields and typed relationships when the actual schema
preserves the artifact contract exactly. Similar names do not establish equal
meaning. Record local state, classification, and relationship mappings when
needed; preserve unmapped dimensions and disclose lossy mappings.

Each editable fact has one authoritative home. Body content carries residual
meaning, not a second metadata block competing with native fields. Generated
views and reciprocal links derive from that home, with stable references and
synchronization ownership. Requirement and work-item identities and lifecycles
remain independent even when they share a host.

## Persistence and mutation boundaries

Drafting or read-only analysis does not authorize external writes. A mutation
has an exact host, project, target identity or new-record destination, current
revision, intended changes, and authority. Assignment, priority, status,
closure, comments, and relationships are included only when the requested
scope or established workflow covers them.

A submitted payload is not persistence evidence. Readback establishes the
persisted identity, fields, formatting, relationships, body, and revision.
Batch results identify successes, failures, and unverified items separately;
atomic success requires host support.
