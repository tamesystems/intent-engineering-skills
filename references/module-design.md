# Module Design

A module is a **controlled dependency surface around a decision or capability that should be able to change independently**. A directory alone is not a module.

## Prefer depth

A useful module hides substantial coherent complexity behind a comparatively small caller-oriented interface. Measure depth qualitatively: how much implementation knowledge can change without forcing callers to change?

Good public operations use domain language and preserve useful evidence in their types. Avoid exposing orchestration steps, database records, provider SDK objects, or internal state merely because they already exist.

## Information hiding

Ask what design decision the module protects. Callers should know the supported capability, not how it is implemented. If an implementation choice changes, unrelated callers should usually remain stable.

## Seams

Create seams where they provide demonstrated leverage: environmental boundaries, meaningful volatility, testing through a real capability, or multiple implementations. Do not create an interface for every concrete class or wrap every third-party import. Speculative seams increase the public surface and can reduce locality.

## Visibility and direction

Treat these separately:

- **Visibility:** who is allowed to access this implementation or entry point?
- **Direction:** which conceptual layer/module is allowed to depend on which other one?

Prefer enforcement in this rough order when appropriate: language/build visibility → package/export surface → static dependency policy → naming/directory convention → documentation.

## Tests

Primary behavioral tests should use the same supported surface as real callers. Internal tests may prove valuable internal invariants, but do not expose helpers solely so tests can reach them.

## Deletion/change test

Imagine removing the module or replacing its hidden implementation. Does complexity remain concentrated behind the interface, or does equivalent ceremony simply move into every caller? A boundary that hides little and delegates everything may be shallow.
