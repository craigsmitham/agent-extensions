# Capture a field note

Write one new file per incident. Never edit an existing note: a second
occurrence is a second file, and that recurrence is the signal.

Use `field-notes/<subject>/<YYYY-MM-DD>-<key>.md`, where `<key>` is a short
kebab slug of the surface and symptom. Use a different root if the subjects
table names one.

```markdown
---
subject: <subject key>
key: <slug>
date: <YYYY-MM-DD>
kind: gap | workaround | blocked
status: open
---

**Expected:** what should have happened, and what led you to expect it
**Actual:** what happened instead
**Gap:** why the two differed
**Suggests:** the smallest durable change that would close the gap

Evidence: commands run, exit codes, paths, quoted output.
```

Report one specific incident with observable evidence. Do not substitute a
general impression.
