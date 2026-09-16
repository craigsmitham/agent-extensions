# Quality Requirement template

Use for one required level of a quality characteristic of the system or a
subsystem, under stated conditions, such as a response time at peak load.
Apply the [Spec profile](../references/profile.md). The Type contract is
normative; the remaining sections guide authoring.

It parallels the [Requirement template](requirement.md), with the
[differences](#differences-from-the-requirement-template) recorded below.

## Type contract

- **QR-1** The title MUST name the obligation briefly as a declarative
  phrase, such as "Search responds within limit at peak load".
- **QR-2** A Quality Requirement document MUST include these sections:
  - **Requirement**: the required level, naming the subject, any conditions
    under which the level applies, the one feature, feature component, or
    external interface it is limited to, if any, any exceptions, and either a
    linked measure with its required limit or range or the criterion by which
    satisfaction is decided, with *shall* for the obligation.
  - **Rationale** *(optional)*: why this level is required.
  - **Verification** *(optional)*: how the level will be assessed, and what
    counts as satisfied.
- **QR-3** A Quality Requirement document MUST state exactly one required
  level of one quality characteristic.
- **QR-4** A Quality Requirement MUST be placed in the folder of the quality
  characteristic whose property it states, even when the level is limited to
  one feature, feature component, or external interface.
- **QR-5** A level that is desired but not required MUST NOT be stated as the
  required level.

A different level for another condition, subject, or concept it applies to is
a separate quality requirement.

## Suggested document

```markdown
---
type: Quality Requirement
title: <Obligation as a short declarative phrase>
description: <The requirement statement, or a one-sentence summary of it>
status: draft
---

# <Obligation as a short declarative phrase>

## Requirement

While <condition>, the <subject> shall keep [<measure>](<link>) for <feature, component, or interface> at or below <limit>.

## Illustrations
## Rationale
## Verification
## Open questions
## Related
```

## Writing guidance

### Differences from the Requirement template

| Difference | Reason |
| --- | --- |
| Links its measure rather than defining it | Every measure lives under the characteristic's **Measures**, as the [Quality Characteristic contract](quality-characteristic.md#type-contract) requires, so that levels on it can be compared. |
| Names *any conditions* rather than *any conditions or trigger* | Compliance is decided over many occurrences, so a stimulus in a scenario is stated as a condition of the level rather than a trigger of one response. |
| Does not state **enforces** or **serves** | Its folder already shows the characteristic it concerns, and rules and objectives are served through the Requirements for functions, which state those relationships. |

The title style, *shall*, exceptions, forms, **replaces**, and provenance in
`sources` are the same as in the Requirement template. Because its folder is
at the system level, placement does not show its subject: the statement names
a Subsystem that must reach the level, as the
[Quality module](../references/modules/quality.md#vocabulary) describes.

### Kind of level

Apply the [Requirement statement guidance](requirement.md#statement). A
quality requirement states one of these kinds of level:

| Kind | Use for | Example |
| --- | --- | --- |
| Measured level | A level of a measure, under any conditions, including a stimulus such as an outage | While the rental system is at [peak load](<link to the operating environment>), the rental system shall keep [search response time](<link to Response time measures>) at or below 2 seconds. |
| Criterion | A property no quantity expresses | The rental system shall reveal no customer's payment details to another customer. |

State a measured level as a limit, such as "at or below 2 seconds", or as a
target with an acceptable range. When the level is limited to one feature,
feature component, or external interface, name and link it in the statement,
such as search response time for [Equipment search](<link>); otherwise the
level applies to the whole subject.

[Search withstands a depot outage](<link>) states a level under a stimulus:
while one depot's network connection is lost, the rental system shall keep
search response time for all other depots no more than 10% above its level in
the hour before the loss. [Reservations are available](<link>) links
reservation availability under [Availability](<link>), even though no other
requirement uses it.

### Rationale and verification

- **Rationale**: the need or risk the level answers, any current or previous
  level as [Not yet defined](../references/modules/quality.md#not-yet-defined)
  describes for baselines, and the trade-offs accepted.
- **Verification**: such as a load test under the stated condition, and
  whether observation in operation confirms it.

### One required level

- A minimum and a desired level are separate: only the minimum is required.
  Record a desired level that is not required under **Rationale** or
  **Open questions**.
- A target that is not yet decided is an open question. Do not choose a
  plausible number.
- [Payment details stay private](<link>) states a criterion for
  Confidentiality and is placed in its folder.
- For two levels that cannot both be fully met, follow
  [Not yet defined](../references/profile.md#not-yet-defined).
