---
type: Guide
title: Applying project-specific requirements policy
description: Layers local terminology, authority, content obligations, rigor, and lifecycle rules over the portable requirements model. Use when adopting the portable requirements model in a project that has its own instructions, or when local policy and portable guidance appear to conflict.
tags: [adaptation, policy, local-instructions, authority, rigor, requirements-engineering]
sources:
  - id: portable-model
    resource: https://github.com/craigsmitham/agent-extensions/blob/c56a54cb5cdb2c14c0d71801709c2b38968c99dd/knowledge/product-engineering/src/solution/requirements/foundations/requirement-authority-and-maturity.md
    title: Requirement authority and maturity
generated: { by: claude/opus-5, at: 2026-09-08T00:00:00Z }
---

# Applying project-specific requirements policy

Treat repository and organizational instructions as the authority for local
domain content and operating policy. Map them onto the portable model rather
than replacing semantics implicitly.[^portable-model]

This guide covers requirements policy only. Its twin, for the content
obligations repository instructions add to a work item, is Applying
repository-specific work-item
considerations (shared concept: `@craigsmitham/knowledge/software-engineering-foundations#work-items/applying-project-specific-considerations`).
The two overlay different artifacts and share one rule: place local policy
inside the portable model rather than beside it, and surface a conflict about
authority or meaning instead of silently resolving it.

Declare at least:

- project terminology and requirement classification;
- authoritative hosts, identifier rules, and duplicate-text policy;
- candidate and normative states, decision authorities, and approval evidence;
- required fields, source types, relationship types, and change history;
- review depth, assurance obligations, and domain-specific specialists;
- verification and validation expectations;
- confidentiality, regulatory, retention, and access constraints;
- lifecycle and integration rules for work items, designs, tests, and releases.

Apply the stricter applicable obligation when portable guidance and local policy
both govern quality. If they conflict on authority or meaning, surface the
conflict rather than silently choosing one. Project instructions may add
content requirements without forcing the portable model to prescribe a universal
form.

[^portable-model]: Requirement authority and
    maturity (shared concept: `@craigsmitham/knowledge/software-engineering-foundations#requirements/requirement-authority-and-maturity`) states the
    portable candidate-and-normative model this rule layers local policy over,
    leaving project-specific authority with the consuming project.
