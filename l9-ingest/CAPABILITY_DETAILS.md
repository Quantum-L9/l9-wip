# Ingest processing contract

    Ingest is the first neutral place for sources requiring transformation. It is not mandatory for already typed State/Memory/Evidence requests. It performs source-processing coordination, not a global agent Work Item scheduler.

    ## Public actions
    `ingest.submit` accepts one bounded source operation. `ingest.sync` requests a source-revision reconciliation under an admitted profile. `ingest.reconcile` reports source/representation/delivery differences. `ingest.replay` resumes safe source processing and unsettled candidate delivery; it does not reexecute domain effects. `ingest.status` returns actual receipt/job state. No `ingest.search`, `ingest.context` or generic database write surface.

    ## Stage contract
| Stage | Input | Transform | Output | Possible effect | Failure |
| --- | --- | --- | --- | --- | --- |
| authorize | Authenticated source request, purpose and profile | Intersect requested use with grants, source access and profile policy | Admission/rejection receipt | None before admission | SOURCE_ACCESS_REFUSED; PROFILE_NOT_ADMITTED |
| capture | Source ref and bounded bytes/artifact | Verify immutable identity, size, digest and safe locator | Captured source ref and integrity receipt | Evidence upload/append through Gate if allowed | SOURCE_CHANGED; DIGEST_MISMATCH; LIMIT_EXCEEDED |
| normalize | Verified content and normalizer ref | Normalize allowed encoding/structure; redact under explicit policy | Normalized representation and source map | No canonical downstream truth change | UNSUPPORTED_ENCODING; REDACTION_FAILED |
| parse | Normalized content and source-kind parser | Produce structure-aware segments, preserving exact source ranges | Parsed units with typed locators | Local bounded computation | PARSER_FAILED; INVALID_SOURCE_RANGE |
| classify | Units plus declarative ingestion profile | Deterministic classes/eligibility; model proposals stay uncertain | Eligibility decisions and uncertainty | No downstream admission | CLASS_UNSUPPORTED; PURPOSE_FORBIDDEN |
| represent | Eligible source units and view contract | Produce deterministic text/views/chunks and optional embedding artifact | Representation candidates with transform/space identity | Optional budgeted model/provider call behind adapter | MODEL_UNAVAILABLE; SPACE_MISMATCH; BUDGET_EXCEEDED |
| extract | Eligible units and extraction contract | Emit independently governable assertions with provenance; no truth promotion | Memory candidates or explicit no-reusable-data | Optional bounded extraction call | NO_ASSERTIONS; EXTRACTION_UNCERTAIN |
| compile | Candidates and destination public contracts | Validate owner payload shape and source/operation identity | Per-destination immutable delivery intents | Persist job/outbox recovery state | DESTINATION_CONTRACT_MISMATCH |
| deliver | Admitted delivery intents | Request destination actions through Gate with stable keys | Per-destination actual owner receipts | Explicit requested owner mutations | REJECTED; QUARANTINED; UNAVAILABLE; OUTCOME_UNKNOWN |
| settle | Actual receipts or failures | Mark each output settled/pending/refused; expose replay needs | IngestReceipt and bounded remaining work | Job state only | PARTIAL; RECONCILIATION_REQUIRED |

    Each stage records input digest, transform/profile version, output digest and explicit status. A deterministic stage retry reuses the same identity. Model-backed stages record model/adapter identity, token/cost limit, observed usage and uncertainty; no seed/model claim is treated as determinism without proof.

    ## Source and job identity
    Source occurrence identity, immutable source revision, representation identity and processing operation identity are distinct. An event replay cannot create a second job accidentally. A new transform version legitimately creates a new representation without changing source truth. Same operation key/different source or profile rejects a collision.

    ## Fan-out semantics
    Evidence accepted plus Memory quarantined is PARTIAL, not complete. A pending artifact projection is not missing canonical memory and cannot be used to revoke a successful owner commit. Store per-destination request digest, idempotency key, attempt history, outcome and receipt ref. Retry only unresolved eligible outputs using the same identity. Permanent refusal is a terminal output with evidence, not something to evade through another namespace.

    ## Source kinds
    Generic profiles can describe structured events, authored artifacts, documents, conversation excerpts, multimodal derivatives and execution results. They are not hardcoded named-agent classes. Existing topology publications enter as already typed source bundles; Ingest must not invent a parallel repository/topology crawler to rediscover owner-issued facts.

    ## Model policy
    A source permitted for evidence retention is not automatically permitted for external inference, vector embedding or memory extraction. Check each use separately. Raw transcripts and bodies remain source evidence only where allowed; they are never directly installed as agent memory. A stricter manifestation policy can prohibit retention altogether.
