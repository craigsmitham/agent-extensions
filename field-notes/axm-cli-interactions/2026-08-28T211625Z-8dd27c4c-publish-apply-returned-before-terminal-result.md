---
id: 2026-08-28T211625Z-8dd27c4c
subject: axm-cli-interactions
key: publish-apply-returned-before-terminal-result
observed_at: "2026-08-28T21:16:25Z"
session: 90e3397d
kind: workaround
status: open
---

**Expected:** The reviewed `axm publish` apply would return one terminal
`publish-result-v3` result covering the complete 17-package release closure.
**Observed:** The command observation returned after 30 seconds while AXM was
in `Applying Publish extensions`, without a terminal exit status or result.
The process later ended, and exact Registry readback found 13 candidate
versions present and four absent.
**Impact:** The terminal result was unavailable, so all 17 exact versions had
to be read back individually before a safe continuation could be selected.
**Recovery:** Do not replay blindly. Run a fresh preview with
`--on-existing verify`, require byte-identical verification of present versions
and pending status only for the four absent versions, then apply that admitted
selection.
**Detected by:** The incomplete retained command output, process inspection,
and exact-version Registry readback.
**Observed factors:** AXM CLI 0.28.1; explicit 17-package dependency closure;
`--on-existing verify`; initial observation window 30 seconds; no AXM process
remained when inspected.
**Diagnostic evidence:** The last retained phase was `Applying Publish
extensions`; no terminal exit status was retained. Registry readback found
`investigate 0.3.0`, `review 1.0.0`, `knowledge/gen-stack 2.0.0`, and
`packs/gen-stack 7.0.0` absent; the other 13 exact versions were present.
**Hypothesis:** The command observation boundary ended before the multi-package
apply returned its terminal result; the reason the apply stopped with four
versions absent is unknown.

Evidence: The original apply output ended at the apply phase, process
inspection later found no running AXM process, and exact Registry version lists
proved a 13-present/four-missing state.
