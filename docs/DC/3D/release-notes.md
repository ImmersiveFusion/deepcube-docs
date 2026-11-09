---
description: Version history for DeepCube&trade;, newest first. Entries keep the product name they shipped under.
---

# DeepCube Release Notes

## Version History

### 1.25.1 <small>November 9, 2026</small> { id="1.25.1" }

**Introduction:**

Everything since 1.23.1 is in this update. Click an error or a log row to open the Diagnostics cube on its trace, and leave the cube to land back on the platform you came from. Ask Tessa to take you to a service and she is set to take you there. She is set to give shorter answers that lead with the answer, and she asks before she saves to your memory. Phantoms now appear on a grid that was already running when the client started, and a queue phantom goes when its queue is read again. The room's glow is gentler and the in-world screens are sharper.

**New Features:**

- **From a Row into the Diagnostics Cube**: On the Recent Errors and Recent Logs screens, click a row to open the Diagnostics cube on that row's trace. On the grid-wide screens, the **Service** and **Instance** cells still take you to that service's platform, and the other cells open the cube; on a platform's own error and log screens, any cell opens the cube. The cube can open only a trace the client still holds, which is about the last ten minutes. For an older row, or a log with no trace, the grid-wide screens take you to the service's platform and a platform's screens do nothing. A cell with no value no longer highlights and cannot be clicked.
- **Back to Your Platform**: Leaving the Diagnostics cube through its portal now takes you back to the platform you were standing on when you went in, wherever the layout has moved it since, the same way a click on a service in a table takes you there. If you went in from somewhere other than a platform, or the platform is gone, you return to the spot you went in from. This applies however you entered the cube, including from a trace block.
- **Take Me There**: Ask Tessa to take you to a service or a dependency, for example "take me to order service", and she is set to take you to its platform. Going there needs no approval from you. The name does not need to match exactly in case or separators, so "order service" finds `order-service`, but it must be the whole name.
- **Tessa Asks Before She Saves to Your Memory**: When Tessa wants to save something to your memory, a **Save to your memory?** dialog shows what she wants to save, with **Allow** and **Deny**. A yes also lets her save other facts from that workspace for 24 hours without asking. One question shows at a time, and a question left unanswered is taken down. When you tell her to remember something, she is set to keep it in the conversation and to save to your memory only when you ask her to keep it for later, or for your name and what to call you. A name you have saved now reaches each new conversation.

**Improvements:**

- **Shorter, Straighter Answers**: Unless you ask for more, Tessa is now set to answer in at most three sentences, about 75 words: the answer with the one number that shows it, the evidence behind it, and the one thing to look at next. When the data does not answer the question, she is set to say so first. She is set to use a short list only to compare three or more things, and to give at most two places for a question about what to check first. Say "more", "details", "explain" or "why" for a longer answer.
- **Grid Questions Stay with Tessa**: A question about your grid is answered by Tessa, with what she knows about where you are and the conversation so far. Earlier versions could hand such a question to a research helper that could see neither, and its answer was generic. A question goes to a research helper when you ask for research or name the helper.
- **Tessa Explains a Red Platform**: When Tessa looks up a service or a dependency, she now also reads what the grid shows on its platform: whether it is red, whether it sends telemetry of its own, how many failed calls and error logs were filed on it, and which services they came from. A database whose platform is red because its callers' calls are failing is no longer called healthy.
- **Workspace Switch from the Chat**: Changed switching workspace from the chat so that Tessa finishes her reply first and then switches. If your message named the workspace, the conversation comes with you; if not, it stays behind and the chat says so. The chat also says how many queued messages were not sent.
- **Clearer Failure Messages**: When Tessa's service does not answer, the chat says what happened, including what the service last replied, instead of always saying it was still starting up.
- **Room Glow and Crisp Screens**: The room's glow is gentler up close, and turning the view no longer smears the picture. In-world screens are sharper, show status colors true, no longer reflect the room, and the map screens now draw the service graph's connections. The Traces & Logs (**M**) and Services & Dependencies (**N**) views take the same look as the screens. The grid floor's tiles and lines are teal.
- **Steam Version Check**: In a Steam installation, the new-version notice now checks the version released on Steam, not the one released for the Windows installer.
- The Windows installer now shows version 1.6.0 of the DeepCube end user license agreement.
- Security fixes.

**Bug Fixes:**

- Fixed phantoms never being drawn for a fault that was already present when the client started. After the client has watched a grid for about five minutes, a call nothing answers, or a queue nothing consumes, that keeps happening is drawn as a phantom.
- Fixed a queue phantom staying on the grid for about five minutes after its queue was read again, or turning into a blank node. It now goes when the queue is read again.
- Fixed clicks on things seen through glass, such as the platforms below a glass floor, doing nothing.
- Changed a switch of workspace from the chat so that it no longer looks as if it had failed. Before, Tessa never confirmed it, the chat showed **Interrupted**, and the next message reached a conversation that knew nothing about the switch.
- Changed saving to your memory so that a save you allow goes through. Before, every save failed and the chat said you had declined it.
- Changed the chat so that its window opens at your **Chat size** preference instead of its default size.
- Changed the chat so that a tool's progress stops showing "running..." once the tool has finished.
- Changed the chat so that a reopened chat window shows the replies you saw instead of raw tool output.
- Changed the chat so that opening it twice quickly, or after a failed open, uses one window instead of sometimes opening a second.
- Changed dialogs, such as the one that opens a link, so that they are drawn above the other parts of the on-screen display instead of under them.

**Known Issues:**

