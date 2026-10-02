import json
from pathlib import Path

from l9_state.digests import canonical_bytes, sha256_jcs


def test_digest_vectors():
    data = json.loads((Path(__file__).parents[1] / "fixtures/DIGEST_VECTORS.json").read_text())
    for vector in data["vectors"]:
        value = (
            vector["input"]
            if vector["kind"] == "state_digest"
            else {
                "action": vector["action"],
                "domain_request": vector["domain_request_without_operation_id"],
            }
        )
        assert canonical_bytes(value).decode() == vector["canonical_utf8"]
        assert sha256_jcs(value) == vector["sha256"]
