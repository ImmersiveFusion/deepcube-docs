# Troubleshooting

This page covers common issues you may encounter with DeepCube and how to resolve them.

---

## Installation & Launch

| Symptom | Cause | Resolution |
|---------|-------|------------|
| App won't install via Steam | Insufficient disk space or Steam client out of date | Ensure at least 4 GB of free disk space. Update Steam to the latest version via **Steam > Check for Steam Client Updates**. |
| App crashes on launch | Missing or outdated GPU drivers | Update your GPU drivers to the latest version from [NVIDIA](https://www.nvidia.com/drivers){target="_blank"}, [AMD](https://www.amd.com/en/support){target="_blank"}, or [Intel](https://www.intel.com/content/www/us/en/download-center){target="_blank"}. |
| "Unsupported GPU" error | GPU does not meet minimum requirements (DirectX 11 / Vulkan 1.1) | Check [Supported Configurations](../Supported-Configurations/index.md) for minimum GPU requirements. Integrated graphics are not supported. |
<!-- SP-074: the Steam path, settings folder, and Player.log paths on this page still say the currently-shipping name.
     Per R-DOCS-005, docs that quote a shipping string stay on the old
     string until the code ships the new one. Do not "fix" these to
     DeepCube ahead of the build. -->

| Antivirus blocking installation | Security software flagging the Unity runtime or installer | Add the DeepCube installation directory to your antivirus exclusion list. The default Steam path is `C:\Program Files (x86)\Steam\steamapps\common\IAPM`, which still carries the old folder name until the Steam depot is renamed, so use it exactly as written. |
| Offline installer fails | Corrupted or incomplete download | Re-download the installer and verify the file hash, then run it again. |
| App crashes immediately after splash screen | Corrupted local settings or cache | Delete the settings folder at `%APPDATA%\..\LocalLow\Immersive Fusion\IAPM` and relaunch the application. |

---

## Connection & Data

| Symptom | Cause | Resolution |
|---------|-------|------------|
| No telemetry data appearing | Application not connected to the DeepCube backend, or no instrumented services sending data | Verify your connection to `otlp.deepcube.ai` on port 443. Confirm your instrumented applications are configured to send OpenTelemetry data to the correct endpoint. See [Network Requirements](#network-requirements) below. |
| "Connection failed" error | Firewall or proxy blocking outbound HTTPS traffic | Ensure ports 443/TCP are open for all endpoints listed in [Network Requirements](#network-requirements). If behind a corporate proxy, configure the proxy settings in your system environment variables. |
| Data stops updating after a while | Network interruption or session timeout | Check your network connection. The application will automatically reconnect when connectivity is restored. If the issue persists, restart the application. |
| Demo telemetry not loading | Demo mode not enabled or backend unreachable | Open **Settings > Data Source** and confirm Demo Telemetry is selected. Verify you have an active internet connection to `api-azure.deepcube.ai`. |

---

## Performance

| Symptom | Cause | Resolution |
|---------|-------|------------|
| Low framerate / stuttering | GPU under heavy load or graphics quality set too high | Lower the graphics quality in **Settings > Graphics**. Close other GPU-intensive applications. Ensure your system meets the [recommended specifications](../Supported-Configurations/index.md). |
| High memory usage | Large number of services or traces loaded simultaneously | Reduce the visible time window for telemetry data. Close unused panels and overlays. Systems with many services (100+) benefit from 32 GB RAM. |
| Rendering glitches | Outdated GPU drivers or unsupported display resolution | Update GPU drivers to the latest stable version. Try switching between fullscreen and windowed mode via **Settings > Display**. |
| Application freezes during high telemetry load | Telemetry volume exceeding client processing capacity | Reduce the data density by narrowing the time range filter. If you have very high-throughput services, consider filtering to specific service namespaces. |

---

## AI Assistant (Tessa)

| Symptom | Cause | Resolution |
|---------|-------|------------|
| Tessa not responding | No active internet connection or backend service temporarily unavailable | Verify connectivity to `api-azure.deepcube.ai` on port 443. Check the connection status indicator in the Tessa chat panel. |
| Voice commands not recognized | Microphone not configured or browser permissions not granted | Ensure your microphone is set as the default input device in your OS audio settings. Grant microphone access when prompted by the application. Check **Settings > Audio > Input Device**. |
| Energy depleted message | AI usage quota has been consumed for the current period | Energy replenishes automatically over time. You can continue using DeepCube without AI features while energy recharges. Check your current energy level in the Tessa panel. |
| Chat history lost | Session ended or application was closed without saving | Chat history is tied to the active session. Starting a new session begins a fresh conversation. This is expected behavior - Tessa maintains context only within a single session. |

---

## VR

VR is not actively maintained right now. If you already run a headset, the issues below still apply.

| Symptom | Cause | Resolution |
|---------|-------|------------|
| VR headset not detected | SteamVR not installed or headset not properly connected | Install [SteamVR](https://store.steampowered.com/app/250820/SteamVR/){target="_blank"} and verify your headset appears in the SteamVR dashboard before launching DeepCube. Check USB and DisplayPort/HDMI connections. |
| Motion sickness / discomfort | Sensitivity to smooth locomotion or low framerate in VR | Enable **Comfort Mode** in **Settings > VR** to use teleportation-only movement. Ensure your system maintains 90 FPS in VR - lower the graphics quality if needed. Take regular breaks. |
| Controllers not mapping correctly | Non-default controller bindings or unsupported controller model | Reset controller bindings to defaults in **SteamVR > Settings > Controllers > Manage Controller Bindings**. DeepCube currently supports Meta Quest (via Quest Link) and HTC Vive controllers. |
| Blurry or distorted display in VR | Headset IPD not adjusted or render resolution too low | Adjust the IPD (inter-pupillary distance) on your headset. Increase the render resolution in **SteamVR > Settings > Video > Render Resolution**. |

---

## Authentication

| Symptom | Cause | Resolution |
|---------|-------|------------|
| Login loop / can't authenticate | Browser cookie or cache issue preventing OAuth completion | Clear your browser cache and cookies for `portal.deepcube.ai`. Try using a different default browser. Ensure pop-ups are not blocked for the authentication domain. |
| Session expired frequently | System clock out of sync or unstable network connection | Verify your system clock is accurate and set to auto-sync. Check that your network connection is stable - frequent disconnects will invalidate sessions. |
| Browser-based auth not opening | Default browser not configured or blocked by security policy | Set a default browser in your OS settings. If in a corporate environment, confirm that `portal.deepcube.ai` is not blocked by your organization's web filter. Try launching the auth URL manually from the login screen. |

---

## Network Requirements

DeepCube requires outbound HTTPS access to the following endpoints. Ensure these are permitted through your firewall and proxy configuration.

| Endpoint | Port | Protocol | Purpose |
|----------|------|----------|---------|
| `otlp.deepcube.ai` | 443 | TCP (HTTPS) | Telemetry ingestion - receives OpenTelemetry data from your instrumented applications |
| `api-azure.deepcube.ai` | 443 | TCP (HTTPS) | API backend - powers Tessa, authentication, and application data |
| `portal.deepcube.ai` | 443 | TCP (HTTPS) | Web portal - browser-based authentication and account management |
| `*.steamcontent.com` | 443 | TCP (HTTPS) | Steam CDN - application downloads and updates (Steam installs only) |
| `*.steampowered.com` | 443 | TCP (HTTPS) | Steam platform - license validation and update checks (Steam installs only) |

!!! tip "Proxy Configuration"
    If your organization uses an HTTPS inspection proxy, ensure the above domains are added to the inspection bypass list. TLS inspection can interfere with real-time telemetry streaming.

---

## Collecting Diagnostic Information

When contacting support, include the following to speed up resolution:

1. **Application version** - found in **Settings > About**
2. **Player.log file** - located at:
    - Windows: `%APPDATA%\..\LocalLow\Immersive Fusion\IAPM\Player.log`
    - macOS: `~/Library/Logs/Immersive Fusion/IAPM/Player.log`
    - Linux: `~/.config/unity3d/Immersive Fusion/IAPM/Player.log`
3. **System specs** - OS version, GPU model, driver version, RAM
4. **Steps to reproduce** - what you were doing when the issue occurred

---

## Getting More Help

| Channel | Details |
|---------|---------|
| :material-chat: Discord Community | [Join the Immersive Fusion Discord](https://discord.gg/6WmQWHAXyp){target="_blank"} for community support and direct access to the team |
| :material-email: Email Support | Contact [support@immersivefusion.com](mailto:support@immersivefusion.com) for technical issues |
| :material-message: Live Chat | Available at [immersivefusion.com](https://immersivefusion.com){target="_blank"} during business hours (US Eastern) |
| :material-bug: Bug Reports | Report bugs via Discord or email with the [diagnostic information](#collecting-diagnostic-information) listed above |
