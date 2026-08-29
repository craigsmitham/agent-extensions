# Interaction and item design

Design the checklist as part of a task-user-environment system. Scope,
granularity, order, branching, wording, verification, roles, and presentation
interact; improving one in isolation can damage another.

## Architect the interaction

Resolve these elements before polishing items:

1. **Identity and selection:** a recognizable title, applicability conditions,
   version, and cues that distinguish neighboring checklists.
2. **Trigger and finish:** the event that begins use, the state that ends it,
   and what an incomplete or failed checklist means.
3. **Sections and pause points:** task-shaped groups that support orientation
   and interruption recovery.
4. **Order:** dependencies and natural workflow order, with critical early
   items protected where interruption may prevent completion.
5. **Roles and verification:** who prompts, acts, observes, confirms, records,
   stops, or escalates; self-attestation is not independent verification.
6. **Exceptions and recovery:** bounded alternative paths, stopping rules,
   escalation, safe resumption, and handoff to a fuller procedure where needed.
7. **Medium:** paper, mobile, desktop, spoken exchange, embedded interface, or
   assistive technology in the real lighting, noise, distance, and hands-busy
   conditions.

Do not compress a long checklist through smaller type or denser language. Split
at meaningful workflow boundaries or reduce scope. There is no universal item
count that substitutes for representative-user testing.

## Write observable items

Each item should usually contain one action, question, state, or verification.
Test it for:

- **Applicability:** the user can tell when the item applies.
- **Agency:** the responsible role is known when roles differ.
- **Specificity:** the action or observation is concrete enough to perform or
  verify without incompatible interpretations.
- **Evidence:** the required state, value, artifact, or response is visible
  where false completion matters.
- **Threshold:** an acceptance limit is named when the domain source supplies
  one; never invent it.
- **Failure behavior:** a negative result leads to stop, correct, escalate,
  record, or consult a named neighboring artifact.
- **Source:** domain-critical content traces to current supplied authority,
  incident evidence, task analysis, or an explicit coordination need.

Avoid vague items such as “ensure quality,” compound items that hide partial
completion, unexplained abbreviations, and yes/no responses where the actual
value or state is necessary evidence.

## Bound branching

Branch only on a condition users can recognize at the point of work. Make the
selected path and return point visible. If users must diagnose among many
conditions, search a large state space, or interpret several interacting
variables, prefer a decision tree, algorithm, playbook, or expert procedure.
Wrong-aid selection can be worse than having no aid.

## Design for people and context

- Use familiar words, short direct sentences, meaningful headings, whitespace,
  and one instruction per block where practical.
- Do not use color, position, sound, or icons as the sole carrier of meaning.
- Preserve sufficient contrast, readable size, logical navigation, and
  compatibility with the intended device and assistive technology.
- Make criticality visible without making every item visually critical.
- Preserve place and remaining work after interruption.
- Do not assume expertise removes reliance errors; avoid redundant explanation
  that consumes expert attention while retaining necessary verification.
- In team use, design for genuine participation and authority to challenge;
  recorded completion cannot prove that the exchange occurred attentively.

## Stress-test the candidate

Use realistic scenarios and ask:

1. Can a user select this checklist and the correct branch?
2. What happens when one critical item is absent, wrong, or impossible?
3. Can two qualified users interpret an item differently?
4. Does the checklist delay an urgent action or displace a better control?
5. Can it resume correctly after interruption?
6. Can users check every box while the intended outcome remains false?
7. Which incentives, hierarchy, or resource gaps encourage ritual completion?
8. Who is excluded by language, presentation, device, or interaction?
9. What exception exceeds the checklist and where does it go?

These questions expose design risks. Only observed representative use can
establish how often they occur.

## Sources

- NASA, [*Human Factors of Flight-Deck Checklists*](https://www.faa.gov/sites/faa.gov/files/2022-11/NASA%20Ames%20Rpt%20CR%20177549%20.pdf)
- AAPM, [Checklist development, implementation, use, and maintenance guideline](https://aapm.onlinelibrary.wiley.com/doi/10.1002/acm2.13895)
- W3C WAI, [Clear and understandable content](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o3-clear-content/)
- Aveling et al., [Qualitative study of checklist use, resources, and hierarchy](https://pmc.ncbi.nlm.nih.gov/articles/PMC3752057/)
- Marshall et al., [Wrong cognitive-aid selection in simulated emergencies](https://pmc.ncbi.nlm.nih.gov/articles/PMC9277856/)
