---
name: docs
description: >
  Creates, reviews, organizes, audits, and remediates documentation using
  portable craft. Use for READMEs, tutorials, how-to guides, reference,
  explanations, principle documents, playbooks, runbooks, reusable checklists,
  and design pattern descriptions, collections, or languages across domains;
  mining patterns for documentation;
  reviewing pattern evidence or smells; reviewing one document; auditing bounded
  documentation corpora or assessing documentation health; proposing structures,
  paths, filenames, or titles; organizing collections; fixing links or stale
  content; designing, adapting, and planning validation of checklists; and
  implementing accepted documentation-audit findings. Apply when
  documentation is the requested artifact, even when another skill covers its
  subject. Not for editing always-on agent instructions, Word or Google Docs
  artifacts, regular expressions, visual motifs, corpus audits beyond
  documentation, or implementing a product or named design pattern.
---

# Author docs

Create the smallest complete documentation improvement or evidence-backed
assessment that serves the reader's job and respects local authority.

## Workflow

1. **Resolve the job and authority.** Distinguish audit-only, review-only,
   creation, and remediation work. Read repository-local instructions, inspect
   the target and its authoritative sources, and preserve unrelated user
   changes. Route by requested artifact: a guide about an agent instruction
   file is documentation work; modifying the instruction file itself is not.
2. **Choose the smallest knowledge route.** Resolve the docs pack sibling
   `@craigsmitham/knowledge/docs` through host knowledge discovery or
   `axm knowledge concepts get`. The paths below are concept IDs within that
   bundle, not workspace file paths. If required guidance is unavailable,
   report the missing docs pack dependency rather than inventing a substitute.

| Request | Start with | Add when needed |
| --- | --- | --- |
| Choose a documentation pattern | `explainers/documentation-craft` | Matching `patterns/<subject>` |
| Write or review a tutorial, how-to, reference, explanation, principle document, playbook, or runbook | Matching `patterns/<subject>` | `guides/documentation-craft` for the shared process |
| Create, review, adapt, or plan validation of a reusable checklist | `patterns/checklist` | Matching `patterns/{execution,verification,readiness,reporting-review,learning}-checklist` for its purpose |
| Mine, write, or review a design pattern description; assess its evidence or smells | `patterns/pattern-description` | `patterns/pattern-collection` for relationships within a collection |
| Author, review, or maintain a pattern collection or language | `patterns/pattern-collection` | `patterns/pattern-description` for individual entries |
| Audit a bounded corpus | `explainers/documentation-audits` | `guides/auditing-documentation` |
| Remediate or restructure a corpus | `guides/documentation-workflow` | Relevant pattern and organization guidance |
| Place, organize, or rename documentation | `guides/organizing-and-naming-documentation` | `explainers/documentation-organization-and-discovery` |
| Clarify repeatedly confused concepts | `guides/comparing-concepts` | The authoritative definitions |
| Distinguish a practice or standard | Matching `explainers/{practice,standard}` | `explainers/standard-authority-and-conformance` |
| Check links, staleness, or factual accuracy | Repository-local sources and validators | Relevant pattern guidance when structure is in scope |

`patterns/` is the documentation pattern collection. Each page describes a
recurring reader problem, a document design that addresses it, applicability,
tradeoffs, evidence, and authoring guidance. Select by fit and adapt the design
to the reader's job; the resulting document follows its own useful structure.
`explainers/` and `guides/` contain broader documentation foundations and
workflows. The docs pack supplies all required guidance.

Pattern subjects can come from any design domain. Mining gathers evidence for
the requested descriptions; domain validation and implementation remain
separate work. Keep the detailed pattern method in the selected knowledge
entries rather than reproducing it in this workflow.

Checklist authoring includes its use protocol and validation plan. Choose
purpose separately from interaction mode, and preserve the distinction between
recorded completion and evidence of the intended outcome. Execution, domain
approval, and real-world effectiveness evaluation remain separate work; the
selected checklist patterns own the detailed design guidance.

3. **Audit when requested.** For a bounded corpus assessment, state the audit
   question, included and excluded scope, audience, authority, and repository
   revision, release, or observation time. Select only relevant dimensions;
   inventory the corpus; declare whether coverage is a path census, full
   review, purposeful sample, journey sample, or combination; and record
   reviewed items and blind spots. Use existing read-only validators and
   distinguish their deterministic evidence from human judgment. Use this
   exact field order for every material finding; do not fold one field into
   another:
   - `<ID> — <title>`
   - `Severity:`
   - `Confidence:`
   - `Condition:`
   - `Evidence:`
   - `Impact:`
   - `Expected state:`
   - `Recommendation:`
   - `Route:`

   Report scope and snapshot,
   disposition, coverage and method, strengths, findings, remediation order,
   limitations, and handoff. Do not collapse unlike qualities into a numeric
   score or change documentation during an audit-only request.
4. **Preserve the reader job.** Name the document's primary reader, need, and
   authority. Keep that job recognizable; link to neighboring material rather
   than making one document perform every function. For an action-oriented
   document, make its description pair the supported outcome with the
   observable situation, event, symptom, or reader intent that makes it
   relevant. Keep that selection condition distinct from the access,
   knowledge, or state preconditions required after selection.
5. **Place and name deliberately.** Follow local information architecture when
   it works. When organization is in scope, choose the axis from reader entry
   points and semantic adjacency; do not invent unsupported host metadata or
   path conventions.
6. **Make authorized changes.** Skip this step for an audit-only request.
   Otherwise, correct facts only from available authority. Keep changes
   bounded, update related indexes and metadata when required, and preserve
   inbound references or plan their migration when paths change.
7. **Verify proportionately.** Re-read for the reader's job, check claims
   against their sources, run available link, metadata, rendering, and package
   validators, and inspect the diff for collateral changes. When an index or
   catalog previews a canonical description, verify that it copies the
   description exactly and that neighboring action documents remain
   distinguishable before opening.
8. **Handoff.** State what changed or assessed, what evidence was checked, and
   any deferred finding, uncertainty, or owner. Do not present an authoring
   review as a corpus audit or either activity as independent approval.

For a combined “audit and fix” request, complete and preserve the diagnostic
finding set before editing. Route each accepted finding through the applicable
authoring step, and ask before remediation materially expands scope, changes an
accepted information architecture, or requires a product decision the
documentation cannot establish.
