# Evaluate Agent Skill

Evaluate whether an Agent Skill activates for the right requests and produces
the intended behavior once activated. The workflow separates routing,
execution, outcome, efficiency, safety, and robustness evidence and can compare
a candidate with a baseline. For governed libraries it also tests isolation,
semantic neighbors, and the actual active cohort separately.

Use it to test, benchmark, verify, or compare skill behavior. It reports
findings without modifying the evaluated skill.

## Install

```sh
axm install @craigsmitham/packs/skill-engineering
```

## Example

> Evaluate this skill against clear positives, paraphrases, adjacent negatives,
> ambiguous requests, and explicit invocation. Compare it with the published
> version and report variance.
