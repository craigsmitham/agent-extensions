---
name: setup-architecture-docs
description: Plans or establishes the smallest discoverable architecture-documentation adoption for one or more repository systems by classifying repository state, resolving system-to-corpus mappings, connecting local authority, and verifying contributor discovery. Use when asked to set up, adopt, initialize, plan, or connect architecture docs or Just Enough Architecture Docs. Not for choosing an architecture, authoring substantive architecture meaning, assessing or repairing an established corpus, or maintaining existing architecture docs.
---

# Set up architecture docs

Plan or establish an explicit, discoverable, and maintainable repository-local
adoption of Just Enough Architecture Docs without inventing architecture
meaning or generating a documentation taxonomy.

Setup succeeds when a future contributor or agent can discover which system or
bounded authority each corpus describes, reach its one canonical root, find the
accepted architecture subjects and local authority routes, distinguish gaps and
proposals from accepted meaning, and select the appropriate authoring or
maintenance workflow. Files are evidence of that outcome, not the outcome by
themselves.

This skill is a non-standalone member of the software-architecture pack. From
the active AXM scope root, begin with
`.axm/extensions/@craigsmitham/knowledge/software-architecture/src/guides/organizing-an-architecture-docs-corpus.md`.
Open `architecture-documentation/just-enough-architecture-docs.md` when the
adoption boundary, authority model, or admission test needs explanation.

## Authority and modes

Use this skill only for an explicit request to plan, set up, adopt, initialize,
or connect architecture documentation. A setup or adoption request authorizes
bounded changes to the selected architecture roots and the canonical persistent
repository instructions. A request to assess, plan, preview, or recommend is
read-only. Do not add a review gate when the request, evidence, and safe defaults
already establish the result.

If an established setup needs broken-link repair, freshness review,
reconciliation, cleanup, or pruning, classify it as established maintenance and
leave that work to `maintain-architecture-docs`. Separate any genuinely missing
adoption choice from the maintenance scope. Substantive accepted meaning belongs
to `author-architecture-docs` even when setup exposes its absence.

## Build the adoption brief

Inspect proportionately before choosing a playbook. Read repository
instructions and the existing architecture, product, requirement, decision,
guide, and proposal material. Inspect enough code, tests, schemas,
configuration, deployment boundaries, and workspace structure to identify
plausible systems and the authorities that already own exact facts. Repository
structure and implementation evidence may identify candidates; they do not by
themselves accept a system boundary, desired-state claim, owner, or format.

Build one working adoption brief with these fields:

- each documented system or bounded authority and its canonical corpus root;
- existing accepted architecture subjects, proposals, and evidence routes;
- the canonical persistent repository instruction authority;
- the documentation format or required profile;
- system lifecycle or support-state authority;
- maintenance responsibility and architecture decision-authority routes;
- local deviations and documentation review triggers; and
- requested mode, expected effects, and repository-state playbook.

Classify each field as **established**, **safely defaultable**, **materially
ambiguous**, **missing but non-blocking**, or **missing and blocking**. Keep the
brief as working state unless the user requested a durable assessment. Persist
only the accepted local choices and useful gaps that belong in the repository.

For a substantial run, open with the understood scope, whether the run is
read-only or mutating, the expected adoption surfaces, and the next possible
decision point. Report progress at repository-state and decision boundaries,
not as a transcript of file inspection.

## Select the playbook

Choose from the repository state and requested mode rather than forcing every
repository through one creation sequence.

| Playbook | Use when | Result |
| --- | --- | --- |
| **Bootstrap** | One system boundary is clear and no architecture corpus exists | Create the smallest useful root and instruction route |
| **Connect** | Useful accepted material exists but no coherent setup or canonical root connects it | Establish one canonical root and link the material in place |
| **Federate** | Repository authority already defines more than one system-to-root mapping | Connect each system to exactly one corpus and expose the mappings without inventing a platform corpus |
| **Recommend** | The request is read-only or a material adoption choice remains unresolved | Return the adoption brief, smallest viable setup, effects, and unresolved decisions without mutation |
| **Defer to maintenance** | A coherent setup already exists but is damaged, stale, duplicated, or contradictory | Preserve it and route the bounded maintenance work |

Do not treat scattered files as an established corpus merely because they use
architecture vocabulary. Do not treat several roots as federation unless an
accepted authority maps each root to a distinct documented system.

## Resolve choices proportionately

Preserve an established coherent root, organization, format, and instruction
route. For one system with no stronger convention, `docs/architecture/` and
plain Markdown are safe defaults. The standard event-driven review triggers in
this workflow are also safe defaults. Do not create a repository-specific
format, profile, instruction authority, or multi-system layout merely for
symmetry or automation.

Missing accepted lifecycle terminology, stewardship, or decision authority is
normally non-blocking: record the available stable route or state the semantic
gap for bounded authoring. Do not infer it from usernames, commit history,
directory ownership, a volatile roster, or the newest artifact.

Stop before dependent writes when materially different results remain
plausible, including:

- platform-wide versus per-product or per-system corpora;
- competing canonical roots;
- conflicting persistent instruction authorities; or
- an unresolved required format or application profile.