- The known issues listed for [1.23.0](#1.23.0) still apply, except that a fault already present when the client started is now drawn as a phantom once it repeats (see Bug Fixes).
- A call or a queue that fails only once, such as a Shoebox diagram run a single time, is not drawn as a phantom. Run it again to see one.
- A queue whose consumer reads it less often than every five minutes, and that was already running when the client started, can show as a phantom until its next read.
- A queue phantom can occasionally stay until you restart the client if the read of its queue arrives late.
- The chat changes in this version have not yet been confirmed in the published build: saving to your memory, the chat window size, a tool's progress, a reopened chat window, a second chat window, dialogs under the on-screen display, and a workspace switch from the chat. If you still see one of these problems, tell us.

### 1.23.1 <small>October 29, 2026</small> { id="1.23.1" }

!!! warning "Before you update: link Steam to your DeepCube account"
    **Go to [id.deepcube.ai/account](https://id.deepcube.ai/account) and link Steam first, before your next launch from Steam.**

    From this version, launching from Steam signs you in with Steam first, before your saved session. If Steam is not linked to your DeepCube account, you are signed in to a separate, new account, without your grids or your subscription.

**Introduction:**

Launching from Steam now signs you in with Steam, with no login screen. Link Steam to your DeepCube account at https://id.deepcube.ai/account before your first Steam launch after this update, so that the Steam sign-in lands on your existing account.

**New Features:**

- **Sign In with Steam**: When you launch from Steam, the client signs you in with your Steam account and goes straight to the Lobby. The Steam sign-in comes first, before a saved session, and a Steam account that is not linked to your DeepCube account signs you in to a separate, new account. If Steam is not running, gives no sign-in ticket within 10 seconds, or the sign-in is refused, the client uses your saved session, and if that fails, shows the Login screen, where **Start** opens the browser sign-in. **Log Out** takes you to the Login screen, and the client does not sign you in again by itself until you press **Start** or restart it; **Start** opens the browser sign-in, and the next Steam launch signs you in with Steam again. Outside Steam, the client never starts Steam and you sign in with your DeepCube account as in 1.23.0; the changes under Improvements apply there too.

**Improvements:**

- **Signed In Where You Are**: Opening a part of the client that needs you signed in now signs you in on the spot, with Steam or your saved session, instead of sending you to the Login screen. If that does not work, Login takes you back to where you were once you sign in. **Start** now takes you to the Lobby.
- The macOS microphone prompt now says **Talk to the AI Assistant**, and the in-app help calls her the AI Assistant or Tessa.

**Known Issues:**

- The known issues listed for [1.23.0](#1.23.0) still apply.

### 1.23.0 <small>October 29, 2026</small> { id="1.23.0" }

**Introduction:**

Everything since 1.18.27 is in this update. Signing in is one step: the client no longer asks which kind of account you have, and it keeps you signed in between launches. Tessa now asks before she clears the service map, builds or runs a Shoebox, requests a replay or changes a preference, and asks every time before she shares a Shoebox or goes to the web. A service is one platform however many instances serve it, and its nameplate says how many are live. Phantoms are drawn only once they have been judged, they show their names, and the lines to them are easier to follow. The full-range skies are back, forty of them. Spans that recorded an exception, or answered with an HTTP 5xx or 429, now count as failures, so some services may show a higher error rate than before.

**New Features:**

- **One Sign-In That Stays**: The Login screen no longer offers a list of account types. Press **Start** and sign in with your DeepCube account in your browser (or inside the app, if **Sign in inside the app** is on under Advanced); the browser tab then says you are signed in, and you can close it. The client remembers your session, so on the next launch it signs you straight in while that session is still valid. Signing out clears it from this machine. If you sign in inside the app, the session is not resumed, and you sign in at each launch. Sign in once after this update, with the same method you used before: signing in with Steam instead creates a separate account unless you first link Steam to your account at https://id.deepcube.ai/account. If you signed in with a Microsoft work or school account, your account, grids and subscription are unchanged. Sessions from earlier versions do not carry over.
- **Tessa Asks First**: Before Tessa clears the service map, builds or runs a Shoebox, requests a replay or changes a preference, she asks you, showing what she wants to run (the start of it, for a long request). One yes covers that kind of action for the rest of the session: a yes to one preference change also covers her later preference changes. Sharing a Shoebox, and fetching from, posting to or searching the web, ask every time. Reading your telemetry, and opening an instance's error, never ask. A no applies to that one request only, and closing the prompt without answering counts as a no.
- **Instances on the Nameplate**: A service's nameplate now counts its instances, for example `2 live` or `1 live, 1 quiet`. An instance is live while it has sent a span within five minutes of the service's latest one, and quiet after that; one that stays silent for an hour drops off the count. Both are measured against the service's newest span, not the clock, so a service that stops sending altogether keeps its last count. The count covers what this client has seen since it started. A service whose spans do not say which instance sent them shows `instances unknown`, and a phantom shows no count. Ask Tessa how many instances a service has and which one is failing, or ask her to open the newest error from one. If that trace has already left the grid, she takes you to the service's platform instead.
- **Forty Skies**: The full-range HDR skies are back, and **Skybox** (Effects, in Preferences) now lists all forty by name. Night and Day keep their places at the top, so the sky you had chosen is still chosen. The new **Sky movement** setting sets how fast the clouds drift, from 0 (still) to 1000, default 300, so clouds now drift unless you set it to 0. Tessa can change both.
- **`/node-ids`**: Type `/node-ids` in the chat for a list of every node on the grid: the identity the client filed it under, its instances (live or quiet, and when each was first and last seen) and how many of its spans the client has seen. The same list is saved as a text file in the client's `logs` folder, so you can send it with a support request. It names your services and their instances, and Demo mode does not hide them, so check it before you share it. Times are as seen by this client, so they start again after a restart.

**Improvements:**

- **One Platform per Service**: A service is now one platform, however many pods or instances answer for it. A deploy or a restart no longer starts a new platform with fresh history, so a grid with many replicas draws fewer platforms than before. There is no setting to go back to one platform per instance.
- **Phantoms, Judged Before They Are Drawn**: A node is drawn as a phantom only once it has been judged one, so a service too new to judge no longer appears as a phantom and then clears itself a few minutes later. Calls to a public host name that none of your reporting services uses, such as a payment or email provider's API, and calls to databases are drawn as external dependencies, not phantoms. A service of your own that sends no telemetry and is reached by a public host name is drawn the same way. A call also counts as answered when a server's span in the same trace answers it, even if that server reports no host name. A fault that was already present when the client started may not be drawn as a phantom (see Known Issues).
- **Strain-Lines You Can Follow**: The line from a caller to a phantom is now the same width whatever the traffic, in the phantom's own colors, and narrows toward the phantom, so it shows which end is missing even when nothing moves. A phantom draws lines to its five most recent callers and names them on its screen with a count of the rest, for example `Callers: payment-service, checkout-service, +7`. An error on that connection no longer repaints the line.
- **More Failures Counted as Failures**: A span that recorded an exception now counts as failed even when its status was never set to error, and so does a span with an HTTP 5xx or 429 response. A service that handles and records its exceptions can now show a non-zero error rate, and turn red, where it showed clean before.
- **Preferences, Easier to Read**: Each setting's control now sits beneath its name instead of at the far edge of the row, dropdowns show many more choices at once, and the mouse wheel moves the list much further per notch.
- **New Defaults for Blocks and Connections**: A fresh installation, or **Reset To Defaults**, now sets **Minimum block lifetime** to 300 seconds (was 30), **Possibly-lost after** to 200 (was 30), **Lost after** to 1200 (was 60), **Keep connections for** to 160 (was 300) and **Blocks per frame** to 500 (was 200). All five are under Advanced in Preferences. On a fresh installation, or after a reset, blocks stay on the grid for at least five minutes. An existing installation keeps the values it already has; to take the new ones, use **Reset To Defaults**, which resets every other setting too, including rendering quality to **Minimum** and **Demo mode** to Off, and does not ask first.
- **Chat Window Collapses**: Double-click the chat window's header, or use its new button, to shrink it to the header, and do the same to bring it back. The chat window and the page your browser shows after sign-in now use the DeepCube look.
- **Tidier Log Files**: The client's log files now roll over and are capped in size, and logs older than 30 days are deleted. On the first launch after this update, the client also deletes every log file earlier versions wrote, whatever its age.
- Security fixes to grid access and data isolation.

**Bug Fixes:**

- Fixed a phantom showing no name or tags. It now shows its name, that it is a phantom, what is missing (for example `no-consumer`) and the key it was inferred from.
- Fixed queues and topics that were being consumed showing a phantom consumer. Consumer spans that arrived too late to draw were never counted; they are now.
- Fixed one third-party API sometimes appearing as two nodes.
- Fixed text containing angle brackets, in log lines, error messages or service names, being read as formatting and garbling rows on in-world screens such as Recent Logs.
- Fixed the interface scaling with screen width, which drew it too large on ultrawide monitors and pushed Preferences off the screen. It now scales with screen height.
- Fixed the camera turning while you dragged an edge of the chat window to resize it. The camera now pans only when you press on the world.
- Fixed resizing the chat window writing to disk on every frame of the drag.
- Fixed two copies of the client getting in each other's way when signing in at the same time.
- Fixed Tessa offering her alert summary as a way to tell whether anyone is being notified or paged. Nothing is notified or paged: the summary is a check of the grid's current health against fixed thresholds.

**Known Issues:**

- The chat handles one conversation at a time. The transcript survives reopening the window, but it is not saved between sessions, so a fresh run starts a fresh conversation.
- An open Preferences screen does not refresh when a setting changes elsewhere, for example when Tessa changes it. Close and reopen Preferences to see the current value.
- If the preferences file cannot be written, a change still applies for the rest of the session but is gone after a restart, with no warning.
- **Phantom after** (Advanced, in Preferences) is still listed, but changing it no longer changes when a phantom is drawn. Phantoms are now judged over a fixed window of about a minute.
- A call nothing answers, or a queue nothing consumes, that was already happening when the client started may not be drawn as a phantom. Check that service's connections and error rate rather than waiting for one.
- If an approval prompt from Tessa is left unanswered for a while, the request can time out, and Tessa may report that you declined it. Ask again and answer the prompt.
- On a platform you have already visited, reloading the demo screens refreshes their rows and titles only. A change to a file's columns, or a file deleted or fixed since your visit, needs an app restart to show there.
- The fix for being carried off a platform as you teleport does not yet apply in VR.
- Asking Tessa to clear the service map does not remove trace blocks.
- At the start of a conversation, a request like "a shoebox of 5 microservices calling each other" can get an answer about writing code. Remind Tessa that a Shoebox is the sandbox, and she builds it.
- After her tools have run, Tessa's written answer can occasionally come back empty. The chat shows what ran, but the answer itself is lost; ask again.
- Demo mode hides only the grid's name. Hosts, URLs and database names in your telemetry are shown as your services report them, with Demo mode on or off. Check what is visible before you demo or share your screen.
- macOS support is experimental and may lack full feature parity with Windows builds.

### 1.18.27 <small>September 30, 2026</small> { id="1.18.27" }

**Introduction:**

Everything since 1.18.8 is in this update. Preferences are rebuilt from the ground up, and Tessa can now read them and change some of them for you. When the frame rate gives out, the client says so and offers one click down. In the Shoebox sandbox, Tessa checks a diagram before she runs it and tells you what she assumed and what did not match. Busy grids do less work every frame, and two causes of falling through the ground are fixed.

**New Features:**

- **Preferences, Rebuilt**: Press F9 in a grid to open Preferences, now grouped into World, Display, Effects, Assistant and Advanced. Rendering quality is a dropdown of six levels, from Ray Tracing (Realtime GI) down to Minimum, and a fresh installation starts on Medium (an existing installation keeps the level it had). The level you choose is now saved with the rest of your preferences. The sky overhead is a setting of its own, and **Reset To Defaults** puts everything back in one press, landing rendering quality on Minimum because reset is what you reach for when the client is misbehaving. It does not sign you out.
- **Tessa Reads and Changes Your Preferences**: Ask Tessa what a setting is set to, or ask her to change it. She can change some preferences, but not rendering settings, sign-in or redaction, which stay yours to set.
- **One Voice Across Clients**: Tessa's voice is saved to your account, so a voice chosen here is the one you hear in DeepCube Web, and the other way round.
- **Frame-Rate Prompt**: If the frame rate stays under 30 for ten seconds (after a 15-second warm-up), the client says so and offers to lower rendering quality by one level. After each prompt it stays quiet for five minutes, and at Minimum it suggests using filters to show fewer blocks instead. Choose **Don't Ask Again** to switch it off, or turn it back on under Assistant in Preferences. The new-version prompt has its own **Don't Ask Again** too.
- **Demo Screens on Platforms**: Turn on **Show demo screens on platforms** (Advanced, off by default) and each service platform shows three demo tables, filled from `demo-screen-1.csv` to `demo-screen-3.csv` in the app's Demo folder. A missing or unreadable file shows an empty screen titled with its file name. The data is whatever you put in the files.

**Improvements:**

- **Shoebox, Checked Before It Runs**: Tessa loads and checks your diagram before anything runs, then runs it as a separate step. She reads out the run's notes alongside the result, tells you what she assumed, and shows you the diagram she drew when she read it from a picture, so you can correct a misreading. Loops in the diagram, and services nothing calls, are reported to you rather than redrawn away. If she reaches a third different diagram without running one, she stops and runs what she has instead. Ask for several runs and she paces them within the turn, saying so if she had to space them closer than you asked. A share link matches the diagram that actually ran, and `/clear` starts a fresh Shoebox.
- **Tessa Sees What You Send Her**: A message that is only an image now reaches her, and recent images stay in the conversation, so she can refer back to one you sent earlier. On the Shoebox grid, paste a screenshot of an architecture diagram and ask her to run it. Anything you send to the Shoebox lands in a public sandbox, so leave out anything proprietary.
- **Tessa Clears the Map**: Ask her to clear the service map and she does.
- **Tessa Says When Her Service Is Waking Up**: When the assistant service is starting, the chat says so once and waits for it. If it never comes up, the chat says the service did not start and that sending your message again should work.
- **A Quiet Turn Says What Ran**: When Tessa's tools finish their work but she adds no closing sentence, the chat shows a short muted note naming what ran.
- **Phantoms as Questions**: Tessa now treats a phantom as a question to answer, saying what was inferred and from what evidence, rather than announcing a discovery.
- **Connections Stay on the Map**: An idle connection now thins but stays on the graph until it has had no traffic for **Keep connections for** (under Advanced in Preferences: 60 to 300 seconds, default 300), instead of disappearing within 20 seconds.
- **Lighter Busy Grids**: Blocks and the service graph do less work every frame. Tesseracts animate only when they are close and in view, and a platform's portal appears only when you are near it, while the hub keeps its own.
- **Help, Rewritten**: The Help screen now describes DeepCube, explains what a block is, and says where to go when the frame rate drops.
- **Teleport Diagnostics on Request**: **Record teleport and fall diagnostics** (Advanced, Diagnostics) is off by default, so the avatar does no extra work each frame. If you fall, turn it on and teleport again: it takes effect from your next teleport, with no restart. Everything it records now goes to the same log file as the rest of the client.
- **Security Update**: Updated a bundled component to fix a high-severity vulnerability (CVE-2026-26127) that could affect the app's availability.

**Bug Fixes:**

- Fixed teleporting off a moving platform carrying you with it as you left, which could drop you through the ground on arrival.
- Fixed falling when the platform you were standing on was removed after five minutes without traffic. You are now returned to the hub.
- Fixed a newly seen service's first traces drawing no queue or dependency nodes, and no connections between its services.
- Fixed the chat staying blank when two copies of the app ran at once. Each copy now gets a working chat, and if the chat cannot start, it says so.
- Fixed the chat waiting forever when one sentence of speech failed.
- Fixed the "Thinking" indicator staying on screen after a turn failed.
- Fixed the new-version prompt linking to a page that no longer exists.
- Fixed the Preferences tabs scrolling sideways.

**Known Issues:**

- The chat handles one conversation at a time. The transcript survives reopening the window, but it is not saved between sessions, so a fresh run starts a fresh conversation.
- An open Preferences screen does not refresh when a setting changes elsewhere, for example when Tessa changes it. Close and reopen Preferences to see the current value.
- If the preferences file cannot be written, a change still applies for the rest of the session but is gone after a restart, with no warning.
- On a platform you have already visited, reloading the demo screens refreshes their rows and titles only. A change to a file's columns, or a file deleted or fixed since your visit, needs an app restart to show there.
- The fix for being carried off a platform as you teleport does not yet apply in VR.
- Asking Tessa to clear the service map does not remove trace blocks.
- At the start of a conversation, a request like "a shoebox of 5 microservices calling each other" can get an answer about writing code. Remind Tessa that a Shoebox is the sandbox, and she builds it.
- After her tools have run, Tessa's written answer can occasionally come back empty. The chat shows what ran, but the answer itself is lost; ask again.
- Demo mode hides only the grid's name. Hosts, URLs and database names in your telemetry are shown as your services report them, with Demo mode on or off. Check what is visible before you demo or share your screen.
- macOS support is experimental and may lack full feature parity with Windows builds.

### 1.18.8 <small>August 30, 2026</small> { id="1.18.8" }

**Introduction:**

Everything since 1.18.0 arrives in one Steam update (1.18.1 through 1.18.7 were not released separately on Steam). Tessa gains hands: ask her to build and break a scenario in the Shoebox sandbox and she does it herself, then hands back a link you can open. The chat window becomes a proper window you can select from, resize, zoom and reopen where you left it, and the service graph now makes failure legible from across the fleet.

**New Features:**

- **Tessa Drives the Shoebox Sandbox**: Ask Tessa to stand up a scenario and break it, and she now does the work: she creates the sandbox for you without asking, sends the scenario over, runs it, and hands back a link. She keeps to the sandbox she created rather than borrowing an identifier, and she will tell you that anything you send lands in a public sandbox, so rename anything proprietary first.
- **Tessa Reads the Map**: Ask "any phantoms here?" and Tessa answers from the phantoms actually on your grid, naming each one the way the map names it and saying why it is a phantom, instead of reciting a definition. When there are none, she says so outright.
- **Chat Commands**: `/help` lists what Tessa can do and `/clear` clears the conversation. A command she does not recognize now gets an answer instead of silence.
- **Failure Cues on the Service Graph**: A phantom drifts to the sparse rim and its edges stretch taut into strain lines, tearing the fabric open instead of dragging healthy services out of shape. Error nodes hold their callers at a stepped-back standoff, a stable cleared ring around the fault. One cue per meaning: motion for danger, color for state.
- **Workspace Instructions**: Tessa picks up a workspace's instruction files as background context, considered but not followed, matching what Studio already does. Nothing changes for a workspace that has none.

**Improvements:**

- **Chat Window, Second Pass**: Select and copy the transcript, drag the edges to resize it, zoom with Ctrl+= and Ctrl+-, and reopen it exactly where and how you left it. Paste an image with Ctrl+V and see it in the composer and in the sent turn, recall what you typed with Up and Down, and open the window with a hotkey. Links in Tessa's answers open in your browser rather than inside the chat.
- **Faster Grid Picker**: Grid descriptions now show inline on the rows and in a tooltip on hover, and the whole list arrives in one pass instead of one lookup per environment. Two environments that share a display name no longer collapse into a single section.
- **Steadier Frame Rate in Dense Scenes**: In-world screens are paced and sized to what they actually need, distant text is culled, and detail culling now measures the detail rather than the whole object.
- **Tessa Speaks the Product's Vocabulary**: The words on screen and the words in her answers are now the same words.

**Bug Fixes:**

- Fixed teleport arrival dropping you through the floor. Arrival now probes for ground, recovers to your last good footing if you fall, and resets cleanly when you teleport out of water.
- Fixed error nodes jittering instead of settling, and fixed the graph slowly flattening while the companion roamed on its tour.
- Fixed the app shutting itself down after a brief interruption to its data connection. It now rides out the interruption and reconnects on its own.
- Fixed the chat losing its transcript when the window was reopened.
- Fixed a message sent with an image not showing your own turn, so you could not see what you had asked.
- Fixed Shift+Enter submitting instead of starting a new line. The composer now grows as you type.
- Fixed the chat panel dimming while you were plainly using it. It now stays bright whenever the pointer is over it, not only when the text box has focus.
- Fixed tooltips left stranded on screen when the row under the pointer disappeared, and fixed one tooltip erasing another.
- Fixed the idle HUD toggle doing nothing in the Lobby.
- Fixed an unreadable chat tab label, and shipped smaller resize cursors.
- Release notifications now point at the current documentation site.

**Known Issues:**

- The chat handles one conversation at a time. The transcript now survives reopening the window, but it is not saved between sessions, so a fresh run starts a fresh conversation.
- macOS support is experimental and may lack full feature parity with Windows builds.

### Renamed to DeepCube <small>August 7, 2026</small> { id="renamed-to-deepcube" }

**Introduction:**

Immersive APM is now **DeepCube™**. This is a name change only. Your account, your grids, your API keys, and your telemetry are unchanged, and no action is needed on your part.

Entries below this one keep the name they shipped under, so the record stays accurate.

### 1.18.0 <small>July 22, 2026</small> { id="1.18.0" }

**Introduction:**

Everything since 1.17.0 arrives in one Steam update (1.17.1 was a build re-tag with no changes; 1.17.2 was a performance update not released separately on Steam). The headline is a dedicated in-world chat window for Tessa, with proper formatting and streaming replies. The service graph also renders its visual effects more efficiently in busy scenes.

**New Features:**

- **In-World Chat Window for Tessa**: Tessa now answers in a dedicated in-world chat panel. Open it from the chat icon, ask your question, and the reply streams back with formatted text, code syntax highlighting, and cards for the tools Tessa runs. The companion menu options now open here as well. The panel centers when it opens, dims while you are not using it, and can be hidden or closed; while you type, your input stays in the chat instead of driving the game. Tessa's identity follows your current workspace and persona.

**Improvements:**

- **Steadier Service Graph**: Service pulses and falling blocks now spawn only when they are on screen and are paced to your frame rate, cutting overdraw and keeping the framerate steadier in busy fleets.

**Known Issues:**

- The chat window handles one conversation at a time, and there is no saved transcript yet, so closing the panel starts a fresh conversation.
- macOS support is experimental and may lack full feature parity with Windows builds.

### 1.17.0 <small>June 30, 2026</small> { id="1.17.0" }

**Introduction:**

A large release for Steam players: everything since 1.15.0 arrives in one update (1.16.x was an internal milestone not released on Steam). Tessa's in-world companion graduates into an autonomous tour guide, the service graph gains holographic "phantom" placeholders for services that are referenced but never seen, the Hall of Supporters is reimagined as the Spatial Observatory, and sign-in becomes faster and more reliable with your choice of native or in-world browser. Tessa can now adopt a workspace's persona, with a consent prompt before it does.

**New Features:**

- **Companion Idle Autopilot**: After about 10 minutes of inactivity, the camera follows Tessa's companion on an autonomous tour of your most interesting facilities, prioritizing failing and anomalous services, with a scenic overview when the fleet is healthy. The companion eases between points of interest, faces each one, and re-targets live as the graph reflows. Any input ends the tour and returns the companion to your avatar; pin it on to keep it running continuously instead.
- **Phantom Nodes**: The service graph now renders holographic placeholder facilities for services that are referenced but never observed: a producer publishing to a queue no one consumes, or a client calling an API with no instrumented server. Phantoms appear with persistent edges back to the callers that referenced them, and are promoted to solid facilities automatically once real telemetry arrives.
- **Spatial Observatory**: The Hall of Supporters is renamed the Spatial Observatory, a community space inside the world of your application. It is open to anyone, and it is where the people behind the work are seen: the supporters who helped the company grow, and the operators who keep systems running. The Buzludzha monument environment is retained.
- **Choose Your Sign-In Browser**: A new option on the Login screen lets you sign in with your native OS browser (default) or an embedded in-world browser. Your choice is remembered.
- **Workspace Persona for Tessa**: Point the app at a workspace and Tessa can adopt that workspace's persona. Before it does, a consent prompt asks your approval, and Tessa never adopts a workspace's guidance without it.

**Improvements:**

- **Energy Recharge Countdown**: When energy is replenishing, the HUD now shows a live countdown to when it resets, driven by the server's own timing.
- More reliable sign-in: cancelling or abandoning a sign-in now unwinds cleanly, retry re-enables correctly, and rapid back-to-back logins no longer flicker or hang.

**Bug Fixes:**

- Fixed long Tessa answers being truncated in the console; oversized output is now chunked so nothing is lost.
- Fixed macOS native sign-in failing on URLs with encoded characters.

**Known Issues:**

- macOS support is experimental and may lack full feature parity with Windows builds. The embedded in-world sign-in browser in particular may have limited support on macOS; the native browser option is recommended there.

### 1.15.0 <small>May 8, 2026</small> { id="1.15.0" }

**Introduction:**

Tessa's in-world companion graduates from preview to a full presence. You can now switch workspaces from voice or the console without leaving the world, the radial menu reorganizes around how you actually work (Help, Quick Read, Deep Analysis), and gamepad players get a proper on-screen cursor with orbit-on-stick movement. The companion also picks up a richer set of idle behaviors that make the world feel less empty during long sessions.

**New Features:**

- **Voice and Console Workspace Switching**: Say or type a workspace command to switch grids without opening the picker. The world reloads cleanly with the new workspace context.
- **Three-Bucket Companion Menu**: The radial menu reorganizes around intent: Help, Quick Read, and Deep Analysis. Workspace-aware Security and Research entries appear when relevant, and GenAI Cost shows up in trace context.
- **Gamepad Cursor and Stick Orbiting**: A screen-center reticle gives gamepad players a true cursor for in-world targeting. Pushing the right stick now activates orbiting around the focal point.
- **Companion Idle Behaviors**: The companion now wanders, plays small skits, picks up props, and chatters while you work, with smoother pose recovery and tilt handling.

**Improvements:**

- The companion menu prefills the console for quick edits before send, and surfaces an active-context diagnostic so you can see what the companion is reasoning over.
- Empty-slice handling and recall easing polish the radial menu interaction.
- The companion is disabled by default until you opt in.

**Bug Fixes:**

- Fixed the companion getting stuck in poses or tilted after rapid prop interactions.
- Fixed input-action bleed when the radial menu opened or closed mid-action.

**Known Issues:**

- macOS support is experimental and may lack full feature parity with Windows builds.

### 1.14.11 <small>April 24, 2026</small> { id="1.14.11" }

**Introduction:**

A series of stabilization patches across the 1.14.x line, focused on Windows installer reliability, in-world polish, and an early look at Tessa's in-world companion that lands properly in 1.15.0. If you are upgrading from 1.14.0, this is the recommended 1.14.x build to install.

**Improvements:**

- **Smaller, More Reliable Windows Installer**: Reworked the Windows installer payload so large worlds package and install reliably on all Windows configurations.
- **Refreshed Installer Branding**: New Windows installer dialog and banner artwork, with the installer, Start Menu shortcut, and app all consistently named **IAPM**.
- **macOS Disk Image Distribution**: A new macOS disk image (DMG) flow ships alongside the Windows installer.
- **Companion Preview**: Early in-world preview of Tessa's companion with idle behaviors, props, and a contextual radial menu. Disabled by default; full release lands in 1.15.0.
- **Service Facility Polish**: Refined service facility content, including overlay menu fixes, tooltip cleanup, and smarter error/log table rendering pulled from receiver buffers.
- **Portal Landing Polish**: Portal teleport landings fall back through to ground reliably, and portal ring orientation faces the hub center correctly.

**Bug Fixes:**

- Fixed graph layout stability with improved bounding box handling and cooling behavior.
- Fixed avatar fall-through after portal teleport.
- Fixed assorted prefab and scale issues across error and log tables.
- Fixed dependency tap-target resolution to use the cell value instead of the row index.

**Known Issues:**

- macOS support is experimental and may lack full feature parity with Windows builds.

### 1.14.0 <small>April 20, 2026</small> { id="1.14.0" }

**Introduction:**

This release delivers a big jump in in-world information density. Services and dependencies now carry their own content screens with error tables, log tables, and cost summaries, and you can tap any table row to teleport directly to the matching facility. A new force-directed service graph replaces the previous physics layout with smoother, more stable placement. Tessa picks up a new visual companion for contextual guidance.

**New Features:**

- **Per-Facility Content Screens**: Services, dependencies, and the root hub each have their own error table, log table, and cost summary screens, pulled live from the telemetry stream.
- **Row-Tap Teleport**: Tap any row in a service, dependency, error, or log table to teleport directly to the corresponding facility.
- **GenAI Cost Visibility**: Dedicated cost summary screens on the root hub, service facilities, and the Diagnostics cube show GenAI spend and token usage at a glance.

**Improvements:**

- **New Service Graph Engine**: The service graph uses a new force-directed layout for smoother transitions, stable node placement, and reliable prevention of ghost nodes.
- **Auto-Flatten Graph**: The graph flattens to 2D when you are in the hub and unfolds to 3D when you approach a facility.
- **Portal Hub Return**: Facility portals now reliably return you to the central hub, with correct orientation and landing position.
- **Loading Screen Timing**: The loading screen now waits for all environment scenes to finish loading before handing off to the world.
- **Paused World**: Pausing the world now freezes the service graph, photons, and physics so you can inspect the scene without motion.
- **Tooltip and Label Polish**: F6 copy hints standardized across tooltips, proximity labels refined, and dependency type now displays database and messaging system details.
- **Installer Packaging**: New Windows Installer (MSI) with dialog and banner graphics, and a new macOS disk image (DMG) distribution flow.

**Bug Fixes:**

- Fixed completed spans being mistakenly classified as lost with inflated durations.
- Fixed ghost nodes appearing in the service graph during high churn.
- Fixed avatar falling through the ground after portal teleport.
- Fixed portal ring orientation so portals face the hub center correctly.
- Fixed graph layout instability with improved bounding box handling and cooling behavior.
- Fixed Diagnostics cube width computation after scene hierarchy changes.
- Fixed numerous trace table and tooltip rendering issues.

**Known Issues:**

- macOS support is experimental and may lack full feature parity with Windows builds.

### 1.12.1 <small>April 5, 2026</small> { id="1.12.1" }

**Introduction:**

This patch refines service context awareness so Tessa can ground her answers in the specific service you are looking at.

**Improvements:**

- Service facilities now carry richer platform context (runtime, operating system, service version) that Tessa can consult when answering questions.
- Refined service context providers for more accurate location and topic awareness.

**Bug Fixes:**

- Fixed an error when the grid selection modal loads before authentication completes.

### 1.12.0 <small>April 3, 2026</small> { id="1.12.0" }

**Introduction:**

This release introduces the Skills system for extensible AI capabilities, multimodal vision for pasting screenshots directly into prompts, and feature parity with IAPM Studio.

**New Features:**

- **Skills**: Tessa can now use modular skills for specialized tasks, with a browsable skill catalog.
- **Multimodal Vision**: Paste screenshots with Ctrl+V and ask Tessa to analyze what you see.
- **Diagnostics Tools**: New diagnostic and analysis tools give Tessa richer troubleshooting insights.

**Improvements:**

- Feature parity with IAPM Studio for memory, orchestration, and context preservation.
- Improved filtering across all telemetry views.

### 1.11.0 <small>March 21, 2026</small> { id="1.11.0" }

**Introduction:**

This release adopts the OpenTelemetry standard data model across the entire visualization pipeline and refines the service graph with smoother placement behavior.

**Improvements:**

- Full adoption of OpenTelemetry-native data model for all trace and log visualizations.
- Service graph now transitions smoothly from startup, with improved node placement.
- Tessa's tools updated with richer descriptions and better accuracy.
- Improved tooltips and stage labels across all views.

**Bug Fixes:**

- Fixed trace blocks occasionally stopping after internal data updates.
- Fixed service graph nodes not settling into stable positions.
- Reduced excessive log noise from missing trace identifiers.

### 1.10.0 <small>January 25, 2026</small> { id="1.10.0" }

**Introduction:**

This release introduces the live service graph, a real-time 3D visualization of service dependencies with animated traffic pulses. Major performance and stability improvements are included, along with a streamlined authentication experience.

**New Features:**

- **Live Service Graph**: Real-time 3D visualization of service dependencies with animated traffic flow, error highlighting, and physics-based layout.
- **Demo Telemetry**: Built-in demo scenarios for exploring the product without connecting live data.
- **Energy System UI**: Energy bar showing AI usage with tier-aware capability levels.

**Improvements:**

- Streamlined authentication (no longer requires a separate browser window).
- Press Escape to interrupt Tessa's speech without losing your prompt queue.
- Significant performance and stability improvements.

**Bug Fixes:**

- Fixed rendering performance under high telemetry load.
- Fixed memory-related stability issues during long sessions.
- Fixed trace visualization scaling and display issues in the Diagnostics cube.
- Fixed lobby flickering during login.
- Fixed voice responses occasionally failing to stream.

**Known Issues:**

- macOS support is experimental and may lack full feature parity with Windows builds.

### 1.9.0 <small>September 11, 2025</small> { id="1.9.0" }

**Introduction:**

This release marks a major milestone for Immersive APM with the debut of **Tessa**, your AI Assistant. Interact with your telemetry data using **natural language**, via **chat or voice**, to explore performance metrics, investigate anomalies, and generate insights without writing a single query. Also new: the Diagnostics cube for immersive trace visualization, a redesigned grid picker, and new ways to explore the world.

**New Features:**

- **AI Assistant (Tessa)**: Chat and voice-driven assistant for root cause analysis, performance exploration, and guided troubleshooting.
    - Ask questions by typing or speaking.
    - `/mute`, `/unmute`, and `/listen` voice toggle commands.
    - Tessa knows which room you are in and adapts her responses.
    - Chat history is saved and restored across sessions.
    - Built-in help section for onboarding new users.
- **Diagnostics cube**: Immersive trace visualization environment for exploring spans and logs in 3D space.
- **Energy System**: Energy bar showing AI assistant usage with tier-aware capability levels.
- **Grid Picker Redesign**: Card-based grid selection replacing the previous dropdown flow.
    - Demo grid support for exploring the product without live data.
- **ProTips**: Context-aware guidance tooltips that help you discover features as you go.
- **WhereAmI Display**: On-screen indicator showing your current room and location.
- **Water Environment**: Swimming mechanics for world exploration.

**Improvements:**

- Initial support for **macOS (experimental)**.
- **Teleportation overhaul**: Teleport from trace blocks, portal tunnel effects with warp animation.
- Enhanced real-time traffic visualization on performance graphs.
- Improved rendering quality and scalability across device profiles.
- Overhead camera with adjustable height for top-down views.
- Improved connection reliability and clearer error messaging.

**Bug Fixes:**

- Fixed trace layout timing in the Diagnostics cube.
- Fixed avatar getting stuck swimming after teleporting.
- Fixed portal teleportation causing character to fall through ground.
- Fixed grid connection and initialization issues.
- Fixed context switching when navigating between rooms.
- Fixed voice interruption causing stalled prompts.
- Fixed crouching animation.

**Known Issues:**

- Authentication still requires a browser-based login flow.
- macOS support is experimental and may lack full feature parity with Windows builds.

### 1.8.0 <small>April 15, 2025</small> { id="1.8.0" }

**Introduction:**

This release includes the addition of the Spatial Observatory, with video and panels for more details. Materials are courtesy of the [Buzludzha Project](https://buzludzha-project.com/en/?source=if).

**Improvements:**

- .NET 9.0 rollup

**Known Issues:**

- Users still have to provide their authentication information in a browser. This is a standard Entra ID flow. We know it's not ideal ;(

### 1.7.0 <small>March 15, 2025</small> { id="1.7.0" }

**Introduction:**

This release includes an update the authentication utility.

**Improvements:**

- .NET 9.0 rollup

**Known Issues:**

- Users still have to provide their authentication information in a browser. This is a standard Entra ID flow. We know it's not ideal ;(

### 1.6.0 <small>January 15, 2025</small> { id="1.6.0" }

**Introduction:**

This release includes several new features, improvements, and bug fixes to enhance the user experience and performance of IAPM.

**New Features:**

- Top view updates with automatic zoom
- *Live Charts!* - Published/Processed/Failed/Lost counts in the Core
- Added Default/Grid/Graph buttons
- Added UI disable when idle

**Improvements:**

- Changed to using time bar chart for grid view. Spiral view is hidden for the moment
- Accounted for OTLP Exporter delays due to buffering
- Improved process cube creation rates and FPS guards
- Updated platform tooltips to show the name of the application and the operation count

**Bug Fixes:**

- Fixed bug that crashes client on exit
- Fixed issue where platforms did not have tooltips

**Known Issues:**

- Filters UI is being developed

**Installation & Upgrade Instructions:**

- Get the [latest build](./Guides/Installation/index.md) and run the MSI. An existing version Immersive APM will be upgraded.

### 1.5.0 <small>December 16, 2024</small> { id="1.5.0" }

**Introduction:**

This release focuses on various fixes and the introduction of beta VR functionality.

**New Features:**

- Added `BETA VR Functionality` warning

**Improvements:**

- Various topology graph reactive and ambience fixes
- Changed out-of-range block colors to have glow

**Bug Fixes:**

- Fixed XR/HMD awareness issues
- Fixed XR UX issues and added tooltips

**Known Issues:**

- Filters UI is being developed
- *Client crashes on exit*

**Installation & Upgrade Instructions:**

- Get the [latest build](./Guides/Installation/index.md) and run the MSI. An existing version Immersive APM will be upgraded.

### 1.4.0 <small>November 1, 2024</small> { id="1.4.0" }

- Teleport fixes
- Added **Reload current grid** button to grid to reload the grid and fix potential world issues
- Added service name and instance ID on platforms
- Added operation count on platforms
- Process/dependency virtual differentiation

Bug fixes:

- Fixed Platform colors
- Fixed Platform teleport functionality
- Fixed photon coloring and visibility
- Various Spatial Observatory fixes
- Fixed 3D/VR Avatar scale and head issues
- Fixed various framerate issues

### 1.3.0 <small>October 10, 2024</small> { id="1.3.0" }

- Unity 6 upgrade
- Minor shader fixes after upgrade
- Context menu prep
- Teleport to platform prep

### 1.2.2 <small>September 13, 2024</small> { id="1.2.2" }

Bug fixes:

- Fixed bug: Trace/process camera zooms
- Fixed bug: Log tooltips

### 1.2.1 <small>September 10, 2024</small> { id="1.2.1" }

- Fixed bug: generic avatar interactive and proximity zones fixed
- Fixed bug: ground spacing fixed

### 1.2.0 <small>September 10, 2024</small> { id="1.2.0" }

- Replacing female avatar with ragdoll. She's not gone and will be back!
- Added areal views for traces/logs and processes

### 1.1.0 <small>September 3, 2024</small> { id="1.1.0" }

- Local storage prep for replay

Bug fixes:

- Fixed bug: modal dialogs overlapping each other

### 1.0.0 <small>August 26, 2024</small> { id="1.0.0" }

- Public release


### 0.9.2 <small>July 29, 2024</small> { id="0.9.2" }

- Unity upgrade
- Stability and perf improvements

### 0.8.7 <small>July 16, 2024</small> { id="0.8.7" }

- Performance, stability, UI improvements
- Fixed pulses from platforms.
- Changed to `blue sky with clouds` sky.

### 0.8.6 <small>July 2, 2024</small> { id="0.8.6" }

- Performance, stability, UI improvements

[//]: # (GitHub Issue example - Fixed #7313: Improved tooltips mounted in sidebar when feature is disabled)
