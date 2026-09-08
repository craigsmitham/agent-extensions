# Product engineering update log

## 2026-09-08

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
