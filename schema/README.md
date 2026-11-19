# Shared evidence schema

The [v1 schema](evidence-bundle-v1.schema.json) defines the bundle envelope for observations, assessments, and coverage. Producer-specific observation values can evolve independently of the envelope.

The [Ingress fixture](fixtures/ingress.json) records a network filter. The [Origin fixture](fixtures/origin.json) cites that observation and records the missing edge identity input. The source locator is illustrative.

Validate each bundle against the schema at import and export. When combining bundles, additionally check that bundle IDs are unique, record IDs are unique within each bundle, references resolve, and referenced bundles share the same project and environment. Preserve unresolved references when a required bundle has yet to be supplied and report the gap.

The v1 structure is implemented. **Workspace metadata, structured snapshot provenance, and coverage-ledger history** are design extensions.[^extensions]

See the [Pensys glossary](../research/glossary.md) for the distinction between coverage, readiness, and assessment.

See [Schema patterns from Trace and security-audit-skill](../research/_tools/schema/README.md).

[^extensions]: See the [suite design](../research/06-tool-boundaries-and-evidence.md#schema) for the target contract. Cross-bundle checks belong in the planned [Evidence Validate command](../research/_tools/evidence-validate/README.md).
