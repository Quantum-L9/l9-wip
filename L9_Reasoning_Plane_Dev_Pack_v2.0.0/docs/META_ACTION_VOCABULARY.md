# Meta-Action Vocabulary

## Purpose

A small common action vocabulary lets L9 evaluate business actions and cognitive actions using the same Reasoning Plane without hard-coding hundreds of branches.

## V2 kinds

- `ACT` — change the external/operational state.
- `LEARN` — acquire potentially decision-relevant evidence.
- `COMPUTE` — spend computation/reasoning resources without acquiring new external evidence.
- `WAIT` — intentionally defer while state/evidence may evolve.
- `STOP` — end optional work / retain current action or no-action baseline.

## Candidate generation boundary

The consumer/runtime generates and authorizes candidates. The plane evaluates them. The plane does not invent permissions or execute the winner.

## STOP law

STOP is first-class when continuation is optional. Hard safety/policy/validation bounds still terminate independently.
