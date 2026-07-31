# Guided Tour

Walk through everything IAPM can do - without touching a single line of code. This tour takes about 15 minutes and covers both the Demo Grid and the Chaos Simulator.

---

## Part 1 - Explore the Demo Grid

The Demo Grid is the fastest way to see IAPM 3D in action. It generates a realistic service topology with live telemetry data, all running locally on your machine.

### Step 1: Launch IAPM 3D

Open IAPM 3D. If you haven't installed it yet, see the [installation guide](../../DC/3D/Guides/Installation/index.md).

!!! note "Version requirement"
    The Demo Grid requires IAPM 3D **v1.10 or later**. Check your version in the app settings.

### Step 2: Select the Demo Grid

In the **grid picker**, select **"Demo"**. Within a few seconds, demo services will begin appearing on the Grid.

### Step 3: Look Around the Grid

You're now standing on a live Grid populated with interconnected demo services. Take a moment to get oriented:

- **Services appear as blocks** on the Grid surface, arranged by their relationships
- **Connections between services** show how requests flow through the system
- **Color and activity indicators** reflect the health and traffic volume of each service

Use your mouse or controller to move around. Zoom in on a service to see more detail, or zoom out to see the full topology.

### Step 4: Switch Between Views

IAPM 3D offers multiple ways to visualize the same data:

| View | Shortcut | What it shows |
| --- | --- | --- |
| **Grid** | ++m++ | Services as blocks on the 3D platform surface |
| **Graph** | ++n++ | Services as nodes in a dependency graph |

Press ++n++ to switch to the **service graph**. Notice how the same services are now displayed as a network diagram showing dependencies. Press ++m++ to return to the grid.

### Step 5: Talk to Tessa

Tessa is IAPM's AI Assistant. Open the Tessa panel and try asking questions about the demo data:

- *"What services are running?"*
- *"Show me the slowest endpoints"*
- *"Are there any errors?"*
- *"Which service has the most dependencies?"*

Tessa works with demo data exactly the same way she works with production data - this is a great time to get familiar with what she can do.

### Step 6: Enter the Diagnostics cube

Press ++m++ for the Traces & Logs Camera View, click a trace cube to port down onto the grid, then click the rhombus on a Trace Aggregate Block to zoom into the **Diagnostics cube**. This is where you can inspect a single trace, read its span waterfall, and understand exactly what happened during a request.

Inside the Diagnostics cube:

- The **span waterfall** (north wall) shows the full journey of the request, each bar a span, its length the span's duration
- The **logs wall** (west wall) shows the trace's logs, colored by level, text readable
- **Error indicators** highlight where things went wrong (if any)

!!! success "Checkpoint"
    You've now seen the three core views of IAPM 3D: the Grid, the Graph, and the Diagnostics cube. Every feature you just used works identically with real production data.

---

## Part 2 - Inject Chaos

Now that you know how to navigate IAPM, it's time to break things on purpose. The Chaos Simulator lets you inject failures into a live microservice environment and watch IAPM detect and visualize them.

### Step 1: Open the Chaos Simulator

Go to [demo.iapm.app](https://demo.iapm.app){ target="_blank" } in your browser. A unique sandbox is created for you automatically - no signup required.

### Step 2: Generate Normal Traffic

Click the buttons to generate normal, healthy traffic. This creates baseline telemetry - requests flowing between services without errors.

Switch to IAPM and watch the services come alive. You should see activity indicators and healthy request traces appearing.

### Step 3: Inject a Latency Spike

Back in the Chaos Simulator, trigger a **latency** scenario. This introduces artificial delays into service responses.

In IAPM, look for:

- **Slower response times** on affected services
- **Trace waterfalls** that show elongated spans
- **Dependency chains** where the delay ripples downstream

### Step 4: Inject Errors

Trigger an **error** scenario. This generates HTTP 500 responses and exception traces.

In IAPM, watch for:

- **Red indicators** appearing on affected services
- **Error traces** in the Diagnostics cube with full stack information
- **Health changes** reflected in service status

### Step 5: Trigger a Cascading Failure

This is where it gets interesting. Trigger a **cascading failure** and watch as a problem in one service propagates to its dependents.

In IAPM, you'll see:

- **The failure origin** - the first service to fail
- **The propagation path** - downstream services turning red as failures cascade
- **The blast radius** - the full scope of affected services

### Step 6: Ask Tessa What Happened

With failures still active, open Tessa and ask:

- *"What went wrong?"*
- *"Which service caused the cascade?"*
- *"What's the root cause?"*

Tessa analyzes the telemetry in real time and can help you trace problems back to their source - exactly how you'd use her during a real incident.

!!! success "Checkpoint"
    You've now seen IAPM handle healthy traffic, latency spikes, errors, and cascading failures. Everything you just experienced works the same way with your own instrumented applications.

---

## Part 3 - What to Try Next

You've covered the basics. Here are some ideas to go deeper before connecting your own applications.

### Experiments to Try

- [ ] **Compare views during a failure** - Toggle between Grid (++m++) and Graph (++n++) during a cascading failure to see which view reveals the problem fastest
- [ ] **Race Tessa** - Inject a failure and try to find the root cause before Tessa does
- [ ] **Latency hunting** - Inject a subtle latency spike and practice tracing it through span waterfalls in the Diagnostics cube
- [ ] **Dependency mapping** - Use the service graph to map out all service dependencies, then predict what will happen when you fail a specific service

### Keep Going

When you're ready to move beyond the sandbox:

[Instrument Your Application :material-arrow-right:](../../Instrument/index.md){ .md-button .md-button--primary }
[Explore IAPM Features :material-cube-outline:](../../DC/3D/index.md){ .md-button }
[Browse Tutorials :material-map:](../../DC/3D/Tutorials/index.md){ .md-button }
