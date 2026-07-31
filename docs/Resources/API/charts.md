# Charts & Dashboards

{!template/subscription-required.mdp!}

The Charts and Dashboards API provides access to chart metadata, rendered chart images, chart data for custom rendering, and dashboard layouts.

!!! info "Authentication Required"
    All endpoints require a valid `Authorization: Bearer {token}` or `api-key: {key}` header. See [Authentication](authentication.md).

---

## Get Chart Metadata

Retrieve metadata for a specific chart, including its type, title, and configuration.

```
GET /apm/charts/{gridSecondaryId}/charts/{chartSecondaryId}
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `chartSecondaryId` | path | `string` (UUID) | Yes | Chart identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/charts/3fa85f64-5717-4562-b3fc-2c963f66afa6/charts/b2c74a11-1234-4abc-9def-567890abcdef?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "id": "b2c74a11-1234-4abc-9def-567890abcdef",
  "title": "Request Latency (p95)",
  "chartType": "line",
  "serviceName": "order-service",
  "metric": "latency_p95",
  "unit": "ms",
  "createdAt": "2026-03-15T08:00:00Z",
  "updatedAt": "2026-04-01T12:30:00Z"
}
```

---

## Render Chart as Image

Render a chart as a PNG image with specified dimensions and theme.

```
GET /apm/charts/{gridSecondaryId}/charts/{chartId}/render
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `chartId` | path | `string` | Yes | Chart identifier |
| `width` | query | `integer` | No | Image width in pixels (default: 800) |
| `height` | query | `integer` | No | Image height in pixels (default: 400) |
| `theme` | query | `string` | No | Color theme - `dark` or `light` (default: `dark`) |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/charts/3fa85f64-5717-4562-b3fc-2c963f66afa6/charts/b2c74a11-1234-4abc-9def-567890abcdef/render?width=1200&height=600&theme=dark&api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  --output chart.png
```

### Response

Returns a `image/png` binary response.

| Header | Value |
|--------|-------|
| `Content-Type` | `image/png` |
| `Content-Disposition` | `inline; filename="chart.png"` |

!!! tip "Embedding Charts"
    Use the render endpoint to embed live chart images in Slack messages, email reports, or external dashboards. Adjust `width` and `height` to fit your layout.

---

## Get Chart Range Data

Retrieve the raw data points for a chart within a time range. Use this to render charts in your own UI or perform custom analysis.

```
GET /apm/charts/{gridSecondaryId}/charts/{chartId}/range-data
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `chartId` | path | `string` | Yes | Chart identifier |
| `rangeStart` | query | `datetime` (ISO 8601) | No | Start of time range |
| `rangeEnd` | query | `datetime` (ISO 8601) | No | End of time range |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/charts/3fa85f64-5717-4562-b3fc-2c963f66afa6/charts/b2c74a11-1234-4abc-9def-567890abcdef/range-data?rangeStart=2026-04-03T08:00:00Z&rangeEnd=2026-04-03T10:00:00Z&api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "chartId": "b2c74a11-1234-4abc-9def-567890abcdef",
  "title": "Request Latency (p95)",
  "unit": "ms",
  "rangeStart": "2026-04-03T08:00:00Z",
  "rangeEnd": "2026-04-03T10:00:00Z",
  "series": [
    {
      "label": "order-service",
      "dataPoints": [
        { "timestamp": "2026-04-03T08:00:00Z", "value": 120 },
        { "timestamp": "2026-04-03T08:15:00Z", "value": 115 },
        { "timestamp": "2026-04-03T08:30:00Z", "value": 130 },
        { "timestamp": "2026-04-03T08:45:00Z", "value": 125 },
        { "timestamp": "2026-04-03T09:00:00Z", "value": 450 },
        { "timestamp": "2026-04-03T09:15:00Z", "value": 980 },
        { "timestamp": "2026-04-03T09:30:00Z", "value": 2100 },
        { "timestamp": "2026-04-03T09:45:00Z", "value": 2340 }
      ]
    }
  ]
}
```

---

## Get Dashboard

Retrieve a dashboard definition including its layout and associated charts.

```
GET /apm/dashboards/{gridSecondaryId}/dashboards/{dashboardSecondaryId}
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `dashboardSecondaryId` | path | `string` (UUID) | Yes | Dashboard identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/dashboards/3fa85f64-5717-4562-b3fc-2c963f66afa6/dashboards/c3d85b22-2345-4bcd-aeef-678901bcdef0?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "id": "c3d85b22-2345-4bcd-aeef-678901bcdef0",
  "title": "Production Overview",
  "description": "Key performance indicators for production services",
  "createdAt": "2026-03-01T10:00:00Z",
  "updatedAt": "2026-04-02T16:45:00Z",
  "charts": [
    {
      "chartId": "b2c74a11-1234-4abc-9def-567890abcdef",
      "title": "Request Latency (p95)",
      "chartType": "line",
      "position": { "row": 0, "col": 0, "width": 6, "height": 4 }
    },
    {
      "chartId": "d4e96c33-3456-4cde-bfef-789012cdef01",
      "title": "Error Rate by Service",
      "chartType": "bar",
      "position": { "row": 0, "col": 6, "width": 6, "height": 4 }
    },
    {
      "chartId": "e5fa7d44-4567-4def-cfef-890123def012",
      "title": "Throughput (req/s)",
      "chartType": "area",
      "position": { "row": 4, "col": 0, "width": 12, "height": 4 }
    }
  ]
}
```

!!! tip "Building Custom Dashboards"
    Use the dashboard endpoint to retrieve the layout, then call the [chart range data](#get-chart-range-data) endpoint for each chart to fetch the data and render in your own UI framework.
