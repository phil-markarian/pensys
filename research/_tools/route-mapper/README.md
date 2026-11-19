# Route Mapper

**Design status: planned.**[^tool-status]

Route Mapper imports existing framework inventories and API specifications, normalizes usable fields, and records their provenance. Prefer an existing export or framework registry before adding source analysis. Use static extraction for offline projects or fields the existing source cannot provide, and record unresolved registrations.

```mermaid
flowchart LR
    source["Source: existing framework route inventory or API specification"]
    source -->|Import route records| mapper["Route Mapper: normalize and cite"]
    checkout["Fallback source: application checkout"] -. Extract unavailable fields .-> mapper
    mapper --> bundle["Output: versioned route evidence bundle"]
    bundle -. Optional import .-> exposure["Edge Traffic Review"]
    linkStyle default stroke:#64748b,stroke-width:2px
```

[Mermaid source](../../_references/diagrams/route-mapper/01-overview.mmd)

Each record carries the application scope, path template, method and handler when known, and a source reference with the revision or export timestamp. Record permission declarations as observations when available. Authorization decisions belong to a separate review. Edge Traffic Review matches observed requests to route templates. Ingress Review supplies the gateway path and any rewrites needed to make that match.

## What existing tools expose

| Source | What it gives us | What Pensys adds |
| --- | --- | --- |
| Application route registry or framework route export | Registered paths and, where the export includes them, handlers and HTTP methods. | Import paths and handlers with provenance. Leave HTTP methods unknown when the listing supplies no method evidence. |
| Existing OpenAPI export | Documented HTTP operations within the specification’s scope. | Use operation records for method evidence and retain the schema's scope. A schema may omit routes, and a URL listing may include pages outside the API. |
| Go chi router | `chi.Walk` visits routes with methods, patterns, and handlers. | Accept an application-provided export of those records. |
| Vue Router | `getRoutes()` returns browser-side route records. | Label these as client navigation. Backend API evidence comes from sources such as an API specification or captured client requests. |

[OpenAPI Specification](https://spec.openapis.org/oas/latest.html), [Go chi Walk](https://pkg.go.dev/github.com/go-chi/chi/v5#Walk), [Vue Router getRoutes](https://router.vuejs.org/api/interfaces/Router.html#getroutes)

## Example: application route evidence

```mermaid
flowchart LR
    app["Source: application route registry"] --> exporter["Existing exporter: framework route listing"]
    exporter -->|Import listing| mapper["Route Mapper"]
    spec["Source: existing OpenAPI export"] -. Optional method evidence .-> mapper
    mapper --> bundle["Output: cited routes and unknown fields"]
    linkStyle default stroke:#64748b,stroke-width:2px
```

[Mermaid source](../../_references/diagrams/route-mapper/03-example-application-route-evidence.mmd)

Start by importing an existing operator-provided listing or OpenAPI file. Record the settings profile or schema scope when known. The import can run offline. Route Mapper adds a small framework adapter when an export needs normalization or the application needs a way to serialize its registry.

## Example: nested route registration

```mermaid
flowchart LR
    mount["Input: parent mount /api from application source"] --> resolve["Resolve full route template"]
    route["Input: child registration GET /invoices"] --> resolve
    resolve --> output["Output: route record GET /api/invoices"]
    linkStyle default stroke:#64748b,stroke-width:2px
```

[Mermaid source](../../_references/diagrams/route-mapper/02-example-nested-route-registration.mmd)

If the adapter cannot resolve a mount prefix, preserve the known child route and record the unresolved registration in coverage.

See [Tool boundaries and shared evidence](../../06-tool-boundaries-and-evidence.md) and [Edge Traffic Review](../edge-traffic-review/README.md).

See the [staging invoices review](../../06-tool-boundaries-and-evidence.md#worked-example-staging-invoices-api) for how this output is used.

[^tool-status]: This page describes intended behavior. See [suite implementation status](../../06-tool-boundaries-and-evidence.md) for what is available today.
