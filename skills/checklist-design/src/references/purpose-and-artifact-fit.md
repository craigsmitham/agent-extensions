# Purpose and artifact fit

Choose the aid from the work it must change, not from the requested format.
The same visual list can be an execution aid, verification control, team
coordination pause, reporting aid, or learning scaffold; those purposes imply
different interaction and evidence.

## Establish the job

Name:

- the outcome sought and the people affected;
- the observable failure the aid should reduce;
- when and where the aid enters the workflow;
- what users already know and can act on;
- the consequence of delay, omission, misselection, and false completion; and
- the outcome level the author intends to claim.

Do not collapse process adherence, task quality, downstream outcomes, and
learning into one success measure. A reporting checklist can improve reporting
completeness without establishing that the reported method or conclusion is
sound. A visible learning prompt can improve aided performance without
establishing retained knowledge.

## Select the primary artifact

| Need | Likely primary artifact | Checklist's possible supporting role |
| --- | --- | --- |
| Bounded known actions or states where omission matters | Checklist | Primary execution or verification aid |
| Complete explanation, rationale, and procedural detail | SOP or runbook | Entry, pause, or final verification points |
| Substantial conditional diagnosis or branching | Decision tree, algorithm, or playbook | Preconditions, handoff, or branch-local verification |
| Judgment across quality dimensions | Rubric | Evidence-gathering or submission-completeness prompts |
| Structured data collection | Form | Reminders for critical fields or follow-up actions |
| Repeated deterministic prevention | Automation or interface constraint | Independent verification or exception handling |
| Durable knowledge, judgment, or transfer | Instruction, practice, simulation, retrieval, and feedback | Temporary scaffold that fades with competence |

A checklist is a weak primary artifact when users cannot recognize the
situation, lack authority or resources to act, require explanation to perform
the item, face many conditional paths, or need continuous control rather than
bounded prompts.

## Choose an interaction mode

| Mode | Primary outcome | Design emphasis | Evidence that matters |
| --- | --- | --- | --- |
| `read-do` | Correct directed execution | Order, dependencies, critical actions, pause points | Omissions, errors, timing, recovery |
| `do-confirm` | Detect missed or incorrect completed work | Observable state, independent confirmation, correction | Missed conditions and defects corrected |
| `challenge-response` | Mutual team verification | Named roles, audible prompt and response, authority to stop | Shared-state and communication failures |
| `readiness-gate` | Sound proceed, stop, release, or escalate decision | Criteria, required evidence, decision owner, failed-gate action | False passes, decision agreement, outcomes |
| `reporting-review` | Coverage, traceability, or inspection | Source traceability, observable criteria, consistent interpretation | Completeness and reviewer agreement |
| `learning-scaffold` | Supported practice toward independence | Rationale, retrieval, feedback, reflection, fading, transfer | Delayed unassisted retention and transfer |

NASA's flight-deck guidance distinguishes stepwise execution from verification
of a configured system and treats challenge-response teamwork as a distinct
mechanism. Use that distinction as evidence for conditional design, not as a
claim that cockpit conventions transfer unchanged to another domain.

## Handle hybrids

Name one primary mode. A secondary mode is legitimate when its outcome and
interaction remain explicit. Surface tensions such as:

- coverage for audit versus speed during operations;
- personal completion versus independent verification;
- detailed novice guidance versus expert attention;
- locally adaptable wording versus invariant safety-critical content; and
- visible compliance versus candid escalation or speaking up.

If the secondary purpose changes item wording, order, roles, evidence, or
validation, represent it as a separate section or companion artifact rather
than an invisible compromise.

## Sources

- NASA, [*Human Factors of Flight-Deck Checklists*](https://www.faa.gov/sites/faa.gov/files/2022-11/NASA%20Ames%20Rpt%20CR%20177549%20.pdf)
- PRISMA, [PRISMA 2020 statement](https://pmc.ncbi.nlm.nih.gov/articles/PMC8008539/)
- Fraunhofer IESE, [Perspective-based versus checklist-based software inspection](https://publica.fraunhofer.de/entities/publication/eb2a71d4-2bfc-43c8-a5bf-8a03f643c016)
- BEME, [Systematic review of test-enhanced learning](https://pubmed.ncbi.nlm.nih.gov/29390949/)
