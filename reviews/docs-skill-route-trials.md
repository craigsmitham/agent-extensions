# Docs skill route trials

These trials tested the routes of the [docs skill](../skills/docs/src/SKILL.md) at version 0.7.0, as [Maintaining the docs bundle](../knowledge/docs/AGENTS.md) requires. Three fresh agents each got one realistic brief and the workspace's full skill listing. No one told them which skill to use. Each agent wrote its deliverable outside the repository and reported which skills it chose, which concepts it loaded, and anything it found unclear. These were agent trials, without reader sessions. No procedure was executed.

## Results

| Brief | Skills selected | Concepts loaded | Resolution | Deliverable against reader goal |
| --- | --- | --- | --- | --- |
| Write a runbook for restoring a Postgres database from a nightly backup, for on-call engineers during an outage | `docs` and `devops-docs` | `guides/writing-a-runbook` | First try, using the fragment form | Usable draft. It flagged an unreliable verification query, an irreversible `--clean` step, and its own added commands. It recorded the exercise history as unknown. |
| Review `skills/okf/README.md` for a first-time installer, without editing | `docs` and `axe` | `explainers/documentation-quality`, plus two axe concepts | First try | Five concrete fixes, checked by a dry-run install and a validator run |
| Audit `knowledge/release-engineering/src` for links, stale content, and structure, audit only | `docs` | `explainers/documentation-audits`, `guides/auditing-documentation` | First try | Report in the contract format. It made no edits and found one medium stale claim. |

## Observations

- **The resolution syntax works.** Every agent used the `#` fragment form shown in the skill, and no lookup failed.
- **Runbook ownership is still ambiguous.** The runbook agent read “even if a subject skill covers the domain but not its documentation” and saw that `devops-docs` does cover runbook documentation. It used both skills. It also found that `devops-docs` forbids inventing commands while the docs guide does not say whether common commands count as invention.
- **The README route is thin.** `explainers/documentation-quality` has no README-specific guidance. The agent found the axe README guide only by also invoking `axe`.
- **The audit route reads as two routes.** The audit row lists two concepts, while the skill says to “load only the relevant route.” The agent treated the row as one route. After the trial, the skill was changed to say “load only the pages named in the relevant row.”

## Open questions

The overlaps between `docs` and `devops-docs` on runbooks and playbooks, and between `docs` and `axe` on extension READMEs, are boundary questions. The skill does not name those extensions, because they are not declared companions. Guidance for this case has been requested from the AXE maintainers.
