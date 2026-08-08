# DeepCube Web

DeepCube™ Web gives you browser-based access to your application telemetry. No installation required - access from any device with a modern browser.

[Launch DeepCube Web :material-web:](https://portal.iapm.app){ .md-button .md-button--primary target="_blank" }

## Key Capabilities

| Feature | Description |
|---------|-------------|
| **Dashboards** | Monitor application health, latency, throughput, and error rates |
| **Trace Analysis** | Span waterfall view, network graphs, and flame graphs |
| **Grid Management** | Create, configure, and organize telemetry data containers |
| **API Keys** | Generate and manage credentials for instrumentation |
| **Account Management** | Subscriptions, billing, team members, and settings |
<!-- | **Alerts** | Configure notifications for performance thresholds | -->

## DeepCube Web vs 3D

| Use Case | DeepCube Web | DeepCube |
|----------|:--------:|:------------:|
| Quick status check | :material-check: | |
| Account management | :material-check: | |
| API key generation | :material-check: | |
| Trace waterfall view | :material-check: | :material-check: |
| Deep troubleshooting | | :material-check: |
| 3D visualization | | :material-check: |
| AI Assistant | :material-check: | :material-check: |

## Getting Started

1. **Log in** - Choose your authentication method (Entra ID or Local/Social)
2. **Select a grid** - Choose an existing grid or create a new one
3. **Explore** - Click **Enter** to view your application telemetry

```mermaid
graph LR
    A[Log In] --> B[Select Grid]
    B --> C[View Dashboard]
    C --> D[Analyze Traces]
    D --> E[Configure Alerts]
```

## Recent Features

| Feature | Description |
|---------|-------------|
| Span View Tab | Waterfall timeline for detailed span analysis |
| Network Graph | Interactive service dependency visualization |
| Nested Span Tags | Collapsible tree view for hierarchical data |
| Dark/Light Themes | Full theme support across all components |

See [Release Notes](release-notes.md) for complete version history.

## Next Steps

| Action | Link |
|--------|------|
| View detailed guides | [DeepCube Web Guides](Guides/index.md) |
| Check browser support | [Supported Browsers](Supported-Configurations/index.md) |
| Instrument your app | [Instrumentation Guide](../../Instrument/index.md) |
| Try 3D visualization | [DeepCube](../3D/index.md) |
