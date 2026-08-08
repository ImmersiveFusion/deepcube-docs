# DeepCube

**DeepCube** is Immersive Fusion's approach to [Application Performance Management](../APM/index.md) that uses 3D visualization to help engineers understand complex distributed systems.

## The Challenge with Traditional APM

Modern applications are complex. A single user request might touch dozens of services, databases, and external APIs. Traditional APM tools present this complexity through:

- Flat dashboards with disconnected charts
- Service maps that become unreadable at scale
- Tab-switching to compare different views
- Time-consuming mental model reconstruction

## The DeepCube Solution

DeepCube transforms how you understand your systems by rendering your application architecture as an interactive 3D environment:

```mermaid
graph LR
    A[Telemetry Data] --> B[DeepCube Platform]
    B --> C[3D Spatial Model]
    C --> D[Desktop Client]
    C --> E[Web Interface]
```

## Service Types on the Service Map

DeepCube automatically discovers and displays two types of services:

| Type | Definition | Billable | How Detected |
|------|-----------|----------|--------------|
| **Instrumented Service** | An application instance emitting telemetry via OpenTelemetry SDK | Yes (1 node) | `service.name` in OTel Resource |
| **Inferred Service** | An entity referenced by span attributes with no direct telemetry | No | `db.system`, `server.address`, `peer.service` in span attributes |

Both appear on the Service Map. When an inferred service becomes instrumented (you add OpenTelemetry to it), DeepCube automatically upgrades it in place, preserving its connections and history.

## Key Characteristics

| Feature | Description |
|---------|-------------|
| **3D Visualization** | Application topology rendered in three dimensions with spatial relationships |
| **Real-Time Data** | Live telemetry via [OpenTelemetry](../Observability/Frameworks/OpenTelemetry/index.md) |
| **AI-Assisted** | AI Assistant for root cause analysis and anomaly explanation |
| **Collaborative** | Multiple team members can explore the same environment |

## How It Differs from Traditional APM

| Aspect | Traditional APM | DeepCube |
|--------|-----------------|---------------|
| **Visualization** | 2D dashboards and graphs | 3D spatial environment |
| **Context** | Switch between multiple views | Unified visual context |
| **Navigation** | Query-based exploration | Walk and teleport navigation |
| **Alerts** | Text-based notifications | Visual anomaly highlighting |
| **Scale** | Cluttered at high complexity | Spatial layout handles scale |
| **Collaboration** | Screen sharing | Shared virtual space |

## Use Cases

### Incident Response

Navigate directly to problem areas highlighted in red. See upstream and downstream dependencies instantly. Understand blast radius at a glance.

### Architecture Review

Walk through your system topology. Identify unexpected dependencies. Spot single points of failure visually.

### Onboarding

New team members can explore the architecture interactively. Build mental models faster through spatial understanding.

### Capacity Planning

Visualize traffic patterns and resource utilization. See where bottlenecks are likely to form.

## From concept to product

DeepCube is the idea; the product that realizes it is documented separately. It ships as three surfaces onto the same platform, and the product documentation covers what each one does, how to install or access it, and how to use it.

See the [DeepCube product documentation](../../../DC/index.md) to get started.

## See Also

- [APM](../APM/index.md) - Application Performance Management fundamentals
- [Spatial Observability](../Spatial-Observability/index.md) - The category DeepCube belongs to
- [Observability](../Observability/index.md) - The three pillars of observability
- [Instrumentation](../Instrumentation/index.md) - How to instrument your applications
