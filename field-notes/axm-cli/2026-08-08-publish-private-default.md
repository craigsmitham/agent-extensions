---
subject: axm-cli
key: publish-private-default
date: 2026-08-08
kind: gap
status: open
---

**Expected:** `axm publish --authored --owner @craigsmitham --on-existing verify --yes --json` would publish this public workspace's selected extensions so anonymous registry clients could install them.
**Actual:** The command reported successful publications, but anonymous registry requests returned `404`; a dependent pack then failed validation because its dependencies were not public and installable.
**Gap:** The publish result did not report the resulting visibility, and the multi-extension command offered no initial-visibility flag, so successful output did not reveal that the releases were non-public.
**Suggests:** Make visibility explicit in publish previews/results and provide a supported CLI operation for inspecting or changing extension visibility.

Evidence: the publish command reported success for five extensions; anonymous `GET /v1/extensions/@craigsmitham/<type>/<name>` requests returned HTTP `404`; `axm packs publish field-notes --include-dependencies --on-existing verify --yes --json` returned `Every pack dependency must resolve to a public, installable Registry version.`
