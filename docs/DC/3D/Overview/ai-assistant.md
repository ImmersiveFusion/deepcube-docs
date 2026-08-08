---
title: Tessa - Your AI Assistant
diataxis: explanation
tags: [explanation, tessa, ai-assistant]
---

# Tessa - Your AI Assistant

This page explains what Tessa is, what makes her different from a generic chatbot, and the conceptual model behind her tools, hats, skills, memory, and energy.

> **Not another chatbot.** Tessa is a purpose-built AI assistant with live access to your telemetry data, your codebase, and a suite of built-in tools. She doesn't guess: she queries your Grid, reads your code, and tells you exactly what's wrong.

## What makes Tessa different

Tessa lives inside the spatial world with you. She can navigate your 3D environment, query live telemetry, read and edit your source code, search the web, spawn specialized sub-agents, and remember context across sessions, all grounded in where you are standing and what you are looking at.

Tessa is available in the immersive surfaces:

- **[DeepCube](../index.md)** (v1.9+) - Chat panel or voice, speak directly to Tessa
- **[DeepCube Studio](../../Studio/index.md)** (v0.1+) - Integrated chat with multi-tab and split pane

Tessa is not part of [DeepCube Web](../../Web/index.md) today. The web portal is for account management and quick monitoring; the assistant lives in the immersive surfaces, where being inside your system is what makes her spatial context work.

Workspaces, conversation history, and Tessa's memory are stored locally on disk; multiple surfaces on the same machine share access through that storage.

## How Tessa thinks: the conceptual model

Tessa is built around four ideas that combine to shape her behavior.

### Tools

Tessa has a fixed set of built-in tools she uses autonomously during a conversation. Tools cover file reading and editing, web search and fetch, voice control, memory, and spawning sub-agents. When connected to a Grid, she also has access to diagnostic tools for live telemetry analysis.

The tools are the *capabilities*. Tessa picks which to use based on what you ask. For the full lookup, see [Tessa tools](../Reference/assistant-tools.md).

### Hats

A **hat** is a lens Tessa wears that changes how she approaches a problem. The Coder hat focuses on small, reviewed code increments. The Architect hat focuses on system design and trade-offs. The Researcher, Reviewer, and Security hats each shape her responses to fit that domain.

You don't have to specify a hat; Tessa picks based on context. But you can put a specific hat on with the `/hat` command when you want to steer her behavior explicitly. For the full hat catalog and command reference, see [Tessa hats](../Reference/assistant-hats.md).

### Skills

A **skill** is a specialist team Tessa can route to. Where hats change *how* Tessa thinks, skills change *who* she calls in. The Problem-Solving skill has agents for research, analysis, architecture decisions, validation, synthesis, and reviews. The Engineering Team skill has agents for backend, frontend, DevSecOps, QA, and security. Other skills cover offensive security, adversarial quality review, systems engineering, and prompt engineering.

You don't invoke skills by name. Describe what you need ("review this code for security issues") and Tessa routes to the right skill and the right agents automatically. Skills are available in the 3D client and Studio; Web integration is not yet shipped. For the full catalog, see [Tessa skills](../Reference/assistant-skills.md).

### Memory

Tessa remembers in three layers. **Session** memory lasts for the current conversation. **Workspace** memory lasts across conversations within a project or Grid. **User** memory lasts across all your workspaces.

Memory is persistent on disk. What Tessa learns in one conversation can surface in the next, which is what makes long-running investigations feel coherent. The persistence model also has confidentiality implications worth understanding before you put sensitive material in front of her. For the layer reference and memory commands, see [Tessa commands and runtime](../Reference/assistant-commands.md).

### Energy

Tessa runs on an energy system. You start each window at **Optimal** (your full subscription quality, full depth of reasoning on hard problems) and drop to **Conserving** (a lighter, faster model) when the window's budget is spent. Every capability still works in Conserving; energy changes how deeply Tessa reasons on hard problems, not which skills she can use. Paid plans always keep a working assistant; free (Start-tier) users who exhaust a window instead wait for it to refill, with a recharge countdown shown. Energy is visible in the chat panel.

The energy bar is the only thing you see. Token counts, model names, and pool sources are deliberately invisible: one bar, one experience. When energy is low, Tessa tells you when she'll be back to full. For tier-by-plan limits, see [Tessa commands and runtime](../Reference/assistant-commands.md).

