---
type: Playbook
title: How to design repository instruction files
description: Build a small, layered repository instruction surface that preserves software-engineering constraints and routes agents to deeper procedures and knowledge.
tags: [harness, instructions, agents.md, repositories, authoring, maintenance]
status: stable
sources:
  - id: agents-md
    resource: https://agents.md/
    title: AGENTS.md
  - id: openai-agents-md
    resource: https://learn.chatgpt.com/docs/agent-configuration/agents-md
    title: OpenAI — Custom instructions with AGENTS.md
generated:
  by: codex/gpt-5.6
  at: 2026-08-09T19:52:22Z
verified:
  - by: codex/gpt-5.6
    at: 2026-08-09T22:13:44Z
stale_after: 2027-02-09
---

# How to design repository instruction files

Use this guide to create or restructure repository instruction files such as
`AGENTS.md` or `CLAUDE.md`. It assumes the reader can inspect the repository,
run its normal checks, and start a fresh agent session. For the mental model,
read [Repository instruction files](../repository-instruction-files.md).

## Goal

Produce the smallest instruction surface that reliably establishes this
scope's invariants, working commands, non-obvious facts, and routes to deeper
material.

## Before you start

Identify:

- the harness and the filenames it actually discovers;
- the loading order, scope boundary, override behavior, and size limits;
- the root and any existing local instruction files;
- canonical READMEs, guides, skills, policies, and executable checks;
- observed agent failures or context bloat motivating the change.

Do not infer precedence from another product. Host behavior controls discovery;
the layering principles in this guide control content.

## Steps

### 1. Resolve the effective instruction chain

From each representative working directory, list the global, root, and local
files that the harness loads. Record which file wins when guidance conflicts
and whether an override replaces or merely extends a base file.

If the harness provides a command or session log that reports active
instructions, use it. A filesystem search alone cannot prove what entered
context.

### 2. Assign each scope an owner

Start with the root. Add a local instruction file only when that subtree has
repeatedly needed different commands, constraints, routing, or environment
facts. The open `AGENTS.md` convention also recommends nested files for
subprojects in large repositories.[^agents-md]

| Scope | Owns |
| --- | --- |
| Global or personal | Stable working agreements that apply across repositories |
| Repository root | Universal repository invariants and discovery routes |
| Package or surface | Differences unique to that subtree |
| Deeper directory | Exceptional local behavior that cannot live with its nearest owner |

Prefer inheritance. Do not copy parent content into children for reassurance.

### 3. Inventory existing content by job

Classify every section or candidate statement:

- invariant or hard constraint;
- working command;
- discovery route;
- non-obvious environment fact;
- procedure;
- explanation or reference;
- mechanically enforceable rule;
- duplication;
- stale or aspirational content.

This separates information that belongs in instructions from information that
merely happens to be there today.

### 4. Keep only high-value feedforward

Retain concise content the agent must know before it can choose its next action:

- genuine safety, compatibility, and ownership invariants;
- commands that differ from obvious or documented defaults;
- constraints agents repeatedly miss;
- environment characteristics the repository cannot reveal directly;
- routing triggers for important on-demand material.

State rules directly. Include the safe path or exception when omitting it would
leave the agent unable to act.

### 5. Move depth to its proper element

For each body that is too detailed for always-on context:

| Content | Destination | What remains in instructions |
| --- | --- | --- |
| Reusable procedure | Skill or how-to guide | Imperative trigger and link |
| Explanation or architecture | Knowledge or design document | Route when the topic becomes relevant |
| Exhaustive facts or options | Reference | Short lookup route |
| Deterministic rule | Linter, formatter, schema, or test | Command or remediation cue if needed |
| Task-specific goal | Issue, plan, or prompt | Nothing persistent |

Move first, verify the destination, then trim. Do not delete useful knowledge
without giving it an owner.

### 6. Write receivable routing triggers

Name the situation and required action. Put likely request vocabulary in the
row.

| Prefer | Avoid |
| --- | --- |
| Before adding or changing a database migration, read `docs/migrations.md`. | Database documentation |
| When editing generated API clients, change the schema and run `scripts/generate`. | Generated files |
| For release preparation, use the release skill. | Release information |

Links should resolve from the instruction file or use the path convention the
harness supports. Keep the route short; the destination owns the depth.

### 7. Promote mechanical rules into checks

For each imperative, ask whether software can decide compliance. If yes, prefer
an executable owner such as a formatter, linter, schema validator, structural
test, or CI check.

Keep prose only when it helps the agent choose or recover. An actionable failure
message should say what violated the rule, where, and how to verify the fix.

### 8. Resolve conflicts explicitly

Read the effective chain from broadest to narrowest scope. Remove accidental
contradictions and make intended overrides obvious. A child should replace a
parent rule only when the local difference is real and supported by the host's
precedence behavior.

Never rely on “the agent will probably infer which statement is newer.”

### 9. Review context weight and discovery coverage

After trimming, compare what was removed with what remains reachable:

- every universal invariant still appears once;
- every moved procedure or concept has a working route when needed;
- no root content belongs only to one package;
- no child restates a parent;
- no long table duplicates a source of truth;
- no index row was removed merely to improve line count.

If the routing index itself is large, group related triggers and sharpen their
boundaries before deleting coverage.

### 10. Verify in fresh runs

Start the harness from the repository root and from representative nested
directories. Ask it to report the instruction sources and summarize the
effective constraints. Then exercise tasks that should and should not trigger
the important routes.

Verify:

- expected files loaded in the expected order;
- local guidance applies only in its intended scope;
- links and commands resolve;
- moved procedures remain discoverable;
- critical instructions survive any host size limit;
- the agent can explain conflicts and safe paths correctly.

For Codex specifically, official documentation describes root-to-current-
directory layering and provides commands for checking active instructions.[^openai-agents-md]

### 11. Maintain from observed work

Treat an instruction miss as a classification problem:

- missing invariant → add concise feedforward;
- missed route → strengthen the trigger or index;
- missing procedure → create or repair a skill or guide;
- stale fact → update its nearest owner;
- repeated deterministic violation → add a check;
- local-only concern at root → push it down;
- bloated body → move depth and preserve discovery.

Rerun the smallest fresh-session test that demonstrates the corrected behavior.

## Minimal shape

Use the repository's established headings when they exist. A compact starting
shape is:

```markdown
# Agent instructions

## Invariants

- Preserve public API compatibility unless the task explicitly authorizes a break.

## Working commands

- Run `project-check` after changing source files.

## Routes

- Before changing a database migration, read `docs/migrations.md`.
```

Add a section only when it owns content that repeatedly changes agent behavior.

## Done when

- the host loads the intended files in the intended scopes;
- universal content appears once and local files contain only differences;
- procedures and explanations live on demand behind receivable routes;
- mechanically decidable rules have executable owners where practical;
- a fresh session can locate the right guidance and complete representative
  tasks without hidden human context.

## Related

- [Repository instruction files](../repository-instruction-files.md)
- [Instruction files](../../../elements/instruction-files.md)
- [How to design an agent skill](../../../guides/agent-skills.md)

[^openai-agents-md]: OpenAI — Custom instructions with AGENTS.md
[^agents-md]: AGENTS.md
