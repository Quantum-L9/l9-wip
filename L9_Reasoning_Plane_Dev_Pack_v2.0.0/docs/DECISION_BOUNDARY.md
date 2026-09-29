# Decision Boundary Analysis

## Cardinal question

> What could change the current decision?

Decision-boundary analysis combines:

- Formal feasibility thresholds;
- Probabilistic variables that can plausibly move;
- Numerical sensitivity to those variables.

Example result shape:

```text
Current selection: A

Decision flips if any declared boundary is crossed:
- contamination > threshold
- freight > threshold
- P(close) < threshold
- competing offer price > threshold
```

## Why it matters

A `DecisionBoundary` identifies what deserves:

- monitoring;
- research;
- enrichment;
- alerting;
- human attention;
- recalculation.

This is stronger than generic uncertainty reduction because it isolates *decision-relevant* uncertainty.

## Boundary law

A sensitivity threshold is not a forecast that the threshold will be crossed. Probabilistic Reasoning supplies that belief separately.
