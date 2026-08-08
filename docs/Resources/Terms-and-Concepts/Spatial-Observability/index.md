---
title: Spatial Observability
diataxis: explanation
tags: [explanation, spatial-observability]
---

# Spatial Observability

Spatial observability is the un-compression of high-dimensional system reality (service topology, request paths, failure neighborhoods, latency distance) back into the dimensions it always had, rather than flattening it onto dashboard panels.

This page is the category definition. The DeepCube product is one implementation of the category; the category itself is a new way of thinking about observability that goes beyond what dashboards can show.

## Why this is a category, not a feature of APM

The distinction is in the definition: spatial observability un-compresses system reality back into the dimensions it always had, where traditional [Application Performance Management (APM)](../APM/index.md) flattens that reality onto dashboard panels. Topology, request paths, failure neighborhoods, and latency distance are rendered in the dimensions the system already has, rather than projected onto a grid of flat charts.

APM remains valid as the predecessor discipline for flat-surface monitoring. Spatial observability is a distinct analytical category that renders the same telemetry spatially.

## How DeepCube implements spatial observability

DeepCube is the product family that implements spatial observability. Three surfaces:

- **[DeepCube](../../../DC/3D/index.md)** renders the full spatial environment on the Grid. Services are objects in a navigable world; their traffic is light moving between them; their stress is heat; their dependencies are gravity. Available as a desktop application and on Steam.
- **[DeepCube Web](../../../DC/Web/index.md)** provides browser-based access to the same spatial telemetry for account management, alerts, and quick investigation without the full immersive client.
- **[DeepCube Studio](../../../DC/Studio/index.md)** is the lightweight native client for AI Assistant chat, voice, and workspaces with Tessa, currently in early access.

All three surfaces consume the same OpenTelemetry-native telemetry. The spatial environment is a rendering of what is already there in the OTel data; we do not require proprietary agents or instrumentation.

## Relationship to APM and Observability

Spatial observability does not replace APM or observability as practices. It is a new category that sits alongside them.

- **[APM](../APM/index.md)** is the predecessor discipline. It is the right reference point for what spatial observability is leaving behind: dashboard-first, flat-surface monitoring. The APM page in this taxonomy remains valid as a definition of that discipline. Engineers who need to understand "what is APM" should start there.
- **[Observability](../Observability/index.md)** is the broader practice of understanding system behavior from external signals (traces, metrics, logs). Spatial observability is one way to *experience* observability data; the underlying observability foundations (OpenTelemetry, structured signals, correlation) are unchanged. The Observability page remains the right starting point for the foundational concepts.

The shortest mapping: observability tells you what the system is doing; APM tells you that in a flat surface; spatial observability tells you that in the dimensions the system already has.

## Not the Metaverse

Spatial observability is sometimes pattern-matched against the consumer metaverse. The pattern-match is wrong, structurally, on three points:

- **No tokens, no NFTs, no virtual land.** Spatial observability is a way of seeing your software. There is no economy attached.
- **No headset required.** The product ships on the desktop and on the web. Optional VR is available for engineers who want the deepest immersion, but it is a mode, not a requirement.
- **A purpose, not a place.** The consumer metaverse built places that hunted for purposes. Spatial observability puts a purpose first: rendering production systems in the dimensions they already have. The "place" is your software.

The right analyst-framing archetype is the Bloomberg Terminal of production systems, not Meta or Horizon Worlds.

## Further reading

- A canonical "what is spatial observability" blog post on immersivefusion.com (coming soon; link to be wired when the post publishes)
- [APM (predecessor discipline)](../APM/index.md)
- [Observability (the broader practice)](../Observability/index.md)
- [DeepCube (the product implementing the category)](../DC/index.md)
- [OpenTelemetry (the open-standard foundation)](../Observability/Frameworks/OpenTelemetry/index.md)
