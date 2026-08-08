# System Requirements

DeepCube runs on Windows, with experimental support for macOS. Linux support is planned.

## Platform Support

| Platform | Status | Notes |
|----------|--------|-------|
| Windows | :material-check: Supported | Full feature support |
| macOS | :material-flask: Experimental | Some features may be limited |
| Linux | :material-clock: Planned | Coming soon |

## Windows Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Operating System** | Windows 10 64-bit | Windows 11 64-bit (latest) |
| **Processor** | 4 cores, 3.0 GHz | 6 cores, 3.5 GHz |
| **Graphics** | DirectX 12, 3 GB VRAM | DirectX 12, 8 GB VRAM |
| **Memory** | 8 GB RAM | 32 GB RAM |
| **Storage** | SSD, 2 GB available | SSD, 4 GB available |
| **Display** | 1280 × 720 | 1920 × 1080 or higher |
| **Internet** | Broadband connection | Broadband connection |
| **Input** | Keyboard + mouse | Keyboard + mouse + microphone |

### VR Requirements (Windows)

!!! warning "Experimental"
    VR support is experimental. Some functionality may be unavailable or limited.

For VR headset support, you'll need additional hardware:

| Component | Requirement |
|-----------|-------------|
| **Graphics** | NVIDIA GTX 1060 / AMD RX 580 or better |
| **Memory** | 16 GB RAM minimum |
| **USB** | USB 3.0 port (for wired headsets) |
| **Headset** | OpenXR compatible (Meta Quest, HTC Vive) |

## macOS Requirements (Experimental)

!!! warning "Experimental Support"
    macOS support is experimental. Some features may not work as expected. VR headset support is not available on macOS.

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Operating System** | macOS 13 (Ventura) | macOS 14 (Sonoma) |
| **Processor** | Apple M1 or Intel 4 cores | Apple M2 or Intel 6 cores |
| **Graphics** | Metal capable, 3 GB | Metal capable, 8 GB |
| **Memory** | 8 GB RAM | 16 GB RAM |
| **Storage** | SSD, 2 GB available | SSD, 4 GB available |
| **Display** | 1280 × 720 | Retina display |
| **Internet** | Broadband connection | Broadband connection |

## Network Requirements

DeepCube requires network connectivity to function:

| Traffic | Port | Protocol | Purpose |
|---------|------|----------|---------|
| Outbound | 443 | HTTPS | API and authentication |
| Outbound | 5671 | AMQP | Real-time data streaming |

### Firewall Configuration

Ensure your firewall allows outbound connections to:

- `*.deepcube.ai`
- `*.iapm.app`
- `*.immersivefusion.com`
- Customer-specific message broker URLs (provided during onboarding)

## Checking Your System

Not sure if your system meets the requirements?

1. **Windows:** Right-click Start → System → Check specs
2. **macOS:** Apple menu → About This Mac

## Troubleshooting Performance

If DeepCube runs slowly:

1. Lower graphics quality in **Preferences** → **General** → **Rendering Quality**
2. Close other GPU-intensive applications
3. Ensure your graphics drivers are up to date
4. Check that you meet minimum requirements
