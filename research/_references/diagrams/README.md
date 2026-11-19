# Reusable Mermaid diagrams

The editable `.mmd` files are grouped by their originating note or tool. Copy a source into a Mermaid block in any Markdown document and link back to the source.

From the repository root, run `./tool sync_diagrams` after editing a source. Run `./tool sync_diagrams --check` to detect stale previews without editing Markdown.

## Initial direction

- [Overview](01-initial-direction/01-overview.mmd)

## How infrastructure and endpoints become visible

- [Overview](02-internet-exposure/01-overview.mmd)
- [Hostnames and IP addresses](02-internet-exposure/02-hostnames-and-ip-addresses.mmd)
- [API routes](02-internet-exposure/03-api-routes.mmd)
- [Reachability: who can connect?](02-internet-exposure/04-reachability-who-can-connect.mmd)
- [Authorization: who can act on this resource?](02-internet-exposure/05-authorization-who-can-act-on-this-resource.mmd)

## Ingress

- [Overview](03-ingress/01-overview.mmd)
- [Cloudflare Tunnel](03-ingress/02-cloudflare-tunnel.mmd)
- [CloudFront with a private origin](03-ingress/03-cloudfront-with-a-private-origin.mmd)
- [CloudFront with an internet-facing ALB](03-ingress/04-cloudfront-with-an-internet-facing-alb.mmd)
- [Public ALB as the entry point](03-ingress/05-public-alb-as-the-entry-point.mmd)
- [Google Cloud: external load balancer and Cloud Run](03-ingress/06-google-cloud-external-load-balancer-and-cloud-run.mmd)
- [Private origin through Private Link](03-ingress/07-private-origin-through-private-link.mmd)
- [Restricted public origin](03-ingress/08-restricted-public-origin.mmd)
- [Fastly](03-ingress/09-fastly.mmd)
- [Self-managed reverse proxy](03-ingress/10-self-managed-reverse-proxy.mmd)

## Origin protection controls

- [Overview](04-origin-protection-controls/01-overview.mmd)
- [Outbound tunnel](04-origin-protection-controls/02-outbound-tunnel.mmd)
- [Public origin with Authenticated Origin Pulls](04-origin-protection-controls/03-public-origin-with-authenticated-origin-pulls.mmd)
- [CloudFront VPC origin](04-origin-protection-controls/04-cloudfront-vpc-origin.mmd)
- [CloudFront with an internet-facing ALB](04-origin-protection-controls/05-cloudfront-with-an-internet-facing-alb.mmd)
- [Private S3 origin](04-origin-protection-controls/06-private-s3-origin.mmd)
- [Cloud Run behind a load balancer](04-origin-protection-controls/07-cloud-run-behind-a-load-balancer.mmd)
- [Front Door Premium with Private Link](04-origin-protection-controls/08-front-door-premium-with-private-link.mmd)
- [Front Door with a public origin](04-origin-protection-controls/09-front-door-with-a-public-origin.mmd)
- [Mutual TLS to the origin](04-origin-protection-controls/10-mutual-tls-to-the-origin.mmd)
- [Same-host reverse proxy](04-origin-protection-controls/11-same-host-reverse-proxy.mmd)
- [Reverse proxy and origin on separate hosts](04-origin-protection-controls/12-reverse-proxy-and-origin-on-separate-hosts.mmd)

## Distributed honeypot telemetry

- [Overview](05-distributed-honeypot/01-overview.mmd)

## Tool boundaries and shared evidence

- [Overview](06-tool-boundaries-and-evidence/01-overview.mmd)
- [CLI wrapper by analysis perspective](06-tool-boundaries-and-evidence/02-cli-wrapper-by-analysis-perspective.mmd)
- [Collection and review](06-tool-boundaries-and-evidence/03-collection-and-review.mmd)
- [Coverage history and shared folders](06-tool-boundaries-and-evidence/04-coverage-history-and-shared-folders.mmd)
- [Append-only evidence history](06-tool-boundaries-and-evidence/05-append-only-evidence-history.mmd)
- [Command history and reusable workflows](06-tool-boundaries-and-evidence/06-command-history-and-reusable-workflows.mmd)

## Evidence Diff

- [Overview](evidence-diff/01-overview.mmd)

## Evidence Validate

- [Overview](evidence-validate/01-overview.mmd)

## Exposure review CLI

- [Overview](exposure-review-cli/01-overview.mmd)

## Ingress Review CLI

- [Overview](ingress-review-cli/01-overview.mmd)

## Origin Review CLI

- [Overview](origin-review-cli/01-overview.mmd)
- [Example: shared edge network](origin-review-cli/02-example-shared-edge-network.mmd)

## Shared review log

- [Overview](review-log/01-overview.mmd)
- [Example: incomplete origin export](review-log/02-example-incomplete-origin-export.mmd)

## Route Mapper

- [Overview](route-mapper/01-overview.mmd)
- [Example: nested route registration](route-mapper/02-example-nested-route-registration.mmd)
- [Example: Django route evidence](route-mapper/03-example-django-route-evidence.mmd)

## Schema patterns from Trace and security-audit-skill

- [Overview](schema/01-overview.mmd)
- [Example: origin identity is unresolved](schema/02-example-origin-identity-is-unresolved.mmd)

## Defensive security analysis research

- [Overview](07-defensive-analysis-research/01-overview.mmd)

## Policy verification benchmark design

- [Overview](08-policy-verification-design/01-overview.mmd)
- [Gitea evidence flow](08-policy-verification-design/02-gitea-evidence.mmd)
- [Ingress comparison](08-policy-verification-design/03-ingress-comparison.mmd)
- [WordPress route evidence](08-policy-verification-design/04-wordpress-inventory.mmd)

## Evidence Evaluate

- [Overview](evidence-evaluate/01-overview.mmd)
- [Manual policy evaluation](evidence-evaluate/02-manual-policy-evaluation.mmd)
