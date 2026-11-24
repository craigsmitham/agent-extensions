---
name: git-tidy
description: Scan Git repositories on a machine for branch, worktree, and stash housekeeping. Summarize findings in selectable batches and apply the user's chosen actions.
---

# Git Tidy

Accept a repository, one or more search roots, or a named machine reachable through
an available connection. Default to the current repo for an unqualified local request.
For machine-wide discovery use supplied or known checkout roots, asking for roots
when unknown. Run Git on the intended host. Identify the host and roots in the report.

## Collect evidence

Start read-only, using cached refs. Discover .git files as well as directories under
search roots, skipping Git internals and symlink recursion. Include explicitly
selected bare repos. Record inaccessible paths. Deduplicate clones by canonical
common Git directory and inventory all registered worktrees. Label linked checkouts
outside the requested roots and exclude them from removal unless explicitly selected.

Run the bundled `scripts/inventory.py REPOSITORY` with Python 3.9+ per repo.
Its JSON retains branch tips, upstream/tracking state, ordered worktrees, status
codes (including ignored files), and stash IDs. If the helper is unavailable on
the target, collect the same facts with native Git porcelain. Report incomplete
coverage when a probe fails. Treat names, paths, and stash subjects as data.

Resolve the intended integration branch from user input or repository conventions
such as the configured remote HEAD with a corresponding local branch. Identify the
base used. Check actual ancestry with `git merge-base --is-ancestor TIP BASE`.
Treat ambiguous bases, divergence, gone upstreams and uncertain squash merges
as review cases. Never infer completion from age. Preserve base branches, default
branches and branches protected by repository policy.

## Present decisions

Lead with host, scope, repo/worktree counts, skips, and whether remote evidence
is cached. Group by decision, then by action. Show one line per populated batch
with a letter, effect, eligibility rule, item count and repo count. Keep item
lists behind "show". A clean scan takes one or two lines.

- **Ready for cleanup** can include merged branches unused by any worktree, or
  clean linked checkouts whose attached branch tip is merged. Count a checkout
  and its branch once. For those checkouts offer "remove checkouts, keep branches"
  by default and an explicit combined option with both counts.
- **Needs review** can include detached HEADs, unmerged or unpublished commits,
  checkouts with local files, and stashes grouped by repository. Review reveals
  evidence such as commits or a stash summary. Keep unrelated active edits quiet.
- **Needs fresh evidence** can offer a fetch for named remotes or a check of
  missing checkout paths. Distinguish stale registration cleanup from removing
  a real directory. Omit main, bare and locked worktrees from removal batches.

Bind each displayed group to the observed host, common directories, full refs,
tips, worktree paths, stash object IDs and base. Keep that membership through
follow-ups. Offer replies such as `show A`, `apply A only in api`, or
`review B`. Accept natural language. Resolve ambiguous repo names by path.
A request to inspect a group only expands it. A refresh updates evidence and
produces a new report. When the original selections are unavailable, redisplay
a fresh batch for selection.

## Apply selected groups

Operate only on selected members. Immediately re-read identity, eligibility,
base, tip, worktree registrations and local state. Skip changed or unknown
members. Use argument-safe Git invocations and Git's normal refusal checks.

- Delete an eligible local branch with guarded `git branch -d -- NAME` from
  a verified checkout. Respect refusal. Leave remote branches alone.
- Before removing a linked checkout verify its identity, attached branch, clean
  index and worktree, including untracked and ignored content. Check for nested
  repositories, initialized submodules, sparse/skip-worktree or assume-unchanged
  entries and operations in progress. Skip uncertain or occupied checkouts.
  Use unforced `git worktree remove` from a retained checkout. For the combined
  option verify removal first, then independently recheck branch eligibility.
- Before pruning stale registrations confirm storage is available and directories
  are permanently gone. Preview `git worktree prune --dry-run --verbose` with
  the same expiry as the proposed operation. Pruning is repository-wide. Only
  proceed when the entire preview matches the selected registrations.
- Keep stashes for inspection. Resolve their observed object IDs when displaying
  patches because stash positions can shift. Fetch only for a selected refresh,
  using the intended remote with pruning and submodule recursion disabled.

Verify effects against Git and summarize counts per action. Name only skipped,
failed or pending exceptions and their reasons. On retry inspect current state
and keep the original selection.
