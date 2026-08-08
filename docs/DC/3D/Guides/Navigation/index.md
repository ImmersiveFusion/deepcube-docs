# Navigation & Controls

<!-- TODO: Verify all keyboard shortcuts are accurate for current DeepCube version -->

Master the controls to move through your application's 3D environment efficiently. Desktop (keyboard and mouse) is the actively maintained navigation mode; VR controls are documented below for existing headset users but are not actively maintained.

| Icon | Meaning |
|------|---------|
| :material-clock: | Coming soon |
| :material-lock: | Not yet configurable |

## Desktop Controls

### Movement

| Action | Keys | Description | Status |
|--------|------|-------------|--------|
| Move Forward | `W` or hold both mouse buttons | Move toward where you're looking or move and turn if holding both buttons | |
| Move Backward | `S` | Move away from where you're looking | |
| Strafe Left | `A` | Slide left while maintaining view direction | |
| Strafe Right | `D` | Slide right while maintaining view direction | |
| Jump | `Space` | Jump for a momentary higher look. Inside a cube, jumping starts you swimming (free vertical movement) | :material-lock: |
| Descend | `Ctrl` | Move down while swimming inside a cube | :material-lock: |
| Sprint | `Shift` + movement | Move faster in any direction | |

### Camera & View

| Action | Control | Description |
|--------|---------|-------------|
| Look Around | Right mouse button + drag | Rotate your view in any direction |
| Zoom In | Scroll wheel up | Get closer to objects |
| Zoom Out | Scroll wheel down | See more of the environment |
| Reset View | `Home` | Return to default camera position |

### Selection & Interaction

| Action | Control | Description | Status |
|--------|---------|-------------|--------|
| Select | Left-click | Interact with world object | |
| Context Menu | Right-click | Show available actions | :material-clock: |
| Deselect | `Escape` | Clear current selection | |
| Follow Trace | - | Animate along the request path | :material-clock: |

### UI & Panels

| Action | Keys | Description | Status |
|--------|------|-------------|--------|
| Toggle AI Assistant | `C` | Open/close the AI assistant panel | :material-clock: |
| Toggle Metrics | - | Show/hide metrics overlay | :material-lock: |
| Toggle Logs | `L` | Show/hide log panel | :material-clock: |
| Toggle Traces | `T` | Show/hide trace details | :material-clock: |
| Traces & Logs Camera View | `M` | Switch to the grid | |
| Services & Dependencies Camera View | `N` | Switch to the service graph | |

### General

| Action      | Keys  | Description                   | Status |
|-------------|-------|-------------------------------|--------|
| Console     | `F12` | Open the developer console    |        |
| Preferences | `F10` | Open preferences and settings |        |

## VR Controls

VR is not actively maintained right now. If you already run a headset, the controls below still apply.

### HTC Vive

See [HTC Vive Integration](../../Integrations/HTC-Vive/index.md) for detailed setup.

| Action | Control | Description |
|--------|---------|-------------|
| Teleport | Trackpad press + aim + release | Move to pointed location |
| Select | Trigger | Select service or UI element |
| Grab | Grip buttons | Grab and manipulate objects |
| Menu | Menu button | Open radial menu |
<!-- | AI Assistant | Grip + voice | Activate voice assistant | -->

### Meta Quest

See [Meta Quest Integration](../../Integrations/Meta-Quest/index.md) for detailed setup.

| Action | Control | Description |
|--------|---------|-------------|
| Teleport | Thumbstick + release | Move to pointed location |
| Select | Trigger | Select service or UI element |
| Grab | Grip | Grab and manipulate objects |
| Menu | Menu button | Open radial menu |
<!-- | AI Assistant | Press A + speak | Activate voice assistant | -->

## Navigation Tips

### Understanding Visual Indicators

| Indicator | Meaning |
|-----------|---------|
| Green glow | Healthy service |
| Red glow | Failure - errors (a service on fire also shows a burning texture) |
| Black node | Absence - a phantom service that should be there but never reported |
| Grey node | Idle - present but not currently active |
| Photons flying along a line | Active request flow (a request emits a photon to the target, a response sends one back) |
| Translucent red line | An error on that connection |
| Thick lines | High throughput |

### The Grid

A structured, organized layout where services are arranged in a grid pattern.

<!--
**Best for:**

- Large systems with many services
- Comparing metrics across services
- Finding specific services quickly
- Presentations and screenshots

**Features:**

- Services arranged in orderly rows and columns
- Consistent spacing for easy scanning
- Sort by name, latency, error rate, or throughput
- Filter to show only specific service types
- Clear labels visible at all zoom levels

 **Controls:**

| Action | Control | Description |
|--------|---------|-------------|
| Sort Services | `S` then select criteria | Reorder grid by metric |
| Filter | `F` then type | Show matching services |
| Group By | `G` + `1-4` | Group by namespace/type/status/custom | 
-->

### The Service Graph

A dynamic, force-directed layout showing actual service relationships and dependencies.

<!-- **Best for:**

- Understanding service dependencies
- Tracing request flows
- Identifying architectural patterns
- Troubleshooting cascading failures

**Features:**

- Services positioned by their connections
- Connected services cluster together
- Request flows visualized as animated paths
- Dependency depth visible at a glance
- Isolated services stand out visually

**Controls:**

| Action | Control | Description |
|--------|---------|-------------|
| Pin Service | `P` on selected | Lock position in space |
| Unpin All | `Shift` + `P` | Release all pinned services |
| Expand Cluster | Double-click cluster | Show hidden services |
| Collapse Cluster | `Shift` + double-click | Group related services | -->

### Switching Views

| Action | Control |
|--------|---------|
| Traces & Logs Camera View | `M` |
| Services & Dependencies Camera View | `N` |

<!-- 
## Camera Modes

### Free Flight (Default)

Move freely in any direction. Best for exploring and getting an overview of your system.

### Orbit Mode

Press `O` to orbit around a selected service. Useful for examining a specific service from all angles.

### Follow Mode

Press `F` after selecting a trace to follow requests through your system. The camera automatically tracks the data flow.

### Top-Down Mode

Press `2` for a birds-eye view of your topology. Good for seeing the overall architecture.

### First-Person Mode

Press `1` to return to standard first-person navigation.
 -->

## Related

- [Preferences](../Preferences/index.md) - Customize controls and display settings
- [AI Assistant](../../Overview/ai-assistant.md) - Voice and chat interaction
- [VR Integrations](../../Integrations/index.md) - Headset-specific guides
