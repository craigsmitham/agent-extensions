---
name: author-docs
description: >
  Creates, revises, classifies, reviews, and maintains repository
  documentation using portable Diátaxis-oriented craft. Use for READMEs,
  tutorials, how-to guides, reference material, explanations, documentation
  reviews, stale docs, broken links, or documentation restructuring. Not for
  always-on agent instruction files, Word/Google Docs artifacts, or inventing
  repository information architecture or metadata schemas.
---

# Author docs

Serve the reader's actual documentation need. Shared doctrine lives in
`@craigsmitham/knowledge/docs`; this skill routes to it and applies it.

## Route the request

1. Read repository-local documentation instructions and inspect the existing
   corpus. Local conventions control paths, metadata, indexes, and validators.
2. Identify the requested operation and the document's one primary job.
3. Read only the doctrine needed from
   `.axm/extensions/@craigsmitham/knowledge/docs/src/`:

| Need | Concepts |
| --- | --- |
| Classify or outline | `docs-explainer.md`; likely type explainer |
| Create or substantially revise | `docs-explainer.md`, `docs-guide.md`; matching type explainer and guide |
| Review type fit | `docs-explainer.md`; relevant type explainers |
| Review structure | Matching type explainer and guide |
| Review staleness or accuracy | `docs-explainer.md`; relevant type explainer; `quality-explainer.md` only for overall quality |
| Evaluate overall quality | `quality-explainer.md` |
| Remediate a corpus | `workflow-explainer.md`, `workflow-guide.md` |

The matching type pair is one of `tutorial-*`, `how-to-*`, `reference-*`, or
`explanation-*`. If the type is unclear, use `docs-explainer.md` before choosing.

## Act according to intent

- Requests to outline, suggest, classify, audit, or review are read-only unless
  the user also asks for changes.
- Requests to create, revise, refresh, restructure, or fix authorize the named
  documentation changes and locally required index updates.
- Confirm before destructive retirement, deletion, or an ambiguous
  reorganization that would materially change ownership or navigation.

For authoring, state the reader need and desired outcome, keep one primary job,
and link to adjacent owners instead of duplicating them. For review, report
specific evidence and distinguish wrong type, mixed jobs, stale facts, duplicate
sources of truth, weak framing, broken links, and missing host-required indexes.

## Boundaries

- Do not invent product facts, architecture policy, repository layout, or a
  frontmatter schema.
- Do not judge placement unless the repository declares a placement rule.
- When an artifact has its own format contract, apply the relevant capability
  only if the host provides it or it is already available; otherwise follow the
  repository-local contract or ask for the missing requirements.
- Do not treat always-on instruction files as ordinary documentation; follow
  host-specific instruction-authoring rules or ask for them.

## Finish

Run the repository's documentation and link validators when available. Report
the documents created or changed, their primary types, validation performed,
and any remaining facts that require an authoritative source.
