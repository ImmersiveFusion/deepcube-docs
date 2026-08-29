---
description: Version history for DeepCube Studio, which is in early access. Newest first.
---

# DeepCube Studio Release Notes

!!! warning "Early Access"
    DeepCube Studio is in early access. Features and interfaces may change between releases.

## Version History

### Renamed to DeepCube <small>August 7, 2026</small> { id="renamed-to-deepcube" }

**Introduction:**

IAPM Studio is now **DeepCube™ Studio**. This is a name change only. Your account, your grids, your API keys, and your telemetry are unchanged, and no action is needed on your part.

Entries below this one keep the name they shipped under, so the record stays accurate.

### 1.3.0 <small>June 30, 2026</small> { id="1.3.0" }

**Introduction:**

Studio reaches 1.0 and beyond, consolidating everything since the 0.8.x line. The biggest change is a single, workspace-bound shell: instead of juggling multiple windows, Studio now runs one window tied to the workspace you're in and switches in place. Voice gets a proper end-to-end listen loop with a single Silent Mode control, Tessa can adopt a workspace's persona behind a consent prompt, and the chat shows when your AI energy resets.

**New Features:**

- **Single Workspace Shell**: Studio now runs as one window bound to the active workspace. Switching workspaces rebuilds the shell in place rather than opening new windows, your open tabs are remembered per workspace, and Studio reopens to your last workspace. A workspace picker is available from the new-tab button and at startup.
- **Voice Conversation Mode**: A single Silent Mode control governs both the microphone and Tessa's voice: turn conversation on and Studio listens and speaks, turn it off for silence. Recognized speech is echoed into the chat as it is heard.
- **Workspace Persona for Tessa**: Point Studio at a workspace and Tessa can adopt that workspace's persona, after an explicit consent prompt. Tessa never adopts a workspace's guidance without your approval, the choice is remembered across restarts, and you are only re-prompted when the workspace's guidance files change.

**Improvements:**

- **Clearer AI Energy Limit**: When you reach your AI energy budget, the chat now shows when your AI energy resets instead of a misleading "no response" message, and the energy indicator shows your current state (Optimal, Conserving, or Replenishing).
- **Auto-Named Tabs**: New chat tabs are named automatically from Tessa's first response; renaming a tab yourself always wins.
- **Tab Isolation**: Each chat tab is fully isolated, so responses no longer leak between tabs or windows.

**Bug Fixes:**

- Fixed the conversation toggle so turning it on opens the microphone, and suppressed the duplicate spoken bubble while in Silent Mode.
- Fixed the latest prompt sticking to the top of the chat so you can always see which question the current answer belongs to.
- Fixed Windows installer issues that could drop files from the package.

### 0.8.23 <small>April 20, 2026</small> { id="0.8.23" }

**Introduction:**

A stabilization series across the 0.8.x line, focused on shipping the Windows and macOS installers reliably and hardening the embedded browser startup. If you are upgrading from 0.8.0, this is the recommended 0.8.x build to install.

**Improvements:**

- **Reliable macOS Disk Image**: The macOS disk image flow is hardened end to end, the installed app is consistently named **IAPM Studio**, proper signing on unsigned ship builds, and reliable artifact downloads.
- **Polished Windows Installer**: Windows installer publishes as **IAPM Studio** with refreshed dialog and banner artwork, and the installer link step resolves harvested file sources cleanly.
- **Hardened Embedded Browser Startup**: The embedded browser now initializes in the correct order, redirects its user data folder out of restricted locations, and logs initialization failures so support can diagnose them.
- **Cleaner Per-OS Publish Pipelines**: Publish pipelines split per operating system so Windows and macOS builds run on their native build agents and produce predictable artifacts.

**Bug Fixes:**

- Fixed embedded browser startup failures caused by initialization order and restricted user data folder paths.
- Fixed installer link errors by resolving harvested file sources through the correct bind path.
- Fixed the macOS app bundle name so the published bundle is consistently named **IAPM Studio**.

### 0.8.0 <small>April 16, 2026</small> { id="0.8.0" }

**Introduction:**

This release makes Studio genuinely multi-workspace: every chat tab now binds to its own workspace, so you can work on several projects side by side without cross-talk. A redesigned tool card surface shows Tessa's actions with side-by-side diffs, chat sessions survive restarts, and Studio is now available for both Windows and macOS.

**New Features:**

- **Per-Tab Workspace Binding**: Each chat tab can target a different workspace, with a workspace picker available from the new-tab button and a current-workspace indicator in the status bar.
- **Tool Card UI**: Tessa's tool actions render as expandable cards with side-by-side before/after diffs so you can see exactly what she changed.
- **Session Restore**: Your open tabs and chat history are restored automatically when you reopen Studio.
- **macOS Distribution**: Studio now ships a macOS disk image alongside the Windows installer.

**Improvements:**

- Rebranded app shell to **IAPM Studio** with a matching Windows installer experience.
- Background authentication token refresh so long sessions no longer hit expired-token errors.
- Installer pipeline overhauled for both Windows (MSI) and macOS (DMG) distribution, with cleaner upgrades and a new blob-published download flow.
- Version is now shown on the login screen for easier support and troubleshooting.

**Bug Fixes:**

- Fixed startup crash related to embedded browser initialization and user data folder location.
- Fixed race condition where switching workspaces could spawn a ghost tab.
- Fixed workspace switching losing chat state mid-conversation.

### 0.7.1 <small>April 5, 2026</small> { id="0.7.1" }

**Introduction:**

This patch cleans up Tessa's output rendering for more consistent formatting in chat responses.

**Bug Fixes:**

- Fixed assorted output formatting glitches in Tessa's responses.

### 0.7.0 <small>April 3, 2026</small> { id="0.7.0" }

**Introduction:**

This release adds the ability to paste images directly into prompts for visual analysis, along with the Skills system and memory for richer AI interactions.

**New Features:**

- **Multimodal Vision**: Paste images into prompts for Tessa to analyze alongside your telemetry data.
- **Skills**: Tessa can now use modular skills for specialized tasks.
- **Memory and Context**: Tessa remembers context across sessions for more coherent conversations.

### 0.5.0 <small>March 27, 2026</small> { id="0.5.0" }

**Introduction:**

This release introduces multi-tab chat with split pane support, so you can run multiple AI conversations side by side. Sessions are saved and restored across restarts.

**New Features:**

- **Multi-Tab Chat**: Run multiple conversations with Tessa simultaneously.
- **Split Pane View**: Drag to split, reorder, and arrange conversation panes.
- **Session Persistence**: Chat history survives application restarts.
- **Workspace Browser**: Browse workspace files and copy paths from the file tree.

**Improvements:**

- Welcome banner and active agent count in the status bar.
- Improved tool result visibility.

**Bug Fixes:**

- Fixed Escape key not canceling active requests.
- Fixed voice stopping behavior.
- Fixed workspace switching issues.

### 0.1.0 <small>March 16, 2026</small> { id="0.1.0" }

**Introduction:**

Initial early access release of IAPM Studio, a cross-platform desktop application for interacting with your telemetry through Tessa.

**New Features:**

- **AI Chat Interface**: Chat with Tessa using natural language to explore your telemetry.
- **Cross-Platform**: Available for Windows, with macOS and Linux support planned.
- **Workspace Management**: Browse and navigate your workspace files.
