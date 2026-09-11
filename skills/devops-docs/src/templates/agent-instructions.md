# Operational documentation discovery pointer

Use this template during setup and maintenance to check and propose a concise
route from agent instructions to the operational corpus. It owns the shared
wording; proposals render it instead of maintaining another copy.

## Inspect and propose

1. Resolve the repository's canonical instruction source and effective scope,
   such as a root `AGENTS.md`, `CLAUDE.md`, or a source used to generate them.
   Follow existing imports, aliases, and managed-source conventions. Do not
   propose edits to generated regions or independent copies for each agent.
   If no source exists, propose the repository-level file supported by the
   active agent; name any unresolved host convention in the plan.
2. Look for equivalent guidance, not an exact text match. Check the operational
   use cases and all ten supported types, the adopted index target, its link
   resolution, and whether repository-wide work receives the pointer. Keep an
   adequate existing pointer; revise a partial or stale one without duplicating it.
3. Render `{{index_link}}` as a Markdown link to the adopted root's `index.md`,
   relative to the instruction file where the text will be read. At the
   repository root with default placement, use `[devops/index.md](devops/index.md)`.
   Account for the consuming location when a canonical source is projected.
   The index establishes actual record coverage; listing supported types does
   not require creating absent records or empty folders.
4. Under the proposal's **Related changes**, show the target source, action
   (add, revise, or retain), exact proposed text for an addition or revision,
   and reason. Include the intended index creation when setup has not created
   it yet. Identify edits outside a narrow requested scope as dependent work.

## Pointer text

```text
Consult {{index_link}} for operational context during onboarding, planning, design, development, review, deployment, operations, troubleshooting, and maintenance. It documents providers, services, teams, tools, environments, organizations, repositories, playbooks, runbooks, and measures.
```

## Apply and verify

During authorized authoring, add or revise the canonical source, preserve
unrelated instructions, and use its existing reconciliation mechanism where
needed. Verify the effective pointer from representative repository working
locations, resolve its link to the created or retained index, and check that
equivalent guidance has not been duplicated. Keep this a discovery hint;
do not add profile rules or require loading the whole corpus for every task.
