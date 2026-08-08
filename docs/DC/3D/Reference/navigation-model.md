---
title: Navigation model
diataxis: reference
tags: [reference, navigation, travel, camera, portals, controls]
---

# Navigation model

This page documents how you move through and view a grid in DeepCube.

## Two systems

| System | Moves the avatar | Purpose |
|--------|-------------------|---------|
| **Travel** | Yes | Click-to-teleport to any highlighted object in line of sight, plus walking for fine local movement |
| **Camera / view** | No | Switch what you are looking at (first-person, the grid, the service graph, the Tessa chat console) |

### Travel

Every portable object carries a rhombus marker.

| Marker state | Appearance | Meaning |
|---------------|------------|---------|
| At rest | Solid dark octahedron/rhombus | Object is not currently targeted |
| Highlighted | Glowing wireframe outline rhombus | Object is selectable; click to teleport there |

Click a highlighted object (or the rhombus on it) to teleport to it, from anywhere it is in line of sight. Fine, local movement after teleporting is done by walking, and **Space** jumps. In the main space (the grid, the service graph, the Core) you do not free-fly and you cannot rise continuously: Space is a jump for a momentary higher vantage, not sustained lift. You move by teleporting to highlighted objects, including clicking nodes in the Services & Dependencies Camera View to port to them. Free flight through the open space is Mosey's alone, in his autopilot mode.

**Inside a cube, you can swim.** The cubes are the exception. Inside a cube, jumping (**Space**) starts you swimming, and you can then move freely in all three dimensions up to the cube's ceiling. In the Diagnostics cube this has a clear use: you swim a large span waterfall, moving up and around the bars to read a complex trace from any angle. You can also swim in the other cubes (Research, Security, Zen), but they have no functional content yet, so there is nothing to do with it there for now.

### Camera / view

Persistent toolbar, bottom-right. None of these move the avatar.

The toolbar has four camera views plus a Home button. Each view is labeled on screen.

| Icon | On-screen label | Shortcut | View |
|------|-----------------|----------|------|
| Location pin | Avatar Camera View | **Escape** | First-person, wherever you currently are |
| Layers | Traces & Logs Camera View | **M** | The grid (Traces & Logs) |
| Globe | Services & Dependencies Camera View | **N** | The service graph |
| Chat | Console | **F12** | Tessa chat overlay on top of your current location |

The **Traces & Logs (M)** and **Services & Dependencies (N)** views are top-down overviews for scanning. The view itself does not move you, but **clicking an object in it ports you down onto that place** (a trace cube on the grid, or a node in the service graph), at which point you are inhabiting it. So the pattern is: open the view to scan from above, click the thing you want, and you land there.

### Home button

| Icon | On-screen label | Effect | Moves the avatar |
|------|-----------------|--------|-------------------|
| Home | Teleport to the Core | Teleports you to the Core | Yes |

Home is the one toolbar control that moves the avatar. It teleports you back to the Core, the hub you land on when you enter a grid.

## Consistency law

**If it highlights, you can go to it.** The same rule applies everywhere: graph nodes, board rows (Recent Errors, Services, Dependencies), portals, platforms below you, and grid aggregate blocks. Highlight, then click, teleports you there in every case.

## Information law

Most objects, platforms, and cubes carry a hover tooltip. Hover an object to see its tooltip, then press **F6** to copy the tooltip contents to the clipboard. Tooltips work both when you are next to an object and from the top-down camera views (Traces & Logs, Services & Dependencies), so you can read a block or node's details while scanning from above, before you port down to it.

## Portals

| Property | Detail |
|----------|--------|
| Activation | Proximity-activated |
| Closed state | Spinning tesseract, animated, at a distance |
| Open state | Luminous swirling ring, when you are close |
| Directionality | Two-ended; travel through either end |
| Visibility | You can see the destination through an open portal |

### Portal kinds

| Kind | Links | Behavior |
|------|-------|----------|
| **Fixed structural** | Core to graph root; the Portal Room to the cubes (Research, Security, Zen) | Permanent |
| **Transient recent-location** | Graph-root floor to recently visited services | Forms a ring on the graph-root floor; ephemeral shortcuts; despawn once stale |
| **Return-to-origin** | Diagnostics cube back to the specific grid Trace Aggregate Block you zoomed in from | Only the Diagnostics cube behaves this way; the Research, Security, and Zen cubes return to the Portal Room instead |

## Play / pause transport

| Control | Effect | Movement while active |
|---------|--------|------------------------|
| **Play** | World runs live | Normal |
| **Pause** | World freezes: sweep, arriving blocks, aging, and traffic all stop | You can still walk through the frozen snapshot |

Play/pause is available everywhere.

## Time travel

| Feature | Status |
|---------|--------|
| Time travel | Temporarily disabled |

## Controls quick reference

| Key / control | Action |
|----------------|--------|
| **W** | Move |
| **Space** | Jump (starts swimming inside a cube) |
| **Left-click** | Select / teleport to a highlighted object |
| **M** | Traces & Logs Camera View (the grid) |
| **N** | Services & Dependencies Camera View (the service graph) |
| **F12** | Console (open the Tessa chat) |
| **Escape** | Avatar Camera View (first-person) |
| **Home** | Teleport to the Core |

## Related

- **For concept and design:** see [Overview](../Overview/index.md).
- **For color states referenced while navigating:** see [Color legend](color-legend.md).
- **For the boards and readouts you navigate from:** see [Readouts and boards](readouts-and-boards.md).
