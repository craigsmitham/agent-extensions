# Use Case template

Use for all the ways a primary actor can succeed or fail to achieve one goal
at a boundary. Apply the [Spec profile](../references/profile.md). The Type
contract is normative; the remaining sections guide authoring.

## Type contract

A Use Case document is placed as the profile's
[rule-placed types](../references/profile.md#rule-placed-types) rules state,
at its home, which also sets its subject.

- **UC-1** The title MUST name the primary actor's goal as an active verb
  phrase in the present tense, such as "Reserve equipment".
- **UC-2** A Use Case document MUST identify these fields:
  - **Primary actor**: the User Class or External Interface whose goal the use
    case serves.
  - **Secondary actors** *(when a step calls on or notifies a party other than
    the primary actor)*: each such User Class or External Interface.
  - **Trigger** *(optional)*: what starts the interaction.
  - **Preconditions** *(optional)*: what is already true when it starts.
  - **Successful result** *(optional)*: what is true for the primary actor
    when the goal succeeds.
- **UC-3** A Use Case document MUST include these sections:
  - **Main success scenario**: a typical path to success, as numbered steps,
    without branches or failures.
  - **Extensions**: each known condition that makes a step fail or vary,
    labeled by the step where it is detected, and its handling once decided.
- **UC-4** Steps and extensions MUST name data at low precision and link to
  the concept that owns its detail.
- **UC-5** Steps and extensions MUST NOT name user interface elements or
  input and output technology.

## Suggested document

```markdown
---
type: Use Case
title: <Goal as an active verb phrase>
description: <Primary actor> <achieves what>, <with what successful result>
status: draft
---

# <Goal as an active verb phrase>

| Context | Value |
| --- | --- |
| Primary actor | [<User class or external interface>](<link>) |
| Secondary actors | [<User class or external interface>](<link>), … |
| Trigger | <What starts the interaction> |
| Preconditions | <What is already true when it starts> |
| Successful result | <What is true for the primary actor when the goal succeeds> |

## Main success scenario

1. <Actor> <verb> <object>.
2. <System> <verb> <object>.

## Extensions

**2a. <Condition detected at step 2>:**

1. <Actor> <verb> <object>.
2. <Where the scenario resumes, or how the use case ends>.

**\*a. <Condition that can occur at any step>:**

1. <Handling>.

## Illustrations
## Open questions
## Related
```

## Writing guidance

### Context fields

- The subject is the boundary that determines what is visible: everything
  inside it is hidden, and everything outside it is an actor. The use case's
  placement sets it; name it in the steps.
- **Secondary actors** are parties the subject calls on for a service or
  notifies, such as the payment service or depot staff.
- Include a **Trigger** when the start is not obvious, such as a time-based
  start.
- **Preconditions** are what the use case assumes and does not check, such as
  an authenticated contractor customer.
- **Successful result** is what is true for the primary actor when the goal
  succeeds, such as a confirmed reservation.

### Scenario and extensions

**Main success scenario** and **Extensions** state the interaction the subject
supports, at the precision they state it. Undecided handling, unknown steps,
and terms whose meaning is not agreed go under **Open questions**. Worked
walk-throughs with sample data go under **Illustrations**; they add no steps or
conditions. **Related** links the concepts the use case is about, beyond
those already linked in its Context table, steps, and extensions.

### Goal

For the size of a use case's goal, follow
[Not yet defined](../references/profile.md#not-yet-defined), as for Reserve
equipment. To check the goal, ask "in order to accomplish what?" and "how?": a
goal that only serves a larger goal in the same sitting is a step.

### Main success scenario

- Write each step as a simple sentence naming who acts, what they do, and to
  what, in the active voice and present tense.
- Each step is a subgoal that moves the goal forward. When another use case
  achieves a step, link it at that step, such as "Contractor customer
  searches for equipment, as [Search for equipment](<link>) describes."
- Three to nine steps usually read well.
- Use technology-neutral verbs such as *identifies*, *enters*, *selects*,
  *presents*, and *notifies*.
- Name data at low precision, such as "Contractor customer provides contact
  information", and link to the [Customer](<link>) entity type for its detail.
- When a step uses an external service, name the service as a secondary
  actor: "Rental system has the payment service authorize the deposit."
- When readers need to know what a screen presents to follow the behavior,
  sketch it as the profile's
  [where content goes](../references/profile.md#where-content-goes) assigns,
  and keep the steps technology-neutral.

### Extensions

- Label each condition with the number of the step where it is detected and a
  letter to distinguish conditions at that step: `2a`, `2b`. Use `*a` for a
  condition that can occur at any step. Letters do not imply order.
- Write a condition as something detected, not an action.
- Write handling steps in the same style as the main success scenario, and
  end with where the scenario resumes or how the use case ends.
- Brainstorm conditions before deciding handling.
- When a Requirement states the binding response, state **specified by** at
  the handling step, such as "Rental system rejects the reservation;
  **specified by**
  [Reservations of unavailable equipment are rejected](<link>)."
- A new goal pursued later, such as cancelling a confirmed reservation, is a
  separate use case, [Cancel a reservation](<link>), not an extension.

### Unknown steps

Number the steps that are known, and record where steps are missing under
**Open questions**, such as "Which steps lie between choosing the equipment
and authorizing the deposit?" A condition known before the step that detects
it is labeled `*a` until that step is numbered.
