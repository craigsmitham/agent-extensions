---
type: Explanation
description: How durable architectural constraints become trustworthy through precise statements and proportionate executable enforcement.
tags: [invariants, enforcement, architecture-tests, constraints, verification]
status: draft
---

# Invariants and enforcement

An architectural invariant is a condition that must remain true across normal
implementation change. It protects a responsibility, boundary, or quality that
would otherwise be easy to violate locally.

A useful invariant states:

- what must or must not happen;
- the scope in which it applies;
- why it matters; and
- which authority decides conformance.

Mechanically decidable constraints belong in executable checks when practical:
import rules, schema validation, contract tests, policy checks, or deployment
guards. Prose explains the meaning; the check detects violations. Duplicating a
complete executable rule in prose creates two authorities.

Not every architectural principle warrants a guardrail. Enforcement has cost
and can freeze an obsolete decision. Automate when violations are consequential,
plausible, and objectively detectable. Leave judgment to review when context is
essential or the rule would be more complex than the risk it controls.

An invariant without an enforcement mechanism can still be valid, but its
owner should know what evidence reveals conformance. “We follow good
architecture” is not an invariant because neither its boundary nor its failure
condition is clear.
