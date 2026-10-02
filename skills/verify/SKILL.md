---
name: verify
description: Demonstrate with evidence that a realized change conforms to its specification and preserves required invariants. Use after implementation and before claiming technical correctness or completion.
---

# Verify

Prove that we built the thing right. "Looks correct" is not evidence.

## Work

1. **Recover the proof obligations.** Use acceptance criteria and invariants; do not derive correctness solely from the implementation.
2. **Choose evidence proportional to risk.** Use the strongest practical mix of tests, type/static checks, architectural constraints, property tests, runtime inspection, logs/traces, benchmarks, security analysis, migration checks, screenshots, or manual inspection.
3. **Exercise changed behavior.** Map evidence to each material acceptance criterion.
4. **Exercise preservation.** Check required existing behavior and invariants, not just the happy path.
5. **Check architectural locality when it was predicted.** If `design-change` or the specification recorded an expected blast radius, compare it with the actual diff/dependency movement. Unexpected cross-boundary changes are discrepancies to explain or investigate, not automatic failures. Count ownership boundaries and leaked knowledge, not just files.
6. **Exercise meaningful failure paths.** Test edges implied by the design and risk, not arbitrary combinatorics.
7. **Inspect reality when possible.** For UI work inspect the UI; for APIs exercise the API; for migrations inspect resulting data; for operational behavior inspect runtime evidence.
8. **State limits honestly.** A passing test proves only what it tests. Identify material properties that remain unverified.

## Return

- **Result:** PASS / FAIL / PARTIAL
- **Evidence by criterion**
- **Invariants/regressions checked**
- **Architectural locality** — expected vs actual blast radius, when applicable
- **Failures**
- **Unverified properties**

## Failure signals

Watch for test-count theater, implementation-shaped tests that merely mirror the code, skipped regressions, ignoring surprising architectural blast radius, treating any cross-boundary edit as automatically wrong, uninspected UI/runtime behavior, and declaring success while required proof obligations lack evidence.

## Done when

Every required verification condition has credible evidence or is explicitly marked unverified; do not report PASS while a required condition lacks evidence.
