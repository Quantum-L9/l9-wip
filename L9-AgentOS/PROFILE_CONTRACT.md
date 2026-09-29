# First-class AgentProfile contract

## Source, resolution, admission and activation
Authoring produces a profile source manifest and separately governed fragment files. Compilation resolves immutable fragments and produces an effective profile plus provenance. Admission verifies profile schema, source trust, requested capabilities and compatibility against deployment policy. Activation binds an admitted digest to a manifestation. These are distinct operations; compiling successfully is not permission to activate.

## Required section meanings
| Section | Required content | Forbidden shortcut |
|---|---|---|
| identity | Presentation role, disclosure and stable profile identity | Security credentials or self-issued node role |
| objectives | Allowed objective shapes, amendment and success rules | Unbounded objective expansion |
| work_items | Canonical WorkItem kinds, schemas and relations | Alternative shared work primitives |
| observations | Source/modality mappings, attribution and source restrictions | Treating all input as operator instruction |
| state | Allowed universal lifecycle refinements and payload constraints | Database-specific paths or direct writes |
| context | Context variants, deterministic mandatory reads and source precedence | LLM router omitting required authority evidence |
| memory | Candidate classes, privacy/purpose/consent, retention and visibility requests | Profile granting cross-subject access |
| autonomy | Triggers, attempt policies, escalation, constraints, no-op and stop rules | Arbitrary Python/eval or implicit effect permission |
| capabilities | Requested action references and schemas | Worker URLs or provider credentials |
| interaction | Audience/party/channel constraints and presentation policies | Permission inferred from a contact name |
| delegation | Scope attenuation, limits, expiry and parent/child semantics | Child widening parent authority |
| projections | Human/domain renderings of canonical objects | New persistence owners or runtime type forks |
| governance | Applicable rules, authority refs, approvals and safe defaults | Overriding platform law |

All manifestations have the same structural section set. Contents vary. Disabled capabilities are explicit; omitted safety sections are not permissive defaults. Conditional capabilities such as voice or human-service procurement are referenced, not reimplemented in the profile.

## Deterministic compilation
Resolve sources from an admitted local/package catalog using immutable refs. Validate every source digest before parsing. Disallow cycles, network-fetch side effects, duplicate conflicting definitions and mutable latest aliases. Normalize canonical JSON according to the chosen owner algorithm. For set-valued fields sort deterministically; for ordered procedures preserve order. Canonicalization must not silently reorder semantically ordered content.

Compose defaults under monotonic policy: capability intersection and minimum applicable budget/expiry; explicit deny wins; incompatible mandatory requirements fail compilation rather than last-wins merge. Distinguish declarative suggestions from normative constraints. Preserve provenance per resolved section and the complete source manifest digest.

Resolve subordinate Context/Memory/State contract refs by owner/version; do not copy their schemas into every cartridge. The profile's digest excludes deployment secrets, runtime timestamps, mutable cache paths and generated instance IDs. It includes all fields that change behavior. A runtime binding records the compiler build identity separately so reproducibility can be verified.

## Lifecycle and changes
Candidate -> compiled -> reviewed/admitted -> active -> retired is the profile artifact lifecycle proposal. Active Work Items are pinned to a digest. A new active profile version applies only to new work unless an explicit rebind operation migrates the Work Item, reruns required checks and records evidence. Emergency revocation blocks new attempts immediately; old context/approval receipts cannot preserve revoked authority.

## Extensibility without a hidden monolith
A new domain should add profile fragments, schemas, translation bindings, projections and fixtures only. Generic core changes require a demonstrated missing universal primitive and architecture review. Heavy new domain behavior goes to a separately owned capability, not a profile-executed plugin with unrestricted network/database access. Avoid a universal Turing-complete policy language.

## Cartridge conformance
The included commercial, assistance, technical and human-services examples are synthetic profile-source specimens, not product deployments. They share identical component keys and WorkItem shape. Their policy differences are explicit sample values. A fifth unseen synthetic profile must pass the same compile and state/context/memory interfaces with no runtime branches.


## v1.1 optional capability behavior
CommunicationBehavior and ReasoningBehavior are declarative profile components under this repo's schema ownership. They select permitted behavior, context/law requirements and presentation, not direct provider endpoints, secrets or credentials. Missing components mean the manifestation does not request that capability. Formal semantics constrain adapter compatibility; they are not a user-controlled provider selector. Communication execution composition is resolved by the Communication owner from admitted capability requirements.

Adding these components does not change the AgentProfile invariant: the compiled profile is the complete declarative manifestation, not a single config file. Live policy and authorization can narrow its permitted requests. No profile may activate a roadmap-only adapter.
