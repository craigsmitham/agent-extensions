# Pattern alignment review

The repository owned 18 pattern descriptions at the start of this review
on `main` (`bc89f76`). The two collection indexes matched the 15 documentation
patterns and three software-testing patterns identified by their metadata.
The inventory also covered named patterns in other maintained sources.
For example, the domain-driven design explainer discusses published patterns
without adding local catalog entries. Installed copies belong to their source packages.

Each row records an editorial walkthrough. The middle column gives a reader
a reason to choose the pattern. The last column changes one fact and follows
the resulting decision. For each documentation form, the pattern's explainer
and authoring guide were checked against those choices. For the testing
patterns, the companion routes lead to the relevant domain guidance.

## Documentation forms

| Pattern | Where it fits | What changes the decision |
| --- | --- | --- |
| [Explanation](../knowledge/docs/src/patterns/explanation.md) | A technician knows the lighting board and wants to understand why a cue behaved unexpectedly. | If the missing fact is the cue number, the cue list can answer the question directly. |
| [Tutorial](../knowledge/docs/src/patterns/tutorial.md) | A technician can practice a crossfade on a setup the instructor chooses and listen to the result. | Preparing tonight's cue introduces a real production target and constraints. A how-to serves that job. |
| [How-to guide](../knowledge/docs/src/patterns/how-to.md) | An operator knows which cue the production needs and must configure it across several controls. | After a cue fails for an unknown reason, the team still has to choose a response. A playbook can guide the investigation. |
| [Reference](../knowledge/docs/src/patterns/reference.md) | An operator needs the trigger for a known cue and can return to work once they find it. | An operator who needs to configure the cue needs directions that connect the controls. |
| [Principle document](../knowledge/docs/src/patterns/principle.md) | A release team weighing frequent delivery against repeated overtime can use its shared commitment to a sustainable pace. | If a binding release embargo fixes the date, the governing rule settles that choice. A proposed commitment also needs agreement before other teams can rely on it. |
| [Playbook](../knowledge/docs/src/patterns/playbook.md) | Checkout errors follow two recent changes. The affected customers and versions can help responders decide which owner to involve. | Once the team selects an approved rollback, the runbook covers that operation. Continuing customer failures reopen the investigation. |
| [Runbook](../knowledge/docs/src/patterns/runbook.md) | A museum technician can publish an approved exhibit image and verify its revision on the named display. Another shift can finish from the recorded state. | If a blank display is the only observation, nobody has established that republishing is the remedy. The technician needs diagnosis first. |
| [Pattern description](../knowledge/docs/src/patterns/pattern-description.md) | Suppose two event teams have tried separating routine pickups from exceptions, one with a counter and one with a roving volunteer. Their accounts offer a design and consequences to compare. | Two teams experiencing queues and citing the same untried sketch establish a recurring problem. The response remains a candidate. |
| [Pattern collection](../knowledge/docs/src/patterns/pattern-collection.md) | A facilitator who wants people to make sense of a discussion can browse Group Works by group need and consider Distilling or Harvesting. | A facilitator who already wants Harvesting can use the name index. Both routes reach the same entry. A claim about the sequence of design decisions would need an example of using patterns together. |

## Checklists

| Pattern | Where it fits | What changes the decision |
| --- | --- | --- |
| [Checklist for recurring omissions](../knowledge/docs/src/patterns/checklist.md) | Experienced staff repeatedly miss a loan handoff they could still complete if prompted. | Someone unfamiliar with the full interlibrary renewal procedure needs instructions for doing the work. |
| [Execution checklist](../knowledge/docs/src/patterns/execution-checklist.md) | An editor returning to an interrupted export needs to know which edition was exported and what action comes next. | Once the export is complete, comparing the finished translation to its criteria calls for verification. |
| [Verification checklist](../knowledge/docs/src/patterns/verification-checklist.md) | A receiver can compare the goods on hand with the purchase order and record a discrepancy. | Authorizing payment introduces a decision and an accountable role. The receiving result can inform that readiness decision. |
| [Readiness checklist](../knowledge/docs/src/patterns/readiness-checklist.md) | A workshop lead can hold the opening if attendance exceeds the confirmed room capacity. | Someone asked only whether two capacity records agree can verify them without authority to open the workshop. |
| [Reporting and review checklist](../knowledge/docs/src/patterns/reporting-review-checklist.md) | A reviewer locates each required client metric in the report or records why it falls outside scope. | Checking the reported totals against the source records calls for verification. A page number establishes where a figure appears. |
| [Learning checklist](../knowledge/docs/src/patterns/learning-checklist.md) | A reviewer practices judging chart comparisons, gets feedback, then tries a fresh chart without prompts. | If every published chart must carry the approved dataset, a lasting execution prompt serves that obligation. |

## Software testing

| Pattern | Where it fits | What changes the decision |
| --- | --- | --- |
| [Executable specifications](../knowledge/software-testing/src/patterns/executable-specifications.md) | A membership team accepts a calendar-day refund rule. The owners can read and check the £120 and £0 outcomes on days 14 and 15. | If the same outputs come only from observing legacy software, a characterization test can preserve the observations. Accepting the rule remains an owner decision. |
| [Evidence-matched test world](../knowledge/software-testing/src/patterns/evidence-matched-test-world.md) | A direct test suffices to check whether the exporter selects André's name. | If the downloaded name loses its accent, inspect the delivered bytes. The download handler can introduce the fault after selection succeeds. |
| [Owned test worlds](../knowledge/software-testing/src/patterns/owned-test-world.md) | An abandoned queue item can make a different test run appear successful. Distinguishing runs lets an owner reclaim expired work while preserving active work. | A pure calculation with local inputs leaves nothing for the next run to inherit. Ordinary ownership of its test code suffices. |

## What the checks establish

Two technical examples were exercised locally. A reader on an existing
SQLite transaction saw the original value after a second connection committed
in write-ahead logging mode. A fresh transaction saw the update. Python
logging checks distinguished the effective level inherited by a child logger
from the levels a handler accepts and showed records from two logger names
reaching the same output. [SQLite isolation](https://sqlite.org/isolation.html)
and [Python logging](https://docs.python.org/3/library/logging.html) describe the behaviors checked.

GitLab documents a restore followed by a recency check. Group Works offers
two working routes to Harvesting. These are observations of published
guidance. How well new operators and facilitators can use it remains an
open question. [GitLab verification](https://runbooks.gitlab.com/customersdot/backups/#verification),
[Group Works by category](https://groupworksdeck.org/patterns_by_category),
and [Group Works by name](https://groupworksdeck.org/patterns_by_name).

The testing collection labels *Owned test worlds* a candidate because
the sources document ownership and isolation practices separately.
Outcomes from adopting the combined design remain open.
