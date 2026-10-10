# Preferences

Press `F9` to open preferences, once you are in a grid. The lobby and the login
screen do not have it.

Preferences are grouped into categories, each with its own sections. Every setting
below is saved to your machine and applies immediately unless noted.

!!! note "Tessa can change some of these"
    Settings marked :material-robot: can be changed by asking Tessa, as well as from
    this screen. The rest are deliberately out of her reach - rendering settings are
    expensive to apply, and sign-in and redaction are not hers to touch.

## World

What the grid draws, and how long it keeps it.

### Visibility

| Setting | What it does | Default | |
|---------|--------------|---------|---|
| Trace blocks | Show blocks for traces on the grid. | On | :material-robot: |
| Log blocks | Show blocks for logs on the grid. | On | :material-robot: |
| Facilities | Show process facilities. | On | :material-robot: |
| Publishers | Show publisher blocks. | On | :material-robot: |
| Consumers | Show consumer blocks. | On | :material-robot: |

### Blocks

| Setting | What it does | Default | |
|---------|--------------|---------|---|
| Keep errored blocks | Errored blocks stay on the grid instead of ageing out. | Off | :material-robot: |
| Keep lost blocks | Lost blocks stay on the grid instead of ageing out. | Off | :material-robot: |
| Detect phantom nodes | Show services that are called but never seen. | On | :material-robot: |

!!! tip "Keeping blocks while you investigate"
    **Keep errored blocks** and **Keep lost blocks** are the two to reach for mid-investigation.
    With them off, the thing you were about to look at can age out from under you.

### Scene

| Setting | What it does | Default | Status |
|---------|--------------|---------|--------|
| Grid map | Which grid map variant to load. | First variant | :material-clock: |
| Avatar | Which avatar to wear. | First variant | :material-clock: |

:material-clock: These two are in the dialog but not finished yet, so the list of
choices may be empty.

### Navigation

| Setting | What it does | Default |
|---------|--------------|---------|
| Reload on grid change | Reload the scene when a different grid is selected. | On |

## Display

### Rendering

| Setting | What it does | Default |
|---------|--------------|---------|
| Rendering quality | How much the renderer is asked to do. Lower it if the frame rate drops. | Medium |
| Window mode | Whether the app runs full screen, borderless or in a window. | Borderless |
| Vertical sync | Waits for the display before drawing. Off removes the frame-rate ceiling. | Every frame |
| Render resolution | Edge length the screen cameras draw at. | Matches quality level |

Nothing is detected from your hardware. Until you choose, these four keep whatever this
machine last used, which on a fresh installation is the default shown. Once set, your choice survives a restart.

#### Rendering quality

Rendering quality is a list of six levels, from the most expensive to the cheapest:

1. Ray Tracing (Realtime GI)
2. Ray Tracing
3. High
4. Medium
5. Low
6. Minimum

A fresh installation starts on **Medium**. Until you choose a level here, the client
keeps the one this machine last used, so an installation that ran an earlier version
can still be on the level it had then.

