## Field notes

Record how work actually goes, so recurring obstacles become durable
improvements instead of repeated friction. Notes about your own confusion,
retries, and improvised workarounds are the most valuable kind — recording one
is expected behavior, not an admission of failure.

Subjects under observation are declared in the `## Field note subjects` table in
this file. **If that section is missing or has no rows, this rule is inactive —
do nothing.**

### When to record

While doing work inside a declared subject, append one note if any of these
hold:

- What happened differed from what instructions, docs, or command output led you
  to expect.
- You retried, guessed, or searched to get past something.
- You improvised a step no document describes. An undocumented workaround that
  worked is a finding, not a non-event.
- A `target`-mode subject was blocked from its target condition.

Not notes: your own typos, a repeat of a note you already wrote this session, or
speculation with no observed incident behind it.

### How to record

One new file per note at `field-notes/<subject>/<YYYY-MM-DD>-<key>.md`, where
`<key>` is a short kebab slug of surface and symptom — use a different root if
the subjects section names one. Never edit an existing note: a second occurrence
is a second file, and that recurrence is the signal.

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

### Stay in the work

Log and continue. Do not investigate the note, fix what it describes, open an
issue, or discuss it beyond one short line at the end of your response. Two
exceptions: raise a live correctness, data-loss, or security problem now instead
of filing it; and stop to ask when genuinely blocked on ambiguous architecture,
data model, or destructive scope, naming the ambiguity in one sentence with two
or three options.

To declare subjects, triage notes, or promote them into findings, use the
`field-notes` skill. Never do that work inline.
