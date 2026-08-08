# Terms and Concepts

Understanding the terminology and concepts behind application performance monitoring is essential for getting the most out of DeepCube. This guide covers everything from foundational APM concepts to advanced observability techniques.

For quick, one-line definitions of the shared terms used across DeepCube, see the [Glossary](../Glossary/index.md). This section goes deeper into the concepts behind them.

## Core Concepts

Build your foundation with these essential concepts:

| Concept | Description |
|---------|-------------|
| [APM](APM/index.md) | Application Performance Management fundamentals and why they matter |
| [Observability](Observability/index.md) | The three pillars: logs, metrics, and traces |
| [DeepCube](DC/index.md) | How immersive 3D visualization transforms APM |

## Data Pipeline

Understand how telemetry flows from your application to actionable insights:

```mermaid
graph LR
    A[Your App] -->|Instrumentation| B[Telemetry Data]
    B -->|Collection| C[Processing]
    C -->|Correlation| D[DeepCube Visualization]
```

| Stage | Description |
|-------|-------------|
| [Instrumentation](Instrumentation/index.md) | Adding telemetry capture to your application code |
| [Collection](Collection/index.md) | Gathering, buffering, and transmitting telemetry data |
| [Correlation](Correlation/index.md) | Connecting related traces, logs, and metrics together |

## Frameworks

DeepCube integrates with industry-standard observability frameworks:

| Framework | Description |
|-----------|-------------|
| [OpenTelemetry](Observability/Frameworks/OpenTelemetry/index.md) | The vendor-neutral observability standard we support |
