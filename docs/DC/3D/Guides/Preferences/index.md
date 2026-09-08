# Preferences

Press `F9` to open preferences.

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

| Setting | What it does | Default |
|---------|--------------|---------|
| Grid map | Which grid map variant to load. | First variant |
| Avatar | Which avatar to wear. | First variant |

### Navigation

| Setting | What it does | Default |
|---------|--------------|---------|
| Reload on grid change | Reload the scene when a different grid is selected. | On |

## Display

### Rendering

| Setting | What it does | Default |
|---------|--------------|---------|
| Rendering quality | How much the renderer is asked to do. Lower it if the frame rate drops. | Engine default |
| Window mode | Whether the app runs full screen, borderless or in a window. | Engine default |
| Vertical sync | Waits for the display before drawing. Off removes the frame-rate ceiling. | Engine default |
| Render resolution | Edge length the screen cameras draw at. | Matches quality level |

Until you choose one, these four follow whatever the engine picks for your hardware.
Once set, your choice survives a restart.

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
| Demo mode | Redact hosts, URLs and database names from everything shown. | Off |

!!! tip "Before you share a screen"
    Turn on **Demo mode** before demoing or screen-sharing. It redacts hosts, URLs and
    database names everywhere they appear, so you do not have to remember which panel
    shows what.

### Sign-in

| Setting | What it does | Default |
|---------|--------------|---------|
| Sign in inside the app | Use the in-app browser for sign-in instead of the OS browser. | Off |

## Resetting preferences

Resetting puts every setting above back to what a fresh installation would have.

Things that are stored but are not settings are left alone: where you dragged the
chat window, and which sign-in scheme you are using. Asking for default settings is
not asking to be signed out.

If you need to clear the file itself, it lives in your platform's application data
folder under `Immersive Fusion/DC`:

- **Windows:** `%USERPROFILE%\AppData\LocalLow\Immersive Fusion\DC\preferences.json`
- **macOS:** `~/Library/Application Support/Immersive Fusion/DC/preferences.json`

The file is encrypted, so it is not meant to be edited by hand. Deleting it returns
everything to defaults on the next start.
