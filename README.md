# Tentative project name: Pensys

Pensys is the working name for a local security review suite for personal and team projects.

# Forward

TL;DR

Unbridled capitalism bad, science good

A more serious TL;DR

A security suite that has human led design and research with carefully measured and considered AI implementations (sometimes human too). In addition, this is a soft-wiki for security. Any and all contributions are welcome. Stealing for profit is bad. Making things for the betterment of humanity is good. The end.

For those who can read good (Zoolander joke):

Research and design are human led. AI implementations are mostly used with specific versioned releases, but only after careful review where proper coding standards and principles are applied to the utmost ability of the maintainer (phil). Any and all branches that are not tagged or versioned should be taken as under-construction and appropriate consideration taken with regards to running and executing this software as is in an unreleased form. See [LICENSE](LICENSE) for those are interested in using this work in their own projects. I adhere to the principle that certain software should always be free of use without any restrictions. That being said, I abhor capitalistic greed to turn a piece of software that should be free for everyone into something that is payed for. This software is an endeavor to help people better learn about networking, penetration testing, vulnerabilities in software, etc. As this project grows I intend to keep a working repository of knowledge based on [research](research) that I have found. I tend to have a keen eye for details (most days so I intend to curate this to be as current as possible with links and proper diagrams for ease of access. In the future, I plan to create an easier accessible wiki page, but that is future work. I appreciate any and all contribution to the project and if anyone is interested in getting started to feel free to DM me directly, raise an issue or make a PR.

Finally to sum things up in as little words as possible, this project is based on the principles of determinism, mathematical rigorousness, and proper critical analysis. If you also agree with those principles, I would love to talk, work together, and create something that we can leave for the next generation that we are proud of. No promises.

[Roadmap](roadmap.md) records the next milestone and development sequence.

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

## License

Original Pensys materials use the [PolyForm Noncommercial License 1.0.0](LICENSE). The [internal commercial use permission](COMMERCIAL-USE.md) allows unmodified standalone internal use and modifications solely for upstream contributions.

The archived Certificate Transparency materials in `research/_references/` are third-party references. Their own terms apply. [Original Certificate Transparency page](https://certificate.transparency.dev/howctworks/)
