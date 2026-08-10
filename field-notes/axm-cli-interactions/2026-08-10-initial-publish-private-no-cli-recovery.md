---
subject: axm-cli-interactions
key: initial-publish-private-no-cli-recovery
date: 2026-08-10
kind: workaround
status: open
---

**Expected:** A first-time publish would either surface its chosen visibility in
preview and apply output or require an explicit visibility choice, with a CLI
path to correct that choice afterward.

**Actual:** Two first-time skill publishes succeeded as private packages without
reporting visibility. They were visible through authenticated `axm view` but not
installable from a fresh workspace. A later publish with `--visibility public`
failed because that flag is valid only for the initial publish, so the packages
had to be made public through the registry web UI.

**Gap:** The publish result concealed a consequential default, and the CLI had
no recovery path after the initial publication.

**Suggests:** Report effective visibility in preview and apply output, require
an explicit visibility choice for first publication, and provide an authenticated
command for changing package visibility.

Evidence: fresh-workspace install previews returned `not_found` for
`specify-codebase-change@0.0.2` and `plan-codebase-change@0.0.2`; their registry
management pages showed `Private`; after changing both to `Public`, the same
install previews returned one ready step and pack `0.0.4` published successfully.
