# First adapter: MongoDB; contract-independent implementation

## Selection
MongoDB is the first selected storage option because the workload is revisioned structured agent state with bounded documents and change notification. This does not make State a database product or LangGraph wrapper. The selected deployment must support transactions and durable recovery; a standalone development mongod does not satisfy the required replica-set proof.

## Private collection proposal
- `state_objects`: current record by `(tenant, namespace, object_id)`.
- `state_operations`: stable operation ID, request digest and immutable result receipt.
- `state_journal`: committed object revision, before/after digests and event identity.
- `state_outbox`: canonical transition intent and delivery settlement.
- `state_claims`: owner, expiry and monotonic fence, with indexes for renewal/acquisition.
- `state_consumer_cursors`: per-consumer partition watermark and acknowledgment identity.

These are private adapter details. They are not public namespace or collection parameters. Unique indexes enforce scope/object identity, scope/operation identity and object/revision identity. All query predicates include authenticated scope.

## One transaction unit
The adapter must expose one unit of work that atomically: checks expected revision/fence, writes the next state record, appends journal event, stores idempotent operation receipt and enqueues publication intent. Do not split StateStore and StateJournal into separately committed backends. The reference public port is one transactional service seam even if helper classes exist.

Read/write concern, primary read preference and retry behavior are explicitly configured and captured in the deployment receipt. Do not assume driver automatic retries establish exactly-once application effects. Retry commit ambiguity by querying the operation receipt under the original operation ID. The exact production topology/version/pins are gate-controlled in 04_stack, not guessed here.

## Change Stream role
Mongo Change Streams are an internal wake-up optimization over the canonical outbox/journal. They are database events, not L9 events. A raw resume token never enters a public State contract. If the token expires or a stream is invalidated, poll/replay the durable outbox by canonical watermark. `updateLookup` can reflect a later document version; therefore derive canonical transition contents inside the original transaction, not by treating a later lookup as the exact transition snapshot. See primary sources WEB-01 through WEB-03.

## Replacing Mongo
A new backend must pass the same conformance suite: atomic record/receipt/event commit, CAS, operation collision, fencing, cursor replay, tombstone, restart and scope. Migration exports provider-neutral records with revisions/operation identities preserved. There is one writer per scope during cutover. Changing backend does not change action names, WorkItem schemas, claims or event meaning.

## Prohibited shortcuts
No consumer Mongo driver, collection selection or query language. No optional evidence sink inside the transaction. No global transaction across State/Memory/Evidence. No unlimited embedded journal array growing forever inside a document. No TTL index used as a precise lease revocation clock.
