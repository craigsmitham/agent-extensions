# JavaScript Temporal

Use this skill when a project already uses Temporal or you have chosen it for
a change. It helps select date and time types, check runtime support, and
convert values at API and storage boundaries.

```sh
axm install @craigsmitham/skills/temporal-dates
```

Try “$temporal-dates review how our Temporal-based API stores a customer's
birthday and the instant their account was created.” Expect a calendar date
for the birthday and an instant for the creation timestamp, with conversions
at the API boundary that preserve both meanings.
