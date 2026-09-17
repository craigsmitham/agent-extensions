# Quality Characteristic template

Use for one property of how well the system or a subsystem works, such as
availability or response time.

## Type contract

- **QC-1** The title MUST name the property as a noun phrase, such as
  "Availability" or "Response time", not a required level or a function.
- **QC-2** A Quality Characteristic document MUST include these sections:
  - **Definition**: what the property means for its system or subsystem,
    following the profile's
    [definition rules](../references/profile.md#definitions).
  - **Importance**: why the property matters, stating **serves** for each
    user class and objective it matters to, and naming any risk that
    makes it matter.
  - **Measures** *(when a quality requirement states a level on a measure)*:
    each such measure.
- **QC-3** A quality characteristic MUST be created only when it has
  quality requirements.
- **QC-4** Each measure on which a quality requirement states a level MUST be
  defined under its own heading in **Measures**, precisely enough that two
  readers would compute the same value for the same population and period.
- **QC-5** A Quality Characteristic document MUST NOT state conditions or
  required levels, which belong to its Quality Requirements.

## Suggested document

```markdown
---
type: Quality Characteristic
title: <Property as a noun phrase>
description: <What the property means for the system or subsystem, in one sentence>
---

# <Property as a noun phrase>

## Definition
## Importance
## Measures
### <Measure name>

| Element | Definition |
| --- | --- |
| Meaning | <What the quantity shows about the property> |
| Population | <What is counted or observed, and what is excluded> |
| Formula and unit | <How the value is calculated, and its unit> |
| Aggregation and window | <Such as the 95th percentile over each hour> |
| Method | <Where and how the quantity is observed> |

## Open questions
## Related
```

## Writing guidance

### Choosing the characteristics

There is no fixed set of quality characteristics. Choose the set for the
system or subsystem:

1. Start from what matters: objectives,
   user class needs, risks, regulations, and the operating environment. Each
   characteristic traces to at least one of them under **Importance**.
2. Check the set against a quality model, such as the characteristics and
   subcharacteristics of ISO/IEC 25010, to find what is missing. The model is
   a checklist, not the list of names. To record the correspondence, give the
   model's name on the **Also called** line of the glossary entry for the
   characteristic's name.
3. Split a characteristic whose parts matter to different stakeholders or are
   judged in different ways, such as performance into response time and
   capacity. Merge characteristics that stakeholders never tell apart.
4. Draw characteristics so that each quality requirement has one clear home:
   the characteristic whose property it states. When a requirement could
   belong to either of two characteristics, redraw them.

Some parts of a quality model are placed elsewhere:

- Functional suitability is stated through Requirements, except measurable
  properties such as the precision of calculated results, which are Quality
  Requirements.
- The required accuracy or currentness of kept data is a Quality Requirement
  of a data quality characteristic that links the Entity Type or Value Type
  under **Related**.
- Targets on artifacts rather than the product, such as code complexity,
  belong in engineering records, unless a stakeholder requires them of the
  delivered product.

Characteristics all live at the system level, and each is defined on its own.
A characteristic that only one subsystem needs links that subsystem under
**Related**, and one whose meaning differs for a subsystem takes a distinct
name. Where stakeholders reason about a group, such as security, create
separate characteristics for the parts they judge, such as *Confidentiality*.

### Naming

- Name the property, not a required level or a function: *Availability*, not
  *High availability*; *Confidentiality*, not *Secure login*.
- Use the stakeholders' word. Other names, including the quality model's name
  when it differs, go on the **Also called** line of the name's glossary
  entry.
- Choose names that will last. The folder takes the characteristic's name, so
  a rename moves the folder and changes inbound links.

### Definition

A quality model's definition is a starting point; narrow it to what the
stakeholders mean. *Availability* for the rental system is "the proportion of
time during which contractor customers can reserve equipment", rather than
"the degree to which a system is operational and accessible when required for
use".

The **Definition** is the only definition of the characteristic's name, as
[P-CON-2](../references/profile.md#one-home) requires.

### Measures

Every measure that a quality requirement states a level on is defined here,
under its own heading, so that required levels of the property can be compared
and a second requirement can link the same measure. A measure is usually
precise enough when each of these elements is answered:

| Element | Content |
| --- | --- |
| Meaning | What the quantity shows about the property. |
| Population | The events, requests, users, periods, or items counted, and what is excluded, such as announced maintenance. For a ratio, which events are eligible, which count as good, and how unknown outcomes count. |
| Formula and unit | The calculation and its unit. |
| Aggregation and window | Percentiles rather than averages where the distribution matters, and the period over which the value is taken, with its time zone or calendar where it matters. |
| Method | Where the quantity is observed, such as at the boundary as a user experiences it, and how: test, analysis, or observation in operation. |

Search response time, which both
[Search responds within limit at peak load](<link>) and
[Search withstands a depot outage](<link>) use, is defined under *Response
time*. Reservation availability is defined under *Availability*, with its
undecided method kept and recorded as a gap:

~~~markdown
### Reservation availability

| Element | Definition |
| --- | --- |
| Meaning | The proportion of time during which contractor customers can reserve equipment |
| Population | The time in the calendar month, excluding maintenance announced 48 hours ahead |
| Formula and unit | Time during which contractor customers can reserve equipment, divided by that time, as a percentage |
| Aggregation and window | Each calendar month |
| Method | Undecided; see **Open questions** |
~~~

How a measure is instrumented, its coverage, and its history are operations
concerns, which belong in operations records.

### Related

Link records behind the characteristic's importance, such as research or
incident reports. Requirements that help achieve the characteristic state
**serves** from their own side.
