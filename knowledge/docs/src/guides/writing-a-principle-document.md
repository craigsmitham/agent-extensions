---
type: Guide
title: How to write a principle document
description: When people repeatedly face a choice that calls for judgment, write a warranted direction they can apply and test it against a case where the usual answer changes.
tags: [docs, principle, authoring, judgment, warrant, how-to]
status: draft
generated: { by: codex/gpt-6, at: 2026-11-21T22:44:16Z }
sources:
  - id: style
    resource: https://peps.python.org/pep-0008/
    title: PEP 8 — Style Guide for Python Code
  - id: goods
    resource: https://globalfacultyinitiative.net/content_item/320
    title: Oliver O’Donovan — Created Order / Theology
  - id: virtue
    resource: https://globalfacultyinitiative.net/fi_pdf/get_document.php?id=462
    title: Oliver O’Donovan — The Place of Virtue Theory in Christian Ethics
---

# How to write a principle document

Bring a decision people have actually struggled with, the people responsible
for it, and whatever gives the proposed direction its standing. An illustrative
brief runs through the steps below. A library team keeps debating how far to
take a cleanup of names. It wants to help maintainers decide which names to
change in future patches.

## 1. Find two decisions the document should help with

Ask for a recent decision and a case where the same answer would cause
trouble. A maintainer wants to rename a new private helper from `fmt` to
`format_caption`. In another patch the name under review is a released
function in customers’ scripts. Write down who would benefit from each
change and who would have to do extra work.

Ask what good the team wants both decisions to serve. Here, users should
be able to read code and continue relying on the names they have learned.
Write a direction that could affect the next patch. “We value consistency”
leaves both reviewers where they started. “Use names people can understand
and keep published names dependable” gives them two consequences to
investigate. O’Donovan’s discussion of goods and principles is useful when
a statement of value has yet to give anyone a reason to act.[^goods]

## 2. Establish what gives the direction weight

Locate the decision record, code of practice, agreement, or other authority
that applies. Check its audience, binding force, and exceptions. PEP 8
supplies a worked precedent for balancing readable names and compatibility.
Its authors also recognize project-specific conventions. A link to PEP 8
alone cannot record what this library's maintainers agreed to.[^style]

In the example, suppose the maintainer confirms a project policy preserving
released names during patch updates. Link the actual policy when drafting
for a real team. Mark a suggested naming preference as a proposal until
the team adopts it. If nobody can substantiate an alleged requirement,
leave it out of the obligations you assign. Check each worked case too.
A cautious suggestion in an example can accidentally become an extra
permission requirement. State whose decision it is and what the source
actually requires. For an inherited maxim, trace the wording to
its source and identify whose later interpretation the team adopted. A
name shared across communities can carry different commitments.

## 3. Write the passage a reviewer could use

State who faces the choice and which consequences should carry weight.
Distinguish a requirement already in force from a preference someone can
reasonably depart from. Here is a draft under the example policy.

> **Keep names useful to the people who depend on them.** In patch reviews,
> prefer a name that lets the next maintainer recognize the operation. Rename
> a private helper when the gain in clarity justifies updating its callers.
> Our compatibility policy protects released names in patch updates. If a
> public name misleads new users, document its behavior now and bring a
> migration proposal to the maintainers.
>
> Before calling a name private, check what the project has promised in its
> published interface. Ask the interface owner when the evidence is unclear.

That last sentence identifies an obligation the reviewer can act on. Ask
what attention, skill, or authority the person deciding will need. If the
document asks for care, show what an attentive reviewer would notice.
O’Donovan connects deliberation with the responsibilities and resources of
the person acting.[^virtue]

## 4. Try a case the draft did not grow up around

Give another maintainer the draft and a patch affecting a helper that is
absent from the public API list but appears in the project's published
examples. Ask what they would do next and which fact could change the
decision. If they treat the missing list entry as permission to rename,
revise the passage to make the conflicting promise visible. If they block
every internal cleanup, make the private-helper case clearer.

When working alone, write out the competing choices and trace each reason
to the draft or the authority it cites. Finish when the reader can name the
good at stake, distinguish a binding limit from a preference, and explain
what they would do when the facts are uncertain. Record any unresolved
policy question for the person who can settle it.

[^style]: [PEP 8](https://peps.python.org/pep-0008/), introduction and consistency guidance.
[^goods]: Oliver O’Donovan, [Created Order / Theology](https://globalfacultyinitiative.net/content_item/320).
[^virtue]: Oliver O’Donovan, [The Place of Virtue Theory in Christian Ethics](https://globalfacultyinitiative.net/fi_pdf/get_document.php?id=462).
