# Quality module

A module of the [Spec profile](../profile.md), version **0.1.0**. It adds
quality characteristics and the required levels of them, with the measures
those levels use. Its tables extend the profile's tables of the same name.

## Concept types

| Type | Description |
| --- | --- |
| [`Quality Characteristic`](../../templates/quality-characteristic.md) | A property of how well the system or a subsystem works, such as availability or response time. |
| [`Quality Requirement`](../../templates/quality-requirement.md) | A required level of a quality characteristic for the system or a subsystem, under stated conditions. |

## Vocabulary

| Term | Meaning |
| --- | --- |
| Measure | A quantity on which a Quality Requirement states a level, defined under a Quality Characteristic's **Measures**. |

A Quality Requirement's subject is the Subsystem its statement names, or
otherwise the System.

## Structure

```text
spec/
  quality/
    <characteristic>/
      <characteristic>.md          # Quality Characteristic
      <quality-requirement>.md     # Quality Requirement
```

### Folders

| Folder | Holds |
| --- | --- |
| `quality/` | A folder for each `Quality Characteristic` |
| `<characteristic>/` | Its `Quality Characteristic` document and its `Quality Requirement` documents |

Quality characteristics are folders, as P-STR-5 requires.

## Placement

### Fixed locations

| Type | Location |
| --- | --- |
| `Quality Characteristic` | `quality/<characteristic>/` |
| `Quality Requirement` | `quality/<characteristic>/`, as the [Quality Requirement contract](../../templates/quality-requirement.md#type-contract) chooses the characteristic |

A measure has one home however many quality requirements use it, as the
[Quality Characteristic contract](../../templates/quality-characteristic.md#type-contract)
requires, because those quality requirements are placed beside it.

## Ownership tests

### Where content goes

| Concern | Owning type |
| --- | --- |
| What a quality characteristic is | That Quality Characteristic, whose **Definition** is the only definition. A glossary entry for its name has no definition and a **Defined by** line. |

### Quality requirement or requirement

- **P-QUA-1** An obligation that could be a Requirement or a Quality
  Requirement MUST be placed by the first of these questions answered yes.

1. Can it be satisfied only by providing a specific function, or by using a
   specific technology, platform, or design? It is a Requirement, a design
   constraint when it names a technology, platform, or design, and it
   **serves** the quality characteristic it helps achieve.
2. Is compliance decided on each occurrence of a single response, such as a
   deadline or value for each notice sent? It is a Requirement.
3. Is compliance decided on a measure taken over a population of occurrences
   or a period, such as a percentile or a proportion of time, or on a
   criterion that holds across the subject's functions? It is a Quality
   Requirement.

An obligation for which no question is answered yes is recorded under
**Open questions** until it is restated.

## Not yet defined

| Topic | Interim practice |
| --- | --- |
| Correspondence between quality characteristics and a quality model, such as ISO/IEC 25010 | Give the model's name for a characteristic on the **Also called** line of the glossary entry for the characteristic's name. |
| Baselines of quality requirements | State the current or previous level, with its source, period, and population, under **Rationale**. |
| Quality characteristics nested within other quality characteristics | Define each characteristic on its own. |