## Diagnostics: where Tessa shines

When Tessa is connected to a Grid, she's not just answering questions; she's running real diagnostics against live telemetry. Every response is backed by actual data. She queries traces, logs, and metrics through dedicated tools, often chaining several in a single response: check health, identify the unhealthy service, compare it to yesterday, find the slow traces.

The diagnostic capability is what makes DeepCube's AI assistant different from a generic chatbot bolted onto a dashboard. For the full diagnostic catalog and the kinds of questions Tessa can answer, see [Tessa diagnostics](../Reference/assistant-diagnostics.md).

## In 3D: how Tessa is grounded (ALPHA)

Everything in this section describes Tessa as she works today in the 3D environment, where she is labeled Assistant (ALPHA). These behaviors are real and on the conversation path; treat them as present-but-alpha rather than as a finished, polished surface. (For how you reach her, and why Mosey is a router rather than a second brain, see [Mosey and Tessa](companion-and-assistant.md).)

### The console inherits your spatial context

The chat console (open it with **F12**) is global: you can open it anywhere, and it appears as an overlay on top of wherever you are. What makes it more than a floating chat box is that where your location is meaningful, it inherits your spatial context. Stand on a service platform and open the console: it is scoped to that service. Open it inside the Diagnostics cube on a specific trace: it is scoped to that trace. Where you stand sets the scope, so you do not paste context or describe what you are looking at, because you are already standing in it. This is why "what's wrong here?" gets an answer about *here*: your avatar's location is what "here" means. A flat dashboard has no "where you are", so this is native to the spatial model rather than bolted on.

### Three response channels

When Tessa answers, she does so across three channels, each with a distinct purpose:

- **Thinking** shows *how she understood what you asked*. It is the transparency layer, letting you check that she got what you meant before you weigh the answer.
- **Spoken** is a deliberately concise summary, the gist rather than the whole answer. It is what she says aloud when voice is on, so she is not reading a wall of text at you.
- **Text** is the whole output, the complete detailed response you read in the console.

Voice is opt-in and off by default, so by default you read the Text. Turn voice on and the pairing becomes "hear the gist, read the detail": she speaks the Spoken summary while the full Text stays on screen. Three channels for three needs: transparency, brevity, and completeness.

### Glass-box reasoning

Tessa's reasoning is visible in the console rather than hidden. She shows her thinking and her tool calls as she works, so you can watch how she arrives at an answer instead of taking it on faith. Because the process is on screen, Tessa is interrogable: she gives an answer, you can push back ("why?", "prove it"), and she grounds the response in the evidence she pulled. It is a back-and-forth, not a one-shot verdict.

### The grounding stack

What makes Tessa's answers specific is the range of context she can reason over at once. Her grounding stack combines:

- **Your telemetry**, the live traces, logs, and metrics from the grid you are in.
- **Your code**, added as a **workspace**. You point Tessa at a codebase, give it a name, and she grounds her reasoning in the source. You can set up multiple workspaces and switch between them mid-session, right in the console dialog. Grounded in your code, an answer can move from a generic "SQL error, wrong table" to "that is intentional behavior for this app", because she read the source.
- **Your spatial location**, as described above: where you stand sets what she is reasoning about.
- **Pasted images**, through vision. Mid-conversation you can paste a screenshot into the console (Ctrl-V) and Tessa takes it in as additional context.

The through-line is that you do not describe context to Tessa; you **give** it to her, by standing somewhere, pointing her at a repo, or pasting a picture. That combination, telemetry plus code plus spatial location plus a pasted image, is what lets her answer about your specific situation rather than in generalities.

## Getting started

1. Open the chat panel in any DeepCube surface.
2. Type a question, or click the microphone to speak.
3. Try: *"How is my system doing right now?"*
4. Follow up naturally. Tessa remembers conversation context.

!!! tip "Context-aware in 3D"
    In the 3D environment, Tessa knows which room you're in and which service you're looking at. Ask "What's wrong here?" and she'll know what you mean.

## Where to next

- **For step-by-step tasks** (voice, image input, prompt patterns): see [How-to guides](../How-to/index.md).
- **For commands, tools, hats, skills, diagnostics tables:** see [Reference](../Reference/index.md).
- **To learn DeepCube hands-on:** see [Tutorials](../Tutorials/index.md).
