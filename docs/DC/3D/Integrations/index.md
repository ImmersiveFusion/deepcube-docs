# VR Headset Integrations

!!! warning "VR support is not actively maintained"
    VR is not a supported surface right now. These pages are kept for anyone already running a headset: the steps may still work, but VR is not currently a maintained part of the product.

DeepCube runs on keyboard and mouse. It can also connect to a supported VR headset, documented here for existing headset users.

## Supported Headsets

| Headset | Models | Connection | Guide |
|---------|--------|------------|-------|
| **Meta Quest** | Quest 2, Quest 3, Quest Pro | Quest Link (wired/wireless) | [Setup](Meta-Quest/index.md) |
| **HTC Vive** | Vive, Vive Pro, Vive Pro 2 | SteamVR | Coming soon |

## System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| GPU | NVIDIA GTX 1060 / AMD RX 580 | NVIDIA RTX 3070 / AMD RX 6800 |
| RAM | 8 GB | 16 GB |
| USB | USB 3.0 (for wired) | USB 3.1 |
| WiFi | 5 GHz (for wireless) | WiFi 6 |

## Quick Start

```mermaid
graph LR
    A[Install DeepCube] --> B[Setup VR Headset]
    B --> C[Launch DeepCube]
    C --> D[Auto-detect Headset]
    D --> E[Enter VR]
```

1. **Install DeepCube** on your PC
2. **Set up your VR headset** following manufacturer instructions
3. **Launch DeepCube** - it automatically detects connected headsets
4. **Put on your headset** and enter the immersive environment

## VR vs Desktop Experience

| Feature | Desktop | VR |
|---------|---------|-----|
| Navigation | WASD + Mouse | Walk + Teleport + Controllers |
| Selection | Click | Point + Trigger |
| AI Assistant | Voice commands + Keyboard chat | Voice commands |
| Spatial awareness | Monitor view | 360° immersion |
| Collaboration | Screen share | Shared VR space |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Headset not detected | Restart DeepCube after connecting headset |
| Poor performance | Lower graphics quality in Preferences |
| Tracking issues | Check room lighting and base stations |
| Wireless lag | Use 5 GHz WiFi, reduce distance to router |

!!! info "Additional Headset Support"
    We're continuously adding support for new VR headsets. [Contact us](../../../contact.md) to request specific hardware support.
