---
type: Explainer
title: Pattern explainer
description: How pattern descriptions communicate recurring solutions in context — their evidence, forces, adaptation, generative potential, and relationships within collections and languages.
tags: [docs, pattern, pattern-description, pattern-library, pattern-language, generativity, umwelt, design, explainer]
status: stable
sources:
  - id: hillside-patterns
    resource: https://hillside.net/patterns
    title: Hillside Group — Design Patterns Library
  - id: patterns-faq
    resource: https://gee.cs.oswego.edu/dl/pd-FAQ/pd-FAQ.html
    title: Patterns-discussion FAQ
  - id: pattern-writing-language
    resource: https://www.hillside.net/index.php/a-pattern-language-for-pattern-writing
    title: Meszaros and Doble — A Pattern Language for Pattern Writing
  - id: fowler-writing-patterns
    resource: https://martinfowler.com/articles/writingPatterns.html
    title: Martin Fowler — Writing Software Patterns
  - id: azure-cloud-patterns
    resource: https://learn.microsoft.com/en-us/azure/architecture/patterns/
    title: Microsoft Azure Architecture Center — Cloud design patterns
  - id: govuk-pattern
    resource: https://design-system.service.gov.uk/patterns/check-a-service-is-suitable/
    title: GOV.UK Design System — Check a service is suitable
  - id: va-maturity
    resource: https://design.va.gov/about/maturity-scale
    title: VA Design System — Maturity scale
  - id: elephants-patterns
    resource: https://wirfs-brock.com/rebecca/papers/ElephantsPatternsAndHeuristics/
    title: Wirfs-Brock and Kohls — Elephants, Patterns, and Heuristics
  - id: generative-patterns
    resource: https://wirfs-brock.com/rebecca/papers/explrgenpat2023/
    title: Hvatum and Wirfs-Brock — Exploring the Generative Nature of Patterns
  - id: patterns-umwelt
    resource: https://wirfs-brock.com/rebecca/papers/patternsumwelt/
    title: Wirfs-Brock and Kohls — Patterns and their Umwelt
  - id: pattern-smells
    resource: https://wirfs-brock.com/rebecca/papers/patternsmells/
    title: Wirfs-Brock and Kohls — Pattern Smells, Get Rid of Them (2026 preprint)
generated: { by: "codex/gpt-6", at: 2026-10-30T20:12:16Z }
---

# Pattern explainer

A design **pattern** is a recurring problem–solution relationship in context.
A **pattern description** names and communicates that relationship: its
essential structure, forces, consequences, and supporting evidence. A
particular implementation is an **instance**. Neither an instance nor its
written description exhausts the pattern.[^elephants-patterns]

The name makes experience discussable. *Circuit Breaker*, *Strangler Fig*, or
*One Thing per Page* can stand for a larger body of judgment once a community
shares the meaning. The entry preserves that meaning: not only what experienced
practitioners tend to do, but when, why, with what tradeoffs, and on what
evidence.

A pattern description is a reusable guidance form, distinct from an explainer,
guide, or principle. Its structured fields serve lookup during work, while its
forces, rationale, and consequences supply the understanding needed to adapt the
solution safely. It can explain both the arrangement and the process of
creating it; a full environment-specific procedure belongs in a linked how-to.
Here, *pattern entry* means the description, and the evidence requirements
below govern the strength of its claims.

To write one, use [Pattern guide](../guides/pattern.md).

## Relationship to reader-need forms

| Part of a pattern | Diátaxis job |
| --- | --- |
| Name, intent, context, problem, applicability | Reference — recognize and compare the entry while working |
| Forces, rationale, consequences | Explanation — understand why the solution fits and what it costs |
| Solution core | Constructive guidance — the reusable arrangement and how it can be created |
| Implementation steps | How-to guide — link rather than absorbing environment-specific instructions |
| Worked introduction for a newcomer | Tutorial — teach separately when first-use learning is a real need |

No single reader-need guide covers the pattern form's distinctive work: mining recurrence,
separating an invariant from its instances, recording evidence, and relating
patterns into a larger collection. That is why pattern authoring has its own
guide.

