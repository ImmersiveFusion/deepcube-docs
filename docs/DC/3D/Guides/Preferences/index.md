# Preferences

Access preferences by pressing `F10` → **Main Menu** → **Preferences**. Customize DeepCube to match your workflow and comfort.

| Icon | Meaning |
|------|---------|
| :material-clock: | Coming soon |
| :material-lock: | Not yet configurable |

## Display Settings

| Setting | Description | Default | Status |
|---------|-------------|---------|--------|
| Resolution | Screen resolution for windowed mode | Native | |
| Quality | Graphics quality preset | High | |
| Field of View | Camera FOV (60-120) | 90 | :material-clock: |
| VSync | Synchronize with monitor refresh | On | :material-clock: |
| Fullscreen | Full screen or windowed mode | Windowed | |

## Audio Settings

| Setting | Description | Default | Status |
|---------|-------------|---------|--------|
| Master Volume | Overall audio level | 80% | :material-clock: |
| Effects | UI sounds and notifications | 100% | :material-clock: |
| Ambient | Environmental audio | 50% | :material-clock: |
| Voice | AI Assistant voice responses | 100% | :material-clock: |

## Control Settings

| Setting | Description | Default | Status |
|---------|-------------|---------|--------|
| Mouse Sensitivity | Look-around speed | Medium | :material-lock: |
| Invert Y-Axis | Invert vertical mouse movement | Off | :material-lock: |
| Movement Speed | Base movement speed | Normal | :material-lock: |
| Sprint Multiplier | Speed increase when sprinting | 2x | :material-lock: |

### Mouse Navigation

- **Both mouse buttons held** - Move forward
- **Right mouse button + move** - Pan camera

### Key Bindings

!!! info "Coming Soon"
    Customizing keyboard shortcuts is not yet available.

## VR Comfort Settings

| Setting | Description | Default | Status |
|---------|-------------|---------|--------|
| Locomotion Type | Smooth walk with optional teleport | Smooth |  :material-lock: |
| Snap Turning | Discrete rotation angles | Off | :material-lock: |
| Turn Angle | Degrees per snap turn | 45° | :material-lock: |
| Vignette | Reduce peripheral vision during movement | Off | :material-lock: |
| Seated Mode | Adjust height for seated play | Off | :material-lock: |

!!! tip "Motion Sensitivity"
    If you experience discomfort in VR, enable **Snap Turning** and **Vignette** for a more comfortable experience.

## AI Assistant Settings

| Setting | Description | Default | Status |
|---------|-------------|---------|--------|
| Voice Activation | Enable "Hey Tessa" wake word | Off | :material-lock: |
| Voice Profile | AI Assistant voice selection | Default | :material-clock: |
| Response Length | Brief, standard, or detailed | Standard | :material-lock: |
| Auto-suggestions | Show proactive insights | On | :material-lock: |

## Connection Settings

| Setting | Description | Default | Status |
|---------|-------------|---------|--------|
| Server Region | Preferred data center region | Automatic | :material-lock: |
| Auto-reconnect | Automatically reconnect on disconnect | On | :material-lock: |
| Connection Timeout | Seconds before connection attempt fails | 30s | :material-lock: |

## Resetting Preferences

To reset all preferences to defaults, delete the preferences file:

<!-- TODO (SP-074, fire-day gated): the on-disk folder is still
     "Immersive Fusion/Immersive APM". Update these three paths to the
     DeepCube folder name only once the shipped app actually creates it. -->

- **Windows:** `%USERPROFILE%\AppData\LocalLow\Immersive Fusion\Immersive APM\preferences.json`
- **macOS:** `~/Library/Application Support/Immersive Fusion/Immersive APM/preferences.json`
- **Linux:** `~/.config/Immersive Fusion/Immersive APM/preferences.json`
