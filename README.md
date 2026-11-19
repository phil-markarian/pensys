# analysis-pen-test

Pensys is the working name for a local security review suite for personal and team projects.

## Start here

1. [Project direction](research/01-initial-direction.md) explains what Pensys is for.
2. [Internet exposure](research/02-internet-exposure.md) separates visibility, reachability, and authorization.
3. [Ingress](research/03-ingress.md) maps how requests reach a service.
4. [Origin protection](research/04-origin-protection-controls.md) explains how backends restrict callers.
5. [Honeypot telemetry](research/05-distributed-honeypot.md) shows what request observations can tell a reviewer.
6. [Suite design and worked review](research/06-tool-boundaries-and-evidence.md#worked-example-staging-invoices-api) shows how tools share evidence.
7. [Defensive analysis research](research/07-defensive-analysis-research.md) summarizes the studies behind the evaluation design.
8. [Policy and app benchmarks](research/08-policy-verification-design.md) defines how to evaluate the suite.
9. [How analysis tools reach conclusions](research/09-how-analysis-works.md) explains how evidence limits results in any analysis system.

## Reference

- [Benchmark catalog](benchmarks/catalog.json) lists planned questions and current implementation status.

- [Pensys glossary](research/glossary.md)
- [Shared evidence schema and fixtures](schema/README.md)
- [Reusable diagram library](research/_references/diagrams/README.md)

**Suite commands are in design.**[^status] Run `./tool --help` for the repository scripts available today.

[^status]: The repository currently includes the v1 bundle schema, example bundles, and Mermaid maintenance tooling.
