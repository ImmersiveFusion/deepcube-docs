---
title: Rendering Absence
diataxis: explanation
tags: [explanation, absence, phantom, service-graph, grid, color]
---

# Rendering Absence

This page explains why DeepCube draws the parts of your system that are missing, not just the parts that are failing.

Most monitoring shows you what is emitting. A service reports, so it appears; a trace arrives, so it is plotted. The quiet consequence is that when something stops reporting, it simply vanishes: a service that should be there just is not on the map, leaving no marker and nothing to look at. DeepCube takes the opposite stance. It draws the gap itself, as a visible object in the world, so that absence becomes something you can see rather than something you have to notice is missing.

## Red is failure; black is absence

DeepCube uses color as a consistent vocabulary, and two of those colors carry the whole idea:

- **Red** means the thing is **there and broken**. A red service node is a service that is failing (the ones genuinely on fire even carry a burning texture), and a red cube on the grid is a trace that ran and errored.
- **Black** means the thing **should be there and is not**. Black is not a louder shade of red; it is a different meaning entirely. Red ran and failed. Black is missing something.

This holds at every layer of the system, which is what makes it worth learning once. In the service graph, a **phantom service** is one that should have existed but did not report, rendered as a void in the topology (a black node) rather than quietly omitted from it. On the grid, a trace that is **missing a span** is rendered black too (a span that should have been part of the trace never arrived). Same law, two layers: red is there-and-broken, black is should-be-there-and-is-not.

It is worth being precise about the neighbors of black in the color law, because they are easy to confuse. Green is healthy and grey is idle, so a service that is simply quiet is grey, not black. Black is reserved for genuine absence. The one overlap to know: an idle service renders grey, unless it is actually a phantom, in which case it renders black. So grey is present-but-idle, and black is should-be-there-and-is-not. (For how white behaves, note that on the grid white is only the hover highlight, not a health state at all.)

## Services versus dependencies

To understand how DeepCube can draw something that is not there, it helps to understand the distinction between a service and a dependency, because absence lives in the space between them.

A **service** is something you have instrumentation for. It emits telemetry directly, and you see it because it is reporting. A **dependency** is something a service has told you about but that is not itself instrumented: a SQL database, a Redis cache, an external payment API, a search cluster, an email sender. You have no agent on the Postgres box, but the instrumented service that calls it reports the call, so the dependency is known **indirectly, from the caller's telemetry**, rather than from the dependency itself.

That indirect, relational knowledge is the crucial part. Because a dependency is known only through what the instrumented services around it report, DeepCube knows the dependency is expected. And knowing it is expected is exactly what makes it possible to notice when an expected dependency has gone silent or an expected call never happened. An expected-but-absent dependency, inferred from the callers, is a **phantom**, and because the system knew to expect it, it can render it as an absence rather than letting it disappear. Dependencies surface concretely at the grid's whole-system summary boards, where "phantom" appears as a first-class dependency type alongside the ones that are actively reporting.

Absence is legible, in other words, precisely because dependencies are known relationally. You cannot draw the shape of a hole unless you knew something belonged there, and the relationships between your services are what tell DeepCube that something belonged there.

## The honest framing

Everything above stays inside a simple, honest framing: what DeepCube shows is **derived from your own telemetry**. The relationships between your instrumented services are what let the system infer that a dependency was expected, and the expected-but-absent case is what gets rendered as a phantom. This page deliberately does not describe the detection mechanism itself; the point to carry away is conceptual. DeepCube renders absence, and it can do so because it knows your system relationally, from the telemetry your services already emit.

## Where to next

- **How the graph and grid sit in one space:** see [The Spatial Model](the-spatial-model.md).
- **Mosey the companion and Tessa the assistant:** see [Mosey and Tessa](companion-and-assistant.md).
- **The section overview:** see [Overview](index.md).
