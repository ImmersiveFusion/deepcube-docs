---
title: The Spatial Model
diataxis: explanation
tags: [explanation, spatial-model, navigation, grid, core]
---

# The Spatial Model

This page explains how DeepCube organizes your whole system as one navigable, vertical space you move through by changing altitude.

Most observability tools ask you to tab between disconnected views: a service map in one tab, a trace list in another, logs in a third. DeepCube makes a different choice. Instead of separate screens, it gives you a single continuous place with your system laid out in it, and you investigate by moving your position rather than by switching context. Understanding that one idea, that everything is a location in one space, is the key to understanding why the rest of the product is shaped the way it is.

## Where you begin: the lobby

When you log in, you land in the **lobby**. It is deliberately open: anyone can enter, with no subscription and nothing to prove at the door. The lobby itself is free; what is priced is the product you do inside a grid. So the lobby is the threshold, not the workspace.

From the lobby you choose where to go. A **Select a Grid** panel lists the grids available to you, grouped by environment and region, and you pick one and enter it yourself. There is no ticket and no guided handoff; you walk in. Grids carry a visibility state that tells you how they are shared: a **Public** grid is open to anyone (the demo grids are Public), while a **Shared** grid belongs to an organization you are part of. A typical user sees the demo grids plus their own.

The lobby is intentionally spacious and, today, quiet. You stand alone on a lit platform until you choose a grid and step into it. Entering a grid is where the spatial model proper begins.

From the lobby you can also reach the **Spatial Observatory**, a separate place with its own purpose. It is not part of entering a grid, so this page does not cover it.

## The master layout: one vertical stack of altitudes

Once you are inside a grid, the single most important thing to understand is that the places you can go are not scattered around; they are **altitudes** stacked in one continuous vertical space. From the bottom of the scene to the top, the stack reads:

- **The service graph** sits at the base. This is the structure of your system, the service skeleton and how the services connect.
- **The Core** sits in the middle. This is the hub, the floating island you land on when you join a grid, and it is where you orient yourself and choose where to go next.
- **The Portal Room** sits directly beneath the Core, one floor below where you spawn, in the basement. It holds the portals to the other cubes in the environment (Research, Security, Zen). Diagnostics is not among them: you reach the Diagnostics cube by selecting a trace on the grid, not from the Portal Room.
- **The grid** (the live Traces and Logs activity) sits above the Core, the temporal view of what is happening right now.
- **The Filter Funnel** is the apex, at the very top. It represents the direction the product is heading (a layer that distills the raw flow down to what matters), rather than a feature you use today. Treat it as a statement of intent about where the top of the stack leads.

This ordering is meaningful, not decorative: structure at the base, the hub in the middle, live activity above it, distillation at the top. Because it is one space rather than a set of tabs, the altitudes stay physically related. You can stand on the Core floor, look down, and click a platform in the service graph below you, because the graph is literally beneath you. The whole product is spatial, so even the way its tools are arranged is spatial.

## The Core: a compass hub with four cubes

The Core is laid out like a compass, with a large translucent themed cube at each cardinal point, its label floating inside it:

- **Diagnostics** to the north
- **Research** to the south
- **Security** to the west
- **Zen** to the east

These cubes are best understood as **workspaces you send things to**, each with its own lens or focus. Diagnostics is the one to know first: it is the destination for examining a trace. When you find a trace out on the grid and want to take it apart, you send it to the Diagnostics cube, where it un-flattens into its logs and its span waterfall for you to walk through. The other cubes carry their own focuses, and Research, Security, and Diagnostics correspond to the focus lenses Tessa can adopt, which is why the cubes sit where those lenses live. (For how those helpers relate, see [Mosey and Tessa](companion-and-assistant.md).)

## The paired pattern: a preview screen beside a portal

The Core is a hub, and it uses one consistent wayfinding pattern for reaching the two big views. Each major view has a **preview screen** (a live window you look through but do not click) placed beside a **portal** (a door you step through to travel there):

- On the southwest side, a **Services** preview screen showing a field of red and green service nodes sits beside the portal down to the service graph.
- On the northeast side, a **Traces and Logs** preview screen sits beside the portal up to the grid.

The preview screens are live, so they double as a glance-ahead: look at the window to see the current state of that view, then step through the door next to it. You never travel blind, and you never have to guess which door leads where. The preview shows you; the portal takes you.

## Why this shape

The point of the whole arrangement is that you **change altitude in one space instead of tabbing between disconnected views**. When structure, hub, and live activity are stacked in one continuous world, moving between them is a physical motion you can see and feel, rather than a jump to an unrelated screen that reloads and reorients you. Your sense of where you are, and of how the piece you are looking at connects to the rest of the system, is preserved as you move. That continuity is the reason a 3D system stays workable rather than overwhelming: the layout itself teaches you where everything is relative to everything else.

## Where to next

- **Why DeepCube draws what is missing:** see [Rendering Absence](rendering-absence.md).
- **Mosey the companion and Tessa the assistant:** see [Mosey and Tessa](companion-and-assistant.md).
- **What Tessa is and how she reasons:** see [Tessa - Your AI Assistant](ai-assistant.md).
- **The section overview:** see [Overview](index.md).
