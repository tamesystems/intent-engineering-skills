# Dependency Graphs

Architecture is partly the set of dependency graphs the repository permits.

## Model

- **Node** — module, package, build target, or other ownership unit.
- **Edge** — one node depends on another.
- **Public edge** — dependency through the owner's supported surface.
- **Forbidden edge** — relationship the architecture rejects.
- **Visibility** — which nodes may create an edge to a target.
- **Direction** — which categories/scopes may depend on which others.
- **Cycle** — mutual reachability that may erase independent change boundaries.
- **Fan-in / fan-out** — signals about surface importance and coupling, not quality scores by themselves.

## Use the cheapest adequate enforcement

Simple source-to-destination restrictions often belong in the existing linter/import policy. Package exports or language/build visibility are stronger when available. Reachability, cycles, transitive graph properties, project tags, or complex package relationships may justify graph-aware tooling.

Do not install dependency-cruiser, Nx, Bazel, or another graph system merely to draw the architecture. Add machinery when an important validated invariant cannot be expressed cheaply with what the repository already has.

## Declared versus observed architecture

The dependency graph says what code currently depends on what. Git history can provide a different **change graph**: what repeatedly changes together. Persistent disagreement between declared boundaries and observed co-change is evidence to investigate.

Do not automatically rewrite boundaries from co-change statistics. Repeated co-change can reflect a missing capability, leaky API, migration, cross-cutting requirement, or genuinely incorrect decomposition.

## Pit-of-success target

A strong repository makes allowed edges discoverable, invalid edges fail quickly, and diagnostics point to the supported replacement. The graph becomes executable architectural documentation rather than a diagram that can drift silently.
