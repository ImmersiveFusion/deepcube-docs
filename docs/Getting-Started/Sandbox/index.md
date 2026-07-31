# Sandbox

Explore IAPM with demo data, no instrumentation and no account required. Both sandbox experiences below are **demo grids**: they carry sample telemetry so you can move through a real system in IAPM without sending any data of your own. You view a demo grid in the IAPM client, and we recommend **IAPM 3D**, where a grid renders as a space you move through.

[Download IAPM 3D :material-download:](../../DC/3D/Guides/Installation/index.md){ .md-button .md-button--primary }

The same demo grids are also viewable in [IAPM Web](../../DC/Web/index.md) from the browser.

## Two Demo Grids to Explore

Both are demo grids; they differ in where the data comes from and whether you can drive failures.

| Feature | Demo grid | Chaos Simulator |
| --- | --- | --- |
| **What is it?** | Built-in demo grid inside IAPM 3D | A demo grid you drive from the open-source web app at [demo.iapm.app](https://demo.iapm.app){ target="_blank" } |
| **Setup** | None, just select "Demo" in the grid picker | None, opens in your browser and creates a sandbox for you |
| **Best for** | Learning the 3D interface, navigation, and Tessa | Testing failure scenarios, seeing how IAPM handles chaos |
| **Data source** | A prepared telemetry stream for a healthy service topology | Live OpenTelemetry data from a simulated microservice app you control |
| **View it in** | IAPM 3D | IAPM 3D or IAPM Web |
| **Interactive failures** | No, shows a healthy demo topology | Yes, inject latency, errors, timeouts, cascading failures |

!!! tip "Start here"
    New to IAPM? Start with the **Demo grid** to get comfortable with the interface, then move to the **Chaos Simulator** to see how IAPM handles real-world problems. Follow the [Guided Tour](guided-tour.md) for a step-by-step walkthrough of both.

---

## Demo Grid

The Demo grid is a built-in demo grid with a realistic service topology and telemetry, so you can explore the full 3D experience immediately. It appears in the grid picker in IAPM 3D.

### How to Use

1. Launch **IAPM 3D**
2. Open the **grid picker**
3. Select **"Demo"**
4. Demo services appear on the Grid, start exploring

That's it. No accounts, no API keys, no instrumentation of your own.

### What You Get

| Feature | Details |
| --- | --- |
| **Realistic topology** | Multiple interconnected services with dependencies |
| **Live telemetry** | Metrics, traces, and logs generated in real time |
| **Full navigation** | The grid, the service graph, the Diagnostics cube - everything works |
| **Tessa** | Ask the AI Assistant questions about the demo data |

---

## Chaos Simulator

The [OpenTelemetry Chaos Simulator](https://github.com/ImmersiveFusion/if-opentelemetry-chaos-simulator-sample){ target="_blank" } is an open-source web application that lets you inject failures into a simulated microservice environment and watch IAPM respond in real time.

![Chaos Simulator Interface](https://github.com/ImmersiveFusion/if-opentelemetry-chaos-simulator-sample/raw/main/.img/screenshot.png)

### How to Use It

1. Go to [demo.iapm.app](https://demo.iapm.app){ target="_blank" }
2. A unique sandbox is created automatically for you
3. Click buttons to generate traffic and inject chaos
4. Open the grid in [IAPM 3D](../../DC/3D/index.md) to watch the telemetry appear live (or in [IAPM Web](../../DC/Web/index.md) from the browser)

### What You Can Simulate

| Scenario | Effect |
| --- | --- |
| **Normal traffic** | Healthy request patterns across services |
| **High latency** | Slow response times that ripple through the system |
| **Errors** | HTTP 500 responses and exception traces |
| **Timeouts** | Connection and request timeouts |
| **Cascading failures** | Failures that propagate from one service to its dependents |

### Your Sandbox Is Isolated

Each session is completely independent:

- **Unique instance** - Created automatically when you access the simulator
- **Persistent** - Bookmark the URL to return to the same sandbox later
- **Isolated** - Your chaos doesn't affect other users

!!! info "Real-time only"
    The Chaos Simulator generates real-time data. Historical data is not retained between sessions.

---

## Next Steps

[Follow the Guided Tour :material-compass:](guided-tour.md){ .md-button .md-button--primary }
[Launch Chaos Simulator :material-flask:](https://demo.iapm.app){ .md-button target="_blank" }
[Instrument Your Own App :material-arrow-right:](../../Instrument/index.md){ .md-button }
