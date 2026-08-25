---
id: 2026-08-25T000309Z-ddc867
subject: axm-cli-interactions
key: zed-role-fallback-repeats-sync
observed_at: "2026-08-25T00:03:09Z"
session: a29d2849
kind: gap
status: open
---

**Expected:** After `axm sync --json --non-interactive` reported the `researcher` subagent projection applied, `axm sync --preview --fail-on-change --json` would report a converged no-op workspace.
**Observed:** The apply exited `0` and reported one applied step while warning that `researcher` was degraded to a role skill for Zed. A later preview exited `1` and proposed the same `researcher` stale-projection step again.
**Impact:** The public extension workspace could not prove AXM convergence after one documented sync apply. The canonical authored package, publication, and other repository updates remained usable; elapsed delay was not measured.
**Recovery:** No repeated mutation or manual projection edit was attempted. Work continued using the authoritative canonical package and the retained reconciliation evidence; full machine-wide completion remained in progress.
**Detected by:** The post-update `axm sync --preview --fail-on-change --json` convergence gate.
**Observed factors:** AXM CLI version `0.27.17`; project agents include Zed; the repeated step names `workspace:@craigsmitham/subagents/researcher` version `0.0.1`; both results reported zero warnings and zero errors in their structured counts.
**Diagnostic evidence:** Apply outcome `applied`, exit `0`, applied count `1`; later outcome `reconciliation-required`, exit `1`, candidate `9a7bfc3065127b07783e59980e4e2031eacdb3a42e7bdf9d9eeba97e67d7f907`, ready count `1`, reason `stale-projection`.
**Hypothesis:** The Zed role-skill fallback materializes the artifact without persisting observation state that the next sync recognizes.

Evidence: The complete apply and preview JSON documents and their separate NDJSON diagnostics were retained. The working tree showed no generated projection diff after the apply.
