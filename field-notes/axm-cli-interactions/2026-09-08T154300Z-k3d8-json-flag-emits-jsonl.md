---
id: 2026-09-08T154300Z-k3d8
subject: axm-cli-interactions
key: json-flag-emits-jsonl
observed_at: "2026-09-08T15:43:00Z"
session: 01UzzaTW9g4F9GJ58suYN17H
kind: gap
status: open
---

**Expected:** `axm sync --preview --fail-on-change --json` to emit one JSON
document parseable by a single `json.load`, as the global flag help states
"--json, -j  Output machine-readable JSON" with no mention of a streaming or
line-delimited shape. `axm lint --json` had already parsed that way in this
same session.
**Observed:** The command emitted multiple concatenated JSON values. `json.load`
failed with `json.decoder.JSONDecodeError: Extra data: line 2 column 1 (char 154)`,
indicating a second document beginning at byte 154.
**Impact:** One extra command invocation. The convergence check was re-run
without `--json` and read from human-readable output instead, so the
structured result was not consumed. Task completed.
**Recovery:** Re-ran `axm sync --preview --fail-on-change` without `--json`
and read the text output ("Workspace materialization is up to date").
**Detected by:** Python `json.load` raising a decode error in the parsing
pipeline consuming the command's stdout.
**Observed factors:** axm 0.28.11; skill compatibility reported `compatible`
against declared range `>=0.28.0 <0.29.0`; workspace at
/Users/craig/Code/craigsmitham/agent-extensions; `axm lint --json` in the same
session parsed as a single document.
**Diagnostic evidence:** tool version 0.28.11; command surface
`axm sync --preview --fail-on-change --json`; error class
`json.decoder.JSONDecodeError`; error detail "Extra data: line 2 column 1
(char 154)"; process exit status not supplied, because the pipeline replaced it
with the formatter status.
**Hypothesis:** `sync` may stream per-stage JSON events while `lint` returns
a single summary document, so `--json` shape varies by command.
**Suggests:** Naming the emitted shape per command in `--json` help text, or
noting where output is line-delimited.
