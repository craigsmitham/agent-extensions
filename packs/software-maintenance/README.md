# Software maintenance

Seven standalone skills for explicit maintenance: align, reconcile, modularize, generalize, reuse, prune, and improve.

Software maintenance keeps software useful as requirements, knowledge, and
circumstances change. This pack brings together seven concise, outcome-focused
skills for direct use during maintenance. Invoke a skill with a scope and the
outcome or constraints that matter. Each leaves methods to the caller and
model; the pack prescribes no execution order.

## Install

```bash
axm install @craigsmitham/packs/software-maintenance
```

Each skill remains self-contained and individually installable. For example:

```bash
axm install @craigsmitham/skills/improve
```

The pack installs its members together. Each skill declares explicit-only
invocation and remains independently usable.

## Choose a skill

All seven skills use identities under `@craigsmitham/skills/`.

| Skill | Choose it when… | Desired outcome |
| --- | --- | --- |
| `align` | Requirements or guidance have changed, or implementation has drifted. | The codebase satisfies applicable requirements and reflects relevant guidance. |
| `reconcile` | Related content repeats the same knowledge or has drifted apart. | Related representations agree on shared meaning, with less unnecessary duplication. |
| `modularize` | Responsibilities are entangled or changes spread across unrelated concerns. | Cohesive responsibilities with simple boundaries that let them evolve independently. |
| `generalize` | A capability should serve a broader family of related cases. | Broader applicability through coherent commonality and appropriate variation. |
| `reuse` | Available capabilities could replace unnecessary implementation. | A coherent integration with suitable existing capabilities and less maintenance burden. |
| `prune` | Elements no longer justify their continued presence. | A smaller, coherent system with less maintenance burden. |
| `improve` | Existing software could better serve its intended purpose. | Worthwhile, evidence-backed gains in relevant qualities. |

The outcomes can share techniques. Generalization may require better boundaries;
reuse may remove superseded machinery. The requested outcome determines scope
and success. Shared mechanisms should preserve independently changing policies,
and similar implementations need not represent the same knowledge.

## Usage

Name the relevant scope and the outcome or constraints that matter. For example:

```text
$align src/api/ with the updated error-handling requirements
$reconcile setup instructions across README.md, docs/, and example projects
$modularize src/billing/ around independently changing responsibilities
$generalize the exporter to support the additional formats in the specification
$reuse the adopted parser's capabilities in src/importers/
$prune obsolete build configuration while retaining supported release targets
$improve the importer's memory use without sacrificing required throughput
```

Use `$skill` in Codex and the host's skill command or mention in other agents.
The packages set `policy.allow_implicit_invocation: false` in
`agents/openai.yaml` for [Codex](https://learn.chatgpt.com/docs/build-skills),
and `disable-model-invocation: true` in `SKILL.md` for
[Claude Code](https://code.claude.com/docs/en/skills),
[Cursor](https://cursor.com/docs/skills),
[Copilot CLI](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference),
and [Zed](https://zed.dev/docs/ai/skills). These settings retain direct invocation
while disabling automatic selection in hosts that support them.

Work can begin with whichever outcome is needed. Changed requirements may
call for alignment, with removal of superseded machinery where obligations
permit. A well-scoped task may need only one skill. The pack prescribes no
sequence or requirement to use every member.

## Philosophy

Renewal is purposeful change in relation to what software is for and what it
must continue to support. A useful result can involve removing something,
improving a quality, extending applicability, satisfying changed guidance,
learning that a proposed change is not worthwhile, or reconciling content that
duplicates or contradicts shared knowledge.

The skills share a concern for context, live obligations, and claims supported
by appropriate evidence. They have distinct outcomes, even when their
techniques overlap. Conformance does not by itself establish improved quality;
broader applicability does not establish that every new case is valuable.

The pack's organizing inspiration is Peter Drucker's treatment of renewal
through abandonment, continuing improvement, exploitation of success, and
systematic innovation. The software mapping is this pack's synthesis:

- Pruning closely corresponds to systematic abandonment.
- Improving closely corresponds to continuing improvement.
- Generalizing and reusing can enable new applications of proven capabilities,
  supporting exploitation of success.
- Aligning adds conformance as requirements and guidance change.
- Reconciling adds coherence among related representations of shared knowledge.
- Modularizing helps responsibilities evolve independently as software changes.

This is not a claim that Drucker proposed seven software practices or a fixed
renewal cycle. The pack supplies a vocabulary of useful outcomes and convenient
installation. The caller and model retain judgment about methods, priorities,
sequence, and the extent of change.

## Sources and inspiration

- **Peter Drucker — [Drucker on Creating an Innovative
  Culture](https://drucker.institute/wp-content/uploads/2018/08/Reading_Drucker-on-Creating-an-Innovative-Culture.pdf).**
  This Drucker Institute reading adapts “Management's New Paradigms” and
  *Innovation and Entrepreneurship*, presenting four ongoing entrepreneurial
  activities. It supplies the organizational inspiration described above.
- **Engineering foundations:** each member's package README credits the
  sources behind its definition and explains the limits of its synthesis.

The pack's explanatory prose is original. Linked sources retain their respective
rights; no source text or code is vendored here.

## License

The pack metadata and README are MIT-licensed. Each included skill retains the
license declared in its own manifest.