Present a material decision in this order: the decision and proposed status;
governing evidence, criteria, and constraints; every viable option in parallel
form; material exclusions; one recommendation after the comparison when the
evidence supports it; and a final request to choose, revise, defer, or seek more
evidence. Use stable descriptive option names. The ordinary text presentation
is authoritative; a host affordance may render the same choices only when its
labels map unambiguously. After emitting a decision gate, wait for the answer.

Use these literal section labels and order for the decision presentation:

1. **Decision** and **Status**
2. **Evidence and criteria**
3. **Options**, with the same consequence fields and comparable detail for
   every viable option
4. **Material exclusions**
5. **Recommendation**, or `None — more evidence is required`
6. **Choose**, explicitly permitting selection, revision, deferral, or a
   request for more evidence

Do not label an option as recommended, give it greater emphasis, or otherwise
reveal the recommendation inside **Options**. Complete the neutral comparison
before emitting the single **Recommendation** section.

## Apply the selected playbook

For **Bootstrap**, create only the canonical root `index.md` and the concise
instruction discovery route. Do not create an overview or collection until
accepted content passes the admission test.

For **Connect**, preserve useful existing files and local organization. Link
accepted material from the canonical root without moving, renaming, or
rewriting it merely to match the portable guide. Treat material as accepted
architecture only when repository authority establishes that status; preserve
proposals, delivery records, and observed evidence in their own lifecycles.
Record a deliberate material path, authority, or format deviation instead of
silently normalizing it.

For **Federate**, use only an accepted system-to-root mapping. Give each system
one canonical corpus root and its own minimal adoption surface. Add one concise
repository instruction route that exposes every mapping and the shared method.
Do not create a platform corpus, cross-system desired-state claim, or common
taxonomy unless separately accepted and authorized.

For **Recommend**, make no changes. Return the evidence-status adoption brief,
the smallest viable file effects, safe defaults, non-blocking gaps, and every
decision that must precede mutation. State explicitly that the repository is
unchanged.

For **Defer to maintenance**, do not recreate, duplicate, or substantively
rewrite the established corpus. Report the existing setup and route broken
navigation, stale claims, contradictions, consolidation, or pruning to the
maintenance workflow.

## Write the minimum adoption surface

Create or revise each selected root `index.md` so it:

- names the documented system or bounded authority;
- records adoption of Just Enough Architecture Docs and the canonical local
  root;
- records the accepted format or profile and material local deviations;
- links every existing admitted architecture subject and states what each
  external authority route establishes;
- links accepted lifecycle, stewardship, and decision routes or names their
  non-blocking semantic gaps; and
- requires review when accepted behavior, responsibility, boundary, Product
  Quality Requirement, architecture consequence, or an evidence route changes.

Keep the root navigational; do not place several substantive architecture
entities in it. Do not create `overview.md` or collection directories without
accepted content that passes the admission test. When a first accepted concept
already exists, preserve or recommend its stable canonical named file and add
only the collection navigation it needs. Never create a plural catch-all such
as `use-cases.md` for later splitting. Setup must not generate ISO/IEC 25010
characteristic directories, Product Quality Requirements, a Product Quality
View, or any other apparently complete taxonomy.

Add or update one concise route in the canonical persistent repository
instructions. Map each documented system to its root and route contributors to
the software-architecture pack. Preserve unrelated instructions and update an
existing route in place. Do not copy the shared method, templates, or folder
tree into repository instructions, and do not create competing host-specific
instruction authorities.

## Verify the outcome

Verify the requested mode and contributor capabilities, not only file
existence:

- every documented system maps to exactly one canonical root and every root
  resolves;
- the persistent instruction route lets a contributor discover each mapping
  and the shared method;
- every existing admitted subject is reachable and proposals remain outside
  accepted architecture;
- lifecycle, stewardship, decision authority, and review triggers are either
  discoverable or truthfully identified as semantic gaps;
- no empty taxonomy, speculative overview, copied volatile inventory, inferred
  desired state, or competing setup was created;
- any declared OKF use is consistent with the installed application profile;
  and
- a read-only run made no changes.

Run applicable documentation, link, profile, and repository checks, then
inspect the diff for unrelated edits and silent semantic decisions.

## Handoff

Lead with the achieved or proposed repository state. Then report, in this
order:

1. each documented system, canonical root, format, and instruction route;
2. existing material preserved or connected and the authority it retains;
3. accepted local choices, safe defaults, and unresolved semantic gaps;
4. files or effects changed, including an explicit no-change statement for a
   read-only or blocked run;
5. verification performed and any limitation; and
6. the next bounded authoring, maintenance, migration, or decision workflow.

Describe what is now true and what remains unresolved rather than leading with
a raw file list. Present possible semantic additions, reductions, migrations,
or reorganizations as recommendations unless the user explicitly authorized
that class and scope of change.

End every completed, proposed, or blocked handoff with one explicit
`Next workflow:` line. Name `author-architecture-docs`,
`maintain-architecture-docs`, a required adoption decision, a separately
authorized migration, or `None` with the condition that would make another
workflow necessary.

Do not choose an architecture, create substantive desired-state claims from
implementation inference, configure unrelated tools, or modify source code,
runtime systems, proposals, and external records. Setup is complete only when
the requested adoption state is discoverable, authority-aware, proportionate,
and verified.
