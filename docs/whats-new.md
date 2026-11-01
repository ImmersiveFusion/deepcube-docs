---
description: Recent feature highlights across DeepCube&trade;, DeepCube Web, and DeepCube Studio, with links to the full release notes for each surface.
---

# What's New

Recent updates and features across DeepCube. For complete version history, see the release notes for [DeepCube](DC/3D/release-notes.md), [DeepCube Web](DC/Web/release-notes.md), and [DeepCube Studio](DC/Studio/release-notes.md).

---

## Latest Highlights

### Sign In with Steam, and Tessa Asks First (3D v1.23.1, v1.23.0)

On the Grid, a service is now one platform however many instances serve it, and phantoms are drawn only once they have been judged. Launching from Steam now signs you in with Steam, falling back to your saved session if that does not work, and after a browser sign-in the next launch signs you straight in while that session is still valid. Tessa asks before she clears the service map, runs a Shoebox or changes a preference. Spans that recorded an exception, or answered with an HTTP 5xx or 429, now count as failures, so some services may show a higher error rate than before.

!!! warning "Before you update: link Steam to your DeepCube account"
    **Go to [id.deepcube.ai/account](https://id.deepcube.ai/account) and link Steam first, before your next launch from Steam.** From 1.23.1, launching from Steam signs you in with Steam first, before your saved session. If Steam is not linked to your DeepCube account, you are signed in to a separate, new account, without your grids or your subscription.

| Feature | Description |
|---------|-------------|
| **Sign In with Steam** | Launch from Steam and the client signs you in with your Steam account and goes straight to the Lobby; if Steam sign-in does not work, it uses your saved session, then the Login screen |
| **One Sign-In That Stays** | Sign in once in your browser, and the next launch signs you straight in while that session is still valid; sessions from earlier versions do not carry over |
| **Tessa Asks First** | Before she clears the service map, builds or runs a Shoebox, requests a replay or changes a preference, she shows you what she wants to run; one yes covers that kind of action for the session, while sharing a Shoebox and using the web ask every time |
| **One Platform per Service** | A deploy or a restart no longer starts a new platform with fresh history, and the nameplate counts live and quiet instances |
| **Phantoms, Judged Before They Are Drawn** | A service too new to judge no longer appears as a phantom and then clears itself; calls to a public host name that none of your reporting services uses, and to databases, are drawn as external dependencies |
| **Forty Skies** | The full-range HDR skies are back, listed by name, and clouds now drift; set the new Sky movement setting to 0 to keep them still |

See the [1.23.1](DC/3D/release-notes.md#1.23.1) and [1.23.0](DC/3D/release-notes.md#1.23.0) release notes for everything in this update.

### Immersive APM is now DeepCube

The product you know as Immersive APM, or IAPM, is now **DeepCube™**, the spatial observability platform. The three surfaces are DeepCube, DeepCube Web, and DeepCube Studio.

This is a name change only. Your account, grids, API keys, and telemetry are unchanged, and existing links to these docs keep working. Release notes for versions that shipped earlier keep the name they shipped under.

### Tessa Gets Hands, and Charts That Tell the Truth (3D v1.18.8, Web 3.177.5)

Tessa can now drive the Shoebox sandbox for you, end to end, and answer from what is actually on your grid. On the Web side, every chart on the Insights board was rebuilt so the numbers match the telemetry underneath them.

| Feature | Description |
|---------|-------------|
| **Tessa Drives Shoebox** | Ask her to stand up a scenario and break it: she creates the sandbox, sends the scenario, runs it, and hands back a link |
| **Tessa Reads the Map** | Ask about phantoms and she answers from the phantoms actually on your grid, with the reason each one is there |
| **Chat Window, Second Pass** | Select and copy the transcript, resize, zoom, image paste, input history, and it reopens where you left it |
| **Failure Cues on the Service Graph** | Phantoms tear away to the rim on strain lines; error nodes hold their callers at a cleared standoff |
| **Every Insights Chart Rewritten** | All 32 charts rebuilt against the current telemetry, with readable units and honest empty states |
| **Faster Grid Picker** | Descriptions inline on the rows, and the list arrives in one pass |

### Mosey & Personal Subscription (3D v1.15, Web 3.140)

Mosey graduates from preview in 3D, with voice and console workspace switching, a three-bucket radial menu, and gamepad cursor support. The Web Portal rolls out the Personal Product License model end to end.

| Feature | Description |
|---------|-------------|
| **Voice & Console Workspace Switching** | Switch grids by voice or console command without leaving the world |
| **Three-Bucket Mosey Menu** | Help, Quick Read, and Deep Analysis with workspace-aware entries and GenAI Cost in trace context |
| **Gamepad Cursor & Stick Orbiting** | Screen-center reticle for in-world targeting, with right-stick orbiting |
| **Mosey Idle Behaviors** | Wandering, skits, prop interactions, and chatter during long sessions |
| **Personal Product License** | Tessa Personal is now a first-class subscription with proper graduated tiered pricing |
| **Admin Seat Management** | Portal admin pages for assigning, revoking, and attesting seats across a tenant |
| **Tier & Energy Source on Energy Bar** | Energy bar shows tier and energy source so personal vs grid usage is no longer ambiguous |

### In-World Content Screens & Per-Tab Workspaces (3D v1.14, Studio v0.8)

Big density jump in the 3D world with per-facility content screens, and Studio makes every chat tab its own workspace.

| Feature | Description |
|---------|-------------|
| **Per-Facility Content Screens** | Services and dependencies carry their own error, log, and cost summary screens in the 3D world |
| **Row-Tap Teleport** | Tap any row in a table to teleport directly to the matching facility |
| **New Service Graph Engine** | Force-directed layout with smoother transitions and stable node placement |
| **Per-Tab Workspaces** | Each Studio chat tab binds to its own workspace, so multiple projects run side by side |
| **Tool Card UI** | Studio renders Tessa's actions as cards with side-by-side before/after diffs |
| **Session Restore** | Studio reopens your tabs and chat history automatically |
| **macOS Studio** | Studio now ships a macOS disk image alongside the Windows installer |

### Skills System & Multimodal Vision (3D v1.12, Studio v0.7)

Tessa gains extensible capabilities and the ability to analyze images.

| Feature | Description |
|---------|-------------|
| **Skills** | Tessa can now use modular skills for specialized tasks, with a browsable skill catalog |
| **Multimodal Vision** | Paste screenshots with Ctrl+V and ask Tessa to analyze what you see |
| **Diagnostics Tools** | New diagnostic and analysis tools give Tessa richer troubleshooting insights |
| **Memory & Context** | Tessa remembers context across sessions for more coherent conversations |

### Smarter Diagnostics & Vision (Web 3.131)

| Feature | Description |
|---------|-------------|
| **Smarter Diagnostics** | Tessa fetches correlated performance data and alert summaries in a single query |
| **Energy Dashboard Redesign** | See energy usage per grid, per tenant, and per tier with breakdown charts |
| **Vision Support** | Send screenshots and images to Tessa for visual analysis |

---

## Recent Updates

### October 2026

- **3D v1.23.1**: Sign in with Steam when you launch from Steam (link Steam to your DeepCube account first), parts of the client that need you signed in now sign you in on the spot
- **3D v1.23.0**: One sign-in that stays between launches; Tessa asks before she clears the service map, runs a Shoebox or changes a preference; one platform per service with live and quiet instance counts; phantoms judged before they are drawn; forty skies; `/node-ids`
- **Web 3.189.0**: Snapshot page and an Around This Span tab, the grid graph keeps one node per service through restarts ([breaking change](DC/Web/release-notes.md#3.189.0) for API clients)
- **Web 3.183.0**: Tessa counts your conversation against your energy, not her fixed instructions; invitations grant nothing until accepted; billing fixes

### September 2026

- **3D v1.18.27**: Preferences rebuilt, Tessa reads and changes some preferences, frame-rate prompt, Shoebox checks a diagram before it runs
- **Studio v1.6.0**: Attached images stay in the conversation, and Tessa answers as Tessa on a model configured in the settings file

### August 2026

- **3D v1.18.8**: Tessa drives the Shoebox sandbox and reads the map, chat window second pass (selection, resize, zoom, image paste, input history, commands), phantom and error cues on the service graph, faster grid picker
- **Web 3.177.5**: All 32 Insights charts rewritten against the current telemetry, readable chart values, honest empty states, node metering fix for multi-grid accounts
- **Studio v1.4.3**: Renamed to DeepCube Studio, sign-in and release notifications moved to the new addresses
- **All surfaces**: Immersive APM is now DeepCube

### July 2026

- **3D v1.18**: In-world chat window for Tessa with streaming replies and tool cards, steadier service graph in busy scenes
- **Web 3.172.3**: Much faster grid list, grids re-tier on plan change, onboarding and billing accuracy fixes
- **Studio v1.3.1**: Assistant platform update

### June 2026

- **3D v1.17**: Companion autopilot tours, phantom nodes, the Spatial Observatory, choose your sign-in browser, workspace persona for Tessa
- **Web 3.169**: Choose Tessa's voice, personal usage view, energy recharge countdown
- **Studio v1.3**: Single workspace shell, voice conversation mode, workspace persona for Tessa, clearer AI energy limit

### May 2026

- **3D v1.15**: Mosey graduates from preview, voice and console workspace switching, three-bucket radial menu, gamepad cursor and stick orbiting
- **Web 3.141**: Stage 2 subscription enablement with cancel cleanup, build pipeline fixes
- **Web 3.140**: Personal product license rollout, admin seat management, tier and energy source on the energy bar

### April 2026

- **3D v1.14.11**: 1.14.x stabilization series, smaller and more reliable Windows installer, macOS disk image, Mosey preview
- **3D v1.14**: Per-facility content screens, row-tap teleport, new force-directed service graph, Mosey companion, macOS disk image
- **3D v1.12.1**: Richer service platform context for Tessa
- **Studio v0.8.23**: 0.8.x stabilization series, hardened Windows and macOS installers, embedded browser startup fixes
- **Studio v0.8**: Per-tab workspace binding, tool card UI with diffs, session restore, macOS distribution
- **Studio v0.7.1**: Output formatting fixes
- **Web 3.132**: Fixed Tessa losing context between multi-step tool turns
- **3D v1.12**: Skills system, multimodal vision, diagnostics tools, Studio feature parity
- **Web 3.131**: Smarter diagnostics, energy dashboard redesign, vision support
- **Studio v0.7**: Multimodal vision, Skills, memory and context

### March 2026

- **3D v1.11**: OpenTelemetry data model adoption, improved service graph, better tooltips
- **Web 3.110**: Faster telemetry queries, OTel terminology alignment, secure AI gateway
- **Studio v0.5**: Multi-tab chat, split pane view, session persistence, workspace browser
- **Studio v0.1**: Initial early access release with AI chat and workspace management

### February 2026

- **Web 3.90**: AI Assistant chat with streaming and voice, energy system, invitation system, permission management, Personal Access Tokens, achievements, GitHub login, demo grid selector

### January 2026

- **3D v1.10**: Live service graph, demo telemetry, energy system UI, streamlined authentication
- **Web 3.82**: Usage dashboard with sparkbox visualizations, navigation redesign, welcome modal

### December 2025

- **Web 3.71**: Dashboard overhaul, Angular 21 upgrade, span view, network graph, dark/light themes

### April 2025

- **3D v1.8**: Spatial Observatory, .NET 9.0 rollup

### September 2025

- **3D v1.9**: Tessa AI Assistant debut (chat + voice), Diagnostics cube, grid picker redesign, ProTips, water environment, macOS experimental support

---

## Coming Soon

| Feature | Product | Status |
|---------|---------|--------|
| Alerts configuration | Web | In development |
| Full macOS support | 3D | Experimental |
| Linux support | Studio | Planned |

---

## Feature Requests

Have an idea for DeepCube? We'd love to hear from you:

- [Discord community](https://discord.gg/zevywnQp6K){ target="_blank" } - Share ideas and vote on features
- [Email feedback](mailto:feedback@immersivefusion.com) - Direct feedback to our team

---

## Stay Updated

| Channel | Link |
|---------|------|
| Release notes (3D) | [View releases](DC/3D/release-notes.md) |
| Release notes (Web) | [View releases](DC/Web/release-notes.md) |
| Release notes (Studio) | [View releases](DC/Studio/release-notes.md) |
| YouTube | [Tutorials & demos](https://www.youtube.com/@immersivefusion){ target="_blank" } |
| LinkedIn | [Company updates](https://www.linkedin.com/company/immersivefusion){ target="_blank" } |
