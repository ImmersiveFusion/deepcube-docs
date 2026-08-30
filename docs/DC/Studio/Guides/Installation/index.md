---
description: Install DeepCube&trade; Studio on Windows or macOS from the alpha installer. No Steam needed, and a subscription is required.
---

# Installation

{!template/subscription-required.mdp!}

!!! warning "Alpha channel only"
    DeepCube Studio is currently in alpha. Only the **alpha** channel is published, on both Windows and macOS. Beta and stable builds will follow.

DeepCube Studio is a native desktop application distributed as a standalone installer. It does not require Steam or any game platform - it is downloaded directly from Immersive Fusion.

## Download

[Latest Alpha Build :material-microsoft-windows:](https://downloads.immersivefusion.com/release/alpha/DCS.latest.msi){ .md-button .md-button--primary }
[Latest Alpha Build :material-apple:](https://downloads.immersivefusion.com/release/alpha/DCS.latest.dmg){ .md-button }

A subscription is required to use DeepCube Studio.

## Windows

1. Download the DeepCube Studio installer from the link above
2. Run the installer and follow the on-screen prompts
3. Launch DeepCube Studio from the Start menu or desktop shortcut
4. Sign in with your DeepCube account credentials
5. Select a grid to connect to

!!! note "Requirements"
    Windows 10 or later (64-bit). See [Supported Configurations](../../Supported-Configurations/index.md) for full details.

## macOS

1. Download the DeepCube Studio disk image from the link above
2. Open the disk image and drag `DCS.app` to your `Applications` folder
3. Open `Terminal` and remove the app from quarantine:

```bash
xattr -d com.apple.quarantine /Applications/DCS.app
```

4. Launch DeepCube Studio from `Applications`
5. Sign in with your DeepCube account credentials
6. Select a grid to connect to

!!! note "Requirements"
    See [Supported Configurations](../../Supported-Configurations/index.md) for full details.

## Updates

During early access, updates are released frequently. DeepCube Studio checks for updates on launch and prompts you to install new versions when available.

## Differences from DeepCube

DeepCube Studio is a separate application from DeepCube. Key differences:

| | Studio | 3D |
|-|--------|----|
| **Distribution** | Direct download from Immersive Fusion | Steam or offline installers |
| **Engine** | Avalonia (native UI) | Unity 3D |
| **Focus** | AI chat, workspaces, artifacts | 3D visualization |
| **Install size** | Lightweight | Larger (3D engine) |
