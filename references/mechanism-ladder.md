# Mechanism Ladder

When an engineering lesson should become durable, encode it in the strongest cheap mechanism that fits the repository.

Prefer, roughly:

1. **Unrepresentable state / API shape** — remove the invalid operation or make the valid construction the only construction.
2. **Compiler / type system** — make invalid programs fail to typecheck.
3. **Static policy** — lint, restricted imports, architecture rules, dependency checks, schema/config validation.
4. **Deterministic verification** — focused tests, scripts, generated-state checks, migration checks, contract checks.
5. **Runtime invariant / observability** — fail loudly or expose drift where static prevention is impossible.
6. **Canonical path** — generator, helper, wrapper, template, or API that makes the good path easier and more discoverable.
7. **Durable documentation** — reserve for judgment, rationale, and facts that cannot be usefully enforced.
8. **Agent instruction** — use sparingly, mainly as a navigation pointer or for irreducible process constraints.

The ordering is not absolute. Choose the strongest mechanism whose maintenance cost is justified by recurrence, consequence, and confidence in the invariant. Do not build a framework to prevent a trivial one-off.

## Prevention before detection

Prefer preventing a bad state to detecting it later. Prefer deterministic detection to a review instruction. Prefer a canonical good path alongside a prohibition so contributors are not left to guess how to comply.

## Prove the ratchet bites

A new or changed mechanical guardrail is not proven merely because the clean repository passes. Where safe and practical, demonstrate all three states:

1. **clean → PASS**
2. **representative forbidden mutation → FAIL for the intended reason**
3. **mutation reverted → PASS**

Use an isolated fixture or temporary working-tree mutation when modifying production source would be unsafe. The negative proof must exercise the same command contributors and CI rely on, or explicitly prove the lower-level check before `wire-check` makes it authoritative.

## Diagnostics are micro-documentation

A mechanical failure should identify the invariant and the preferred path when possible. Prefer:

> HTTP handlers must not import persistence implementations. Depend on the application repository capability. See `docs/architecture.md#persistence`.

over:

> restricted import

## Escape hatches

Necessary exceptions should be visible, narrow, and justified. Treat broad ignores, disabled rules, `@ts-ignore`, `@ts-nocheck`, skipped/focused tests, unchecked assertions, and verification-config edits as possible bypasses to inspect rather than routine fixes.
