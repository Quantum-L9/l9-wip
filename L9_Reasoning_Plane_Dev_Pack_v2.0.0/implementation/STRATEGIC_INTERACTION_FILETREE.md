# Proposed Strategic Interaction Shared Surfaces

```text
l9-reasoning/
  contracts/v2/
    dynamic-state.schema.json
    state-transition.schema.json
    actor-observation.schema.json
    actor-model.schema.json
    strategy-hypothesis.schema.json
    higher-order-belief.schema.json
    response-model.schema.json
    strategic-state.schema.json
    strategic-outcome-path.schema.json
    strategic-interaction-request.schema.json
    strategic-interaction-result.schema.json
    strategic-lookahead-request.schema.json
    strategic-lookahead-result.schema.json
  strategic/
    adapter_contract.py          # pure contract/reference semantics only
    projection_contract.py
    receipt_join_contract.py

AgentOS / consumer runtime
  strategic_reasoning/
    adapter_wiring.py            # Gate calls / sequencing under runtime owner
    state_projection.py
    authorization.py

l9-probabilistic-reasoning/
  ... existing provider-neutral inference services ...

l9-numerical-reasoning/
  strategic/
    best_response.py
    lookahead.py
    exploitability.py
    bargaining.py
    disclosure_value.py
```

Repository/file names are proposed implementation shape and must be reconciled against live repo templates before birth.
