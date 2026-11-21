---
type: Guide
title: How to design a verification checklist
description: When someone must check completed work, write a checklist that ties each conclusion to evidence from the finished item and sends discrepancies for correction and recheck.
tags: [docs, verification-checklist, authoring, verification, comparison, discrepancy]
status: draft
generated: { by: codex/gpt-6, at: 2026-11-21T22:49:04Z }
sources:
  - id: bagit
    resource: https://www.rfc-editor.org/rfc/rfc8493.html
    title: RFC 8493 — The BagIt File Packaging Format (V1.0)
---

# How to design a verification checklist

Take the finished item, a criterion for accepting it, and an example of
something that went wrong. Suppose an archive receives concerts packaged
using BagIt. Staff want a short card for logging the result of a delivery
check. Their validator already knows the file format. The card should help
staff associate its conclusion with the right delivery and handle trouble.

## 1. Define the claim and find evidence that could disprove it

Replace “delivery OK” with the claim the receiver can actually establish.
For a BagIt delivery, validity requires both completeness and successful
verification of all manifest checksums. Obtain a full validation report
for the received package. The format allows a quick preliminary check
of the total byte and file counts. A success on that check alone leaves validity open.
Identify the part of the report that distinguishes the two.[^bagit]

If the archive also needs to identify the performance, locate the agreed
accession record and a way to check what was recorded. Give that claim its
own check. Restrict the checksum result to the comparison it performed.

## 2. Write the comparisons and the response to a discrepancy

Here is the core of the illustrative archive card. Replace labels and
responsibilities with those used at the receiving desk.

| At receipt | Evidence and response |
| --- | --- |
| Is this the delivery under review? | Match the received package identifier to the accession record and the validation report. If any identifies another delivery, set the report aside and obtain the correct one. |
| Is the package complete and valid? | Locate the full validator result for that package. Record the report location. If the check failed, record the missing path or checksum discrepancy. A skipped comparison stays unverified. |
| What happens to a discrepancy? | Hold the package for the sender to supply a corrected copy. Validate the replacement and attach its own result before closing the discrepancy. |

Keep mechanical comparisons in the validator. When translating criteria
into prompts staff will use, follow the shared [checklist design guide](designing-a-checklist.md)
for item wording and the use protocol.

## 3. Try a correct case and cases that look correct

Use a test copy. Run the actual validation on a known-good package. Change
one byte of a payload file without altering its length or the manifest and
run it again. Follow the card with both reports. The second package should
take the discrepancy route even though its filenames and sizes look right.
Then give the reviewer the good report with a different delivery identifier.
Can they spot the mismatch before they record acceptance?

If a reader can pass a damaged delivery by ticking “report present,” revise
the item to ask which comparison ran and what it found. Record the cases
tried. The test addresses those discrepancies. Production use can reveal
failures the test copies did not contain.

For the archive card, a useful trial log records which validator output
the receiver inspected and whether a damaged package still reached accession. For a reusable candidate, include the
[maintainer note](designing-a-checklist.md#decide-what-would-justify-keeping-it)
with the card and identify any open ownership or evidence questions.

[^bagit]: [RFC 8493](https://www.rfc-editor.org/rfc/rfc8493.html), §§2.2.2 and 3.
