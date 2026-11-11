---
type: Guide
title: Selecting a requirement specification method
description: Selects a specification form proportional to ambiguity, consequence, interaction complexity, and assurance need. Use when prose is leaving an obligation ambiguous, or when choosing among structured syntax, examples, models, and formal notation.
tags: [specification-method, prose, ears, examples, model, formal-method, requirements-engineering]
generated: { by: codex/gpt-6, at: 2026-11-11T19:19:09Z }
---

# Selecting a requirement specification method

Choose the lightest form that makes the obligation precise enough for its
consequence and uncertainty.

| Need | Useful forms |
| --- | --- |
| Simple observable obligation | Controlled natural language or structured prose |
| Conditional or unwanted behavior | [EARS](../foundations/easy-approach-to-requirements-syntax.md)-like condition-response syntax |
| Many rule combinations | Decision table or example table |
| User interaction and alternatives | Scenario, use case, journey, or prototype |
| Stateful or temporal behavior | State model, sequence, temporal rule, or invariant |
| Data relationships and limits | Schema, data model, table, or mathematical expression |
| High consequence or proof obligation | Formal notation plus defined analysis |

Text and model should complement one another. Name the authoritative element
when several representations overlap, and link examples as clarification or
tests rather than letting them silently redefine the requirement.

Do not force every requirement into one syntax. A structured sentence improves
clarity only if it preserves the actual conditions, subject, and outcome.

Some obligations need a form that people outside the authoring team can read and
that fails automatically when the system stops honoring it. Executable specifications (optional companion reading: `@craigsmitham/knowledge/software-testing#patterns/executable-specifications`)
connects that form to its applicability, readable rules and examples, automation
bindings, and continuing evidence. Choosing and accepting the requirement's
form remains a requirements decision; the software-testing pattern explains
how to realize and sustain its executable verification. The requirement record
stays authoritative over the rule unless the project has declared the
specification text to be the requirement.
