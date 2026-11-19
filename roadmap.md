# Pensys roadmap

Pensys helps reviewers assemble, verify, and reuse evidence about software they own or are authorized to review. This file records the current direction and the conditions for moving on. Use Git history for earlier versions and the linked designs for technical detail.

**Current state:** The v1 evidence schema, two example bundles, and diagram tooling exist. The suite commands and runnable benchmarks are planned.[^status] [Schema releases](schema/README.md), [Benchmark catalog](benchmarks/catalog.json)

## Next milestone: one complete offline review

Use the existing ingress and origin fixtures to answer one question: does the evidence establish that the origin accepts requests only from the intended edge? The current fixture should support the network-filter observation and leave edge identity unresolved.

- [ ] Build **Evidence Validate**. Check version, structure, timestamps, unique IDs, scope, and citations. Check that the existing pair validates with edge identity unresolved. Verify distinct results for an absent ingress bundle, an invalid citation, and a scope mismatch.
- [ ] Produce one bundle from a saved configuration export or a small synthetic fixture. Keep the input and its provenance available for replay.
- [ ] Present a cited result that explains what the evidence supports, what remains unresolved, and which input could answer the open question. Follow the citations manually.
- [ ] Repeat with complete, incomplete, and changed inputs. Add the smallest **Evidence Diff** needed to explain what changed. Add **Evidence Trace** when manual citation lookup becomes a recurring cost. Have a reviewer compare the results against independent expectations.

**Exit condition:** A reviewer can reproduce the result from pinned inputs, trace its claims, and distinguish a changed conclusion from lost coverage. [Suite design](research/06-tool-boundaries-and-evidence.md), [Evidence Evaluate](research/_tools/evidence-evaluate/README.md)

## Discover tools alongside the first milestone

Keep a short inventory of tools and exports that can answer an actual review question. For each candidate, record what it produces, where the evidence comes from, what it misses, whether it can run or export offline, and the cost of integration and upkeep. Choose among reusing an export, writing an adapter, or building a narrow analyzer. Revisit the inventory when a benchmark exposes a gap.

**Work AST analyzer reuse is a candidate.**[^ast] Trial a small importer for a neutral export using approved or synthetic inputs. Keep the producing tool, source revision, locator, and coverage with each record. Candidate facts include nested registrations, handler references, and dependency edges. Compare one result against an existing framework export or a hand-checked fixture. Measure additional correctly cited coverage, false alarms, and verification effort. Treat structural and architectural signals as leads for security review unless relevant evidence supports a specific security claim. [Route Mapper](research/_tools/route-mapper/README.md)

**GitHub AI Scan for repositories** is a possible match for the remembered GitHub feature.[^github] Evaluate already available scanner output only when a benchmark question calls for it. GitHub documents SARIF support for code scanning, which is a candidate interchange format for tools that can supply it. Keep scanner alerts attributable to their producer. [GitHub AI Scan announcement](https://github.blog/changelog/2026-10-28-ai-scan-for-repositories-in-public-preview/), [GitHub SARIF support](https://docs.github.com/en/code-security/reference/code-scanning/sarif-files/sarif-support)

## After the offline slice

| Milestone | What to demonstrate |
| --- | --- |
| Route inventory | Import one existing export and record its limits. Use the representative app benchmarks to test whether evidence remains comparable when deployments change. |
| Policy pilot | Compare one Lean policy model, an executable Python baseline, and application regression evidence on independently labeled cases. Measure whether the proof catches a meaningful modeled regression and remains practical through a policy revision. |
| Connected review | Correlate routes, ingress, origin assessments, and edge traffic on a pinned full application. Use the same evaluation process to decide what should improve. |
| Expand on demonstrated need | Add provider connectors when export collection is a recurring cost. Add replay automation when repeated manual runs establish the workflow. Add search indexes when file lookup becomes a measured bottleneck. |

Apply lessons from runs and papers to the [working-knowledge note](research/09-how-analysis-works.md). Link the question, evidence, limitation, decision, and follow-up check. Use those records to revisit the roadmap.

[^status]: The milestones and exit conditions describe the proposed development sequence. The benchmark definitions are scaffolded.
[^ast]: Reuse depends on permission, export availability, and evidence that the importer fills a real gap. Keep proprietary code and data outside this repository unless reuse has been authorized.
[^github]: **Identification is tentative.** If the remembered feature ran inside the Copilot app, the [GitHub security extension](https://github.blog/changelog/2026-10-28-security-extension-for-the-github-copilot-app/) is another possibility.
