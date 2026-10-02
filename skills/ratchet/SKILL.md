---
name: ratchet
description: Convert a recurring or consequential engineering failure, correction, or fragile convention into the strongest cheap durable repository mechanism. Use when a lesson should become harder or impossible to violate rather than another instruction.
---

# Ratchet

Turn engineering experience into accumulating executable constraints. This is a **meta-engineering skill**, not a ninth intent operator: it changes the environment future `realize` and `verify` work executes inside.

Read `references/ratchets.md` and `references/mechanism-ladder.md` before choosing a mechanism.

## Work

1. **Observe the evidence.** Name the concrete failure/correction and whether it is repeated, costly, consequential, or likely enough to justify permanent machinery. Do not invent a standard from taste alone.
2. **Generalize the failure class.** State the invariant independently of the observed file or incident. Distinguish a mechanical property from a judgment call.
3. **Interview the repository.** Find its existing compiler, linter, architecture checks, tests, generators, umbrella check command, CI, and local documentation. Prefer extending existing machinery over adding a new tool.
4. **Choose the strongest cheap mechanism.** Use the mechanism ladder. Prefer prevention over detection and detection over instruction. Before creating a custom mechanism, check whether the existing toolchain or a well-established compatible executable already implements the invariant.
5. **Keep the good path cheap.** Identify the intended alternative. If the new prohibition would leave contributors guessing, improve the canonical API/type/helper/generator/diagnostic or add a narrow navigation pointer.
6. **Route implementation.** Use `harden-boundary` for dependency topology, `create-check` for deterministic rejection, `wire-check` for authoritative execution, and `harden-check` for meaningful bypasses. A single small ratchet may be implemented directly when delegation would add ceremony.
7. **Prove and report.** A mechanical ratchet is not complete until a representative recurrence is rejected and the clean repository passes again. Important checks must be wired into the authoritative path.

## Return

- **Outcome:** RATCHETED / DOCUMENTED_JUDGMENT / NOT_WORTH_RATCHETING / BLOCKED
- **Observed lesson**
- **Generalized invariant**
- **Mechanism chosen** — and why stronger/cheaper alternatives were unsuitable
- **Installed change**
- **Positive path**
- **Negative proof**
- **Authoritative path** — where the check runs
- **Remaining exposure**

## Failure signals

Correct course if you add prose without testing stronger mechanisms, add a new dependency when existing tooling can express the rule, create a prohibition without a usable alternative, declare success because clean code passes without proving the rule bites, or overfit a permanent constraint to one harmless anomaly.

## Done when

The lesson has a justified durable disposition and, for a mechanical ratchet, repository-owned enforcement has been proven against a representative violation and appropriately wired into normal verification.
