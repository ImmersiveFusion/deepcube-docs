---
title: Color legend
diataxis: reference
tags: [reference, color, health-states, grid, service-graph, diagnostics]
---

# Color legend

This page documents what each color means on the service graph, the grid, and inside a trace.

## Color law

One vocabulary applies at every scale: a service node, a connection between two services, the aggregate blocks on the grid, and an individual span or log inside a trace.

| Color | Meaning | Applies to |
|-------|---------|------------|
| **Green** | Healthy | Service nodes, grid aggregate blocks, spans, logs (not edges: healthy edges are translucent glass, see below) |
| **Orange** | Warning | Log Aggregate Block (a warning log, when no error is present); log lines at warning level |
| **Red** | Failure. The thing is there and it is broken | Service nodes (burning texture when on fire), connections/edges, grid aggregate blocks, spans, logs |
| **Black** | Absence. The thing should be there and is not | Service nodes (phantom services), Trace Aggregate Block (a trace with a missing span) |
| **Grey** | Idle. Present but not currently active | Service nodes, grid aggregate blocks |
| **White** | Hover / mouse-over highlight only. Not a health state | Grid aggregate blocks, other highlightable objects |

Red distinguishes failure from absence: red means the thing exists and failed; black means the thing was expected and never arrived or never reported. This distinction holds at every layer (service, trace, span).

One overlap applies to node color: an idle service renders grey, unless it is a phantom (absent) service, in which case it renders black rather than grey.

## Per-surface breakdown

### Service node (service graph)

| State | Color | Detail |
|-------|-------|--------|
| Healthy | Green | Glowing ring |
| Unhealthy | Red | Glowing ring; a service genuinely on fire also renders a burning texture in the center |
| Idle | Grey | Present, not currently active |
| Phantom (absent) | Black | Expected service that never reported; rendered as a void in the topology |

### Connection / edge (service graph)

Edges use their own two-state scheme, separate from node health. There is no green edge.

| State | Color |
|-------|-------|
| Healthy / default | Translucent glass |
| Error on that connection | Translucent red |

Edge thickness encodes traffic volume over time (thicker = more traffic) and is independent of color.

### Service platform neon

| State | Color |
|-------|-------|
| Service is healthy | Green |
| Service has a problem | Red |

The platform neon reflects the health of the service you are standing on.

### Grid aggregate blocks

On the grid, a trace occupies one position as two adjacent aggregate blocks (see [Spatial Vocabulary](spatial-vocabulary.md)): a **Trace Aggregate Block** holding all spans that share the trace ID, and a **Log Aggregate Block** holding all logs with that trace ID. Their color is independent: the Trace Aggregate Block reflects its spans, the Log Aggregate Block reflects its logs.

**Each block takes the color of the highest-severity status it contains.** A single error span turns the whole Trace Aggregate Block red. A single warning log turns the Log Aggregate Block orange. If a Log Aggregate Block contains both a warning and an error, it is red, because error outranks warning.

| State | Color | Applies to |
|-------|-------|------------|
| Healthy | Green | Both aggregate blocks |
| Warning | Orange | Log Aggregate Block (a warning log, when no error is present) |
| Error | Red | Either block (an error span or an error log) |
| Absence (missing span) | Black | Trace Aggregate Block (a span expected in the trace did not arrive) |
| Idle | Grey | Both aggregate blocks |
| Hover highlight | White | Not a health state |

The severity order is error (red) > warning (orange) > normal (green). A block always shows its worst contained status.

Trace Aggregate Block **height** grows with the combined duration of all the trace's spans (a taller block took longer to complete) and is separate from color. Height and color read together: a tall red block is a slow, failed trace; a black block is a trace missing a span.

The block's **color and shape are what you read from a distance.** The error text and trace details are not printed on the block face; hover the block for its tooltip to see them (and press **F6** to copy).

### Diagnostics cube: spans

| State | Color |
|-------|-------|
| Healthy span | Green |
| Errored span | Red |

## Diagnostics log levels

Inside the Diagnostics cube, the logs wall color-codes each log line by log level. This is a separate scale from the grid/graph health-state colors above.

| Log level | Color |
|-----------|-------|
| Error | Red |
| Warning | Yellow |
| Info | White / grey |
| Debug | (one of the five levels; rounds out the scale) |
| Trace | (one of the five levels; rounds out the scale) |

Inside the Diagnostics cube, a warning log line is yellow. On the grid, a warning rolls up to orange on the Log Aggregate Block (when no error is present). Warning never appears on the service graph, which has no warning state.

## Related

- **For concept and design:** see [Overview](../Overview/index.md).
- **For navigation and travel:** see [Navigation model](navigation-model.md).
- **For readouts and boards:** see [Readouts and boards](readouts-and-boards.md).
- **For Tessa's energy state ("% Optimal"):** see [Tessa commands and runtime](assistant-commands.md).
