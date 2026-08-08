# Sign up and instrument

This walkthrough takes you from signing in to seeing your own application's telemetry in DeepCube. All three sign-in methods (Email, GitHub, Microsoft) follow the same path; where Microsoft differs, it is called out.

!!! info "New to the ideas?"
    DeepCube renders your telemetry as a space you move through rather than a set of dashboards. If you want the background first, read [Spatial Observability](../../Resources/Terms-and-Concepts/Spatial-Observability/index.md), then come back.

## Step 1: Sign in

Choose how you want to sign in. All three reach the same product; the difference is only which identity you bring.

- **Email** or **GitHub**: for individual developers. You land in the web app at **my.iapm.app**.
- **Microsoft**: for organizations on Microsoft 365 or Entra ID, using work or school accounts and SSO. You land at **azure.iapm.app**.

Both hosts are the same application on the same backend; the address differs only by how you signed in, so bookmark whichever one you land on.

[Sign in to DeepCube :material-rocket-launch:](https://portal.iapm.app){ .md-button .md-button--primary target="_blank" }

The link opens **portal.iapm.app**, the sign-in chooser. Pick a method, and it forwards you into the web app. A short Quick Start wizard then names your account, has you choose a plan, and provisions your first grid. Sending your own telemetry requires an active subscription and a provisioned grid: the **Start** plan is free, but provisioning a grid requires a valid credit card even on Start. (Exploring the [demo grids](../Sandbox/index.md) needs none of this, no subscription and no payment.)

## Step 2: Get your API key

Your API key authenticates telemetry with DeepCube. Each grid has its own key.

1. In the web app, open **Administration → Grids**.
2. Click the **Instrument** button on the grid you want to send data to.
3. Copy the API key.

Treat the key like a password: do not commit it to source control.

## Step 3: Instrument your application

Point your OpenTelemetry OTLP exporter at DeepCube. The endpoint is `otlp.deepcube.ai:443` (gRPC over TLS), and your API key travels in the `api-key` header:

    # OTLP exporter configuration
    exporters:
      otlp:
        endpoint: "otlp.deepcube.ai:443"
        headers:
          "api-key": "your-api-key-here"

[View full instrumentation examples :material-code-tags:](../../Instrument/index.md){ .md-button .md-button--primary }

!!! tip "Want to see it work before instrumenting your own app?"
    Send a stream of ready-made traces first with the trace generator, a single command-line tool you run locally, so there is no application to write. Follow [Send your first trace](../your-first-trace.md), then come back and point your real application here.

!!! tip "New to OpenTelemetry?"
    The official [Language APIs and SDKs](https://opentelemetry.io/docs/languages/){ target="_blank" } cover instrumentation for your programming language.

!!! warning "Nothing showing up?"
    If you sent telemetry but no services appear after a couple of minutes, the cause is almost always the key or the endpoint. Check that the endpoint is exactly `otlp.deepcube.ai:443`, that the `api-key` header holds the key for the same grid you are viewing, and that your exporter uses gRPC over TLS. Still stuck? Reach [support](../../contact.md).

## Step 4: Explore your system

Once telemetry is flowing, choose how to look at it.

### DeepCube

Enter the World of Your Application® with mouse and keyboard. Your services stand as towers, traffic flows between them, and a service that has gone dark shows up as a gap you can see.

[Install DeepCube :material-download:](../../DC/3D/Guides/Installation/index.md){ .md-button .md-button--primary }
[3D documentation :material-book-open:](../../DC/3D/index.md){ .md-button }

### DeepCube Web

Access traces, metrics, logs, alerts, and account management from any browser. Sign in through [portal.iapm.app](https://portal.iapm.app){ target="_blank" }; you land in the web app at my.iapm.app or azure.iapm.app depending on how you signed in.

[Sign in to DeepCube Web :material-web:](https://portal.iapm.app){ .md-button .md-button--primary target="_blank" }
[Web documentation :material-book-open:](../../DC/Web/index.md){ .md-button }
