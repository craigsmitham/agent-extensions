# Data module

A module of the [Spec profile](../profile.md), version **0.1.0**. It adds
entity types and value types, which describe the business data the system
keeps. Its tables extend the profile's tables of the same name.

## Concept types

| Type | Description |
| --- | --- |
| [`Entity Type`](../../templates/entity-type.md) | A kind of thing in the business domain that has identity and about which the system keeps data. |
| [`Value Type`](../../templates/value-type.md) | A kind of value in the business domain that has no identity and is defined by its meaning, attributes or domain, and allowed values. |

## Vocabulary

| Term | Meaning |
| --- | --- |
| Attribute | A data attribute: an item of data kept about an Entity Type's instance or making up a Value Type's value. |
| Instance | An item of the data that an Entity Type describes. |
| Invariant | A condition that every instance of an Entity Type, or every value of a Value Type, satisfies because of what the data means. |

## Structure

```text
spec/
  entities/                        # Entity Type documents
  values/                          # Value Type documents
```

## Placement

### Fixed locations

| Type | Location |
| --- | --- |
| `Entity Type` | `entities/` |
| `Value Type` | `values/` |

Features link to entity types rather than containing them. A data attribute
that only one feature needs still belongs to its entity type.

## Ownership tests

### Where content goes

| Concern | Owning type |
| --- | --- |
| The states of an entity type's instances, the permitted transitions, what creates an instance, and whether an ended instance is removed, retained, or anonymized | The Entity Type's **Lifecycle** |
| What the system must do when a transition occurs, or when a transition that the lifecycle does not permit is attempted | Requirement, linking to the lifecycle |
| How long instances or their data are kept, and who may see them | Not the Entity Type; the rule or obligation that sets it, placed by the other ownership tests |
| A value that more than one entity type, value type, or external interface uses | A Value Type |

### Invariant, business rule, or requirement

- **P-DAT-1** A condition on data MUST be placed by the first of these
  questions answered yes.

1. Would changing the condition change what the data means? It is an
   invariant of the Entity Type or Value Type.
2. Did the business choose the condition, or does an outside authority impose
   it, such as a policy that limits a relationship's cardinality further than
   the data allows? It is a Business Rule, or, in a corpus without the Rules
   module, is written as the profile's [Modules](../profile.md#modules) table
   gives.
3. Otherwise, the solution imposes it, and it is a Requirement that is a
   design constraint.

What the system must do to keep an invariant or rule true, across
transitions, concurrency, retries, and failures, is a Requirement.

### Entity type, value type, or data attribute

- **P-DAT-2** A kind of thing or value in the business data MUST be placed by
  the first of these questions answered yes.

1. Must its instances be told apart even when all their data is equal? It is
   an Entity Type.
2. Otherwise, its equal values are interchangeable, and it is a Value Type,
   or a data attribute defined where it is used when the
   [where content goes](#where-content-goes) allows.
