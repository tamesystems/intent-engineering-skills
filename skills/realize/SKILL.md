---
name: realize
description: Safely transform the current system toward a decided state. Use when implementing code, configuration, migrations, infrastructure, integrations, or other concrete changes, while preserving invariants and keeping the result verifiable.
---

# Realize

Make the chosen change real while preserving system integrity. Code existing is not completion.

## Work

1. **Recover the contract.** Know the governing intent, relevant specification, decision, invariants, and intended verification. For a small task, these may be implicit and lightweight; do not invent ceremony.
2. **Minimize blast radius.** Make the smallest coherent change that satisfies the contract. Avoid unrelated cleanup.
3. **Respect architecture.** Use established boundaries and abstractions unless the decision explicitly changes them. Do not bypass constraints for convenience.
4. **Preserve invariants.** Protect required behavior, data integrity, security boundaries, compatibility, and operational safety.
5. **Work in inspectable increments.** Prefer states that can be independently understood and verified.
6. **Harden boundaries proportionally.** Validate untrusted inputs, handle external failures deliberately, bound side effects, and make retryable operations idempotent where relevant.
7. **Keep behavior observable.** Add the instrumentation necessary to operate, verify, or validate new behavior.
8. **Route invalid premises backward.** If implementation disproves the specification, investigation, or decision, stop forcing the implementation and return to the owning skill.

## Return

Produce the actual requested change, then summarize:

- **Changed**
- **Preserved**
- **Deviations** from the decision/specification
- **New risks or assumptions**
- **Verification entry points**

## Failure signals

Watch for scope creep, opportunistic refactors, bypassed architecture, hidden side effects, implementation that cannot be observed, and continuing after a premise has been disproven.

## Done when

A coherent candidate change exists, required invariants have not knowingly been violated, and the result is in a state that can be independently verified.
