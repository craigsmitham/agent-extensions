---
id: 2026-08-24T184513Z-m3v7
subject: axm-cli-interactions
key: zed-role-fallback-never-converges
observed_at: "2026-08-24T18:45:13Z"
session: sess-q9r4
kind: blocked
status: open
---

**Expected:** After a successful `axm sync`, `axm sync --preview --fail-on-change` should report the workspace converged when canonical source and native projections are current.
**Observed:** Sync successfully projected researcher, including the documented Zed role-skill degradation, but the following convergence assertion again proposed researcher from `previous source=none` with reason `stale-projection`.
**Impact:** The final workspace convergence gate cannot pass for this subagent while Zed remains a configured target; native subagent projections and AXM lint remain current and clean.
**Recovery:** None within the original QRSPI work; retained the portable fallback with an explicit same-context blocked contract.
**Detected by:** `axm sync --preview --fail-on-change --json --non-interactive` immediately after successful sync.
**Observed factors:** AXM lint reports zero findings; `axm subagents list` reports Claude Code, Codex, Cursor, and GitHub Copilot CLI current and Zed unsupported; the Zed role-skill fallback exists under `.agents/skills/researcher`.
**Hypothesis:** The observer does not attribute the generated Zed role-skill polyfill to the canonical researcher subagent when deciding convergence.
**Suggests:** Teach sync observation to recognize its own Zed role-skill polyfill as the satisfied fallback projection.

Evidence: Successful sync returned `outcome: applied`; the immediate fail-on-change preview returned `outcome: reconciliation-required` and the same researcher stale-projection step.
