# Your First DeepCube Session

**Difficulty:** :material-star: Beginner | **Time:** ~10 minutes

Your first time inside DeepCube. This walkthrough takes you from launch to confidently navigating your application's 3D environment, reading visual indicators, and having your first conversation with Tessa.

## What You'll Learn

- How to move through the 3D environment
- What the colors and animations mean
- How to switch between the grid and the service graph
- How to interact with Tessa, your AI assistant

---

## Step 1: Launch and Enter Your Grid

1. **Open DeepCube** from Steam or your desktop shortcut.
2. **Sign in** with your DeepCube account credentials.
3. **Select a grid** from the grid selector. If you don't have a production grid yet, choose the demo grid.
4. **Click Enter** to load into the 3D environment.

!!! info "What you see"
    The environment loads around you. You're standing on the Grid - a dark, expansive platform stretching out in every direction. Your services appear as glowing objects arranged in rows and columns in front of you. Each glows with its health color. Your current location is shown at the top center of the screen, directly under the grid name.

---

## Step 2: Look Around

1. **Hold the right mouse button** and drag to rotate your view.
2. **Scroll the mouse wheel** to zoom in and out.
3. Look in every direction - above you, below you, behind you. The environment extends in all directions.

!!! info "What you see"
    As you pan your view, you see the full scope of your application laid out spatially. Services closer to you appear larger and more detailed. Distant services are smaller but still visible, their color indicators readable even from afar. Thin lines connect services to each other, and photons fly along the active ones, showing live traffic flowing between them.

---

## Step 3: Move Through the Space

1. **Press `W`** to move forward toward your services.
2. **Press `A` and `D`** to strafe left and right.
3. **Press `S`** to move backward.
4. **Press `Space`** to jump for a momentary higher vantage point.
5. **Hold `Shift`** while moving to sprint.

!!! info "What you see"
    You teleport to a service and walk its immediate area. As you get close, its details become clearer: you can read its name, hover it for its metrics, and observe the connections branching out from it. Jumping with `Space` gives a momentary higher look. For the full topology at a glance, press `N` for the Services & Dependencies Camera View. (Free, continuous vertical movement is swimming, which happens only inside a cube.)

!!! tip "ProTip"
    If you ever feel lost, check the location readout at the top center of your screen, directly under the grid name. It shows where you currently are.

---

## Step 4: Read the Visual Indicators

1. **Look at the colors** of your services as you walk past them.
2. **Watch the connecting lines** between services - notice the photons flying along the active ones.

| Color | Meaning |
|-------|---------|
| :material-circle:{ style="color: #4CAF50" } Green | Healthy - operating normally |
| :material-circle:{ style="color: #F44336" } Red | Failure - errors detected (a service on fire also shows a burning texture) |
| ⚫ Black | Absence - a phantom service that should be there but never reported |
| :material-circle:{ style="color: #9E9E9E" } Grey | Idle - present but not currently active |

For the full color law across every surface, see the [Color legend](../Reference/color-legend.md).

| Line | Meaning |
|------|---------|
| Photons flying along a line | Active request flow between services (a request emits a photon to the target; a response sends one back) |
| Thick lines | High throughput connections |
| Thin lines | Low throughput connections |
| Translucent red line | An error on that connection |

!!! info "What you see"
    Most of your services glow green, humming along normally. You might spot a few glowing red - those are worth investigating. The lines connecting services carry photons at different rates and come in different thicknesses, painting a live picture of how traffic flows through your architecture. It's like watching your application breathe.

---

## Step 5: Switch Between the Grid and the Service Graph

1. **Press `M`** to switch to the grid (if not already active). Services snap into an organized rows-and-columns layout.
2. **Press `N`** to switch to the service graph. Services rearrange based on their actual connections.

!!! info "What you see"
    In the **grid**, your services are arranged in a clean, orderly layout - easy to scan and compare. When you press `N` for the **service graph**, the layout transforms. Services drift and settle into clusters based on their dependencies. Tightly connected services pull toward each other. Isolated services float to the edges. The force-directed physics simulation makes the layout feel alive as services find their natural positions.

---

## Step 6: Meet Tessa

1. **Open the chat panel** by clicking the chat icon or pressing the chat shortcut.
2. **Type:** `Hello, Tessa`
3. **Press Enter** to send.

!!! info "What you see"
    Tessa responds in the chat panel. She's your AI assistant - ready to answer questions about your system, run diagnostics, find problems, and guide your investigation. The chat panel shows the conversation history and Tessa's responses.

---

## Step 7: Ask About Your System

1. **Type:** `What's the health of my system?`
2. **Press Enter** and wait for Tessa's response.

!!! info "What you see"
    Tessa runs a health check across your entire grid. She reports back with a summary - how many services are healthy, how many have elevated latency, and whether any are in a critical state. She might call out specific services that need attention, giving you an instant situational overview without clicking through a single dashboard.

!!! tip "Energy System"
    Each interaction with Tessa uses energy. Your energy refills over time. The energy indicator shows your remaining balance - use it wisely during investigations.

---

## Step 8: Select a Service

1. **Walk toward a service** that catches your eye, or teleport to its platform (maybe one glowing red).
2. **Left-click** on the service to select it.

!!! info "What you see"
    The selected service highlights with a visible selection indicator. Hover the service for its tooltip, which shows its name, key metrics (throughput, latency, error rate), and status. The connections leading to and from this service become more prominent, making it easy to see what talks to what.

---

## Step 9: Enter the Diagnostics cube

1. **Press `M`** for the Traces & Logs Camera View (the top-down view), then **click a trace cube** to port down onto the grid. You land next to it, where each trace sits as a Trace Aggregate Block (its spans) and a Log Aggregate Block (its logs).
2. **Click the rhombus on a Trace Aggregate Block** to zoom deeper into that trace. You descend into the Diagnostics cube.

!!! info "What you see"
    The environment shifts. You're no longer looking at the grid from outside, you are inside a single trace in the Diagnostics cube. The trace un-flattens onto two walls: the span waterfall on the north wall (each bar a span, its length the span's duration) and the logs wall on the west wall (the trace's logs, colored by level, text readable). Tessa's context is now focused on this trace. It's the deepest level of detail DeepCube offers.

---

## Step 10: Return and Explore

1. **Navigate back** to the Grid using the navigation controls.
2. You're now ready to explore on your own.

---

## What to Explore Next

Now that you know the basics, try these scenarios:

| Next Step | Scenario |
|-----------|----------|
| Troubleshoot a real problem | [Investigating a Latency Spike](latency-spike.md) |
| Diagnose cascading failures | [Root Cause Analysis with Tessa](root-cause-analysis.md) |
| Understand your architecture | [Understanding Your Service Topology](service-graph.md) |

## Quick Controls Reference

| Action | Control |
|--------|---------|
| Move | `W` `A` `S` `D` |
| Look | Right mouse + drag |
| Zoom | Scroll wheel |
| Move up/down | `Space` / `Ctrl` |
| Sprint | `Shift` + movement |
| Select | Left-click |
| Traces & Logs Camera View | `M` |
| Services & Dependencies Camera View | `N` |
