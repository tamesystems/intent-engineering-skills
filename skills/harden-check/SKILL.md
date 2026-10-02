---
name: harden-check
description: Attack an engineering guardrail for realistic bypasses and close the cheap escape hatches that would let contributors or agents make verification green without satisfying the invariant.
---

# Harden Check

A check is only as strong as its cheapest routine bypass. Adversarially inspect a guardrail without turning the repository into a prison.

## Work

1. **Name the protected invariant.** Read the check and its intended scope before attacking it.
2. **Enumerate realistic bypasses.** Depending on the stack, inspect suppressions/disable comments, `@ts-ignore`/`@ts-nocheck`, unsafe assertions, skipped/focused tests, ignored paths, mocks that erase the seam, config edits, alternate scripts, generated-file exclusions, or CI paths that omit the check.
3. **Prioritize cheap consequential bypasses.** Do not ban every escape hatch in existence. Close bypasses that are easy, likely, and capable of defeating the invariant without conspicuous review.
4. **Keep exceptions explicit.** When an escape hatch is legitimately necessary, require narrow scope and visible justification where practical rather than prohibiting all exceptions.
5. **Prove the hardening.** Demonstrate at least one previously plausible bypass is now rejected or made conspicuous, and that legitimate code still passes.
6. **Do not protect the checker from intentional governance.** Maintainers must still be able to deliberately change policy through review. The goal is to prevent accidental or opportunistic evasion, not make configuration immutable.

## Return

- **Invariant**
- **Bypasses examined**
- **Bypasses closed**
- **Legitimate exception path**
- **Proof**
- **Remaining exposure**

## Failure signals

Banning useful language features globally without evidence, making policy impossible to evolve, treating any config change as malicious, or adding more complexity than the protected invariant warrants.

## Done when

The consequential cheap bypasses are closed or made explicitly reviewable, the intended exception path remains usable, and the hardened guardrail is proven on representative cases.
