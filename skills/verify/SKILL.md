---
name: verify
description: Demonstrate with evidence that a realized change conforms to its specification and preserves required invariants. Use after implementation and before claiming technical correctness or completion.
---

# Verify

Prove that we built the thing right. "Looks correct" is not evidence.

## Work

1. **Recover the proof obligations.** Use acceptance criteria and invariants; do not derive correctness solely from the implementation.
2. **Choose evidence proportional to risk.** Select the smallest sufficient evidence for each required criterion and material risk, using tests, type/static checks, architectural constraints, runtime inspection, or other appropriate methods. Prefer existing checks and fixtures before creating a harness. Stronger evidence is warranted when it can change the correctness or release decision, not merely because it is available.
3. **Exercise changed behavior.** Map evidence to each material acceptance criterion.
4. **Exercise preservation.** Check required existing behavior and invariants, not just the happy path.
5. **Check architectural locality when it was predicted.** If `design-change` or the specification recorded an expected blast radius, compare it with the actual diff/dependency movement. Unexpected cross-boundary changes are discrepancies to explain or investigate, not automatic failures. Count ownership boundaries and leaked knowledge, not just files. When a design claims improved maintainability, compare a representative operation and, when relevant, state transition in the realized code with the prior design or agreed baseline. Check the overall tradeoff in tracing burden, state burden, leaked knowledge, risk, and change scope; neither burden must independently decrease when a justified boundary improves the whole. Tests passing or files shrinking cannot establish the claim.
6. **Exercise meaningful failure paths.** Test edges implied by the design and risk, not arbitrary combinatorics.
7. **Inspect reality when possible.** For UI work inspect the UI; for APIs exercise the API; for migrations inspect resulting data; for operational behavior inspect runtime evidence.
8. **State limits honestly.** A passing test proves only what it tests. Identify material properties that remain unverified.

Reuse successful evidence for unchanged behavior; repeat broader checks only when relevant changes, failures, environment differences, or authoritative repository requirements warrant them. Separate optional assurance from release-blocking criteria. A fixture/setup/probe failure establishes a measurement gap, not automatically a product defect: use a known-working control or a different observation when needed. Stop expanding verification when the required criteria and material risks have sufficient evidence.

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
