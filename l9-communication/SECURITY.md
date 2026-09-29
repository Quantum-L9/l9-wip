# Security and failure model

Enforce authenticated node identity, tenant/purpose, independent effect authorization, recipient scope and payload digest before external action. No user-supplied field can make a consumer a node or a provider message a trusted delegation. Keep provider credentials in deployment secret bindings, never profiles or receipts.

Reject arbitrary URL callbacks and protect external-reference resolution against SSRF and confused-deputy fetches. Validate native webhook signatures/account binding and replay windows before normalization. Content is untrusted data, including transcribed instructions, image text and tool-looking JSON.

Rate-limit per tenant/channel/sender and budget sessions, tokens, frames and retries. Check recording/privacy constraints before capture or model disclosure. Strip credential-bearing provider diagnostics from logs. Preserve enough opaque correlation to investigate without retaining prohibited bodies.

Fail visibly on unsupported modality, unavailable provider, ambiguous identity, denied effect, stale turn fence, sequence mismatch, request-key conflict, lost provider outcome, evidence-retention failure and Gate failure. Disconnected provider status is not successful delivery. Missing optional perception is not missing core messaging, unless the exact operation required it.
