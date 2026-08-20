# Research-question frame contract

Use this contract to select concerns, preserve blindness, and shape the final
research frame.

## Independent framing

A blind check is a property of the context, not merely neutral wording. When
the input contains an originating analysis:

1. Create a hypothesis-neutral brief containing only:
   - the neutral subject or system boundary;
   - directly observable conditions, events, needs, or outcomes;
   - relevant population, environment, and timeframe;
   - the decision or understanding the research must support;
   - authoritative constraints; and
   - neutral terminology needed to locate evidence.
2. Exclude suspected or established causes, causal narratives, findings,
   diagnoses, conclusions, confidence levels, recommendations, proposed fixes,
   favored alternatives, and details selected because they support a
   hypothesis. Do not single out an actor, component, or mechanism unless it is
   indispensable to the neutral boundary.
3. When the host supports an isolated context, pass only the neutral brief and
   this contract into it for question generation. Do not pass the originating
   material, exclusions, or a summary of what was removed. Relay the isolated
   result without adding substantive content or reordering it according to the
   originating analysis.
4. When isolation is unavailable, return the neutral brief and state that a
   fresh context is required. If the caller explicitly accepts same-context
   generation, label the result `hypothesis-neutral, not procedurally blind`.

Before release, ask whether a competent researcher could infer an originating
hypothesis from a question's wording, specificity, ordering, or emphasis.
Rewrite or remove any question that could reveal it.

Prefer symmetric causal questions. For example:

- Revealing: `Did connection-pool exhaustion cause the latency change?`
- Neutral: `What conditions coincided with the latency change, and what
  evidence distinguishes among application, dependency, resource, workload,
  and environmental explanations?`

## Select concerns

First characterize what kind of subject is present: a claim, opportunity,
problem, proposal, decision, product, system, process, event, policy, design,
or another kind. Determine whether the investigation primarily asks what is
true, valuable, desirable, possible, necessary, effective, preferable, or
risky.

Derive concerns from that characterization. Possible lenses include:

- purpose, needs, value, and desired outcomes;
- concepts, definitions, assumptions, and explanatory models;
- stakeholders, perspectives, incentives, and distribution of effects;
- functional behavior, capability, quality, and experience;
- structure, dependencies, interfaces, and constraints;
- feasibility, economics, operations, and lifecycle;
- safety, security, privacy, legality, ethics, and misuse;
- alternatives, tradeoffs, opportunity costs, timing, and reversibility;
- evidence quality, uncertainty, and decision criteria; and
- unintended consequences and failure modes.

These are selection prompts, not a mandatory checklist. Retain only concerns
whose answers could materially improve the intended decision or understanding.

## Form and prioritize questions

Prefer questions that:

- test a central value, truth, outcome, or explanatory proposition;
- expose an assumption capable of changing the frame;
- distinguish among plausible explanations or alternatives;
- reveal consequential constraints, dependencies, tradeoffs, or effects;
- surface a materially affected but neglected perspective; or
- establish what evidence would justify a conclusion.

Do not require every category. Reject questions that are generic, overlapping,
loaded, unanswerable with plausible evidence, or included only for exhaustive
coverage. Avoid numerical risk scores unless the caller supplies an anchored
scale.

## Research Brief contract

Default to fewer than 700 words and return these sections in order:

# Research Brief

## Research context

State in compact bullets:

- **Intended decision or use:** the decision, understanding, or action the
  research should support.
- **Subject and boundary:** what is in and out of scope.
- **Observable context:** neutral facts needed to understand the questions.
- **Constraints:** timeframe, jurisdiction, source, effort, or other
  authoritative limits; use `None supplied` when absent.
- **Consequential assumptions:** assumptions that could change the priorities,
  or `None identified`.
- **Independence status:** `ordinary`, `procedurally blind`, or
  `hypothesis-neutral, not procedurally blind`.

## Relevant concerns

Name the three through six selected concerns and give one sentence explaining
the material relevance of each.

## Priority research questions

Return five through eight rows unless the caller requests another limit:

| ID | Priority | Research question | Concern | Why the answer matters | Evidence needed |
| --- | --- | --- | --- | --- | --- |

Assign stable IDs `Q1`, `Q2`, and so on in priority order. The `Evidence needed`
field should identify the kind of observation, comparison, source, measurement,
or disconfirming evidence that could answer the question; it must not answer the
question.

## Deliberate omissions

Name up to three plausible concerns excluded as low relevance and give a short
reason. In blind mode, never refer to removed originating material.

When blind isolation cannot be completed, return only:

# Blind research brief

## Subject and boundary
## Observable context
## Intended decision or use
## Authoritative constraints
## Next step

The next step requests question generation in a fresh context and must not list
what was removed.
