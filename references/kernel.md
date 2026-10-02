# Intent Engineering Kernel

## Controller

- **intent** — the default entry point for non-trivial work. It is not a ninth operator. It recovers the governing intent, determines the smallest unresolved predicate, routes to the operator that owns it, tracks evidence-backed progress, re-routes when premises fail, and owns the overall task completion claim.

The controller should not duplicate operator methods. Each operator owns its own work and postcondition; `intent` owns transitions between them.

## The operators

- **ground** — establish the smallest evidence-backed model of current reality sufficient for the next move.
- **specify** — turn intent into observable success, constraints, invariants, and verification/validation conditions without prematurely choosing implementation.
- **investigate** — resolve a consequential uncertainty with discriminating evidence.
- **decide** — select a sufficient intervention from credible alternatives and preserve the rationale.
- **realize** — transform the system toward the decided state while preserving invariants and limiting blast radius.
- **verify** — demonstrate that the realized change conforms to the specification and preserves required behavior.
- **validate** — determine whether the verified result actually satisfies the governing intent under representative conditions.
- **learn** — turn surprise, failure, correction, or friction into a durable improvement to future work; recurring mechanical lessons may route into the ratchet skill family.

## Ratchets

Ratchets are **not additional cognitive operators**. They change the engineering environment future operators execute inside. `learn` may route recurring or consequential mechanical lessons into:

- **ratchet** — select the strongest cheap durable mechanism.
- **create-check** — compile an invariant into deterministic rejection.
- **wire-check** — make important checks authoritative locally and in CI.
- **harden-boundary** — enforce architectural dependency topology.
- **harden-check** — close cheap, consequential verification bypasses.

See [`ratchets.md`](ratchets.md) and [`mechanism-ladder.md`](mechanism-ladder.md).

## Not a waterfall

Choose the smallest sufficient path. Skills may transition backward when evidence invalidates prior work.

Examples:

- trivial correction: `realize → verify`
- unfamiliar bug: `ground → investigate → realize → verify → learn`
- consequential feature: `ground → specify → investigate? → decide → realize → verify → validate → learn?`

## Shared evidence discipline

Prefer, when applicable:

1. direct runtime observation / reproducible experiment
2. authoritative system of record / executable test
3. implementation and configuration
4. primary documentation and history
5. human testimony / secondary documentation
6. inference

The ordering is contextual, not absolute. Always distinguish observed facts, supported conclusions, assumptions, and unknowns.

## Shared stop rule

Do not maximize certainty. Stop a cognitive operation when additional work is unlikely to change the next consequential decision enough to justify its cost.

## Shared escalation rule

If a skill discovers that its premise is false, transition to the skill that owns the invalid premise rather than forcing progress:

- bad model of reality → `ground`
- ambiguous/wrong success condition → `specify`
- unresolved consequential uncertainty → `investigate`
- intervention no longer justified → `decide`
- implementation defect → `realize`
- insufficient proof of conformance → `verify`
- outcome misses intent → `validate` then route to the appropriate earlier operator
- recurring systemic weakness → `learn`

## Progress

Progress is the set of evidence-backed predicates already satisfied plus the smallest unresolved predicate controlling the next move. Do not use percent complete unless the task has a real measurable denominator. For multi-step, long-running, or resumable work, follow [`progress.md`](progress.md).

## Completion

Producing prose is never sufficient evidence of completion. Each operator defines a postcondition. If the postcondition cannot be met, report the blocker or remaining uncertainty explicitly.

An operator completing does not make the overall task complete. The `intent` controller owns the terminal task result and must distinguish implementation, verification, and validation claims.
