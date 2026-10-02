---
name: pave-path
description: Make a validated architectural path the easiest supported way to create or extend code by adding a generator, template, constructor, helper, public entry point, test harness, or other repository-owned affordance. Use when contributors repeatedly need to perform the same architectural operation or the correct path is harder than a known-invalid one.
---

# Pave Path

Make doing the right thing require less invention than doing the wrong thing. Constraints without an attractive supported path create thrashing; a pit of success needs both guidance and gravity.

## Work

1. **Name the recurring operation.** Examples: create a module, add a command, define a capability, add a migration, construct a domain value, register a route, or test a user-visible behavior.
2. **Confirm the architecture is validated.** The path must represent a real, repeated or consequential convention. If ownership/boundary design is unsettled, route to `design-change` or `design-module` first; do not fossilize a guess in a generator.
3. **Observe the best existing instance.** Recover the minimum structure, imports, verification, naming, and registration steps that make a native implementation correct.
4. **Choose the smallest affordance.** Prefer, depending on the problem: an obvious public API/constructor; a copyable local example; a typed helper; a generator/codemod; a package template; a verification harness. Do not build a framework when a function or tiny script removes the decision.
5. **Encode only stable decisions.** Generate/abstract the parts contributors should not have to reinvent. Leave product/domain choices explicit rather than filling them with fake defaults.
6. **Make output repository-native.** Generated code should use existing naming, package manager, formatting, tests, types, public surfaces, and check commands. It must not introduce a parallel architecture.
7. **Prove the path.** Use the affordance to create or exercise one representative instance, run the authoritative checks, and inspect the result. For generators/codemods, prefer idempotence or a safe refusal over destructive reruns.
8. **Pair with enforcement when justified.** If an easy forbidden path still competes with the paved path, route the validated invariant to `harden-boundary`, `create-check`, or `ratchet`.
9. **Explain discoverability.** Ensure an unfamiliar contributor can find the paved path from local repository context, diagnostics, scripts, or concise navigation documentation.

## Return

- **Operation paved**
- **Affordance created/improved**
- **Decisions encoded**
- **Decisions deliberately left open**
- **Proof it produces native valid work**
- **Remaining competing footguns**

## Failure signals

Watch for generating speculative architecture, giant scaffolds full of placeholders, a new tool where an existing API suffices, hiding meaningful product decisions behind defaults, generators that drift from the repository's checks, and prohibiting a path without making the replacement easy to discover.

## Done when

A representative contributor can perform the recurring operation through a discoverable repository-owned path that produces valid native structure with less architectural invention than doing it manually, and remaining cheap competing footguns are identified for ratcheting.
