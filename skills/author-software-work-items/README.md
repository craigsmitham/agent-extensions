# Author software work items

Creates and revises evidence-rich software Change Specifications, Bugfix
Specifications, Defect Reports, Operational Incident Records, and the titles
and summaries that make them legible in a tracker. It also classifies each
material work item's possible effect on authoritative Requirements,
Architecture, and Evaluations without advancing the item into an unsupported
decision.

Use it to draft tracker-ready content or, when explicitly requested and the
host is available, to file or update the item. It preserves the boundary
between source intake, bounded proposed change, authorized correction,
accepted expectations, live incident response, and delivery work. It
faithfully carries supplied findings, architecture and code
sketches, implementation plans, and testing strategies without inventing or
approving missing design. It inventories originating evidence before synthesis
and checks persisted tracker readback so delayed handoffs do not lose material
source identifiers or links. It does not manage backlogs or implement the
change.

This skill is a non-standalone member of the Gen Stack pack because it composes
the work-item guides, Requirement-impact method, and canonical Requirement
authority model from one Gen Stack knowledge bundle.

## Revision 3.0.0

- Replaces request-centered change authoring with Change Specifications for
  bounded proposed or authorized System and Architecture changes.
- Adds Bugfix Specification routing for authorized correction of an identified
  Bug while preserving separate Defect Report provenance.
- Keeps unbounded requests as Signals or host-owned source records and refuses
  to invent a bounded change, accepted desired state, Design, or delivery
  authority from intake alone.
- Updates the behavioral evaluation source for change, corrective, defect,
  incident, routing, provenance, and authority boundaries.

This is a breaking behavioral revision from `2.0.2`. Consumers that used the
skill to produce request-intake work items should retain those records in their
source or feedback workflow and create a Change Specification only after a
candidate change has a recognizable boundary. Rollback is to `2.0.2`.

## Revision 2.0.2

- Updates the coupled work-item guide root to the top-level Gen Stack knowledge
  `0.5.1` path at `src/work-items/`; behavior and evaluation contracts are
  unchanged.

## Revision 2.0.1

- Routes work-item and Requirement-impact guidance through the subject-first
  Gen Stack knowledge `0.5.0` paths under `control-loop/` and
  `architecture/requirements/`.

## Revision 2.0.0

- Loads work-item, Requirement-impact, Architecture, and Evaluation guidance
  from Gen Stack knowledge `0.3.0`.
- Removes the retired software-engineering and software-architecture knowledge
  packages as runtime and evaluation support paths.
- Versions the evaluation suite with the consolidated support-path contract.

Revision `2.0.0` is a breaking packaging change from `1.0.0`; rollback is to
skill `1.0.0` with the former knowledge packages.

## Install

```bash
axm install @craigsmitham/packs/gen-stack
```

## Example

> Turn these reproduction steps and expected behavior into a defect report for
> our issue tracker. Keep the suspected cache cause clearly labeled as a
> hypothesis. Link the applicable Requirement and state whether this is
> possible non-satisfaction, changed intent, or an evidence gap.

## License

MIT. The Gen Stack knowledge bundle retains its separately declared license.
