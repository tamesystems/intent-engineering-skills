# Performance Evidence

Use this checklist when a performance number will drive a design, adoption, or release decision. Scale the rigor to the claim. A rough observation may need one labeled run; a comparative claim needs evidence that separates the alternatives from noise and measurement error.

## Define the claim

Write the claim before measuring. Name the operation, metric and unit, workload, data size, concurrency, environment, and whether the comparison concerns shipped defaults or tuned production-equivalent configurations. Do not silently turn a default-configuration comparison into a claim about the best achievable implementation.

## Establish measurement validity

1. **Read the harness.** Identify the timed region, setup and teardown outside it, warmup, sampling, aggregation, timeouts, and ignored failures.
2. **Prove the work happened.** Count successful completed operations and validate representative outputs. Confirm lazy results were consumed, asynchronous work was awaited, requests reached the intended service, and the optimizer could not discard the result.
3. **Account for failures.** Report errors, rejections, retries, and timeouts. A fast failure is not successful throughput; retry latency is not single-attempt latency.
4. **Make sides comparable.** Hold workload, data, versions, resources, build mode, and relevant configuration constant unless the changed variable is the stated subject of the comparison. Describe unavoidable differences.
5. **Control order and noise.** Check competing load. Interleave alternatives when drift, caches, thermal state, or warmup could favor one side. Record run order.

## Test the result

- Repeat enough times to characterize variation for the decision at hand. Report the per-run values or a suitable summary and range, not only the best run. Do not use an arbitrary run count as a substitute for inspecting variance.
- Treat an effect that is not distinguishable from observed variation as no measurable difference or inconclusive. Use a suitable statistical method when the decision is close or noisy.
- Check physical and logical bounds. Compare the claimed gain with the changed component's share of end-to-end time and with CPU, I/O, network, memory, or request-rate limits. An impossible result usually means cached, skipped, failed, or mis-timed work.
- Measure the representative end-to-end path alongside a microbenchmark when user impact is part of the claim. State the optimized component's share of the whole.
- Profile or instrument when the decision requires a causal explanation or when a surprising result needs diagnosis. Run intrusive profilers separately from reported timing runs.

## Report

Lead with one of: faster, slower, no measurable difference, or inconclusive. Include the metric and unit, workload, environment, successful-work and error counts, run count and variation, configuration basis, and material limitations. Name the limiter when established; label it unknown when the comparative result is still valid but causality was not resolved.
