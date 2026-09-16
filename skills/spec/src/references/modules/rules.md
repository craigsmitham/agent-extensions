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
  rules/
```

### Folders

| Folder | Holds |
| --- | --- |
| `rules/` | `Business Rule` documents |

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
  placed as the following question decides.

Would it still apply if the business worked without the system? If so, it is a
Business Rule, whether the business chose it or an outside authority, such as
a law, regulation, standard, or contract, imposes it. If not, it is a
Requirement. How the system detects, prevents, permits an override of, or
reports a violation of a rule is a Requirement that **enforces** the rule.

## Relationships

| Relationship | Meaning | Stated in | Links to |
| --- | --- | --- | --- |
| enforces | How the system respects a rule | Requirement | Business Rule |

## Not yet defined

| Topic | Interim practice |
| --- | --- |
| Business rule categories, such as computation, inference, action enabler, and constraint, and wording that shows them | Write a rule that people could break with *must*, *must not*, or *may … only if*, and a rule that defines, infers, or computes as a plain statement of fact. |
| Business rule volatility | State under the rule's **Rationale** whether its values are expected to change, and how often. |
| Relationships between business rules, such as one rule using another's result | Link the rule whose result is used under **Related**. |
| Business rule enforcement levels, and rules that permit an actor to break another rule | State the exception in the rule, as the profile's [Exceptions](../profile.md#exceptions) requires, and give its source or rationale under **Rationale**. |
