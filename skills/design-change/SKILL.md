---
name: design-change
description: Determine where an intended software change belongs, what should own it, which collaborators it may need, and the expected architectural blast radius. Use before realizing a consequential change when placement, ownership, or locality is not already obvious.
---

# Design Change

Make the intended change obvious and local before writing it. Architecture should reduce the contributor's search space, not merely describe the finished system.

## Work

1. **Start from the change, not the folder tree.** State the behavior or capability that must change and the governing intent/specification. Do not choose a module merely because its name resembles the request.
2. **Find the dominant unit of change.** Inspect domain language, nearby behavior, public APIs, dependency rules, tests, recent relevant changes, and existing ownership. Ask which design decision should be independently changeable. Prefer observed change patterns over aesthetic symmetry.
3. **Name the owner.** Identify the module/subsystem that gives the behavior meaning. Reuse an existing owner when one is coherent; do not create a new module to avoid making a placement decision.
4. **Identify the supported surface.** Determine the public operation/API the change should enter through and which implementation details should remain hidden. If the required capability does not exist, say whether extending the surface is part of the change.
5. **Map collaborators and boundaries.** Record dependencies the owner may legitimately use and architectural boundaries it should not cross. Distinguish visibility (who may access an implementation) from direction (who may depend on whom).
6. **Predict blast radius.** List the paths/modules expected to change and the important areas expected to remain untouched. Optimize for few ownership boundaries crossed, not merely few files.
7. **Challenge the placement.** Ask whether the proposed shape creates horizontal scattering, a shared/common sink, a shallow pass-through module, a speculative abstraction, or an unexpected cross-domain dependency. If consequential uncertainty remains, route to `investigate` or `design-module` rather than guessing.
8. **Make the hypothesis falsifiable.** Preserve the expected blast radius so `verify` can compare it with the actual diff. Unexpected movement is evidence to investigate, not automatically a violation.

## Return

- **Change**
- **Owner**
- **Supported surface**
- **Allowed collaborators**
- **Expected blast radius** — paths/modules likely to change
- **Expected containment** — important areas that should not need changes
- **Open design uncertainty**, if any

## Failure signals

Watch for choosing a technical layer instead of an owner, defaulting everything to `shared`/`utils`, creating a module because a directory would look tidy, prescribing vertical slices regardless of the system's real unit of change, counting files instead of boundaries, and treating the predicted blast radius as unquestionable architecture.

## Done when

An unfamiliar contributor has a defensible, evidence-backed answer to where the change belongs, how it enters the owning module, what it may depend on, and what architectural movement would be surprising enough to investigate during verification.
