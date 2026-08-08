# System Requirements

!!! warning "Early Access"
    DeepCube Studio is in early access. System requirements may change as the application evolves.

DeepCube Studio is a lightweight native desktop application. It does not require a web browser, GPU acceleration, or VR hardware.

## Platform Support

| Platform | Status | Notes |
|----------|--------|-------|
| Windows | :material-check: Supported | Full feature support |
| macOS | :material-check: Supported | Apple Silicon |

## Windows Requirements

| Component | Requirement |
|-----------|-------------|
| **Operating System** | Windows 10 64-bit or later |
| **Processor** | 2 cores, 2.0 GHz or faster |
| **Memory** | 4 GB RAM |
| **Storage** | 500 MB available |
| **Display** | 1280 x 720 |
| **Internet** | Broadband connection |
| **Input** | Keyboard + mouse; microphone for voice interaction |

## macOS Requirements

| Component | Requirement |
|-----------|-------------|
| **Operating System** | macOS 12 (Monterey) or later |
| **Processor** | Apple Silicon (M1 or later) |
| **Memory** | 4 GB RAM |
| **Storage** | 500 MB available |
| **Display** | 1280 x 720 |
| **Internet** | Broadband connection |
| **Input** | Keyboard + mouse/trackpad; microphone for voice interaction |

## Runtime Dependencies

DeepCube Studio bundles its required runtime components. No separate installation of .NET or other frameworks is necessary.

## Network Requirements

DeepCube Studio requires network connectivity to communicate with the DeepCube backend.

| Traffic | Port | Protocol | Purpose |
|---------|------|----------|---------|
| Outbound | 443 | HTTPS | API and authentication |

### Firewall Configuration

Ensure your firewall allows outbound connections to:

- `*.deepcube.ai`
- `*.iapm.app`
- `*.immersivefusion.com`

## What Studio Does Not Require

Unlike the 3D client, Studio does not need:

- A dedicated GPU or graphics card
- Steam or any game platform
- A VR headset
- A web browser
