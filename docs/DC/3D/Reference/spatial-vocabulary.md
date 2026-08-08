---
title: Spatial Vocabulary
diataxis: reference
tags: [reference, spatial-model, terminology]
---

# Spatial Vocabulary

This page documents the canonical names for the objects, places, and behaviors in DeepCube's 3D client, and where each one sits. Use these terms and positions exactly. This page is the source of record for the 3D spatial vocabulary: when another 3D page describes an object, a direction, or a color, it matches what is written here. For terms shared across 3D, Web, and Studio (trace, span, log, service, grid, and the rest), see the [Glossary](../../../Resources/Glossary/index.md).

## Spatial layout (canon)

The whole environment is one continuous vertical space. You change altitude to move between views rather than switching tabs. From bottom to top:

| Altitude | What is there |
|----------|---------------|
| Bottom | The **service graph** (structure: service nodes and their dependencies) |
| Middle | The **Core** (the hub you land on, with the four cardinal cubes and the Portal Room beneath it) |
| Above the Core | The **grid** (live activity: the Trace and Log Aggregate Blocks over the last ~60 seconds) |

**Inside the Diagnostics cube**, a single trace un-flattens onto two walls, each at a fixed compass direction:

| Wall | Direction | What is on it |
|------|-----------|---------------|
| Span waterfall | **North** | The trace's spans as a 3D waterfall (bar length = span duration) |
| Logs wall | **West** | The trace's logs as stacked bars, colored by log level |

The **Portal Room** is a floor below where you spawn on the Core, in the basement directly beneath it. It holds the portals to the various cubes in the environment (Research, Security, Zen). It does **not** hold a portal to Diagnostics: the Diagnostics cube is reached only by selecting a trace on the grid, not from the Portal Room.

**Entering the Diagnostics cube** is always done from the grid: click the rhombus on a Trace Aggregate Block to zoom deeper into that trace. You descend into the trace (the block is not carried with you), and Tessa's context focuses on that trace while you are inside. The Diagnostics cube returns you to the grid position you came from; the other cubes return you to the Portal Room.

## Objects

| Term | What it is |
|------|-----------|
| **Service node** | A single service in the service graph, drawn as a glowing ring. Its color is its health (see [Color legend](color-legend.md)). |
| **Trace Aggregate Block** | On the grid, the block aggregating all spans that share one trace ID. It grows in size with the combined duration of all the spans in the trace, so slower traces stand taller. Red if a span in the trace errored. |
| **Log Aggregate Block** | On the grid, the block aggregating all logs that share the same trace ID. Red if a log in the trace was an error log. |
| **Span Block** | Inside the Diagnostics cube, a single span from the trace, laid out in the span waterfall. Red if that span errored. |
| **Log Block** | Inside the Diagnostics cube, a single log line from the trace, on the logs wall. Colored by log level. |

Both aggregates key on trace ID: the Trace Aggregate Block holds every span with that trace ID, and the Log Aggregate Block holds every log with the same trace ID. On the grid, a trace occupies one position as these two adjacent aggregate blocks. Inside the Diagnostics cube, that trace un-flattens into its individual Span Blocks (the span waterfall) and Log Blocks (the logs wall).

**Blocks take the color of the highest-severity status they contain.** A single error span turns the whole Trace Aggregate Block red. A single warning log turns the Log Aggregate Block orange. If a Log Aggregate Block contains both a warning and an error, it is red, because error outranks warning. See [Color legend](color-legend.md) for the full severity order.

## Places and views

| Term | What it is |
|------|-----------|
| **Lobby** | Where you land when you log in. It holds the Select a Grid panel and is the entry point to the grid flow. Open to anyone; free to enter. |
| **Grid** | The temporal view of your system: a live, roughly 60-second window of traces, rendered as a skyline of Trace and Log Aggregate Blocks. The Traces & Logs Camera View (**M**) is a top-down view of the field; click a trace cube to port down onto the grid at that spot. You can also travel into it through the NE portal on the Core. |
| **Service graph** | The structural view of your system: services as nodes, dependencies as edges. The Services & Dependencies Camera View (**N**) is a top-down flattened overview; click a node to port down onto it (the graph then returns to its organic 3D form). You can also travel into it through the SW portal on the Core. |
| **Core** | The hub you land on when you enter a grid. The Home button ("Teleport to the Core") returns you here. |
| **Diagnostics cube** | The workspace you send a trace to for deep inspection, where it un-flattens into a logs wall and a span waterfall. One of the four cardinal cubes on the Core. |

## Motion and effects

| Term | What it is |
|------|-----------|
| **Photons** | Points of light that fly between service nodes to show live traffic (a request emits a photon to the target; a response sends one back). Performance-gated: they appear when the frame rate is high enough. |

## Time controls

| Term | What it is |
|------|-----------|
| **Time stop** | The play/pause transport. Pausing freezes the world (traffic, blocks, and nodes hold still) while you keep moving, so you can walk through a frozen moment and study it. Available everywhere. |
| **Time travel** | Replaying your system's state at a past moment, on both the grid and the service graph. **Currently disabled** while replay is being reworked; it is not available today. |

## Naming notes

- **Grid** is the current public term for the temporal view. The DeepCube naming is held until the trademark lands and is not used in public copy.
- **Time travel** is documented as a returning feature, never as a present-tense capability, until replay ships again.

### Colloquial terms and their canonical names

In running prose you may use the short colloquial noun. Use the full on-screen camera-view label when you introduce the shortcut or the toolbar control.

| Colloquial (use in prose) | Canonical on-screen label | Shortcut |
|---------------------------|---------------------------|----------|
| the grid | Traces & Logs Camera View | **M** |
| the service graph | Services & Dependencies Camera View | **N** |
| first-person | Avatar Camera View | **Escape** |
| the console | Console | **F12** |

Do NOT use "Grid view" or "Graph view" as terms; they are ambiguous. Say "the grid" and "the service graph", or the full camera-view label.

## Related

- **For what each color means:** see [Color legend](color-legend.md).
- **For how to move and view:** see [Navigation model](navigation-model.md).
- **For the spatial layout these terms sit in:** see [The spatial model](../Overview/the-spatial-model.md).
