---
id: 2026-08-24T184420Z-b6n8
subject: axm-cli-interactions
key: subagent-no-fallback-blocks-sync
observed_at: "2026-08-24T18:44:20Z"
session: sess-q9r4
kind: blocked
status: open
---

**Expected:** A portable subagent manifest with `fallback: none` should either remain materializable for hosts with native support or make the unsupported Zed projection visible during preview.
**Observed:** `axm sync --preview --json --non-interactive` reported one ready projection with no warning, but applying the same sync failed validation because Zed lacks native subagent support and fallback was none.
**Impact:** Workspace reconciliation failed once and required a manifest/prompt compatibility adjustment before validation could continue.
**Recovery:** Permit AXM's platform fallback while requiring the researcher prompt to reject same-context execution as blocked; reconciliation had not yet been retried when this note was captured.
**Detected by:** Failed `axm sync --json --non-interactive` result.
**Observed factors:** AXM version is 0.27.15; project agents include Zed; the subagent manifest explicitly set `fallback` to `none`; preview reported `warningCount: 0` and `errorCount: 0`.
**Hypothesis:** Sync preview does not run or surface the same target-capability validation as apply.
**Suggests:** Make sync preview report the Zed native-subagent incompatibility before apply.

Evidence: Preview reported the researcher step `ready`; apply returned `ok: false`, `errorCode: validation`, and `Subagent researcher requires native subagent support for zed because fallback is none`.
