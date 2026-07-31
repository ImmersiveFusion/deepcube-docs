---
title: Talk to Tessa with voice
diataxis: how-to
tags: [how-to, tessa, voice]
---

# Talk to Tessa with voice

This guide shows how to use speech to ask Tessa questions and hear her responses, without taking your hands off your work.

> Talk to Tessa like a teammate. Ask questions out loud, get spoken answers back - no keyboard required.

Voice interaction lets you have a natural conversation with Tessa using speech recognition and synthesis, keeping your hands free while you work in the 3D environment.

## Activating Voice

1. **Click the microphone icon** in the chat panel to begin listening
2. **Type `/voice on`** to enable voice mode
3. **Type `/voice`** to toggle voice on or off

Once active, Tessa listens for your question, processes it, and responds with synthesized speech while also showing the text response in the chat panel.

## Voice Commands

| Command | What It Does |
|---------|--------------|
| `/voice` | Toggle voice mode on/off |
| `/voice on` | Enable voice mode |
| `/voice off` | Disable voice mode |
| `/mute` | Mute Tessa's speech output (she still responds in text) |
| `/unmute` | Re-enable Tessa's speech output |

!!! tip "Mute vs voice off"
    `/mute` silences Tessa's spoken responses but keeps voice recognition active - you can still speak to her. `/voice off` disables both speech input and output.

## Changing Tessa's Voice

Tessa can speak in different voices. You choose her voice in [IAPM Web](../../Web/index.md), not in the 3D client:

1. **Sign in to IAPM Web** and open your **Account**.
2. **Go to Preferences** and find the **Tessa Voice** dropdown.
3. **Pick a voice** from the list. Voices are named by language, gender, and style, for example:
    - British English - Female - Crisp (en-GB)
    - British English - Male - Refined (en-GB)
    - US English - Female - Bright (en-US)
    - US English - Female - Calm (en-US)
    - US English - Male - Steady (en-US)
    - French - Female - Warm (fr-FR)
    - German - Female - Clear (de-DE)
    - Spanish - Female - Bright (es-ES)

Your selection is saved to your account and applies to Tessa wherever she speaks, including the 3D client.

!!! note
    You cannot change the voice from inside the 3D client. Voice selection is available only in IAPM Web account preferences. Once you set it there, the 3D client uses your chosen voice.

## Interrupting Tessa

If Tessa is speaking and you need to cut in:

- **Press Escape** to stop her current speech immediately

Pressing Escape does not lose your place in the conversation. Tessa's text response remains in the chat, and you can continue asking follow-up questions right away.

## Tips for VR Headset Users

VR is not actively maintained right now. If you already run a headset, voice is the primary interaction mode:

- **Keep voice mode on** so the microphone stays active between questions. You can have a continuous conversation without re-activating the mic each time.
- **Be specific with service names** - speak them clearly. Tessa uses your Grid's service catalog to match what she hears.
- **Combine voice with navigation** - teleport to a service platform and ask "What's wrong here?" Tessa uses your position as context.

## Combining Voice and Text

Voice and text work interchangeably in the same conversation:

- Speak a question, then type a follow-up
- Type a question, then speak "Tell me more"
- Switch between modes freely - conversation context is preserved regardless of input method

Chat history captures both voice and typed interactions, and everything is saved across sessions.

## Related

- **For concept and design:** see [Tessa - Your AI Assistant](../Overview/ai-assistant.md).
- **To share images alongside voice questions:** see [Share images with Tessa](assistant-vision.md).
- **For prompt patterns that work with voice:** see [Write better prompts for Tessa](assistant-prompts.md).
