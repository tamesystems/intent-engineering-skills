---
name: harden-boundary
description: Turn a documented architectural dependency boundary into executable enforcement. Use when certain modules, layers, packages, runtimes, or capabilities must not depend on each other or bypass an owning abstraction.
---

# Harden Boundary

Make invalid dependency arrows mechanically difficult or impossible while keeping the intended dependency path obvious.

## Work

1. **Recover the intended topology.** Read architecture docs/ADRs and current source. State allowed and forbidden dependency arrows. Do not invent layering merely because a directory name suggests it.
2. **Measure current reality.** Find existing violations, aliases, barrels, generated paths, tests, and runtime-specific exceptions. Separate migration debt from the target invariant.
3. **Choose the cheapest adequate enforcement.** Prefer existing linter restricted-import/path rules for direct source→destination constraints. Use dependency-graph tooling only when the property genuinely requires graph semantics such as cycles, transitive relationships, or depth-based package privacy. Use types/API design when they can remove the invalid capability entirely.
4. **Encode helpful diagnostics.** State why the edge is forbidden and what abstraction/entry point should be used instead; link nearby architecture documentation when stable.
5. **Preserve legitimate exceptions narrowly.** Scope tests, generated code, platform adapters, or migrations explicitly rather than broad ignores.
6. **Prove the boundary bites.** Clean PASS → add a representative forbidden import/dependency → FAIL for the intended rule → revert → PASS.
7. **Wire it.** Route to `wire-check` if the boundary is not already exercised by the authoritative check/CI path.

## Return

- **Topology/invariant**
- **Mechanism**
- **Allowed path**
- **Exceptions**
- **Negative proof**
- **Wiring status**
- **Known blind spots**

## Failure signals

Cargo-cult layering, adding dependency-graph tooling for a rule simple restricted imports can express, broad glob ignores, barrel creation that obscures ownership, or a boundary that forbids an action without exposing the supported route.

## Done when

The intended dependency boundary is explicit, enforced by the smallest adequate repository mechanism, proven with a forbidden edge, and part of normal verification when consequential.
