# Product engineering update log

## 2026-09-08

- **Migration**: Moved the nine concepts of the standalone `product-management`
  bundle into this one and retired that bundle. Seven went to
  [What to solve](problem/), [Product strategy](strategy/product-strategy.md)
  to [Where to play](strategy/), and
  [Product meaning and requirements](solution/product-meaning-and-requirements.md)
  to [What to build](solution/). The problem section index replaces its
  planned-scope table with the migrated concepts.
- **Decision**: Retired `product-management` rather than keeping it beside this
  bundle. Its four content areas were the four planned areas of What to solve,
  so keeping both would have left two bundles owning outcomes, risk, and
  discovery, which is the contradiction this corpus is meant to avoid. The
  discipline survives as a topic, not as a section identity; sections are named
  for questions, not for the people who answer them.
- **Decision**: Product strategy sits in Where to play, not What to solve. It
  is the rung of the choice cascade that turns an arena choice into product
  direction, and it reads as strategy work rather than problem selection. The
  section intro now says it owns that translation, and What to solve begins
  where a team picks problems inside the resulting direction.
- **Decision**: Product meaning and requirements moved to What to build,
  because its subject is where product meaning stops and a normative statement
  begins, and this bundle gives the requirement to the section that owns the
  commitment to form. What to solve links to it rather than holding it.
- **Structure**: Flattened the `value-and-demand/` subfolder into
  [What to solve](problem/). A sub-index competing with the section index
  splits discovery for no gain at this size; the subfolder's framing paragraph
  became the section's Value and demand heading.
- **Rename**: "Product management overview" became
  [Product decisions and accountability](problem/overview.md). Its list of how
  product work connects was a second telling of the seven questions, so it now
  describes the loop this section holds and names the neighbors that own the
  rest.
- **Attribution**: Rewrote the source entries that pointed at
  `product-management` paths or at this bundle by URL, so in-bundle references
  are relative, and normalized the "Strategy — ..." reference titles left from
  the strategy migration to "Where to play — ...".
- **Boundary**: Discovery and delivery stays in What to solve as the pair of
  work a product team joins. The mechanics of release belong to How to ship it
  and production health to How to run it; the problem section index says so.
- **Restructure**: Split the problem and solution questions apart and gave
  design a home. `product/` became `problem/` ("What to solve") and
  `requirements/` became `solution/` ("What to build"). No concepts moved;
  both sections were still scope-only.
- **Decision**: "What it must do" was retired as a section identity. Naming a
  section for the requirement made it artifact-shaped, which this bundle's own
  organizing argument rejects, and its question was unanswerable on its own
  terms: what a product must do cannot be stated without having chosen a
  solution concept. The requirement survives as a concept the section owns —
  the form a design choice takes once it must be disputed, traced, and
  verified.
- **Decision**: Design is defined once, in [What to build](solution/), as
  choosing the form a solution will take at a deliberate resolution from
  alternatives genuinely considered, plus the record of that choice. The test
  "a statement becomes design the moment it constrains form" is what separates
  What to solve from What to build.
- **Decision**: Design is not a section. It recurs at four altitudes —
  solution concept, interaction, technical, operational — and sections own
  altitudes rather than the word. This is the facets-not-folders rule applied
  to an activity. It also resolves a collision: "Design and architecture" under
  How to build it was renamed "Architecture and technical design" so the word
  no longer names two different things in two sections.
- **Decision**: An eight-section scheme giving design its own question was
  considered and set aside. It manufactures a design-then-requirements handoff
  that the sources deny, and forces an arbitrary ruling on concepts that are
  genuinely both, such as appetite and breadboarding. The seam is documented in
  What to build if section size later forces the split.
- **Naming**: "What to build" moved from the problem section to the solution
  section because that is what the phrase means in practice, and the problem
  section became "What to solve". All seven titles now share one grammatical
  form. Judgment lives in the question, not the title, following the precedent
  already set by "Where to play".
