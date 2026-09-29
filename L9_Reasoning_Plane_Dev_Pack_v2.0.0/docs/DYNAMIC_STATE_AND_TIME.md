# Dynamic State and Time

## Constitutional statement

The state of the world is time-indexed. A reasoning result is bound to the state revision against which it was produced. Material state change, new evidence, policy change, objective change, or another actor's action may invalidate all or part of the previous decision surface.

```text
State(t)
 + MyAction(t)
 + OtherActorAction(t)
 + NaturalEvolution(t→t+1)
 + Observation(t+1)
 -> State(t+1)
```

## State classes

- **VisibleState:** admitted facts observable to the consumer.
- **HiddenState:** latent facts/actor states represented probabilistically.
- **BeliefState:** probability distributions over hidden state.
- **StrategicState:** current state plus actor models, interaction history, action sets, objectives, and time horizon.

## Re-evaluation law

Each materially informative action or observation triggers a bounded re-evaluation of the affected decision. Implementations may incrementally reuse solver/inference state, but may not pretend the previous result remains semantically current when a material premise changed.

## Temporal semantics

Every material state/evidence item SHOULD carry applicable:
- observed/effective time;
- validity window;
- freshness/staleness semantics;
- supersession relation;
- temporal scope (durable, seasonal, episodic, event-specific).

A one-off event must not silently become a permanent actor trait.
