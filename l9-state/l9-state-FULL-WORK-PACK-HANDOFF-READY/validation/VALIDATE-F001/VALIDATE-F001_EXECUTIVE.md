# VALIDATE-F001 closure

`VALIDATE-F-001` is locally remediated.

The private hard-erase path now treats an active claim as coordination/fencing evidence rather than retention authority. An active claim requires the exact current `claim_id` and `fencing_token`; the externally authorized retention executor does not have to impersonate the claim holder. The private receipt continues to name the retention executor and the external retention authorization evidence.

Local executable evidence is clean: 73/73 source tests, 73/73 installed-wheel tests, 13/13 signed Gate actions from both source and wheel, 19/19 F001 checks, 20/20 Mongo handoff static checks, 43/43 REMED-01, 125/125 STATE-03, and 153/153 STATE-04. Public schema bytes are unchanged.

There are zero known code failures. Remaining work requires the Cursor environment: Ruff, mypy, and a real transaction-capable Mongo replica set with fault injection and restart/failover proof. Use `handoff/CURSOR/CURSOR_HANDOFF_CONTRACT.yaml` exactly. No merge, publish, deployment, admission, topology expansion, or retention-policy invention is authorized.
