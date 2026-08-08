# DeepCube Studio Features

!!! warning "Early Access"
    DeepCube Studio is in early access. Features and interfaces may change between releases.

{!template/subscription-required.mdp!}

DeepCube Studio provides AI-powered telemetry analysis through a lightweight native desktop client. These features give you fast access to Tessa, workspaces, and organizational knowledge - without the full 3D environment.

## Feature Overview

| Feature | Description | Since |
|---------|-------------|-------|
| **AI Chat Interface** | Natural language conversations with Tessa to explore telemetry data | v0.1.0 |
| **Voice Interaction** | Speak to Tessa and hear spoken responses | v0.1.0 |
| **Workspace Management** | Browse, navigate, and manage workspace files and artifacts | v0.1.0 |
| **Multi-Tab Conversations** | Run multiple Tessa conversations simultaneously in separate tabs | v0.5.0 |
| **Split Pane View** | Drag, split, and reorder conversation panes side by side | v0.5.0 |
| **Session Persistence** | Chat history and sessions survive application restarts | v0.5.0 |
| **Workspace Browser** | Browse workspace files and copy paths from the file tree | v0.5.0 |
| **Multimodal Vision** | Paste images into prompts for Tessa to analyze alongside telemetry | v0.7.0 |
| **Skills System** | Tessa uses modular skills for specialized analysis tasks | v0.7.0 |
| **Memory and Context** | Tessa remembers context across sessions for coherent conversations | v0.7.0 |

## AI Chat Interface

Chat with Tessa using natural language to query your APM data, investigate issues, and get root cause analysis. Tessa understands your telemetry context and can answer questions about metrics, traces, logs, and system health.

- Ask questions in plain language
- Get intelligent explanations and recommendations
- Query live APM data through conversational prompts
- Review tool results inline within the conversation

## Multi-Tab Conversations

Run multiple independent conversations with Tessa at the same time. Each tab maintains its own context and history, so you can investigate different issues in parallel.

| Action | How |
|--------|-----|
| New tab | Create a new conversation tab from the tab bar |
| Switch tabs | Click on any tab to switch between conversations |
| Close tab | Close a tab when you are done with a conversation |
| Reorder tabs | Drag tabs to rearrange their order |

## Split Pane View

Arrange multiple conversations side by side for comparison and multitasking. Drag tabs to split the view horizontally, then resize panes to your preference.

## Voice Interaction

Speak to Tessa and receive spoken responses. Voice interaction lets you keep your hands free while exploring telemetry data.

## Multimodal Vision

Paste screenshots, diagrams, or other images directly into your prompt. Tessa analyzes the visual content alongside your telemetry data - useful for sharing error screenshots, architecture diagrams, or dashboard snapshots.

## Skills System

Tessa uses modular skills to perform specialized tasks. Skills extend Tessa's capabilities with purpose-built analysis workflows, giving you more precise and actionable results for specific types of investigations.

## Workspace Management

Browse and manage your workspace files and artifacts from within Studio. The workspace browser provides a file tree view where you can navigate files and copy paths for use in your conversations.

## Session Persistence and Memory

Your conversations are saved automatically and restored when you restart Studio. Tessa also retains context and memory across sessions, so you can pick up where you left off without re-explaining your environment.

## Comparison with Other DeepCube Surfaces

| Capability | Studio | 3D | Web |
|------------|--------|----|-----|
| Tessa chat and voice | :material-check: | :material-check: | :material-check: |
| Workspaces and artifacts | :material-check: | :material-check: | :material-check: |
| Multi-tab conversations | :material-check: | :material-close: | :material-close: |
| Multimodal vision | :material-check: | :material-close: | :material-close: |
| Skills system | :material-check: | :material-close: | :material-close: |
| 3D visualization | :material-close: | :material-check: | :material-close: |
| Browser access | :material-close: | :material-close: | :material-check: |
