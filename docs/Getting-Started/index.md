---
description: "From first look to your own telemetry in the Grid: explore a demo grid with a free account, then subscribe and send your own data."
---

# Getting Started

Most monitoring tools hand you dashboards and charts and leave you to reconstruct what your system is doing. DeepCube takes your OpenTelemetry traces, metrics, and logs and renders them as a place you can move through: services stand as towers, calls flow between them as traffic, and a service that has gone missing shows up as a gap you can see. This is spatial observability, and DeepCube is the product that does it.

This guide takes you from first look to your own telemetry rendered in the Grid: explore a demo grid with a free account, then subscribe and send your own data.

!!! tip "Meet Tessa"
    Tessa is your AI Assistant inside DeepCube. Once your data is flowing, you can ask her about your system in plain language and she answers from what is actually in your telemetry. Tessa is in ALPHA.

## Try it before you sign up

You can explore DeepCube with demo data before creating an account. Demo grids carry sample telemetry from simulated services, so you can move through a real system in DeepCube without instrumenting anything of your own.

The fastest way in is **Shoebox**, a demo grid you drive yourself at [shoebox.deepcube.ai](https://shoebox.deepcube.ai){ target="_blank" }: generate traffic, inject failures, and watch the telemetry appear live. See [Sandbox](Sandbox/index.md) for the full walkthrough.

To see it, you need the DeepCube client. We recommend **DeepCube**, where the demo grid renders as a space you move through:

[Download DeepCube :material-download:](../DC/3D/Guides/Installation/index.md){ .md-button .md-button--primary }

The same demo grids are also viewable in [DeepCube Web](../DC/Web/index.md) from the browser. For the full sandbox walkthrough, including the built-in Demo grid, see [Sandbox](Sandbox/index.md). No subscription is needed to explore any demo grid, and in DeepCube you can also try light AI usage on them.

When you are ready to bring in your **own** telemetry, subscribe and provision a grid below.

## Sign up and send your first telemetry

Signing up is self-serve end to end: you choose how to sign in, name your account, pick a plan, and land in the product. New accounts start on the free **Start** plan.

!!! info "Free to start, but sending your own data needs a subscription"
    Exploring the demo grids needs a free account. No subscription, no payment details, no sales call. Sending your **own** telemetry is different: it requires an active subscription and a provisioned grid. The **Start** plan is free, but provisioning a grid requires a valid credit card even on Start. See [Plans & Pricing](https://immersivefusion.com/pricing){ target="_blank" } for all options.

### Choose how you sign in

You can sign in three ways. All of them reach the same product; the only difference is which identity you bring.

| Sign-in method | Best for |
|----------------|----------|
| **Email** | Individual developers; a self-managed email and password |
| **GitHub** | Developers who would rather use their GitHub identity |
| **Microsoft** | Organizations on Microsoft 365 or Entra ID, with work or school accounts and SSO |

[Sign in to DeepCube :material-rocket-launch:](https://portal.deepcube.ai){ .md-button .md-button--primary target="_blank" }

Email and GitHub accounts land you in the web app at **my.deepcube.ai**; Microsoft accounts land you at **azure.deepcube.ai**. Both are the same application behind the same backend; the address differs only by how you signed in, so bookmark whichever one you land on.

For the full step-by-step, see [Sign up and instrument](Step-By-Step-Instructions/index.md).

### What the sign-up flow asks you

The first time you sign in, a short Quick Start wizard walks you through three steps:

| Step | What happens |
|------|--------------|
| **1. Account** | Name your tenant (the label for your subscription, environment, and grid). One field; the rest is filled in for you. |
| **2. Subscription** | Choose a plan. Pick a Grid tier, optionally add Tessa and support add-ons, all in one cart. Some higher tiers show **Coming soon** while capacity is brought online; the tiers you can pick today are the ones ready to serve you. Start on an available tier now and upgrade when the higher tiers open. |
| **3. Final checks** | Choose where your data is stored, accept the terms, and add a payment method. Metered items are billed on what you use at the end of the cycle, not charged up front. |

When the wizard finishes it provisions your subscription, environment, and grid, and drops you on the product hub.

## Send your first trace

Once you are in, the fastest way to see the Grid light up is to send a stream of ready-made traces before you touch your own application:

[Send your first trace :material-vector-line:](your-first-trace.md){ .md-button .md-button--primary }

This uses a ready-made trace generator, a single command-line tool you run locally, so there is no application to write or deploy. You point it at your grid with an API key and watch services appear.

## Instrument your own application

When you are ready for your real system, add OpenTelemetry to it and point it at DeepCube. Grab your grid's API key from **Administration → Grids** in the web app, point your OTLP exporter at DeepCube, and deploy; services appear in the Grid within a couple of minutes. The [instrumentation guide](../Instrument/index.md) has the per-language setup and the exact endpoint.

[Instrument your application :material-code-tags:](../Instrument/index.md){ .md-button .md-button--primary }

## Explore your system

With telemetry flowing, choose how you want to look at it:

| Surface | What it is | Learn more |
|---------|------------|------------|
| **DeepCube** | The full spatial experience: walk your system, read it by shape and color, investigate a trace by moving into it | [3D docs](../DC/3D/index.md) |
| **DeepCube Web** | Browser-based traces, metrics, logs, and account management | [Web docs](../DC/Web/index.md) |

## Need help?

| Channel | Best for |
|---------|----------|
| [Live Chat](javascript:zE.activate()) | Quick questions, immediate support |
| [Discord](https://discord.gg/zevywnQp6K){ target="_blank" } | Community help, feature discussions |
| [YouTube](https://www.youtube.com/@immersivefusion){ target="_blank" } | Video tutorials, walkthroughs |
| [Contact Us](../contact.md) | Sales, licensing, enterprise support |
