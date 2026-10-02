---
name: design-module
description: Design or reshape a module around an independently changing decision or capability, with a small supported surface and substantial hidden complexity. Use when ownership is clear but the module boundary, public API, internal responsibilities, or seams are not.
---

# Design Module

Create a deep change boundary: substantial coherent behavior behind a small supported surface. A module is not a folder; it is a controlled dependency surface around something that should be able to change independently.

## Work

1. **Name the decision/capability being hidden.** Explain what should be independently changeable and why callers should not need to know its implementation decisions.
2. **Recover real callers and changes.** Inspect current call sites, tests, adjacent modules, relevant history, and the intended change. Design for demonstrated needs; do not invent generic interfaces for hypothetical consumers.
3. **Design the smallest useful public surface.** Prefer operations in domain language that express what callers need, not wrappers exposing implementation steps. Keep public types and errors explicit enough to preserve evidence.
4. **Put complexity behind the surface.** Identify policies, workflows, persistence coordination, provider details, internal state, and helpers that the module owns and should hide.
5. **Choose seams only where they buy something.** Introduce an adapter/interface when there is a real environmental boundary, test seam, volatility, or multiple implementations. Do not wrap every library or create an interface merely because one could exist.
6. **Protect locality.** Keep behavior that changes together together. Avoid global horizontal layers that scatter one capability across controllers/services/repositories unless the system's dominant unit of change genuinely follows that pipeline.
7. **Define visibility and direction.** State which entry points are public, which internals are private, what the module may depend on, and who may depend on it. Prefer language/package/build visibility over naming conventions when available.
8. **Test through the supported surface.** Behavioral tests should primarily exercise the interface real callers use. Internal tests are allowed when they prove meaningful internal invariants, but testability alone is not a reason to leak helpers.
9. **Apply the deletion/change test.** If the module disappeared or its hidden implementation changed, would complexity remain contained behind its surface? If deleting the abstraction merely moves equivalent ceremony to callers, it may be shallow.
10. **Hand enforcement to ratchets.** Once the boundary is justified, use `pave-path` to make correct use easy and `harden-boundary`/`ratchet` to make invalid access difficult or impossible.

## Return

- **Module / capability**
- **Decision hidden**
- **Public surface**
- **Owned internals**
- **Dependencies / seams**
- **Visibility and dependency direction**
- **Testing surface**
- **Enforcement opportunities**

## Failure signals

Watch for interface-per-class ceremony, one-line pass-through modules, giant barrels, speculative adapters, premature micro-packages, generic `shared` ownership, leaking persistence/provider types through the public API, and maximizing boundaries instead of the value of boundaries.

## Done when

The module has a small caller-oriented surface, coherent hidden responsibilities, justified seams, explicit visibility/direction, and a credible story for keeping likely future changes local.
