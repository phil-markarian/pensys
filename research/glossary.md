# Pensys glossary

Use these terms in documentation, diagrams, and command help.

| Term | Meaning |
| --- | --- |
| **Source / export / input** | A source is the system or artifact that supplies information. An export is data extracted from it. An input is the concrete file, snapshot, policy, or bundle passed to a command. |
| **Snapshot / source locator** | A snapshot preserves inputs and collection provenance. A source locator identifies where a record came from. In v1 it is a string, such as a file path and JSON fragment. |
| **Evidence bundle / report / run log** | A bundle exchanges structured evidence. A report presents results to a person. A run log records Pensys execution events. An access log records requests seen by an application or edge. |
| **Observation / assessment / finding** | An observation records what a source shows. An assessment states what the evidence supports about a claim. A finding is an assessment surfaced for the reader's attention. |
| **Coverage / readiness** | Coverage records which inputs were reviewed and which were unavailable, unsupported, or out of scope. Readiness describes whether the evidence can answer a particular question: sufficient, partial, or insufficient. Include a reason and next input when relevant. |
| **Coverage ledger / evidence history** | The ledger is the current view across review questions. Evidence history is the append-only record behind that view. A comparison can mark a question resolved or no longer evaluable while retaining earlier assessments. |
| **Workspace / evidence scope / investigation** | A workspace holds review artifacts. In v1, project and environment define evidence scope. An investigation groups evidence references around a question. Moving files preserves original scope and identity. |
| **Command run / workflow run** | A command run records one invocation. A workflow defines reusable steps, and a workflow run groups their executions. V1 bundles have one producing `run_id`. Workflow parentage remains a design extension.[^workflow] |
| **Internal / external** | Internal commands use operator-side evidence. External commands use observations from a declared client vantage, which can be public, authenticated, or private. |
| **Application route / ingress routing rule / request path** | A route is an application registration. An ingress routing rule maps requests to a backend. A request path is the value observed in traffic or a client result. |
| **Service exposure review / Edge Traffic Review** | Service exposure review covers visibility, reachability, and authorization. Edge Traffic Review summarizes operator-side access logs and correlates them with available route, ingress, and origin evidence. |

The [v1 schema](../schema/README.md) uses assessment statuses `supported`, `mismatch`, and `unresolved`. Coverage statuses are `reviewed`, `missing`, `unsupported`, and `out_of_scope`. Readiness and comparison outcomes describe the review without changing these values. A record citation identifies both the bundle and the record.

[^workflow]: **Workflow run linkage is planned.** A later contract can link command runs to the workflow run that launched them.
