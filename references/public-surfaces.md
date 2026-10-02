# Public Surfaces

Public surfaces make supported dependency paths explicit. They are one of the strongest ways to turn repository organization into architecture.

## Principle

Expose the capabilities consumers are meant to use; keep implementation details inaccessible where the ecosystem permits it.

Mechanisms vary by ecosystem: language/module visibility, build-target visibility, package export maps, workspace/package boundaries, TypeScript project/package entry points, or static import restrictions. Use the strongest existing mechanism that fits the repository before adding a new dependency-analysis tool.

## Good surface properties

A public surface should be:

- small enough that callers do not need implementation knowledge;
- explicit enough that discovery is easy;
- stable around likely implementation changes;
- typed in domain terms rather than infrastructure representation;
- compatible with the repository's dependency direction;
- testable through the same operations real callers use.

## Avoid

- unrestricted deep imports;
- giant barrels that make every internal symbol look supported;
- exporting helpers for test convenience;
- leaking ORM/provider types across ownership boundaries;
- `shared` packages whose only ownership rule is "used by more than one thing".

Reuse does not determine ownership. A concept remains owned by the domain that gives it meaning even when another domain consumes it.

## Diagnostics

When enforcing a public surface, errors should teach the repair path. Prefer "deep imports from X are forbidden; import Y from the package entry point" over a generic "restricted import" message.
