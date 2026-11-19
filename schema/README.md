# Shared evidence schema

The [v1 schema](evidence-bundle/v1/schema.json) defines the bundle envelope for observations, assessments, and coverage. Producer-specific observation values can evolve independently of the envelope.

The [Ingress fixture](evidence-bundle/v1/fixtures/ingress.json) records a network filter. The [Origin fixture](evidence-bundle/v1/fixtures/origin.json) cites that observation and records the missing edge identity input. The source locator is illustrative.

## Release layout

Store each major contract at `schema/<artifact>/v<major>/schema.json` with its fixtures alongside it. Select the canonical path through a supported-major lookup. An integer-valued JSON number such as `1.0` resolves to `v1` if accepted by the validator. Reject unsupported majors. The schema's `const` enforces that version.

The [current schema](evidence-bundle/schema.json) is a relative symlink to the active major's canonical file. Its version comes from that file. When releasing a new major, update the link and keep the old version directory. Use the current link when authoring a new bundle and the bundle's declared major when validating an existing one. Use the canonical version path directly if the checkout represents symlinks as plain text.

| Contract | Original release date |
| --- | --- |
| [Evidence bundle v1](evidence-bundle/v1/schema.json) | 2026-11-19 |

Keep released contracts immutable. Use a new major when existing readers could reject or misinterpret new bundles. V1 rejects unknown properties and uses closed status lists, so adding an optional property or a status can require a major bump. Documentation, fixtures, and validator tooling can evolve independently. Introduce an explicit revision only if readers need to select among multiple compatible contracts within one major.

## Validation

Validate each bundle against the schema at import and export. Require an available RFC 3339 timestamp checker and assert `date-time` formats explicitly. A malformed timestamp must fail even when the validator defaults to annotation-only format handling. When combining bundles, additionally check that bundle IDs are unique, record IDs are unique within each bundle, references resolve, and referenced bundles share the same project and environment. Preserve unresolved references when a required bundle has yet to be supplied and report the gap. Resolve v1 source locators from a known base supplied by the producer or workspace. Report unavailable sources explicitly. Bundle and record citations identify observations and assessments. V1 coverage rows have no record IDs.

The v1 structure is implemented. **Workspace metadata, structured snapshot provenance, and coverage-ledger history** are design extensions.[^extensions]

See the [Pensys glossary](../research/glossary.md) for the distinction between coverage, readiness, and assessment.

See [Schema patterns from Trace and security-audit-skill](../research/_tools/schema/README.md).

[^extensions]: See the [suite design](../research/06-tool-boundaries-and-evidence.md#schema) for the target contract. Cross-bundle checks belong in the planned [Evidence Validate command](../research/_tools/evidence-validate/README.md).
