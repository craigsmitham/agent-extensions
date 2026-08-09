---
name: garden-context
description: >
  Evaluates and improves project or workspace context for software-engineering
  agents by mapping authority, discovery, scope, freshness, and ownership
  across instructions, specifications, documentation, skills, code, tests,
  tools, and runtime evidence. Use when asked to garden, audit, organize,
  prune, clean up, or improve repository, project, workspace, coding-agent,
  memory-bank, or AI context. Not for editing one known instruction file,
  ordinary documentation cleanup, or feature implementation.
---

# garden-context

Cultivate the context system used for project work. Start at the active
workspace, then expand only to project-scoped repositories, services, remote
workers, or external sources that evidence makes relevant.

## Operating contract

- Match the requested authority: inspect and report for an audit; edit when the
  user asks to garden, improve, organize, or clean up.
- Preserve existing work and use repository-owned tools for generated or
  managed surfaces.
- Distinguish evidence, inference, and unresolved policy. Never invent a source
  of truth, lifecycle, owner, or team convention.
- Prefer retirement, relocation, and stronger routing over destructive deletion.
- Do not create a standalone report file unless the user requests one.

## Load knowledge progressively

This skill is coupled to direct siblings in the harness-engineering pack.
Prefer `axm knowledge open harness-engineering <concept-id>` in project scope;
use `axm knowledge open --scope user harness-engineering <concept-id>` for a
user-scope installation. When a direct sibling path is necessary, resolve
`.axm/extensions/...` from the active AXM scope root: the project root for a
project installation or the user's home directory for a user installation.
Never route through an agent projection.

Read the governing practice first:

`axm knowledge open harness-engineering practices/context-gardening`

Open only the concepts whose signal is present:

| Signal | Concept ID |
| --- | --- |
| Context boundaries or selection are unclear | `foundations/context-engineering` |
| Intent, state, authority, capability, or feedback is illegible | `foundations/agent-legibility` |
| Initial context is noisy or deeper material is hard to find | `patterns/progressive-disclosure` |
| Local, repository, remote, or distributed coding environments interact | `domains/software-engineering/harnesses` |
| Always-on repository guidance is implicated | `domains/software-engineering/repository-instruction-files` |
| Reusable agent workflows are implicated | `elements/agent-skills` |
| Specifications, plans, or competing truth claims appear | `domains/software-engineering/practices/spec-driven-development` |
| A spec guides one change and then becomes historical | `domains/software-engineering/patterns/spec-first` |
| A spec persists beside human-edited implementation | `domains/software-engineering/patterns/spec-anchored` |
| Implementation is regenerated from the canonical spec | `domains/software-engineering/patterns/spec-as-source` |

`axm knowledge open` supplies the concept body but not its OKF frontmatter.
When a finding concerns provenance, `status`, `generated`, `verified`, or
`stale_after`, inspect that concept's canonical Markdown frontmatter from the
active AXM scope root after selecting it.

Treat these concepts as decision support, not project policy. When instruction
files are the chosen owner, use the pack's `improve-instructions` skill. If it
must be opened directly, resolve
`.axm/extensions/@craigsmitham/skills/improve-instructions/src/SKILL.md` from
the active AXM scope root.

## Workflow

### 1. Bound the garden

Identify the project outcome, active workspace, relevant roots and
environments, and two or three representative tasks. Infer reasonable examples
from commands, tests, entry points, and recent work when the user did not supply
them. Do not widen into user-global or external systems without evidence and
authority.

### 2. Inventory by route

Read applicable instruction files first. Use fast listings and targeted search
to locate likely specifications, plans, architecture material, skills, source,
tests, schemas, tool configuration, generated artifacts, and operational
evidence. Follow existing indexes before opening content in bulk.

For each relevant surface, record its scope, intended reader or consumer,
owner when known, lifecycle status, authority claim, discovery route, and
verification path. Useful lifecycle states include proposed, active,
historical, superseded, generated, and unknown.

### 3. Map authority

Separate the authorities for:

- intended behavior;
- implemented behavior;
- mechanically verified contracts;
- observed runtime behavior; and
- rationale and history.

For specifications, determine whether evidence supports spec-first,
spec-anchored, spec-as-source, or no explicit model. Also identify whether
changes flow back among artifacts, flow forward as new records, or begin in a
living specification. Surface ambiguity instead of resolving policy by guess.

### 4. Trace representative tasks

For each representative task, start from the context an agent actually receives
and follow the routes it can discover. Check whether:

- the initial surface exposes the right next decision;
- irrelevant context stays out;
- routes select the correct depth;
- destinations fulfill their advertised purpose;
- authority and freshness remain legible; and
- the agent can verify completion or recover from conflict.

Distinguish a bad destination from a route that was never discoverable or
selected.

### 5. Classify findings

Require concrete evidence and classify each finding as one of:

| Class | Meaning |
| --- | --- |
| Missing | Needed context has no durable owner |
| Undiscoverable | Useful context exists but likely entry points do not route to it |
| Wrong scope | Context arrives too broadly, too narrowly, or in the wrong environment |
| Stale | Context no longer matches its claimed authority or lifecycle |
| Redundant | Multiple surfaces repeat a claim without a reason to co-own it |
| Contradictory | Surfaces make incompatible claims without a precedence rule |
| Unverifiable | Guidance lacks a practical check or observable feedback path |
| Wrong owner | The concern belongs in a different harness element or system of record |

### 6. Choose cultivation moves

Choose the smallest move that addresses the evidence:

- **Plant** missing context with an explicit owner and scope.
- **Prune** irrelevant or redundant active context without erasing needed history.
- **Transplant** material to the surface that truthfully owns it.
- **Connect** missing routes, triggers, indexes, and links.
- **Promote** recurring procedure or mechanically decidable policy into a skill,
  tool, schema, test, or check.
- **Retire** superseded context and remove it from active selection.
- **Verify** discovery, authority, and behavior on representative work.

Broad invariants and routes belong in scoped instructions; reusable procedure
and judgment belong in skills; detailed durable facts belong in knowledge or
reference; executable contracts belong in code, tests, schemas, or checks; live
facts belong behind tools and observations; transient goals belong in task
state.

### 7. Propose or apply

For an audit, report findings and recommended moves without editing. For an
authorized improvement, make reviewable changes within scope and preserve
generated boundaries. Stop for direction when a change would establish new
project policy, choose between competing legitimate authorities, or delete
material whose historical value is unresolved.

### 8. Verify and report

Re-run relevant validators, link checks, searches, tests, or managed generators.
Trace the representative tasks again and compare discovery, scope, authority,
and verification with the original state.

Report:

1. garden scope and representative tasks;
2. authority and lifecycle map;
3. evidence-backed findings by class;
4. changes made or proposed cultivation moves;
5. validation evidence; and
6. unresolved policy decisions and intentionally deferred work.
