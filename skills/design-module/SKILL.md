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

Evaluate the reader's burden on a representative operation and, when the capability is stateful, a representative transition. Compare the proposed design with the current or simplest credible alternative:

- **Tracing burden:** which calls, layers, and files must a reader follow to understand the behavior? Each hop should hide a meaningful decision or enforce a real boundary. Collapse forwarding-only indirection when it adds no such value; preserve useful security, runtime, and ownership boundaries. File count alone is not the criterion.
- **State burden:** which independent facts, flags, mirrored values, ordering rules, and lifecycle relationships must the reader hold simultaneously? Give coordinated transitions a clear owner, derive values when possible, and represent meaningful states with their required data. Splitting coupled state across helpers or hooks does not reduce the burden if callers still coordinate it.

Judge the design by what a caller or maintainer no longer needs to know. A justified boundary may add a hop or retain necessary complexity while reducing leaked knowledge, risk, or change scope. Avoid replacing a straightforward flow with a generic state-machine framework or another abstraction unless it demonstrably improves the overall tradeoff.

## Return

- **Module / capability**
- **Decision hidden**
- **Public surface**
- **Owned internals**
- **Reader burden** — representative trace and transition; knowledge eliminated and necessary complexity retained
- **Dependencies / seams**
- **Visibility and dependency direction**
- **Testing surface**
- **Enforcement opportunities**

## Failure signals

Watch for interface-per-class ceremony, one-line pass-through modules, giant barrels, speculative adapters, premature micro-packages, generic `shared` ownership, leaking persistence/provider types through the public API, and maximizing boundaries instead of the value of boundaries.

## Done when

The module has a small caller-oriented surface, coherent hidden responsibilities, justified seams, explicit visibility/direction, and a credible story for keeping likely future changes local. A representative trace and, when relevant, state transition show that the boundary improves the overall reader and change burden rather than merely redistributing code.
