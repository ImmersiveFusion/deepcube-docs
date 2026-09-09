# Navigation & Controls

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
| Jump | `Space` | Jump for a momentary higher look | |
| Sprint | `Shift` + movement | Move faster in any direction | |

The arrow keys move as well, and do the same as `W`, `A`, `S` and `D`.

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
| Context Menu | Right-click | Show available actions | |
| Deselect | `Escape` | Clear current selection | |
| Follow Trace | - | Animate along the request path | :material-clock: |

### UI & Panels

| Action | Keys | Description | Status |
|--------|------|-------------|--------|
| Traces & Logs Camera View | `M` | Switch to the grid | |
| Services & Dependencies Camera View | `N` | Switch to the service graph | |

### General

| Action      | Keys  | Description                   | Status |
|-------------|-------|-------------------------------|--------|
| Help        | `F1`  | Open the help dialog          |        |
| Copy        | `F6`  | Copy                          |        |
| Pause       | `P`   | Pause                         |        |
| Preferences | `F9`  | Open preferences and settings |        |
| Main Menu   | `F10` | Open the main menu            |        |
| Console     | `F12` | Open the developer console    |        |

!!! note "Not available on every screen"
    `F1` and `F9` work once you are in a grid. The lobby and the login screen do
    not have them, and neither dialog opens there.

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

### Meta Quest

See [Meta Quest Integration](../../Integrations/Meta-Quest/index.md) for detailed setup.

| Action | Control | Description |
|--------|---------|-------------|
| Teleport | Thumbstick + release | Move to pointed location |
| Select | Trigger | Select service or UI element |
| Grab | Grip | Grab and manipulate objects |
| Menu | Menu button | Open radial menu |

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

### The Service Graph

A dynamic, force-directed layout showing actual service relationships and dependencies.

### Switching Views

| Action | Control |
|--------|---------|
| Traces & Logs Camera View | `M` |
| Services & Dependencies Camera View | `N` |

## Related

- [Preferences](../Preferences/index.md) - Customize controls and display settings
- [AI Assistant](../../Overview/ai-assistant.md) - Voice and chat interaction
- [VR Integrations](../../Integrations/index.md) - Headset-specific guides
