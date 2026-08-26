---
type: Guide
title: Designing evaluations for C4 structure
description: Use when C4 Software Systems, Containers, or Components need satisfaction and realization evidence; evaluate canonical elements without treating Views as subjects.
tags: [evaluations, c4, software-systems, containers, components, requirements]
status: draft
sources:
  - resource: designing-a-system-evaluation-approach.md
    title: Designing a system evaluation approach
  - resource: ../architecture/structure/c4-model.md
    title: C4 model
---

# Designing evaluations for C4 structure

## Goal

Evaluate Requirement satisfaction and structural realization across the
canonical C4 Software System → Container → Component hierarchy.

## Steps

1. Attach each Definition to the narrowest canonical C4 element whose accepted
   responsibility or boundary owns the claim. C4 Views select and project
   elements; they are evaluation context, not evaluation subjects.
2. For `requirement-satisfaction`, reference subject-colocated Requirement IDs
   and assess the realized element under stated conditions.
3. For `architecture-realization`, assess the accepted structural response:

   - Software System: software boundary, value-bearing responsibility, direct
     interactors, external relationships, and system-level constraints;
   - Container: containing System, runtime or data-store boundary,
     responsibility, technology consequences, interfaces, data ownership,
     communication, resilience, and deployment assumptions; and
   - Component: one owning Container, cohesive responsibility, defined
     interface, dependencies, state or authority ownership, and containment.

4. Combine static architecture checks, dependency and schema analysis,
   contract tests, dynamic scenarios, deployment inspection, fault injection,
   and operational measures according to the claim. A generated diagram or
   dependency graph is an Observation until a Definition applies criteria.
5. Project Results down and up the C4 hierarchy and across linked Surface,
   Feature, Capability, and Bounded Context views. Do not infer those mappings
   from C4 containment.
6. Publish separate Requirement-satisfaction and Architecture-realization
   reports. Parent status must disclose failing, missing, stale, or unknown
   descendants; child conformance does not prove system-level relationships or
   outcomes.

## Final check

- Every subject is a canonical C4 element, never a View or suite folder.
- Each Container has one System and each Component one Container in the
  evaluated model.
- Boundary and relationship claims receive evidence, not just element
  existence checks.
- Cross-view links are explicit and do not create a new containment hierarchy.
- Requirement satisfaction and structural realization remain separate claims.

## Related

- [Designing a system evaluation approach](designing-a-system-evaluation-approach.md)
- [C4 model](../architecture/structure/c4-model.md)
- [Reviewing responsibilities with scenarios](../architecture/reviewing-responsibilities-with-scenarios.md)
