# The job this skill serves

The work this skill supports is one job: **grow and maintain a software
system's specification**. Read this page when the profile and Type contracts
do not decide what to do, such as when a request fits no type, concerns
something the profile has not yet defined, or leaves a choice of what to do
first.

The [profile](profile.md) and Type contracts govern. This page guides only
where they are silent or leave a choice, and never justifies departing from a
rule. Content about a concern the profile does not define still follows
[P-CON-5](profile.md#concerns-not-yet-defined); this page helps choose how.

## The job

A [specification](profile.md#vocabulary) is the agreed account of what a
software system does, whom and what it serves, and why. The job is the same
whatever holds it: documents, tickets, tests, or people's memory. A corpus is
the form this profile gives it.

The job serves a broader one, growing and maintaining the software system
itself. The specification is what tells everyone doing that work what the
system must do and for whom, which is what makes each requirement meaningful.

### Job performer

The steward of the specification: whoever is accountable for what the system
does and whom it serves, such as a tech lead, a product-minded engineer, a
product owner, or a solo builder. The person using this skill is usually the
steward or acts for one. An agent performs steps on the steward's behalf;
decisions about what the system does and whom it serves remain the steward's,
or belong to whoever the steward names.

The people and systems that the software serves are not this job's performers.
Their jobs are content of the specification.

### Circumstances

- The system is grown or maintained at every stage of its life, from strategy
  and discovery through delivery, operations, and maintenance.
- A pass begins with growth, such as new capability or new people or systems
  served, or with maintenance, such as a fix, an adaptation, discovered drift,
  or a retired capability.
- Much work on the system is design, dependency, performance, or operations
  work, and some of it changes, or risks changing, what the system does or
  whom it serves.
- Agents make much of the change and start each session without memory of
  earlier decisions.
- What was decided is scattered across conversations, tickets, pull requests,
  code, and people's heads, and gaps are easily filled with plausible
  invention.
- Several people and agents change the system and use terms differently.
- Formal requirements management is heavier than most stewards can sustain.

### Progress sought

- **Functional:** anyone changing the system, at any stage, can find what it
  must do, whom and what each part serves, and why; can tell what is decided
  from what is open; and can rely on that account staying true as the system
  changes.
- **Emotional:** confidence that a change, whether the steward's or an
  agent's, keeps faith with whom and what the system serves, without
  re-explaining the system in every session.
- **Social:** the system can be handed to others, and a decision can be
  explained to stakeholders by pointing to what was agreed.

## Layers

The specification states what the system does and whom and what it serves.
How the system does it, including architecture, implementation, dependencies,
performance tuning, and operations, belongs to records, as
[P-CON-7 and P-CON-8](profile.md#work-management-and-design) state.

Work on how the system does something still draws on the specification: it must
not break what the specification binds, and it can show that the
specification is wrong or silent. Moving the rental system to a new hosting
provider is design and operations work, yet
[Search responds within limit at peak load](example.md#quality) and
Reservations are available still bind it.

## Job map

A pass runs from an event that might change what the system does or whom it
serves to the point at which the specification can be relied on again. A
request can enter at any step, and not every pass needs every step. The
outcomes say what doing a step well means.

| Step | What must be accomplished | Outcomes |
| --- | --- | --- |
| Define | Determine whether a change affects what the system does or whom it serves, why, and whose decision governs it | Minimize the likelihood that a change to how the system works that affects those it serves goes unrecognized · Minimize the likelihood of acting on a change that nobody with authority decided |
| Locate | Find what the specification already says about the affected area, and the sources of what it should say: people, research, business rules, counterpart systems, and current behavior | Minimize the likelihood of missing an existing commitment that the change touches · Minimize the time to recover what an unspecified part of the system does |
| Prepare | Sort each piece of content by kind and home, and agree on terms | Minimize the likelihood of the same content being stated in two places · Minimize the likelihood of one term carrying two meanings |
| Confirm | Establish that the content is ready to rely on: conflicts settled or visible, the right people in agreement, and unknowns recorded rather than filled | Minimize the likelihood of invented detail passing as agreed · Minimize the time to see what is still undecided |
| Execute | State the change so that it is unambiguous, verifiable, and connected to whom and what it serves | Minimize the likelihood that two readers disagree on what is required · Minimize the likelihood of an obligation recorded without whom it serves |
| Monitor | Check that the specification still holds: consistent with itself, matched by the system's behavior, and still what those it serves need | Minimize the time between drift and its discovery · Minimize the likelihood that a later change contradicts an earlier decision unnoticed |
| Modify | Resolve a divergence by revising the specification or by identifying the behavior as a defect | Minimize the likelihood of revising the specification to match a defect · Minimize the effort to find everything that a revision affects |
| Conclude | Retire superseded content, leave open questions visible, and make the current specification findable for the next person or session | Minimize the likelihood that stale content remains discoverable · Minimize the time for a new session to recover the current state |

## Using the job where the rules are silent

- **Place the request on the map.** A request to change code, dependencies,
  or operations usually calls for Define, Locate, and Monitor against the
  specification rather than new documents. A request to write a document is
  Execute, and it is sound only when Define and Confirm are.
- **Serve the step's outcomes.** Among the choices the rules allow, prefer the
  one that serves the outcomes of the step at hand.
- **Let the guarding outcomes win.** When completeness or speed competes with
  not inventing detail or with who decides, record the gap under **Open
  questions**, as [P-CON-4](profile.md#record-gaps-instead-of-inventing)
  requires, and ask the steward.
- **Do not settle a divergence alone.** When behavior and the specification
  disagree, neither is presumed right. If reservations were held for 60
  minutes while the specification states a 30-minute
  [hold period](example.md#reservations-and-notices), ask whether the
  behavior is a defect or the hold period has changed.
- **Say when a step has no practice.** Where the skill gives no practice for a
  step, such as document status for Confirm or impact analysis for Modify,
  tell the steward what the step needs rather than inventing a convention in
  the corpus.
