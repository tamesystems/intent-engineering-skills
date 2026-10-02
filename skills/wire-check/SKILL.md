---
name: wire-check
description: Make important engineering checks authoritative by connecting existing lint, type, architecture, test, build, or generated-state checks to one normal contributor command and CI without duplicating policy.
---

# Wire Check

A guardrail that contributors and CI do not reliably execute is not an effective ratchet.

## Work

1. **Map verification entry points.** Inspect package/build scripts, CI workflows, hooks, task runners, monorepo affected commands, and documented contributor commands. Identify the command that should define repository health; reuse an existing `check`, `ci`, `validate`, or equivalent when possible.
2. **Find unwired or divergent checks.** Identify important checks that exist but are absent from the umbrella command or CI, and CI paths that run materially different verification from local contributors.
3. **Compose, do not duplicate.** Wire existing commands into one stable local entry point. Keep cheap feedback cheap; if the full suite is materially slow, preserve a fast `check` plus an exhaustive `check:all`/CI path rather than making agents avoid verification.
4. **Make CI authoritative.** Ensure merge-gating CI invokes the canonical exhaustive command or the same constituent checks. Hooks may improve latency but are not a substitute for CI because they are locally bypassable.
5. **Prove execution.** Demonstrate the umbrella command reaches the target check. When safe, use the check's known negative fixture/mutation and show the authoritative path fails because of it, then restore and pass.
6. **Document one entry point.** Keep agent/contributor guidance boring: name the authoritative command and any fast/full distinction. Do not copy every underlying rule into instructions.

## Return

- **Authoritative local command**
- **CI path**
- **Checks wired**
- **Fast/full split**, if any
- **Execution proof**
- **Remaining bypasses**

## Failure signals

Adding another parallel command instead of converging, relying only on pre-commit hooks, making the common check so slow it discourages iteration without justification, or claiming CI coverage without tracing the workflow to the actual command.

## Done when

Important checks have an explicit, stable contributor entry point, CI executes the required authoritative verification, and execution has been demonstrated rather than inferred from configuration alone.
