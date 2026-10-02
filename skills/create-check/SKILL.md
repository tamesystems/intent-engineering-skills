---
name: create-check
description: Turn a mechanically expressible engineering invariant into the smallest deterministic repository-owned check that rejects violations. Use for lint rules, static checks, contract tests, generated-state checks, or tiny verification scripts.
---

# Create Check

Compile an engineering invariant into executable rejection. Prefer the repository's existing verification substrate and build the smallest check that proves the property.

Read `references/ratchets.md` and `references/mechanism-ladder.md`.

## Work

1. **State the invariant and counterexample.** Write one sentence describing what must hold and one minimal representative violation that must fail.
2. **Inspect existing mechanisms first.** Check compiler options, existing lint rules/plugins, restricted-import support, architecture tooling, test framework, package scripts, and repository-local checks. Reuse before inventing.
3. **Select the narrowest adequate mechanism.** Prefer compiler/type constraints, then existing static policy, then a small custom lint/check, then a deterministic test/script. Do not create a general policy framework for one invariant.
4. **Implement repository-owned enforcement.** Give diagnostics enough context to identify the invariant and preferred corrective path. Preserve local configuration and unrelated policy.
5. **Prove the check bites.** Run the clean check and observe PASS. Introduce the representative violation in an isolated fixture or safe temporary mutation and observe FAIL for the intended diagnostic. Revert and observe PASS again.
6. **Expose the command.** Ensure the check has a stable command or entry point. If it is not already part of the authoritative repository check, route to `wire-check` when the invariant is important enough to gate changes.

## Return

- **Invariant**
- **Mechanism**
- **Files/command**
- **Clean proof**
- **Negative proof**
- **Final proof**
- **Wiring status**
- **Known analysis limits**

## Failure signals

A check that only passes existing code, snapshots implementation trivia instead of the invariant, silently ignores relevant files, depends on agent cooperation, weakens types/tests to get green, or emits a diagnostic with no corrective path.

## Done when

The smallest adequate deterministic check exists in repository-owned machinery, a representative violation is observed failing for the intended reason, clean state passes again, and its execution path is explicit.