If the frame rate is low, choose a cheaper level: **Minimum** is the one most likely to
run on a machine that is struggling, and you can go straight to it rather than stepping
down one at a time. **Reset To Defaults** also lands on **Minimum** (see
[Resetting preferences](#resetting-preferences)). If it is still slow at **Minimum**,
lower [Blocks per frame](#budget) next, or use filters to show fewer blocks.

The client can also offer to lower it for you. With **Tell me when the frame rate
drops** on (the default, under [Assistant > Prompts](#prompts)), after a 15-second warm-up the
client watches for a frame rate under 30 for ten seconds and offers to step down one
level. After each prompt it stays quiet for five minutes. Once you are on **Minimum**
there is nothing lower to offer, so it suggests using filters to show fewer blocks
instead.

Rendering quality changes in only two places: this screen (choosing a level, or
**Reset To Defaults**), and that prompt. If the client is too slow to open Preferences
and the prompt does not appear, there is no other way to lower it from inside the
client: [contact support](../../../../contact.md) and say which GPU you have.

!!! info "Minimum requirements"
    On Windows, the client needs at least a DirectX 12 capable GPU with 3 GB of memory,
    on 64-bit Windows 10, and 8 GB is recommended. Below the minimum, lowering these
    settings may not be enough. The full list, including experimental macOS support, is
    on [Supported Configurations](../../Supported-Configurations/index.md).

### Interface

| Setting | What it does | Default | Range | |
|---------|--------------|---------|-------|---|
| Chat size | How large the chat window is drawn. | 1.35 | 0.75-3 | :material-robot: |

## Effects

### Scene

| Setting | What it does | Default | |
|---------|--------------|---------|---|
| Skybox | Which sky is drawn overhead. | First variant | :material-robot: |

## Assistant

### Chat

| Setting | What it does | Default |
|---------|--------------|---------|
| Tessa's voice | Which voice the assistant speaks with. | Account default |

Tessa's voice is saved to your account rather than to this machine, so it follows
you to another install.

### Prompts

| Setting | What it does | Default | |
|---------|--------------|---------|---|
| Tell me about new versions | Check for a newer release on start-up. | On | :material-robot: |
| Tell me when the frame rate drops | Offer to lower rendering quality when the frame rate stays low. | On | :material-robot: |

## Advanced

### Budget

| Setting | What it does | Default | Range |
|---------|--------------|---------|-------|
| Blocks per frame | How many blocks may be created or updated in a single frame. | 200 | 10-1000 |

Raising this fills the grid faster and costs frame rate. Lowering it is the first
thing to try if the client struggles on a busy grid.

### Privacy

| Setting | What it does | Default |
|---------|--------------|---------|
| Demo mode | Meant to redact hosts, URLs and database names. In this version it hides only the grid name (see the warning below). | Off |

!!! warning "Do not rely on Demo mode to hide your infrastructure"
    In this version, Demo mode hides only the grid's name. Hosts, URLs and database names
    in your telemetry are shown as your services report them, with Demo mode on or off.
    Until this is fixed, check what is visible before you demo or share your screen, or
    use a grid whose data you are happy to show.

### Diagnostics

| Setting | What it does | Default |
|---------|--------------|---------|
| Record teleport and fall diagnostics | Records how each arrival lands, and why a fall happened. | Off |

!!! tip "If you fall through the ground after a teleport"
    Turn this on, do it again, and send the log. It is off by default because it
    checks the ground every frame.

### Demo

| Setting | What it does | Default |
|---------|--------------|---------|
| Show demo screens on platforms | Shows the demo screens on platforms. | Off |

The screens are filled from `demo-screen-1.csv` to `demo-screen-3.csv` in the
Demo folder of the app's data directory, and **the data in them is made up**.
Turn the setting off and on again to reload the files.

### Sign-in

| Setting | What it does | Default |
|---------|--------------|---------|
| Sign in inside the app | Use the in-app browser for sign-in instead of the OS browser. | Off |

## Resetting preferences

**Reset To Defaults** puts every setting above back to what a fresh installation would
have, including **Borderless** for window mode and **Every frame** for vertical sync, with
one exception: **Rendering quality** resets to **Minimum**, not Medium. Reset is what
you reach for when the client is misbehaving, so it lands on the level most likely to
draw. Raise it again once the client is behaving.

It resets everything at once and cannot be undone. That includes **Demo mode**, which
goes back to Off.

Things that are stored but are not settings are left alone: where you dragged the
chat window, and which sign-in scheme you are using. Asking for default settings is
not asking to be signed out.

If you need to clear the file itself, it lives in your platform's application data
folder under `Immersive Fusion/DC`:

- **Windows:** `%USERPROFILE%\AppData\LocalLow\Immersive Fusion\DC\preferences.json`
- **macOS:** `~/Library/Application Support/Immersive Fusion/DC/preferences.json`

The file is encrypted, so it is not meant to be edited by hand. Deleting it returns
the settings it stores to their defaults on the next start, but it is not the same as
Reset: rendering quality, window mode and vertical sync are left at whatever this
machine last used. To drop to **Minimum**, use Reset.
