# Troubleshooting

!!! warning "Early Access"
    DeepCube Studio is in early access. If you encounter issues not listed here, please contact support.

{!template/subscription-required.mdp!}

## Common Issues

| Issue | Possible Cause | Resolution |
|-------|---------------|------------|
| **App won't start** | Unsupported OS version or missing system libraries | Verify your system meets the [minimum requirements](../Supported-Configurations/index.md). On macOS, ensure you are running macOS 12+ on Apple Silicon. |
| **App blocked on macOS** | macOS Gatekeeper blocks unidentified apps | Go to **System Settings** - **Privacy & Security** and allow the application to run. |
| **Can't connect to grid** | Network issue or incorrect credentials | Check your internet connection. Verify your DeepCube account credentials. Ensure your firewall allows outbound HTTPS on port 443 to `*.deepcube.ai`, `*.iapm.app`, and `*.immersivefusion.com`. |
| **Voice not working** | Microphone not connected or permissions denied | Ensure a microphone is connected and that DeepCube Studio has microphone permissions in your OS settings. On macOS, check **System Settings** - **Privacy & Security** - **Microphone**. |
| **Workspace not loading** | Connectivity issue or session expired | Check your network connection. Try signing out and signing back in. If the issue persists, restart the application. |
| **Chat history lost** | Application data was cleared or corrupted | Session persistence stores data locally. If local data was deleted or corrupted, previous sessions cannot be recovered. Ensure antivirus or cleanup tools are not removing application data. |
| **Session not restoring** | Application did not shut down cleanly | If the application was force-closed or crashed, session state may not have been saved. Restart the application normally. Chat history from completed messages should still be available. |
| **Pasted image not recognized** | Clipboard does not contain a supported image format | Ensure you copied a valid image (PNG, JPEG) to your clipboard. Screenshots taken with the OS screenshot tool are supported. |
| **Skills not available** | Running an older version of Studio | Update to v0.7.0 or later. DeepCube Studio checks for updates on launch. |

## Getting Help

If your issue is not listed above:

1. Check that you are running the latest version of DeepCube Studio
2. Restart the application
3. Contact Immersive Fusion support at [immersivefusion.com](https://www.immersivefusion.com){ target="_blank" }