## Orientation

| | |
| --- | --- |
| **Reader need** | Select and adapt an established response to a recurring problem |
| **Success** | The reader recognizes fit, understands the tradeoffs, and can produce a locally appropriate realization |
| **Voice** | Conditional and constructive: *in this context, when these forces recur, arrange the solution this way* |
| **Typical prompt** | *We keep encountering X — what established approach fits, and what will it cost?* |
| **Title cue** | A short, memorable name for the solution rather than the tool or one project |

## What makes it a pattern

A useful description of an established pattern makes these properties clear:

- **Recurring** — it abstracts over multiple occurrences rather than
  presenting one invention or anecdote.
- **Contextual** — it states the conditions under which the problem and
  solution are relevant.
- **Force-resolving** — it exposes competing goals and constraints instead of
  declaring an unexplained best practice.
- **Constructive** — it tells readers enough to construct a new realization,
  while leaving incidental form open to local conditions.
- **Named** — its concise, evocative name becomes shared vocabulary.
- **Evidence-backed** — known uses, research, review, or other observations
  support the claim that it recurs and helps.
- **Connected** — it identifies alternatives, complements, predecessors, and
  consequences rather than pretending to work alone.

The shortest useful definition — *a solution to a problem in a context* — is a
starting point, not a sufficient entry. Without forces, evidence, and
consequences it is easy to package ordinary advice as something more proven
and transferable than it is.

## Adaptation and generative potential

Pattern descriptions convey design heuristics: useful, fallible guidance.
Applying them requires judgment, including knowledge the description leaves
implicit. Experts may supply that knowledge readily; newcomers may need
contrasting examples to recognize the same pattern across different
implementations.[^elephants-patterns]

Hvatum and Wirfs-Brock distinguish degrees of **generativity**. A pattern can
solve an immediate problem well without having much wider effect. More
generative patterns can reshape the problem situation and enable benefits
beyond the immediate solution, often through combinations of patterns. Their
quality depends on what people create and experience, not just the elegance
of the description.[^generative-patterns] This bundle therefore expects
constructive guidance without making strong generativity a universal entry
requirement.

**Umwelt** names the situated perceptions and experience through which someone
recognizes what matters. Authors, designers applying patterns, and people
living with the resulting solutions may see different needs. A description
must bridge those perspectives. Application involves **unfolding**: making
successive design choices, observing their fit, and adapting. Leave room for
those choices while explaining the essential structure.[^patterns-umwelt]

## Canonical anatomy

Pattern traditions use different forms. Their stable semantic core matters
more than reproducing one template exactly.

| Element | Question it answers |
| --- | --- |
| **Name and intent** | What reusable idea does this name stand for? |
| **Context** | In what circumstances does the problem arise? |
| **Problem** | What recurring tension needs resolution? |
| **Forces** | Which goals, constraints, and pressures conflict? |
| **Solution** | What essential arrangement resolves those forces, and how can it be created? |
| **Consequences / resulting context** | What improves, worsens, or becomes necessary next? |
| **Applicability** | When should or should not the reader use it? |
| **Evidence / known uses** | Where has it recurred, and why should the reader trust the claim? |
| **Related patterns** | Which alternatives, complements, predecessors, follow-ons, or variants matter? |

The first five form the minimum conceptual spine. Evidence is what separates
an established pattern from a promising candidate. Consequences,
applicability, and relationships make the pattern safe and useful in a
library. Examples, diagrams, aliases, variants, implementation notes, and
sources are optional when they materially improve recognition or application.

Keep the **problem** and **solution** easy to scan. A reader browsing a library
should be able to use the name, intent, problem, and solution as a thumbnail,
then read context and forces to test fit, and only then enter the deeper
rationale, evidence, and examples.

## Pattern vs neighboring artifacts