- **Basis**: Ryan Singer on shaping as primarily design work, on requirements
  as chosen rather than real, and on appetite as a design input; Bill Buxton on
  getting the right design before getting the design right, on sketches asking
  rather than telling, and on design preceding engineering; Nielsen Norman
  Group on the problem-space boundary of discovery, and on process frameworks
  as scaffolding for managing risk rather than as stages.
- **Boundary**: Usability stays in What to solve as a risk that evidence
  retires; the craft of designing for it belongs to What to build. Both section
  indexes say so, and both state that the What to build / How to build it pair
  is a division of questions, not a handoff.
- **Deferred**: No content migrated. `product-management` and
  `requirements-engineering` still supply their sections; the solution concept,
  fidelity, and interaction design areas of What to build have no source bundle
  and will be written from scratch.
- **Initialization**: Created the bundle skeleton as seven sections, one per
  practitioner question, with a root discovery map and a section index for
  each. No concepts yet; existing bundles migrate in later changes.
- **Decision**: Documentation craft stays in the separate `docs` bundle rather
  than becoming a section here. Expressing knowledge for a reader is its own
  discipline, and it applies well beyond product engineering.
- **Decision**: `knowledge-management` and `field-notes` are not recorded as
  migration sources for [How to learn](learning/). The section scope stands as
  intent; sourcing is deferred until those bundles have a clearer purpose.
- **Migration**: Moved the eight concepts of the standalone `strategy` bundle
  into [Where to play](strategy/) and retired that bundle. The section index
  replaces its planned-scope table with the migrated concepts, and every
  bundle-root link now resolves under `/strategy/`.
- **Decision**: Widened the section's first area from "Participation and
  advantage" to "Participation, advantage, and value" so
  [Value creation and capture](strategy/value-creation-and-capture.md) has a
  home. Value capture is part of how an arena is won, not a separate question.
- **Attribution**: Repointed the two `product-management` source entries that
  cited the retired bundle at their new location, and corrected the footnote
  text that named the Strategy bundle as owner.

### Migrated history from the `strategy` bundle

- **2026-09-08 — Attribution**: Resolved every declared-but-uncited source by
  footnoting the specific claims each one supports in Strategy overview, The
  choice cascade, Advantage and coherence, Value creation and capture, and
  Strategy as hypothesis.
- **2026-09-08 — Discovery**: Rewrote the description of Developing and
  reviewing Wardley maps to pair its supported outcome with the situation that
  selects it, and matched the index entry.
- **2026-09-08 — Navigation**: Added related-concept links so a reader arriving
  by search can reach neighboring concepts without returning to the index.
- **2026-08-29 — Ownership**: Re-established Wardley Mapping as portable
  strategy guidance, separating situational awareness from strategic choice.
- **2026-08-21 — Migration**: Removed Wardley mapping after its canonical
  ownership moved to the architecture collection.
- **2026-08-20 — Strategic mapping**: Added a Wardley mapping draft connecting
  user need, value-chain visibility, evolution, movement, inertia, action, and
  explicit review of strategic hypotheses.

### Migrated history from the `product-management` bundle

- **2026-09-08 — Discovery**: The bundle root routed to the Value and demand
  section instead of flattening its four concepts alongside it, and stated the
  bundle's boundaries. That section index said what it owned and what the rest
  of the bundle covered.
- **2026-09-08 — Attribution**: Cited the previously declared but unreferenced
  SVPG sources in the product management overview, Outcomes and evidence,
  Discovery and delivery, Product risks, and Empowered product teams.
- **2026-09-08 — Navigation**: In-bundle footnote references gained linked
  titles, and Jobs to Be Done and Value and demand model linked to their
  neighbors so a concept reached by search could reach the rest.
- **2026-08-29 — Value and demand model**: Added portable Offering, Audience,
  Need, Job to Be Done, and Value Proposition concepts, with authoring guidance
  and a boundary between product meaning, behavioral views, requirements,
  realization, and evidence. Tracker form, stage eligibility, controlled
  cross-artifact relationships, and architecture-specific classification stayed
  outside the bundle.
