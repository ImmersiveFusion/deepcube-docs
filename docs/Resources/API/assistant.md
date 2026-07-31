# AI Assistant

{!template/subscription-required.mdp!}

The AI Assistant API provides programmatic access to Tessa - IAPM's purpose-built AI for application diagnostics. Send chat prompts, convert text to speech, recognize spoken audio, track usage, and manage Grid-level limits.

!!! info "Authentication Required"
    All endpoints require a valid `Authorization: Bearer {token}` or `api-key: {key}` header. See [Authentication](authentication.md).

## Instance Identifiers

The Chat and Speech endpoints use an `instanceSecondaryId` rather than a `gridSecondaryId`. An AI Assistant instance represents a Tessa session within a specific Grid. When a user starts a Tessa session (via IAPM 3D, Web, or Studio), an instance is created and its ID is returned. Use this ID for all chat and speech requests within that session. Usage and Limits endpoints continue to use `gridSecondaryId`.

---

## Chat

### Process Chat Prompt

Send a natural language prompt to Tessa and receive a diagnostic response. Tessa analyzes your Grid's live telemetry data to answer questions about application health, performance, and incidents.

```
POST /assistant/chat/{instanceSecondaryId}
```

#### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `instanceSecondaryId` | path | `string` (UUID) | Yes | AI Assistant instance identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

#### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `prompt` | `string` | Yes | Natural language question or command |
| `conversationId` | `string` (UUID) | No | Conversation ID for multi-turn context |

#### Example Request

```bash
curl -X POST "https://api-azure.iapm.app/assistant/chat/a1b2c3d4-e5f6-7890-abcd-ef1234567890?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Why is the payment service returning errors?",
    "conversationId": "conv-98765432-abcd-ef01-2345-678901234567"
  }'
```

#### Example Response

```json
{
  "response": "The payment-service is experiencing a high error rate (8.5%) caused by database connection pool exhaustion. The PostgreSQL primary connection pool has been at 100% capacity (200/200 connections) since 09:42 UTC. This is causing TimeoutException errors on the POST /api/payments endpoint. I recommend increasing the connection pool size or investigating long-running queries that may be holding connections.",
  "conversationId": "conv-98765432-abcd-ef01-2345-678901234567",
  "sources": [
    {
      "type": "diagnosis",
      "description": "Root cause analysis - connection pool exhaustion",
      "confidence": 0.92
    },
    {
      "type": "traces",
      "description": "847 timeout exceptions in payment-service",
      "traceCount": 847
    }
  ],
  "suggestedFollowUps": [
    "Show me the slowest queries on the PostgreSQL primary",
    "When did this issue start?",
    "Which endpoints are most affected?"
  ],
  "energyConsumed": 1
}
```

---

## Speech

### Text-to-Speech

Convert text to spoken audio using Tessa's voice. Returns an audio file suitable for playback in applications or VR environments.

```
POST /assistant/speech/{instanceSecondaryId}/synthesize
```

#### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `instanceSecondaryId` | path | `string` (UUID) | Yes | AI Assistant instance identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

#### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `text` | `string` | Yes | Text to convert to speech |
| `voice` | `string` | No | Voice identifier (default: Tessa's voice) |
| `speed` | `number` | No | Playback speed multiplier (default: `1.0`) |

#### Example Request

```bash
curl -X POST "https://api-azure.iapm.app/assistant/speech/a1b2c3d4-e5f6-7890-abcd-ef1234567890/synthesize?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "The payment service error rate has returned to normal levels.",
    "speed": 1.0
  }' \
  --output response.wav
```

#### Response

Returns an audio binary response.

| Header | Value |
|--------|-------|
| `Content-Type` | `audio/wav` |

---

### Speech Recognition

Upload an audio file and receive the transcribed text. Use this for voice-driven interaction with Tessa.

```
POST /assistant/speech/{instanceSecondaryId}/recognize
```

#### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `instanceSecondaryId` | path | `string` (UUID) | Yes | AI Assistant instance identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

#### Request Body

Multipart form data with an audio file.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `audio` | `file` (binary) | Yes | Audio file (WAV, MP3, OGG) - max 1 MB |

!!! warning "File Size Limit"
    Audio uploads are limited to 1 MB. Longer recordings should be split into smaller segments.

#### Example Request

```bash
curl -X POST "https://api-azure.iapm.app/assistant/speech/a1b2c3d4-e5f6-7890-abcd-ef1234567890/recognize?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -F "audio=@recording.wav"
```

#### Example Response

```json
{
  "text": "What is the current error rate on the payment service?",
  "confidence": 0.96,
  "durationMs": 3200
}
```

---

## Usage

### Get Energy Status

Retrieve the authenticated user's current AI Assistant energy balance. Energy is consumed by chat interactions and regenerates over time.

```
GET /assistant/usage/energy
```

#### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `api-version` | query | `string` | Yes | API version - `2.0` |

#### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/assistant/usage/energy?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

#### Example Response

```json
{
  "currentEnergy": 42,
  "maxEnergy": 50,
  "regenerationRate": 1,
  "regenerationIntervalMinutes": 30,
  "nextRegenerationAt": "2026-04-03T10:30:00Z"
}
```

---

### Get Grid Usage Status

Get the AI Assistant usage status for the authenticated user within a specific Grid.

```
GET /assistant/usage/{gridSecondaryId}/status
```

#### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

#### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/assistant/usage/3fa85f64-5717-4562-b3fc-2c963f66afa6/status?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

#### Example Response

```json
{
  "gridSecondaryId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "enabled": true,
  "promptsUsedToday": 18,
  "promptLimitToday": 100,
  "lastUsedAt": "2026-04-03T09:55:00Z"
}
```

---

### Get Usage Summary

Retrieve an aggregated usage summary for the authenticated user within a Grid over a date range.

```
GET /assistant/usage/{gridSecondaryId}/summary
```

#### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `from` | query | `datetime` (ISO 8601) | Yes | Start date for the summary |
| `to` | query | `datetime` (ISO 8601) | Yes | End date for the summary |
| `api-version` | query | `string` | Yes | API version - `2.0` |

#### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/assistant/usage/3fa85f64-5717-4562-b3fc-2c963f66afa6/summary?from=2026-03-01T00:00:00Z&to=2026-04-01T00:00:00Z&api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

#### Example Response

```json
{
  "gridSecondaryId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "from": "2026-03-01T00:00:00Z",
  "to": "2026-04-01T00:00:00Z",
  "totalPrompts": 342,
  "totalEnergyConsumed": 342,
  "totalSpeechSyntheses": 28,
  "totalSpeechRecognitions": 15,
  "dailyBreakdown": [
    { "date": "2026-03-01", "prompts": 12, "energy": 12 },
    { "date": "2026-03-02", "prompts": 8, "energy": 8 }
  ]
}
```

---

### Get My Usage Across Grids

Retrieve the authenticated user's AI Assistant usage across all Grids they have access to.

```
GET /assistant/usage/me
```

#### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `api-version` | query | `string` | Yes | API version - `2.0` |

#### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/assistant/usage/me?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

#### Example Response

```json
{
  "grids": [
    {
      "gridSecondaryId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "gridName": "Production",
      "promptsUsedToday": 18,
      "promptLimitToday": 100,
      "enabled": true
    },
    {
      "gridSecondaryId": "9ab12c34-d567-8901-ef23-456789abcdef",
      "gridName": "Staging",
      "promptsUsedToday": 5,
      "promptLimitToday": 50,
      "enabled": true
    }
  ]
}
```

---

## Limits

### Get Grid Limits

Retrieve the AI Assistant limits and current usage for a Grid.

```
GET /assistant/limits/{gridSecondaryId}
```

#### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

#### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/assistant/limits/3fa85f64-5717-4562-b3fc-2c963f66afa6?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

#### Example Response

```json
{
  "gridSecondaryId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "dailyPromptLimit": 100,
  "dailyPromptsUsed": 67,
  "monthlySpeechMinutes": 60,
  "monthlySpeechMinutesUsed": 12.5,
  "maxConcurrentSessions": 5,
  "activeSessions": 2
}
```

---

### Update Grid Limits

Update the AI Assistant limits for a Grid. Allows Grid owners to adjust daily prompt limits, speech minutes, and concurrent session caps.

```
PUT /assistant/limits/{gridSecondaryId}
```

!!! warning "Owner Role Required"
    This endpoint requires the **Owner** role on the Grid. Users with Member, User, or Guest roles will receive a `403 Forbidden` response.

#### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

#### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `dailyPromptLimit` | `integer` | No | Maximum prompts per user per day |
| `monthlySpeechMinutes` | `integer` | No | Maximum speech minutes per month |
| `maxConcurrentSessions` | `integer` | No | Maximum concurrent AI Assistant sessions |

#### Example Request

```bash
curl -X PUT "https://api-azure.iapm.app/assistant/limits/3fa85f64-5717-4562-b3fc-2c963f66afa6?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "dailyPromptLimit": 150,
    "monthlySpeechMinutes": 120,
    "maxConcurrentSessions": 10
  }'
```

#### Example Response

```json
{
  "gridSecondaryId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "dailyPromptLimit": 150,
  "monthlySpeechMinutes": 120,
  "maxConcurrentSessions": 10,
  "updatedAt": "2026-04-03T10:15:00Z",
  "updatedBy": "user@example.com"
}
```
