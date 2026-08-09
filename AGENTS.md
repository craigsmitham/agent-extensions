# Public agent extensions

This repository is the authoritative source for Craig's public agent
extensions. Author every extension here as an AXM workspace package under
`.axm/extensions/@craigsmitham/<plural-type>/<name>`. Route extension work
through AXM rather than editing agent-specific projections directly; read the
`axm` skill and the relevant `axm help` topic before acting.

## Public-by-construction policy

Treat every tracked file, manifest, generated artifact, symlink target, commit,
branch, tag, release, issue, and pull request as permanent public information.
Do not add sensitive material with the intention of sanitizing it later. If
public suitability is uncertain, stop and keep the extension in
`agent-extensions-private`.

An extension belongs here only when all of the following are true:

- It is useful outside Craig's particular machines, accounts, repositories,
  employer, clients, or personal knowledge system.
- Every included detail is intentionally safe to associate publicly with
  Craig, copy, index, mirror, and retain indefinitely.
- It is portable: no real usernames, hostnames, private URLs, absolute local
  paths, private repositories, account inventories, or unpublished extension
  dependencies are required.
- Examples and fixtures are synthetic rather than copied or lightly anonymized
  from real systems.
- Craig owns the content or has the rights to redistribute it, and manifests
  plus notices accurately declare all applicable licenses and attribution.
- Scripts, hooks, MCP definitions, and instructions use least privilege,
  disclose material side effects, and avoid destructive or externally mutable
  defaults.

Never commit credentials, tokens, cookies, private keys, certificates,
authentication exports, `.env` contents, real personal data, communications,
calendar or email contents, customer or employer material, database dumps,
incident artifacts, raw logs, or private documents. Store secret values outside
Git and use symbolic references such as `${SERVICE_TOKEN}` where configuration
is required.

The public publisher identity `@craigsmitham`, this repository URL, and content
Craig deliberately publishes under his own name are allowed. That exception
does not extend to incidental operational or personal detail.

## Extension isolation and package boundaries

Treat every extension as independently installed. Canonical package content
must not assume another extension is present merely because it shares an owner,
repository, workspace, or common installation.

- An extension may reference its own files relative to its `src/` root.
- Do not name, invoke, delegate to, link to, read from, or otherwise require
  another extension unless both are direct members of the same pack. This
  includes extension names, FQNs, canonical paths, agent projections, commands,
  examples, and routing instructions.
- A same-pack reference is permitted only when all of these are true:
  - One pack manifest lists both extensions as direct dependencies.
  - The referencing extension sets `standalone: false` and names that pack in
    `recommendedPacks`.
  - A required file uses AXM's canonical cross-extension path under
    `.axm/extensions/<@owner>/<plural-type>/<name>/src/`.
- `recommendedPacks` alone is not proof of co-installation. Neither is a shared
  owner, repository, workspace, lockfile, trust record, or local installation.
- Never reference another extension through an agent projection such as
  `.agents/skills` or `.claude/skills`, a pack-relative path, or `..` traversal.
- Without a qualifying common pack, keep the extension self-contained, describe
  an optional capability generically without implying availability, accept the
  needed input from the caller, or create an intentional pack.
- Pack manifests may name their dependencies. Package metadata may declare
  recommended packs. Repository catalogs, migrations, and publishing docs may
  name packages for distribution purposes, but must not create a runtime or
  authoring dependency between unrelated extensions.
- Public packs may depend only on public, active extensions.
- Treat generated AXM state as reviewable content; do not assume manifests,
  lockfiles, trust records, or symlinks are harmless merely because a tool
  produced them.

## Authoring quality

Keep skills extremely concise. Treat context as scarce and include only
guidance that materially changes decisions or execution. Prefer one sharp rule
or representative example over exhaustive explanation. Do not duplicate
upstream API documentation; encode workflows, heuristics, conventions,
integration guidance, and non-obvious pitfalls instead.

Write skill descriptions as routing rules for the model. Write manifest
descriptions for humans browsing the registry. Give every public package useful
keywords, a repository location, a homepage, an SPDX license expression, and
accurate `recommendedPacks` metadata.

For Effect v4 work, inspect current public Effect v4 source, tests, and examples
before documenting an API. Keep guidance specific to v4 and do not carry
forward Effect v3 conventions.

## Review and publishing gate

Before committing or publishing:

1. Inspect the complete diff, untracked files, generated files, and symlink
   targets.
