---
title: Share images with Tessa
diataxis: how-to
tags: [how-to, tessa, vision, multimodal]
---

# Share images with Tessa

This guide shows how to paste screenshots, dashboards, or photos into the chat so Tessa can analyze the image alongside your question.

> *Available since IAPM v1.12, Web v3.131, and Studio v0.7*

Paste a screenshot into the chat and Tessa will analyze it. No need to describe what you see - just show her.

## How to Send Images

There are two ways to share images with Tessa:

### Clipboard (Ctrl+V / Cmd+V)

1. **Copy an image** to your clipboard (a screenshot, snip, or any image)
2. **Paste it into the Tessa chat panel** with **Ctrl+V** on Windows and Linux, or **Cmd+V** on macOS
3. The image appears in the chat as an attachment
4. **Type your question** about the image and send

### Commands

| Command | What It Does |
|---------|--------------|
| `/paste` | Load image from clipboard and analyze (optionally add a prompt after) |
| `/paste What does this error mean?` | Load clipboard image with a specific question |
| `/image path/to/file.png` | Analyze an image file from disk |
| `/image screenshot.png What's wrong here?` | Analyze a file with a specific question |

## Supported Formats

PNG, JPEG, GIF, WebP, and BMP. Images can be loaded from clipboard, file path, or byte stream.

## What Tessa Can Analyze

### Error Messages and Stack Traces

Paste a screenshot of an error dialog, exception, or stack trace. Tessa reads the text, identifies the error, and explains what it means in the context of your system.

!!! example "Try asking"
    - "What does this error mean?" *(with screenshot pasted)*
    - "I'm seeing this exception - what should I do?"
    - "Is this stack trace related to the issue we were discussing?"

### Dashboard Screenshots

Share a screenshot from any monitoring tool - Grafana, Azure Monitor, or even IAPM itself. Tessa interprets the visual data and provides analysis.

!!! example "Try asking"
    - "What do you see in this dashboard?"
    - "Does this graph show anything concerning?"
    - "This chart spiked at 2pm - what happened?"

### Log Output

Paste a screenshot of log output that's hard to copy as text (terminal windows, remote desktop sessions, mobile photos of screens).

!!! example "Try asking"
    - "Can you read these logs and tell me what's wrong?"
    - "What patterns do you see in this log output?"

### Configuration and Code

Share snippets of configuration files, code, or infrastructure diagrams for Tessa to review.

!!! example "Try asking"
    - "Is there anything wrong with this config?"
    - "Does this code look like it could cause the timeout issue?"

## Tips for Best Results

- **Crop to the relevant area** - a focused screenshot gives better results than a full desktop capture
- **Include context in your question** - "What does this error mean?" works, but "This error started appearing after we deployed v2.3 - what does it mean?" works better
- **Combine with diagnostics** - paste a screenshot and ask Tessa to cross-reference it with live data: "I see this error - is it related to the latency spike on order-service?"
- **Use high resolution** - Tessa can read small text, but larger and clearer images produce faster, more accurate results

## Related

- **For concept and design:** see [Tessa - Your AI Assistant](../Overview/ai-assistant.md).
- **To use voice alongside pasted images:** see [Talk to Tessa with voice](assistant-voice.md).
- **For prompt patterns:** see [Write better prompts for Tessa](assistant-prompts.md).
