import pytest

from l9_state.cursor import CursorClaims, CursorCodec, CursorError, filter_digest


def codec() -> CursorCodec:
    return CursorCodec(b"c" * 32)


def event_claims(*, consumer_ref: str, position: int) -> CursorClaims:
    c = codec()
    return CursorClaims(
        purpose="events",
        scope_binding=c.scope_binding("tenant-a", "scope.1"),
        consumer_binding=c.consumer_binding(consumer_ref),
        position=position,
    )


def test_cursor_round_trip_and_tamper_rejection():
    c = codec()
    token = c.issue(event_claims(consumer_ref="agent-a", position=7))
    claims = c.decode(token, purpose="events")
    assert claims.position == 7
    assert claims.consumer_binding == c.consumer_binding("agent-a")

    body, mac = token.split(".")
    tampered = ("A" if body[0] != "A" else "B") + body[1:] + "." + mac
    with pytest.raises(CursorError) as exc:
        c.decode(tampered, purpose="events")
    assert exc.value.code == "CURSOR_INVALID"


def test_cursor_purpose_is_bound_and_list_filter_digest_is_order_independent():
    c = codec()
    token = c.issue(
        CursorClaims(
            purpose="list",
            scope_binding=c.scope_binding("tenant-a", "scope.1"),
            consumer_binding=c.consumer_binding("agent-a"),
            position=0,
            filter_digest=filter_digest(schema_refs=("schema-a",), lifecycle="active"),
            resume_seq=3,
            last_object_id="object.1",
        )
    )
    with pytest.raises(CursorError):
        c.decode(token, purpose="events")

    assert filter_digest(schema_refs=("b", "a"), lifecycle="active") == filter_digest(
        schema_refs=("a", "b"), lifecycle="active"
    )


def test_maximum_v1_list_cursor_stays_within_public_bound():
    c = codec()
    token = c.issue(
        CursorClaims(
            purpose="list",
            scope_binding=c.scope_binding("t" * 200, "s" * 200),
            consumer_binding=c.consumer_binding("c" * 512),
            position=0,
            filter_digest=filter_digest(schema_refs=("schema-a", "schema-b"), lifecycle="active"),
            resume_seq=9_223_372_036_854_775_807,
            last_object_id="o" * 200,
        )
    )
    assert len(token) <= 512
