---
description: "Authenticate to the DeepCube&trade; Platform API with a personal access token: create one, send it as a Bearer token, choose its scopes, and read 401 and 403 errors."
---

# Authentication

{!template/subscription-required.mdp!}

Scripts and tools call the DeepCube&trade; Platform API with a **personal access token**. Create the token in DeepCube Web and send it in the `Authorization` header of every request.

!!! warning "Microsoft Entra ID tokens are refused"
    The Platform API no longer accepts tokens issued by Microsoft Entra ID (Azure AD) or Azure AD B2C. A request that sends one gets `401`. Replace them with a personal access token.

## Create a personal access token

1. Sign in to DeepCube Web at [web.deepcube.ai](https://web.deepcube.ai){ target="_blank" }.
2. Go to **Settings > Access > Personal access tokens**.
3. Choose what the token can do. Each level grants these [scopes](#scopes):

    | Level | Scopes |
    |-------|--------|
    | **View** (the default) | `read` |
    | **Investigate** | `read`, `write` |
    | **Manage** | `read`, `write`, `manage` |

    Add `credentials` separately, only if the script must create tokens or keys.

4. Give the token a name and choose how long it lasts: 7, 30 (the default) or 90 days.
5. Copy the token. It is shown once.

The same page lists your tokens with their scopes and when each was last used. **Revoke** stops a token on its next request.

!!! warning "Keep tokens secret"
    A token acts as you. Do not commit it to source control; keep it in an environment variable or a secrets manager. Give each script its own token with only the scopes it needs, and revoke a token as soon as it may have leaked.

## Send the token

Send the token as a Bearer token in the `Authorization` header:

```bash
curl -X GET "https://web.deepcube.ai/apm/diagnostics/{gridSecondaryId}/health?api-version=2.0" \
  -H "Authorization: Bearer YOUR_PERSONAL_ACCESS_TOKEN"
```

A request with a body sends the same header. This trace query needs `read`:

```bash
curl -X POST "https://web.deepcube.ai/apm/traces/{gridSecondaryId}?api-version=2.0" \
  -H "Authorization: Bearer YOUR_PERSONAL_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{ "rangeStart": "2026-04-02T00:00:00Z", "rangeEnd": "2026-04-03T00:00:00Z" }'
```

See [Traces](traces.md) for the full query body.

The Platform API reads no other header for authentication.

## Scopes

A token carries one or more scopes. Each endpoint needs one of them; a few, such as token introspection, accept any valid token.

| Scope | What it allows |
|-------|----------------|
| `read` | Read telemetry and configuration: every `GET`, and the trace and log queries sent as `POST`. |
| `write` | Create investigative work, such as clips, tracks, preferences and chat with Tessa. |
| `manage` | Change and delete resources such as grids, environments and invitations. |
| `credentials` | Create credentials: personal access tokens and grid API keys. Only you can grant it, while signed in to DeepCube Web. |

The scopes are independent: `manage` does not include `read`. A script that reads data and then changes a grid needs both.

Scopes limit a token; they never extend your access. A token reaches only the grids you have a role on, and only what your role allows.

### Scope by API page

| Page | Scope |
|------|-------|
| [Traces](traces.md), [Logs](logs.md), [Diagnostics](diagnostics.md), [Charts & Dashboards](charts.md) | `read` for every endpoint |
| [AI Assistant](assistant.md) | `write` for chat, `manage` to change limits, `read` for everything else |

A token that carries only the retired `member` scope reaches no endpoint. Create a new token with the scopes it needs.

## Grid API keys

A grid API key sends telemetry from your applications to one grid. It is not a Platform API credential: it reaches no data endpoint. To get one and configure your OpenTelemetry exporter, see [API Keys](../../Getting-Started/Api-Key/index.md).

## Errors

### 401 Unauthorized

The request has no valid token.

**Common causes:**

- No `Authorization` header, or a value that does not start with `Bearer `
- The token has expired or was revoked
- A Microsoft Entra ID or Azure AD B2C token
- A token copied incompletely

### 403 Forbidden

The token is valid but cannot do this.

When the token lacks the scope the endpoint needs, the response names it. The body includes:

```json
{
  "title": "Forbidden",
  "status": 403,
  "detail": "This token does not hold the 'read' scope this operation needs.",
  "code": "INSUFFICIENT_SCOPE",
  "requiredScope": "read"
}
```

Create a token that carries `requiredScope`.

Other `403` responses:

- `INTERACTIVE_SIGN_IN_REQUIRED`: only a person signed in to DeepCube Web can do this, never a token. Creating a token that carries `credentials` is one such action.
- No `code`: your role on the grid is not high enough for the action, or the token is limited to a different grid. Ask the grid's owner for a higher role, or use a token for that grid.

Most grid endpoints answer `404`, not `403`, for a grid you have no role on, so they do not reveal that it exists.

### 429 Too Many Requests

You sent too many requests. The response has the code `RATE_LIMITED` and a `Retry-After` header: wait as long as it says, then retry. Rate limits for personal access tokens are counted per person, not per token or IP address.