| Artifact | Difference from a pattern |
| --- | --- |
| **Principle** | [Action-directing articulation of a recognized good](principle.md); guides judgment without binding one recurring problem to a constructive solution |
| **Practice** | [Socially sustained structure of meaningful participation](practice.md) within which patterns may be discovered and enacted; it is not itself a recurring problem-solution claim |
| **Standard** | [Recognized basis for judgment or coordination](standard.md); may constrain or assess realizations but does not supply the pattern's recurring problem-solution relation |
| **How-to guide** | Steps toward one concrete outcome in a particular situation; realizes a pattern when appropriate |
| **Template** | A form to fill in; fixes document or artifact structure without necessarily resolving contextual forces |
| **Example / reference architecture** | One realization; may provide evidence but is not itself the invariant |
| **Component / library** | Reusable implementation rather than reusable design knowledge |
| **Decision record** | Preserves one decision in one context; several records may provide evidence for a pattern |
| **New idea** | A proposed solution without demonstrated recurrence; honestly call it a candidate or proto-pattern |

A **best practice** commonly sounds universal. A pattern is more honest: the
advice is conditional, alternatives remain possible, and the liabilities are
part of the entry. A pattern can record a widely accepted practice, but the
label does not turn preference into evidence.

An **antipattern** records a recurring, initially plausible response that
produces harmful consequences, normally so readers can recognize it and move
toward a better solution. Mere dislike, one failure, or a list of mistakes is
not enough to establish an antipattern.

A principle may guide selection among several patterns, while a pattern may
embody and balance several principles. The principle is normatively focal: it
starts from a good and a direction for judgment. The pattern is situationally
focal: it starts from a recurring contextual problem and offers an established
arrangement. Both still require sound judgment by a practitioner.

## Pattern vs how-to guide (the hard boundary)

Both can influence action. Their unit and promise differ:

| | Pattern | How-to guide |
| --- | --- | --- |
| Unit | Recurring problem/solution relation | One real-world goal |
| Reader decision | Whether and how to adapt the solution | Which actions complete the task |
| Specificity | Stable invariant with local variation | Concrete directions in the reader's situation |
| Sequence | May describe a recurring process for creating or evolving the arrangement | Ordered enough to execute |
| Rationale | Forces and tradeoffs are central | Only what supports successful action now |
| Evidence | Known uses support the pattern claim | Verification shows this procedure works |

If a draft becomes a sequence of commands for one platform, move that material
to a how-to and link it as an implementation. If the advice cannot identify a
stable solution beyond one procedure, it may be a good how-to but not a
pattern.

## Collection, catalog, library, and language

This bundle uses the following working distinctions. *Catalog* and *library*
are organizational conventions here, not universal maturity grades:

- A **collection** is any group of patterns.
- A **catalog** makes them consistently browsable and comparable, commonly by
  problem, intent, domain, or force.
- A **library** is a maintained catalog with evidence, lifecycle, ownership,
  contribution, and retirement practices.
- A **pattern language** connects patterns through meaningful relationships
  and sequences so readers can generate coherent larger solutions within a
  declared domain. It is a kind of collection, not a compulsory destination
  for every catalog.

A folder of pattern pages is not yet a language. The language claim becomes
useful only when the collection guides movement: a larger pattern establishes
context, one pattern creates a resulting problem, another completes it, and
alternatives or specializations are distinguishable.

Useful relationship labels include:

- **precedes / follows** — one pattern establishes the context or resulting
  problem for another;
- **alternative to** — different force balances solve substantially the same
  problem;
- **complements** — orthogonal patterns work together;
- **specializes / generalizes** — the same core appears at narrower or broader
  scope; and
- **conflicts with** — applying both would create an incompatible structure or
  force balance.

## Evidence and maturity

Patterns are mined from experience, not made true by being written in pattern
form. The patterns community's **rule of three** — look for three independent
uses — is a practical heuristic for recurrence, not a substitute for judgment.
Two unusually diverse and well-understood cases may teach more than three
copies descended from one source.

Distinguish lifecycle honestly:

