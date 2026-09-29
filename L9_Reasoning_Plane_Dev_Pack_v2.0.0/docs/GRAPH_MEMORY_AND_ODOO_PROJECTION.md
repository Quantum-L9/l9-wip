# Graph Memory and Odoo Projection Boundary

## Principle

Agents need denser contextual state than humans should be forced to curate or inspect. That does not justify turning Odoo into a hidden cognitive database.

## Odoo

Odoo remains authoritative for operational/commercial events and facts such as offers, prices, counters, acceptance/rejection, quantities, timestamps, transactions, claims, facilities, demand, capacity, and related business records.

A human-facing field such as **Negotiating Style** may expose a concise derived projection, for example:

> Price-sensitive; usually counters once; relationship-oriented; stated “final” price historically moves.

This field is a human aid, not canonical reasoning state.

Odoo MAY also carry opaque `actor_model_ref` and `actor_model_revision` identifiers when useful. It SHOULD NOT duplicate the dense inferred ActorModel into hidden columns merely to avoid a memory dependency.

## Graph Memory

Graph Memory may preserve:
- ActorObservations;
- actor↔context↔action↔outcome relations;
- temporal/seasonal patterns;
- StrategyHypotheses;
- versioned ActorModels;
- higher-order beliefs;
- provenance back to authoritative observations;
- supersession/calibration relationships.

Graph Memory is contextual memory, not truth authority. Durable facts still belong to their authoritative system.

## Availability degradation

If Graph Memory is unavailable, Odoo remains operational. Consumers may fall back to authoritative facts and explicitly degraded reasoning. They must not fabricate missing ActorModel state.
