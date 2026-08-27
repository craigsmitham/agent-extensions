---
id: 2026-08-27T012208Z-r8n3
subject: axm-cli-interactions
key: evaluator-codex-stdin
observed_at: "2026-08-27T01:22:08Z"
session: sess-k7m2
kind: gap
status: open
---

**Expected:** The enabled evaluator's bundled Codex adapter would complete one
case 70 authoring-smoke trial after source validation and preflight passed.
**Observed:** The trial adapter invoked Codex once, Codex exited `1`, and the
runner preserved the attempt as `harness-error` with an `Inconclusive`
selected-case conclusion.
**Impact:** No behavioral authoring-smoke evidence was produced for the revised
skill; deterministic suite validation remained available.
**Recovery:** Preserved the generated run as inconclusive and continued with
deterministic verification without retrying or treating the harness error as a
target failure.
**Detected by:** The evaluator returned exit status `1` and a completed run with
`outcomes.harness-error: 1`.
**Observed factors:** Runner `0.2.2`, Codex adapter `1.0.0`, Codex CLI `0.149.1`,
Node `v24.13.1`, model declaration `gpt-5.6`, one selected execution case, and
workspace-write sandbox. The Codex stderr log contained “Reading additional
input from stdin...” and no candidate response.
**Diagnostic evidence:** Run
`2026-08-27T01-21-39-825Z-2ccb12e7`; adapter exit `1`; signal `none`; timeout
`false`; output exceeded `false`; one invocation consumed; runner conclusion
`Inconclusive`.
**Hypothesis:** The bundled adapter's non-interactive stdin behavior is
incompatible with this Codex CLI version.
**Suggests:** Add a runner conformance case covering the adapter's prompt and
stdin invocation against supported Codex CLI versions.

Evidence: The preserved attempt records a `harness-error`, both mapped critical
assertions as `unknown`, and an empty trial adapter stdout log.
