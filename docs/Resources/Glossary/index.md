---
title: Glossary
diataxis: reference
tags: [reference, glossary, terminology]
---

# Glossary

The terms below are shared across every DeepCube surface: 3D, Web, and Studio. Use them exactly as written.

For the 3D client's spatial vocabulary (the Core, the Diagnostics cube, photons, altitude, camera views), see [Spatial Vocabulary](../../DC/3D/Reference/spatial-vocabulary.md), which names the objects and places specific to the 3D environment.

## Telemetry

| Term | What it is |
|------|-----------|
| **Trace** | The record of a single request as it moves through your services, tying together every operation that request triggered. |
| **Span** | One operation within a trace (a service call, a query, a handler). A trace is a tree of spans. |
| **Trace ID** | The identifier shared by every span and log belonging to the same request. DeepCube keys a request's telemetry on its trace ID. |
| **Log** | A timestamped record of a discrete event. Logs that carry a trace ID are correlated to that request. |
| **Metric** | A numeric measurement captured over time (a rate, a count, a duration). |
| **Telemetry** | The traces, metrics, and logs your instrumented application emits. |

## Instrumentation

| Term | What it is |
|------|-----------|
| **Instrumentation** | Adding OpenTelemetry to your application so it emits telemetry to DeepCube. |
| **OpenTelemetry (OTel)** | The open standard DeepCube builds on for traces, metrics, and logs. |
| **OTLP** | The OpenTelemetry Protocol, the wire format your application uses to send telemetry to DeepCube. See [Instrument your application](../../Instrument/index.md) for the current endpoint. |
| **API key** | The credential that authorizes your application to send telemetry to a specific grid. |

## Your data in DeepCube

DeepCube organizes your telemetry in a hierarchy:

| Term | What it is |
|------|-----------|
| **Account** | Your organization's DeepCube identity. |
| **Tenant** | An organizational unit within your account (a company or department). |
| **Environment** | A deployment stage (development, staging, production). |
| **Grid** | The telemetry container for a single application. Your instrumented data flows into a grid, and each grid has its own API key. In the 3D client, the same word also names the temporal view you travel into to see that data; see [Spatial Vocabulary](../../DC/3D/Reference/spatial-vocabulary.md). |
| **Service** | An instrumented component that emits telemetry, drawn from the `service.name` on your spans. |
| **Service graph** | Your services as nodes and the calls between them as edges. |

This glossary covers the telemetry model. For subscription, plan, and billing terms, see [Getting Started](../../Getting-Started/index.md).

## Assistant

| Term | What it is |
|------|-----------|
| **Tessa** | The DeepCube AI Assistant. Once your telemetry is flowing, Tessa answers questions about your system from what is actually in your data. |
