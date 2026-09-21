---
observed_at: "2026-09-21T16:37:36Z"
session: "session-k4m8v2"
area: "field-notes evaluation"
---

# Required resource reads counted as enrichment

## Context
An authoring smoke trial exercised the new field-note capture behavior against
case 1 of the versioned evaluation suite.

## Friction
The grader failed the no-enrichment assertion because the candidate read
`SKILL.md` and its declared `references/capture.md` template before writing the
note. Those reads are required skill execution, while the assertion intended to
exclude diagnostic or investigative calls made to enrich the occurrence.

## Cost / impact
One otherwise representative smoke trial failed and required the assertion to
be clarified and rerun. Elapsed time and token cost were not measured.

## Outcome
The failed run was preserved. The assertion was narrowed to allow declared
skill-resource reads while still prohibiting diagnostic or enrichment calls and
additional analysis.

## Evidence
Run `2026-09-21T16-36-29-722Z-cf4b8867` reported one failed case. Its critical
failure cited two command-execution reads of `SKILL.md` and `capture.md` as the
only contrary evidence.
