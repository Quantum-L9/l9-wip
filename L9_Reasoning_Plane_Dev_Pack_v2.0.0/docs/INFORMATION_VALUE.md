# Information Value Analysis

## Cardinal question

> Is more information worth acquiring before acting, and through which authorized acquisition action?

## Numerical method family

### EVPI
Upper bound on the expected value of resolving an uncertainty perfectly before the decision.

### EVSI
Expected value of a particular imperfect information source/test/action.

### Net VOI
Expected decision improvement minus acquisition, latency, risk, attention, privacy and opportunity costs, plus any separately justified Systemic Future Value of reusable information.

### Sequential VOI
Acquire cheap/high-value evidence first, update beliefs, then recompute remaining information value. Stop when no remaining LEARN action has positive marginal Strategic Value or a hard bound applies.

## Routing

Positive VOI selects a valuable `LEARN` candidate. It does not hard-code Research as executor. Candidate sources may include Research, Memory, File, Human, Test, API, Enrichment, Sensor, Database, or WAIT-for-evidence.

## Signal relation

Information gain measures belief change. VOI measures decision value. Expected Signal Value additionally accounts for signal capture/processing/propagation costs and future reusable value.
