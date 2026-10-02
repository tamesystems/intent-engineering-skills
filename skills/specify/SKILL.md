---
name: specify
description: Turn an intent, problem, or request into observable and falsifiable success conditions without prematurely choosing implementation. Use when desired outcomes, acceptance criteria, constraints, invariants, or the distinction between solution and objective are unclear.
---

# Specify

Define what must become true before deciding how to make it true.

## Work

1. **Recover the governing intent.** Ask what real-world outcome is desired. Preserve proposed solutions as context, but do not mistake them for the objective.
2. **Name affected actors and boundaries.** Identify who experiences the outcome, what systems participate, and what existing behavior must remain true.
3. **Make success observable.** Translate vague qualities into falsifiable conditions. Do not invent numerical targets without evidence.
4. **Separate constraints from preferences.** Record compatibility, security, architecture, performance, operational, migration, cost, or policy constraints only when justified.
5. **State invariants and non-goals.** Make preservation requirements and scope boundaries explicit.
6. **Define proof.** Distinguish verification (conformance to specification) from validation (satisfaction of intent).
7. **Expose ambiguity.** If an unanswered question materially changes the solution space, mark it for investigation or human clarification rather than fabricating precision.

## Return

- **Intent**
- **Desired outcomes**
- **Acceptance criteria**
- **Invariants**
- **Constraints**
- **Non-goals**
- **Verification conditions**
- **Validation conditions**
- **Open questions**

## Failure signals

Watch for solution-shaped requirements, untestable adjectives, proxy metrics becoming the objective, arbitrary targets, and requirements with no traceable reason to exist.

## Done when

A capable independent reviewer could determine whether a result satisfies the specification without asking what the author meant, and important criteria trace back to the governing intent or a real constraint.
