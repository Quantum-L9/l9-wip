# State cursor runtime contract

STATE-03 uses State-issued, provider-independent opaque cursors for list pagination,
scope-journal recovery, and object history pagination.

## Authority and isolation

A cursor is authenticated by State and binds the semantic identity needed for its
purpose. The serialized token contains compact digests, not raw tenant, scope,
consumer, or object identity. Provider-native resume tokens never leave adapters.

- list: tenant + scope + consumer + filter set + captured resume position + seek key
- events: tenant + scope + consumer + journal position
- history: tenant + scope + object + revision position

The binding digests are not authority. The HMAC proves that State issued the claims.
The request's validated transport context and State authorization checks remain the
authority for use.

## Runtime secret

`CursorCodec` requires at least 32 bytes of HMAC key material. Production runtimes
MUST provide a stable secret shared by the active State runtime instances for the
lifetime in which issued cursors are expected to remain usable. `CursorCodec.ephemeral()`
is only for local conformance/staging use and invalidates cursors on restart.

Key rotation must either preserve validation of still-supported cursors or deliberately
invalidate them and force cold resynchronization. Cursor validity must never depend on
MongoDB resume tokens or provider identity.

## Public size bound

The public contract limits cursors to 512 characters. State therefore serializes
fixed-width authenticated binding digests instead of raw maximum-length identities.
Issuance fails closed if a cursor would exceed the public bound.

## Cold resume

1. First `state.list` captures the current scope journal high-water before enumeration.
2. List pages use an object-ID seek cursor and preserve that exact captured high-water.
3. The first page also returns a consumer-bound event cursor positioned at the captured high-water.
4. After list enumeration, the consumer reads `state.events` from that captured cursor.
5. Any mutations committed after the capture are therefore visible in the journal catch-up path.
6. If retention has removed required journal coverage, State returns `resync_required` and the consumer restarts cold resume.

The list is intentionally not a globally transactional directory snapshot. The journal
closes the race window.

## Event pages and acknowledgments

Every successful event page returns `next_cursor`, even when the page is empty and
coverage is complete. That cursor is therefore always ackable.

`state.ack` is a durable mutation. Its OperationKey follows the same exact-retry and
collision laws as other State mutations. The consumer checkpoint and the immutable
ack receipt commit atomically. Checkpoints may advance or remain equal; they may never
regress.

A cursor authenticated for one consumer cannot be used by another consumer. Delegated
consumer use is allowed only when the State service receives an explicit authorization
for that consumer reference. Identity fields such as `on_behalf_of` are not themselves
interpreted as authorization by State.

## History coverage

`state.history` is event-backed and revision ordered for one StateKey. It reports:

- `complete` when the requested retained range reaches the current revision;
- `bounded` when another retained page remains;
- `history_unavailable` when retained history cannot support the requested starting point.

It never reports truncated retained history as complete.
