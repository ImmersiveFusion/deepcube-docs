---
title: Send your first trace
diataxis: tutorial
tags: [tutorial, getting-started, instrumentation, opentelemetry]
---

# Send your first trace

In about five minutes you will send real telemetry into DeepCube and watch a system take shape in the Grid: services appearing as you feed them, connected by the calls between them. You will use a ready-made trace generator, so there is no application to write and nothing to deploy. This is the known-good baseline: one command, real OTLP traces, your data in DeepCube.

You are not instrumenting your own application yet. That comes next, and it is easier once you have seen what "working" looks like.

## What you will learn

- How to point an OpenTelemetry exporter at DeepCube using your grid's API key
- What a healthy stream of traces looks like when it arrives
- Where your services and traces show up in DeepCube

## Prerequisites

- **A subscription and your own grid.** Sending your own telemetry requires an active subscription (the free Start plan works) with a provisioned grid. Provisioning a grid requires a valid credit card, even on Start. If you have not done this yet, complete [Getting Started](index.md) first. (Just want to look around? The [demo grids](Sandbox/index.md) need no subscription.)
- The grid's API key. You will copy this in Step 1.
- [Go](https://go.dev/dl/){ target="_blank" } 1.21 or later installed, so you can run the generator with a single command. (No Go knowledge is needed; you are only running a tool written in it.)

## Step 1: Get your grid API key

Your API key authenticates your telemetry with DeepCube. Each grid has its own key.

1. Sign in at [portal.deepcube.ai](https://portal.deepcube.ai){ target="_blank" } (the sign-in chooser). After you choose a method you land in the web app: `my.deepcube.ai` if you signed in with Email or GitHub, `azure.deepcube.ai` if you signed in with Microsoft. Go to **Administration → Grids**.
2. Click the **Instrument** button on the grid you want to send traces to.
3. Copy the API key from the wizard.

Keep the key somewhere safe for the next step. Treat it like a password: do not commit it to source control.

For more detail, see the [API Keys reference](Api-Key/index.md).

## Step 2: Install the trace generator

The [OpenTelemetry Trace Generator](https://github.com/ImmersiveFusion/opentelemetry-tracegen){ target="_blank" } is a single binary that simulates a realistic, multi-service application and sends its traces over OTLP. Install it with:

```bash
go install github.com/ImmersiveFusion/opentelemetry-tracegen/cmd/tracegen@latest
```

This puts a `tracegen` command on your system.

**What you should see:** the command completes with no output. Run `tracegen -help` to confirm it is installed; you will see the list of available flags.

## Step 3: Send traces to DeepCube

Now point the generator at DeepCube. Replace `YOUR-API-KEY` with the key you copied in Step 1:

```bash
tracegen -endpoint otlp.deepcube.ai:443 -headers "api-key=YOUR-API-KEY" -complexity light
```

A note on each part:

- `-endpoint otlp.deepcube.ai:443` sends to DeepCube's OTLP endpoint over gRPC.
- `-headers "api-key=YOUR-API-KEY"` authenticates with your grid key. The header name is `api-key`, lowercase, exactly.
- `-complexity light` generates a clean, ten-service topology: enough to be interesting, small enough to read at a glance. (You can rerun later with `normal` or `heavy` for a larger graph.)

**What you should see:** the generator starts emitting traces and logs to your terminal as it simulates an e-commerce platform: a web frontend, an API gateway, an order service, a payment service, and a handful of others, exercising flows like *Create Order* and *User Login*.

!!! tip "Sending to a local collector first?"
    To try the generator against a local Jaeger, Tempo, or Collector before involving DeepCube, drop the headers and use `tracegen -insecure` (defaults to `localhost:4317`). Then come back and run the DeepCube command above.

## Step 4: See your trace in DeepCube

Switch to DeepCube and open the grid you used in Step 1.

**What you should see:** within a couple of minutes, services begin appearing in the Grid: nodes for `web-frontend`, `api-gateway`, `order-service`, and the rest, connected by the calls between them. Open a service and drill into a trace to see its span waterfall: the ordered timeline of every operation in a single request.

You have now sent your first trace into DeepCube and watched it arrive. That is the whole loop: telemetry leaves your machine, DeepCube receives it, and the Grid shows you the shape of the system.

## What you did

In about five minutes you:

- Authenticated a telemetry source to DeepCube with a grid API key
- Sent real OTLP traces using a ready-made generator
- Watched services and traces appear in the Grid

## Next steps

- **Instrument your own application.** Swap the generator for your real service: see [Instrument Your Application](../Instrument/index.md) for language-specific guides (.NET, Java, Python, Go, Node.js).
- **Explore failures.** Rerun the generator with `-errors 5` to inject failures and watch how they propagate through the Grid.
- **Ask Tessa about it.** With data flowing, open the AI Assistant and ask "How is my system doing right now?" to see DeepCube's diagnostics in action. Tessa is in ALPHA.

## Related

- **To explore without installing anything:** open the [Chaos Simulator](Sandbox/index.md), a demo grid you drive from your browser at [chaos.deepcube.ai](https://chaos.deepcube.ai){ target="_blank" } and view in DeepCube.
- **For lookup of API key properties and rotation:** see the [API Keys reference](Api-Key/index.md).
- **For background on traces and spans:** see [Concepts](../Resources/Terms-and-Concepts/index.md).
