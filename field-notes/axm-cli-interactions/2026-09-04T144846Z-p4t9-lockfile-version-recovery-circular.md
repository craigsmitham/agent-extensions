---
id: 2026-09-04T144846Z-p4t9
subject: axm-cli-interactions
key: lockfile-version-recovery-circular
observed_at: "2026-09-04T14:48:46Z"
session: 2ea7960b-9b16-49b3-af43-6c38406a731b
kind: workaround
status: open
---

**Expected:** `docs/publishing.md` opens release work with `axm upgrade`, then
expects `scripts/check-public-safety.sh` and `axm version` / `axm publish` to
run. When the upgraded CLI rejected the committed lockfile, its own first
machine-readable suggestion was `axm sync --preview`, so that command was
expected to produce a fresh resolution plan in the supported format.
**Observed:** AXM 0.28.5 rejected the tracked `axm-lock.yaml` with
`workspace-lockfile-version-unsupported` (observedVersion 6, supportedVersion 7,
direction "older"). Every workspace-scoped command failed identically:
`axm lint --json`, `axm version @craigsmitham/packs/software-engineering minor
--preview --json`, and `scripts/check-public-safety.sh`. `axm sync --preview
--json` — the suggested recovery — failed with the same error rather than
previewing, so the suggestion list could not be followed in the order given.
**Impact:** Blocked commit, push, and publish of an already-prepared
software-engineering release until the lockfile was replaced. Four extra
commands were spent discovering that the suggested recovery was unusable, and
the migration re-resolved four external `@agentxm` skills a minor each, widening
a documentation release into a dependency update. Elapsed time not measured.
**Recovery:** Applied the list's first suggestion instead of its first command:
copied `axm-lock.yaml` into a scratch directory, removed it from its
authoritative path, then ran `axm sync --preview --json` (ok=true, 2 ready
units, 0 blocked, 0 failed) followed by `axm sync`. The regenerated file
declared `lockfileVersion: 7` and `axm lint --json` then returned ok=true with 0
errors. The release task completed through commit and push.
**Detected by:** The documented release preflight command
`scripts/check-public-safety.sh` exited non-zero before reaching its custom
validators.
**Observed factors:** `axm upgrade` reported AXM already up to date at 0.28.5
(Homebrew), so no upgrade ran in this session; the lockfile was last committed
in `2ad01d4`. Only 0.28.5 was present in the Homebrew Cellar. `axm.json` lists
seven external `@agentxm` entries. `docs/publishing.md` does not mention a
lockfile format migration step.
**Diagnostic evidence:** tool `axm` 0.28.5 (Homebrew); error code `validation`,
title "Unsupported workspace lockfile version", problem code
`workspace-lockfile-version-unsupported`, cause tag `LockfileVersionUnsupported`;
affected artifact `axm-lock.yaml` observedVersion 6 / supportedVersion 7;
`scripts/check-public-safety.sh` exit status 1. Post-recovery sync candidateId
`ed0e92fb37efee92c6911558a5eb1914c3e8809ba49c940fd3e928bb5fbb27ab`,
holdbackCount 0, releaseAgeBypassCount 0. Retryability: the failing commands
were read-only and repeatable; no mutation was retried. Request or correlation
ID: not supplied.
**Hypothesis:** The suggestion list appears ordered as prose guidance rather
than an executable sequence — the prerequisite step is stated only in the first
prose-only suggestion, while the two commands beneath it both require that step
to have already been taken.
**Suggests:** A lockfile-version rejection could name the preserve-and-remove
step as the first *command*, or `axm sync` could accept an explicit
re-acceptance flag that migrates an older supported-direction lockfile in place.

Evidence: `axm-lock.yaml` before recovery declared `lockfileVersion: 6` on line
1; after recovery, line 1 declared `lockfileVersion: 7`. Re-resolution moved
`agent-skill-evaluator` 0.2.2 -> 0.3.0, `audit-agent-instructions` 0.1.6 ->
0.2.0, `author-agent-instructions` 0.1.6 -> 0.2.0, and `evaluate-agent-skill`
0.3.2 -> 0.4.0, leaving `agent-engineering` 0.11.0, `audit-agent-skill` 0.8.0,
and `author-agent-skill` 0.11.0 unchanged. The preserved version-6 file was kept
outside the repository for the duration of the session.
