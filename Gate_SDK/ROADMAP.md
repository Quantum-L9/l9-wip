# Repository roadmap

Planned implementation only. PRs remain scoped to this repository; dependencies are evidence gates, not permission to edit another owner.

## SDK-01 - Mechanically separate authenticated application clients and nodes

Prerequisites: BASE-01

1. Inspect execute/root builder and current role authentication at Gate.
2. Define credential-bound client/node provenance mapping with Gate owner.
3. Preserve one transport, no destination parameter and no hidden execution replay.
4. Test both valid application and node paths from installed wheel.

**Acceptance:** Ordinary client credentials cannot gain node capability by changing provenance. Current valid node routes remain compatible.

**Required negatives:** Spoofed origin_kind=node fails with client identity. A profile node-mode string creates no trust.

## SDK-02 - Prove scoped response, child lineage and single-deadline contracts

Prerequisites: SDK-01

1. Exercise child request through existing packet derivation for node callers.
2. Verify response correlation, source/destination, scope, signatures and operation identity.
3. Expose only necessary ergonomic APIs; keep service-domain models out of SDK.
4. Document canonical error taxonomy and no automatic execution retry.

**Acceptance:** Every runtime capability call has one transport implementation and deadline. Normal responses to clients are legal but worker dispatch to clients is not.

**Required negatives:** Wrong-correlation or cross-tenant response rejected. Timeout yields one network execution attempt.

## SDK-03 - Prove bounded semantic turn transport and close only real gaps

Prerequisites: SDK-02, EXT-01

1. Inspect existing chunk/stream/session and child-lineage contracts.
2. Prove single-budget bounded semantic operations and correlated responses.
3. Where streaming is absent, require explicit unavailable/final-turn operation rather than alternate transport.
4. Add only owner-native minimal protocol changes when separately justified by current evidence.

**Acceptance:** One transport implementation and no peer connection escape. SDK remains domain-payload opaque.

**Required negatives:** Provider-specific turn/payload classes do not enter SDK core. A client cannot become a node by requesting a session.