| State | Meaning |
| --- | --- |
| **Candidate / proto-pattern** | The relation is plausible and worth testing, but recurrence or effectiveness is not yet well supported |
| **Established** | Independent known uses and review support the context, forces, and solution claim |
| **Deprecated** | Evidence, changed conditions, or a better replacement makes new use inadvisable |

Those are concepts, not a required metadata vocabulary. A host may use
*proposed*, *available*, *deployed*, *best practice*, or other labels. What
matters is that readers can see the confidence level and that deprecated
entries direct them to a replacement instead of silently disappearing.

Keep **known uses** distinct from illustrative examples. A synthetic example
can teach the shape safely; it cannot establish that the pattern recurs in the
world. Record provenance precisely enough that a reviewer can assess whether
apparently independent uses truly are independent.

## Quality signals

- The name evokes the solution and works naturally in design conversation.
- A reader can recognize the problem without already agreeing with the
  solution.
- Forces explain why the problem is difficult and why alternatives remain
  plausible.
- The solution is specific enough to construct but not coupled to one tool or
  example.
- Consequences include liabilities and newly created problems, not only
  benefits.
- “When not to use” permits a quick, confident rejection.
- Evidence supports the claimed maturity, and uncertainty is visible.
- Related-pattern links state the relationship rather than offering an
  undifferentiated *See also* list.
- The entry is skimmable as a catalog item and coherent when read deeply.

## Failure modes (common)

Wirfs-Brock and Kohls call warning signs in patterns and their descriptions
**pattern smells**. They invite investigation; they are not automatic defects
or a validated scoring system. The following is this bundle's working list,
not a reproduction of their taxonomy.[^pattern-smells]

- **Template theatre** — all expected headings are present, but the relation
  among context, forces, and solution is weak.
- **Solution looking for a problem** — a favored technology appears first and
  the problem is reverse-engineered to justify it.
- **One-example generalization** — a local design is promoted before recurrence
  is known.
- **Universal best practice** — applicability and contraindications disappear,
  so conditional advice becomes dogma.
- **Example as rule** — incidental details of one realization are mistaken for
  the invariant.
- **Implementation swamp** — commands and platform mechanics bury the reusable
  idea.
- **Benefit-only consequences** — the entry sells a solution instead of
  helping a reader choose.
- **Decorative relations** — links name nearby pages without saying whether
  they are alternatives, prerequisites, or follow-ons.
- **Maturity inflation** — a candidate is called proven because the author
  believes in it.
- **Flat forces** — pressures are listed without explaining their relative
  importance or interactions.[^pattern-smells]
- **Fantasy assumptions** — the solution silently depends on resources or
  human behavior its users cannot reasonably expect.[^pattern-smells]
- **Dead library** — patterns have no owner, evidence refresh, deprecation, or
  replacement path.

## Related

- [Pattern guide](../guides/pattern.md)
- [Practice](practice.md)
- [Standard](standard.md)
- [Principle explainer](principle.md) · [Principle guide](../guides/principle.md)
- [Documentation craft](documentation-craft.md)
- [Reference explainer](reference.md) · [Reference guide](../guides/reference.md)
- [Explanation explainer](explanation.md) · [Explanation guide](../guides/explanation.md)
- [How-to explainer](how-to.md) · [How-to guide](../guides/how-to.md)

[^elephants-patterns]: Wirfs-Brock and Kohls, [Elephants, Patterns, and Heuristics](https://wirfs-brock.com/rebecca/papers/ElephantsPatternsAndHeuristics/).
[^generative-patterns]: Hvatum and Wirfs-Brock, [Exploring the Generative Nature of Patterns](https://wirfs-brock.com/rebecca/papers/explrgenpat2023/).
[^patterns-umwelt]: Wirfs-Brock and Kohls, [Patterns and their Umwelt](https://wirfs-brock.com/rebecca/papers/patternsumwelt/).
[^pattern-smells]: Wirfs-Brock and Kohls, [Pattern Smells, Get Rid of Them](https://wirfs-brock.com/rebecca/papers/patternsmells/), 2026 preprint; the authors identify evaluation of the smells and remedies as future work.
