---
id: 2026-08-28T160056Z-h9v4
subject: axm-cli-interactions
key: host-invocation-frontmatter
observed_at: "2026-08-28T16:00:56Z"
session: codex-8f2c
kind: discrepancy
status: open
---

**Expected:** A host invocation field documented by current Claude Code and VS
Code Agent Skill profiles could be retained in canonical `SKILL.md` metadata or
represented through an AXM host projection.
**Observed:** `axm lint --json` rejected `disable-model-invocation` as an
unexpected field under the pinned Agent Skills standard, and no Claude or
Copilot skill-metadata sidecar was discoverable in the authored extension
sources.
**Impact:** The explicit-only contract can use the OpenAI sidecar and portable
routing language, but the authoring package cannot directly encode the native
Claude and Copilot control while remaining AXM-clean.
**Recovery:** Removed the unsupported shared frontmatter, retained
`agents/openai.yaml` for Codex, and kept the explicit-only boundary in the
portable description and workflow.
**Detected by:** AXM's structured lint findings after adding the documented
host field.
**Observed factors:** AXM CLI and bundled skill 0.28.1; ten affected skills;
first lint exit status 1; each finding used rule
`skill/frontmatter-standard-valid`.
**Diagnostic evidence:** Finding message `Unexpected frontmatter fields:
disable-model-invocation`; current official Claude Code and VS Code skill
references both document that exact field.
**Hypothesis:** AXM intentionally pins only portable Agent Skills metadata but
does not yet expose host-specific Claude or Copilot projection metadata.
**Suggests:** Add host-delta sidecars or projection transforms for invocation
controls that cannot live in the pinned portable frontmatter.

Evidence: The field was rejected consistently across all ten focused skills;
removing it restored the canonical portable shape for a subsequent clean lint.
