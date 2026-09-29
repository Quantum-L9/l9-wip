# Target Filetree Additions — Meta Decision / Strategic Value

```text
l9-reasoning/
  contracts/v2/
    meta-action.schema.json
    strategic-value-assessment.schema.json
    systemic-future-value-projection.schema.json
    information-value-assessment.schema.json
    computation-value-assessment.schema.json
    resource-allocation-result.schema.json
    decision-boundary.schema.json

l9-numerical-reasoning/
  src/.../
    strategic_value/
      evaluator.py
      effect_ownership.py
      trajectory_value.py
      attribution.py
      topology_unroll.py
    information_value/
      evpi.py
      evsi.py
      sequential.py
    computation_value/
      voc.py
    allocation/
      optimizer.py
    decision_boundary/
      analyzer.py
  tests/
    test_strategic_value.py
    test_systemic_future_value.py
    test_topology_unroll.py
    test_value_of_information.py
    test_value_of_computation.py
    test_resource_allocation.py
```

No module named `future-value_score`, `future-value_projection`, or equivalent should exist in canonical v2 implementation.
