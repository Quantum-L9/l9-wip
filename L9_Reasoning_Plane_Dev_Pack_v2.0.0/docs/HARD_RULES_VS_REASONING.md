# Hard Rules vs Reasoning

## Keep hard-coded/declarative hard rules for

- security and authorization;
- protocol invariants;
- schema/type validity;
- non-negotiable policy;
- regulatory or physical impossibility when authoritative;
- hard resource ceilings;
- state mutation permissions.

## Prefer the Reasoning Plane when the branch depends on

- uncertain consequences;
- competing costs and benefits;
- information value;
- computation value;
- timing and optionality;
- strategic response by other actors;
- dynamic state evolution;
- resource allocation;
- future systemic effects;
- decision-relevant signals.

The plane does not replace law/policy. It replaces brittle procedural branching where choice quality depends on reasoning.