2. Audit every changed package for cross-extension references. For each other
   extension name, FQN, or canonical extension path in package content, prove
   that it is a direct sibling in a common pack and that the referencing package
   satisfies the rules above. Current workspace installation state is not
   evidence; an unexplained reference is a release blocker.
3. Run `scripts/check-public-safety.sh`.
4. Verify provenance, attribution, licenses, and synthetic examples manually;
   scanners cannot establish these properties.
5. Use `axm publish --preview --json` and confirm the exact package and
   dependency selection.
6. Bump every package whose published archive changes. Existing registry
   versions are immutable.

Publish public packages only from this repository. The private repository may
install them from the registry but must not retain a second workspace-authored
copy. Promote a formerly private extension through a clean, reviewed current
copy; do not import private Git history unless every commit has separately
passed the public gate.

If a secret is exposed, stop publishing and revoke or rotate it first. Removing
the file or rewriting Git history is secondary and does not undo copies,
clones, caches, or prior access.

## Field note subjects

| Subject | Mode | Scope | Target condition | Retire when |
| --- | --- | --- | --- | --- |
| axm-cli | survey | any session running `axm` | — | a target condition can be stated |

<!-- axm:start region=knowledge-base -->
## Knowledge Base

### @craigsmitham

| Bundle | Description |
| --- | --- |
| [docs](.axm/extensions/@craigsmitham/knowledge/docs/src/index.md) | Portable documentation craft: *-explainer + *-guide pairs for overall craft and each Diátaxis type, plus workflow remediation and quality theory |
| [field-notes](.axm/extensions/@craigsmitham/knowledge/field-notes/src/index.md) | Observing work in progress and converting it into durable improvement: work-as-imagined vs work-as-done, survey and target subjects, recurrence thresholds, and verified closure |
| [harness-engineering](.axm/extensions/@craigsmitham/knowledge/harness-engineering/src/index.md) | Harness and context engineering principles, domain profiles, elements, patterns, and practices for reliable agent systems |
| [workflow-automation](.axm/extensions/@craigsmitham/knowledge/workflow-automation/src/index.md) | Platform-agnostic understanding of workflow automation through a common model, vendor mappings, recurring patterns, and established integration and delivery practices |
<!-- axm:end region=knowledge-base -->
<!-- axm:start region=rules -->
<!-- axm:rule @craigsmitham/rules/field-notes@0.1.0 -->
## Field notes

Record how work actually goes, so recurring obstacles become durable
improvements instead of repeated friction.

Subjects under observation are declared in the `## Field note subjects` table in
this file. **If that section is missing or has no rows, this rule is inactive —
do nothing.**

Recording a field note is expected behavior, not an admission of failure. Notes
about your own confusion, retries, and improvised workarounds are the most
valuable kind.

### When to record

While doing ordinary work, if the work falls within a declared subject and any
of these hold, append one field note:

- What happened differed from what the instructions, docs, or command output led
  you to expect.
- You retried, guessed, or searched to get past something.
- You succeeded by improvising a step no document describes. Record these — an
  undocumented workaround that worked is a finding, not a non-event.
- A subject in `target` mode was blocked from its target condition.

Do not record your own typos, a restatement of a note you already wrote this
session, or speculation with no observed incident behind it.

### How to record

Write one new file per note. Never edit an existing note — a second occurrence
is a second file, and that recurrence is the signal.

Path: `field-notes/<subject>/<YYYY-MM-DD>-<key>.md`, where `<key>` is a short
kebab slug of surface and symptom. Use a different root if the subjects section
names one.

```markdown
---
subject: <subject key>
key: <slug>
date: <YYYY-MM-DD>
kind: gap | workaround | blocked
status: open
---

**Expected:** what should have happened, and what led you to expect it
**Actual:** what happened instead
**Gap:** why the two differed
**Suggests:** the smallest durable change that would close the gap

Evidence: commands run, exit codes, paths, quoted output.
```

Report a specific incident with observable detail. A general impression is not a
field note.

### Stay in the work

Log and continue. Do not investigate the note, fix what it describes, open an
issue, or discuss it beyond one short line at the end of your response.

Two exceptions:

- What you observed is a live correctness, data-loss, or security problem —
  raise it now rather than filing it.
- You are genuinely blocked on ambiguous architecture, data model, or
  destructive scope — stop and ask, naming the ambiguity in one sentence with
  two or three options.

To declare subjects, triage notes, or promote them into findings, use the
`field-notes` skill. Never do that work inline.
<!-- axm:end region=rules -->
