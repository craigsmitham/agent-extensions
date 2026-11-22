---
name: docs
description: >
  Writes, reviews, organizes, audits, and repairs documentation across domains,
  including knowledge-base articles, READMEs, tutorials, how-to guides,
  reference, explanations, principles, playbooks, and runbooks. Explains
  document forms and helps choose one for the reader’s purpose. Use for
  designing, adapting, or planning validation of reusable checklists, mining
  design patterns, reviewing pattern evidence or smells, and curating pattern
  collections or languages. Covers documentation health, structure, filenames,
  titles, links, stale content, and implementing accepted audit findings.
  Applies when documentation is the requested artifact even if a different
  skill covers the subject. Excludes always-on agent instructions, Word or
  Google Docs artifacts, regular expressions, visual motifs, audits of other
  corpora, and implementation of products or named design patterns.
---

# Docs

Create or assess documentation for the reader and subject in the brief.
The typical setting is a software engineering workspace. Assume readers will
access the documentation digitally unless the request or their working
conditions call for another medium. Ground examples in the reader’s domain.
In guidance for authors, distinguish a reusable design choice from its
implementation, such as keeping an interruption marker with the work item.
In a checklist for the person doing the work, give the concrete action
that fits their setting.

Respect the requested scope and output format. Preserve applicable local
authority and source support. Distinguish audit, review, authoring, and
remediation outcomes.

Resolve `@craigsmitham/knowledge/docs` through host discovery or
`axm knowledge concepts get`. The following are concept IDs within that required
pack sibling; report a missing dependency rather than inventing its guidance.
Load only the relevant route.

For a cataloged form, select one starting page by intent. To understand how
the form works, open `explainers/<subject>`. To choose or assess its design,
open `patterns/<subject>`. To write or revise it, open the guide in its row.
Use a companion when a further question calls for it.

| Form | Subject | Authoring guide |
| --- | --- | --- |
| Explanation | `explanation` | `guides/writing-an-explainer` |
| How-to guide | `how-to` | `guides/writing-a-how-to-guide` |
| Tutorial | `tutorial` | `guides/writing-a-tutorial` |
| Reference | `reference` | `guides/writing-reference-documentation` |
| Principle document | `principle` | `guides/writing-a-principle-document` |
| Playbook | `playbook` | `guides/writing-a-playbook` |
| Runbook | `runbook` | `guides/writing-a-runbook` |
| Pattern description or mining | `pattern-description` | `guides/writing-a-pattern-description` |
| Pattern collection or language | `pattern-collection` | `guides/curating-a-pattern-collection` |
| Checklist | `checklist` | `guides/designing-a-checklist` |
| Execution checklist | `execution-checklist` | `guides/designing-an-execution-checklist` |
| Verification checklist | `verification-checklist` | `guides/designing-a-verification-checklist` |
| Readiness checklist | `readiness-checklist` | `guides/designing-a-readiness-checklist` |
| Reporting and review checklist | `reporting-review-checklist` | `guides/designing-a-reporting-and-review-checklist` |
| Learning checklist | `learning-checklist` | `guides/designing-a-learning-checklist` |

| Other need | Knowledge route |
| --- | --- |
| Choose among unfamiliar forms | `explainers/documentation-craft`, then the relevant pattern |
| Review the evidence or reasoning in a pattern description | Review guidance in `guides/writing-a-pattern-description` |
| Review one document, including a README | `explainers/documentation-quality`, plus a matching pattern when its form matters |
| Bounded corpus audit | `explainers/documentation-audits` and `guides/auditing-documentation` |
| Organization, placement, or naming | `guides/organizing-and-naming-documentation` |
| Repeatedly confused concepts | `guides/comparing-concepts` and authoritative definitions |
| Practice, standard, or conformance | Relevant `explainers/` concepts |
| Factual or link correction | Local authoritative sources and relevant validators |

For audits, preserve the exact finding fields and report order in the audit
report contract. Audit-only requests do not authorize changes. For combined
audit and remediation, retain the diagnostic finding set before editing.

Pattern descriptions inform design without imposing their own headings on every
resulting artifact. Checklist purpose and interaction mode are distinct; recorded
completion is not evidence of the intended outcome. Mining patterns does not
validate their domain effectiveness or authorize implementation.

Keep related indexes, metadata, and references coherent with authorized edits.
Keep index and catalog previews accurate for their readers. Copy a canonical
description verbatim when the host requires it.
Report actual verification and unresolved source gaps; authoring review is not
reader testing, independent approval, or procedure execution.
