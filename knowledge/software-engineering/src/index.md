---
okf_version: "0.2"
---

# Software engineering

Portable engineering craft for reviewing software products through repository
and other available evidence, designing test architecture, and shaping
repository execution surfaces.
Use this bundle for outcome-centered assessment of suitability, correctness,
reliability, security, safety, efficiency, usability, compatibility,
evolvability, and intelligibility; for explicit treatment of cross-cutting
context and evidence; for selecting representative cross-boundary and
browser-dependent test worlds; and for tool-neutral guidance on task graphs
and invocation contracts. It is not a software-change method, requirements or
architecture lifecycle, work-item system, documentation-craft guide, or
language and framework reference.

## Review codebases

- [Codebase review](codebase-review/) - An outcome-centered review framework with ten product-quality criteria lists, eight typed cross-cutting records, separate supporting-artifact assessments, optional evidence and method aids, and explicit uncertainty and lifecycle guidance.

## Design repository task interfaces

- [Designing a coherent repository task interface](repository-task-interface.md) - Use when repository tasks, scripts, launchers, wrappers, or CI paths compete, or when placing new repeatable work; design one discoverable resolved task contract that humans, agents, and automation can invoke consistently without forcing every workflow into one tool.

## Design tests

- [Designing cross-boundary and end-to-end tests](designing-cross-boundary-and-end-to-end-tests.md) - Use when a material risk spans components, processes, services, storage, artifacts, or deployment configuration; design the smallest representative test world that can provide attributable evidence across the necessary boundaries.
- [Choosing browser-dependent interface tests](choosing-browser-dependent-interface-tests.md) - Use when an interface claim may depend on real browser rendering, interaction, accessibility, or platform behavior; admit the least costly browser-capable test and evidence matrix that can faithfully reveal the risk.
