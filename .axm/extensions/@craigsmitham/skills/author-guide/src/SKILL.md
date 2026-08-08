---
name: author-guide
description: >
  Create or revise a how-to guide (or another Diátaxis documentation type when
  asked) using portable docs craft. Use when writing a new guide, restructuring
  an existing how-to, or "author a guide". Not for always-on instruction files
  (use improve-instructions). Not for inventing repo folder layout or metadata
  schemas.
---

# author-guide

Author documentation with a clear **primary job**, defaulting to a **how-to
guide**.

Shared definitions — open `@craigsmitham/knowledge/docs` before acting:

- `docs-explainer` and `docs-guide` (always)
- Matching type **explainer** + **guide**, defaulting to how-to:
  - `how-to-explainer` + `how-to-guide`
  - or `tutorial-explainer` + `tutorial-guide`
  - or `reference-explainer` + `reference-guide`
  - or `explanation-explainer` + `explanation-guide`

Companion: `review-docs` audits existing docs. Instruction-file trim is
**`improve-instructions`** (harness-engineering), not this skill.

## Defaults

- **Dry-run** first: propose type, path, and outline; write only after confirm
  (or the user said "apply" / "create the guide").
- Prefer the **repository’s** documentation guidelines when they exist;
  portable knowledge is the quality bar, local profile wins on paths, fields,
  and checks.
- Do **not** invent product or architecture policy — only structure what the
  user and existing sources support.
- Do **not** invent a folder taxonomy or frontmatter schema for the host.

## Non-goals

- Editing `AGENTS.md` / `CLAUDE.md` always-on bodies (route to
  `improve-instructions`)
- Capturing backlog issues (`capture-issue` / `refine-issue`)
- Authoring product marketing sites unless framed as one of the four docs types
- Migrating an entire docs tree into a knowledge extension
- Prescribing OKF or other host formats (use local rules / `okf-author` when
  the corpus is OKF)

## Steps

### 1. Intake

Confirm: topic, intended type (default how-to), target path if known, new vs
revise, dry-run vs apply. If type is unclear, walk `docs-explainer` with the
user.

### 2. Load doctrine

Read `docs-explainer`, `docs-guide`, the matching type explainer, and the
matching type guide. Then open any repo-local documentation guidelines if
present.

### 3. Bound the job

Follow `docs-guide`: name the reader need, pick one type, state purpose or
goal, list non-goals, link owners of adjacent jobs.

### 4. Structure

Follow the matching type **guide** (steps, preconditions, pitfalls). Use the
type **explainer** for quality signals and belongs/does-not-belong checks.

Apply **local** metadata and index conventions only when the host already uses
them.

### 5. Propose (dry-run)

Present:

1. Type and path
2. Outline
3. Host-specific updates needed (indexes, registries) if the repo uses them
4. Open questions

Stop for confirm unless apply was pre-authorized.

### 6. Apply (gated)

On confirm only:

1. Write or update the document
2. Update host indexes only when the local corpus already maintains them
3. Run the **repo’s** documentation validators if known; otherwise note that
   the user should run their usual checks
4. Do not hand-edit generated AXM-managed regions unless the user requires it

### 7. Report

- Path created/updated
- Type and concepts applied
- Follow-ups (other type needed, review-docs pass, instruction-file work)

## Rules

- Dry-run default; confirm writes and deletes.
- Link to existing owners; do not copy full procedures from other docs.
- Keep one primary documentation job per file.
- If the task is really instruction-file bloat, stop and recommend
  `improve-instructions`.
