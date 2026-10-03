---
name: validate
description: Determine whether a verified change actually satisfies the governing intent under representative conditions. Use when technical correctness alone cannot establish that the right outcome was achieved.
---

# Validate

Determine whether we built the right thing. Verification establishes conformance; validation establishes intended effect.

## Work

1. **Return to the intent.** Temporarily ignore implementation success and restate the real-world change this work was meant to produce.
2. **Define outcome evidence.** Identify observations that would support or falsify achievement of that intent. Do not substitute convenient implementation metrics without justification.
3. **Use representative conditions.** Prefer realistic actors, environments, data, workloads, workflows, and dependency behavior.
4. **Detect proxy success.** Deployment is not adoption; traffic is not demand; passing tests is not usability; feature completion is not problem resolution.
5. **Compare reality with intent.** Classify the outcome as satisfied, partially satisfied, not satisfied, or insufficient evidence.
6. **Expose discrepancy.** Describe the gap without rationalizing it. Route the discrepancy to grounding, specification, investigation, decision, or realization as appropriate.

For a UI added to an existing product, inspect the complete representative workflow inside its real layout and compare it with the product's established screens. Evaluate hierarchy, primary actions, density, typography, spacing, and relevant viewport behavior. An isolated component capture or passing interaction test does not establish visual integration. Record discrepancies or unavailable visual evidence explicitly; do not substitute functional coverage for usability or fit.

## Return

- **Governing intent**
- **Validation method**
- **Outcome evidence**
- **Result:** SATISFIED / PARTIAL / NOT SATISFIED / INSUFFICIENT EVIDENCE
- **Discrepancies**
- **Remaining uncertainty**
- **Next loop**, if needed

## Failure signals

Watch for validating the implementation instead of the intent, proxy metrics silently becoming goals, unrealistic test conditions, and declaring victory because the artifact shipped.

## Done when

There is sufficient representative evidence to assess the intended outcome, or the inability to obtain that evidence is itself explicit and actionable.
