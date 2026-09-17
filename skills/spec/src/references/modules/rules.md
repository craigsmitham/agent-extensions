# Rules module

A module of the [Spec profile](../profile.md), version **0.1.0**. It adds
business rules, which state what the business decides independently of the
system, so that requirements can enforce them. Its tables extend the
profile's tables of the same name.

## Concept types

| Type | Description |
| --- | --- |
| [`Business Rule`](../../templates/business-rule.md) | A rule under the business's jurisdiction that restricts conduct, requires an action, infers a fact, or computes a value, and that the system must respect. |

## Structure

```text
spec/
  rules/                           # Business Rule documents
```

## Placement

### Fixed locations

| Type | Location |
| --- | --- |
| `Business Rule` | `rules/` |

## Ownership tests

### Where content goes

| Concern | Owning type |
| --- | --- |
| How the business decides whether something belongs to a classification, such as *high-risk customer* | Business Rule. The classification's meaning is a glossary entry with a **Decided by** line. |

### Business rule or requirement

- **P-RUL-1** Content that could be a Business Rule or a Requirement MUST be
  placed by the first of these questions answered yes.

1. Would it still apply if the business worked without the system, whether
   the business chose it or an outside authority, such as a law, regulation,
   standard, or contract, imposes it? It is a Business Rule.
2. Otherwise, it is a Requirement.

How the system detects, prevents, permits an override of, or reports a
violation of a rule is a Requirement that **enforces** the rule.

## Named links

| Named link | Meaning | Stated in | Links to |
| --- | --- | --- | --- |
| enforces | How the system respects a rule | Requirement | Business Rule |
