# Acceptance Criteria

The pack is architecture/implementation-ready only when all applicable criteria hold.

## Plane

- Formal, Probabilistic and Numerical semantic ownership is non-overlapping.
- consumers remain outside the plane;
- Gate/Gate_SDK remains transport owner;
- no super-node, hidden sibling orchestration, or fourth Strategic Interaction sibling exists;
- family/method/algorithm/primitive/provider vocabulary is explicit.

## Probabilistic

- exact/reference fixtures validate;
- no hidden priors or hidden evidence acquisition;
- BeliefState preserves distributional uncertainty;
- probability never becomes formal truth implicitly;
- contradictory/new evidence may reduce confidence without being treated as failure.

## Dynamic / strategic

- state and result revisions are time-bound;
- material new observations can invalidate/recompute affected decisions;
- ActorObservation and ActorModel are distinct;
- higher-order beliefs are explicitly depth-bounded;
- strategic lookahead is horizon/resource/VOC bounded;
- other-actor predictions are distributions, not certainties;
- game theory remains a method family beneath a composed Strategic Interaction pattern;
- no ML provider is required for the reference slice.

## Memory / Odoo

- Odoo remains authoritative for business events/facts in its domain;
- Graph Memory stores derived context/relationships/ActorModels without becoming truth authority;
- human-facing Negotiating Style is a lossy derived projection;
- dense inferred cognitive state is not mirrored into hidden Odoo columns;
- Odoo remains operational when Graph Memory is degraded/unavailable.

## Meta-decision substrate

- ACT/LEARN/COMPUTE/WAIT/STOP are candidate semantics, not executors;
- STOP can win a value comparison;
- hard security/authorization/protocol constraints dominate utility;
- positive VOI does not imply Research specifically;
- human attention can be valued as a scarce resource;
- resource allocation can return a vector/frontier;
- decision-boundary output identifies flip conditions without asserting they will occur.

## Strategic Value / Systemic Future Value

- StrategicValue arithmetic is reproducible;
- SystemicFutureValue is counterfactual, provenance-bound, and time-horizon bound;
- future work elimination is representable as a first-class value dimension;
- each underlying state delta is booked once;
- one-way/bilateral/closed-loop/mesh topologies can be represented;
- cycles are unrolled through time and terminate under convergence/horizon/budget;
- mesh attribution cannot manufacture more value than the underlying downstream state delta;
- predicted and realized value remain distinct.

## Signal bridge

- Signal Leverage remains external propagation owner;
- signal meaning is context/state dependent;
- redundant/correlated signals are not treated as independent evidence;
- strategically generated signals can use incentive-aware likelihoods;
- ExpectedSignalValue can be calculated without overriding mandatory safety/audit signal handling.

## Validation

- all JSON and YAML parse;
- every v2 JSON Schema passes Draft 2020-12 meta-validation;
- all mapped examples validate against public schemas;
- exact probabilistic reference arithmetic passes;
- StrategicValue/VOC/SignalValue arithmetic passes;
- SystemicFutureValue topology math passes;
- strategic interaction probability/depth/horizon tests pass;
- normalized allocation sums to 1;
- stale machine vocabulary scan passes;
- SHA manifest passes;
- ZIP integrity passes;
- no cache/macOS junk exists.
