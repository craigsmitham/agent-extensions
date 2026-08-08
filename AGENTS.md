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

## Portability and package boundaries

- Reference files inside one skill relative to that skill's `src/` root.
- Use AXM's canonical cross-extension path only for another member of the same
  pack, and declare the pack in `recommendedPacks`.
- Public packs may depend only on public, active extensions.
- Do not reference agent projections such as `.agents/skills` or
  `.claude/skills` from canonical package content.
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
2. Run `scripts/check-public-safety.sh`.
3. Verify provenance, attribution, licenses, and synthetic examples manually;
   scanners cannot establish these properties.
4. Use `axm publish --preview --json` and confirm the exact package and
   dependency selection.
5. Bump every package whose published archive changes. Existing registry
   versions are immutable.

Publish public packages only from this repository. The private repository may
install them from the registry but must not retain a second workspace-authored
copy. Promote a formerly private extension through a clean, reviewed current
copy; do not import private Git history unless every commit has separately
passed the public gate.

If a secret is exposed, stop publishing and revoke or rotate it first. Removing
the file or rewriting Git history is secondary and does not undo copies,
clones, caches, or prior access.

<!-- axm:start region=knowledge-base -->
## Knowledge Base

### @craigsmitham

| Bundle | Description |
| --- | --- |
| [docs](.axm/extensions/@craigsmitham/knowledge/docs/src/index.md) | Portable documentation craft: *-explainer + *-guide pairs for overall craft and each Diátaxis type, plus workflow remediation and quality theory |
<!-- axm:end region=knowledge-base -->
