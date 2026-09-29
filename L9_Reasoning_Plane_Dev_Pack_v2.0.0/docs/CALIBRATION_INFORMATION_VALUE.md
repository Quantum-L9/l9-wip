# Calibration, Information Gain, Information Value, and Computation Value

## Calibration boundary

Calibration is not another reasoning sibling. Consumers decide which outcomes are relevant to which model/parameter. Probabilistic Reasoning performs mathematical belief updates; Numerical Reasoning may compare predicted and realized value for model calibration.

## Information gain

Probabilistic question: how much did admitted evidence change belief?

## Information value

Numerical + consumer question: would acquiring evidence improve decision utility enough to justify acquisition/latency/risk/attention cost, including any non-overlapping future reusable value?

Methods: EVPI, EVSI, Net VOI, Sequential VOI.

## Computation value

Would another bounded inference/solver/lookahead step improve the eventual decision enough to justify compute, latency, opportunity and risk cost?

VOC is the semantic stop mechanism for optional deeper belief depth and longer strategic lookahead, subject to hard ceilings.

## Outcome calibration

A realized transaction, rejection, counter, walk-away, delay, claim or revealed hidden state becomes new evidence. It may reinforce or contradict the previous ActorModel/BeliefState; calibration must permit certainty to decrease.
