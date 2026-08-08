---
name: review-docs
description: >
  Review and refresh documentation for type fit (tutorial / how-to / reference /
  explanation), single source of truth, audience clarity, accuracy, and broken
  links. Use when "docs review", "stale docs", "refresh this guide", or
  pre-merge doc hygiene. Not for trimming always-on agent instruction files
  or creating a new guide from scratch. Not for imposing a folder taxonomy on
  the host.
---

# review-docs

Audit existing documentation and propose (or apply) maintenance fixes.

Classify each document by its primary job: a tutorial teaches through a learning
experience, a how-to guide enables a practical goal, reference supports lookup,
and an explanation builds understanding.

## Defaults

- **Dry-run** first; write only after confirm (or user said "apply").
- Scope defaults to paths the user names, or files touched in the current
  change set when that is the request.
- Prefer repo documentation guidelines and validators when present.
- Never invent new product policy while "refreshing" — only fix structure,
  accuracy, links, and ownership.
- Never invent a host folder layout or metadata schema.

## Modes

| Mode | Focus |
| --- | --- |
| **audit** (default) | Findings only |
| **refresh** | Fix stale facts, links, and host freshness fields when used |
| **retype** | Wrong primary job (e.g. how-to buried in explanation) — split or reframe |
| **retire** | Superseded docs → deprecate/point/remove (confirm) |

## Steps

### 1. Intake

Confirm: paths or bundle, mode, dry-run vs apply.

### 2. Load doctrine

Open local documentation guidelines if they exist. Use only review criteria
contained here or supplied by the host.

### 3. Inventory

For each target document:

- Primary type by job fit, not folder path
- Mixing of jobs that should be split or linked
- Accuracy and link health
- Overlap with another document that already owns the topic
- Host indexes/metadata only if the corpus already uses them

### 4. Rubric (per finding)

| Class | Signal | Typical fix |
| --- | --- | --- |
| **Wrong type / mixed job** | Document answers the wrong Diátaxis need, or several at once | Retype, split, or make one job primary |
| **Duplicate SoR** | Second full copy of a procedure or fact set | Cut; link to owner |
| **Stale** | Broken path, retired command, wrong API | Refresh facts; update host freshness signals if any |
| **Weak framing** | No clear purpose or outcome | Add a short purpose / goal statement |
| **Missing host index** | Local corpus uses an index that omits the file | Add index entry (only if host convention exists) |
| **Orphan / retire** | Superseded with no pointer | Deprecate + link owner |

Do **not** report “wrong folder” unless the **repository** declares placement
rules the file violates.

### 5. Propose

Present:

1. Health one-liner
2. Findings table — location · class · why · proposed change · risk
3. Draft patches for refresh/retype modes
4. Out of scope (needs authoring, design, or instruction-file work)

Stop for confirm unless apply was pre-authorized.

### 6. Apply (gated)

On confirm only:

1. Edit the agreed docs (and host indexes when applicable)
2. Run repo doc validators when known
3. Do not delete without explicit confirm

### 7. Report

- Counts by finding class
- Files changed
- Follow-ups (new guide, instruction-file skill, missing owner doc)

## Rules

- Dry-run default; confirm destructive deletes and renames.
- **Link, do not copy** when fixing duplication.
- Do not use this skill to rewrite always-on instruction files end-to-end —
  hand off to an applicable instruction-authoring capability if one is already
  available.
- Portable skill text must not prescribe monorepo paths, command names, or a
  universal docs tree.
