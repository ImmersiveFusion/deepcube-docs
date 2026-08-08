# Node.js Instrumentation

{!template/subscription-required.mdp!}

Instrument your Node.js applications with OpenTelemetry to send traces, metrics, and logs to DeepCube. This guide covers Express.js, NestJS, auto-instrumentation, and manual SDK usage.

[:octicons-arrow-left-24: Back to Instrument Overview](../index.md)

## Install Packages

Install the core OpenTelemetry packages:

=== "npm"

    ```bash
    npm install @opentelemetry/sdk-node \
      @opentelemetry/api \
      @opentelemetry/exporter-trace-otlp-grpc \
      @opentelemetry/exporter-metrics-otlp-grpc \
      @opentelemetry/auto-instrumentations-node \
      @opentelemetry/resources \
      @opentelemetry/semantic-conventions
    ```

=== "yarn"

    ```bash
    yarn add @opentelemetry/sdk-node \
      @opentelemetry/api \
      @opentelemetry/exporter-trace-otlp-grpc \
      @opentelemetry/exporter-metrics-otlp-grpc \
      @opentelemetry/auto-instrumentations-node \
      @opentelemetry/resources \
      @opentelemetry/semantic-conventions
    ```

## Auto-Instrumentation Setup

Create a `tracing.js` (or `tracing.ts`) file that initializes OpenTelemetry before your application code loads:

```javascript
// tracing.js - must be required/imported BEFORE your app
const { NodeSDK } = require('@opentelemetry/sdk-node');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-grpc');
const { OTLPMetricExporter } = require('@opentelemetry/exporter-metrics-otlp-grpc');
const { PeriodicExportingMetricReader } = require('@opentelemetry/sdk-metrics');
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');
const { Resource } = require('@opentelemetry/resources');
const { ATTR_SERVICE_NAME, ATTR_SERVICE_VERSION } = require('@opentelemetry/semantic-conventions');

const sdk = new NodeSDK({
  resource: new Resource({
    [ATTR_SERVICE_NAME]: process.env.OTEL_SERVICE_NAME || 'my-node-app',
    [ATTR_SERVICE_VERSION]: '1.0.0',
  }),
  traceExporter: new OTLPTraceExporter({
    url: 'https://otlp.iapm.app',
    headers: { 'api-key': 'YOUR-API-KEY' },
  }),
  metricReader: new PeriodicExportingMetricReader({
    exporter: new OTLPMetricExporter({
      url: 'https://otlp.iapm.app',
      headers: { 'api-key': 'YOUR-API-KEY' },
    }),
  }),
  instrumentations: [getNodeAutoInstrumentations()],
});

sdk.start();

// Graceful shutdown
process.on('SIGTERM', () => {
  sdk.shutdown()
    .then(() => console.log('OpenTelemetry shut down'))
    .catch((err) => console.error('Error shutting down OpenTelemetry', err))
    .finally(() => process.exit(0));
});
```

### Running with the Tracing File

Load the tracing file before your application:

=== "Node.js require"

    ```bash
    node -r ./tracing.js app.js
    ```

=== "TypeScript"

    ```bash
    ts-node -r ./tracing.ts app.ts
    ```

=== "Environment variable"

    ```bash
    NODE_OPTIONS="--require ./tracing.js" node app.js
    ```

## Express.js Setup

With auto-instrumentation configured via `tracing.js`, Express routes are traced automatically:

```javascript
// app.js
const express = require('express');
const app = express();

app.get('/api/orders', async (req, res) => {
  const orders = await db.query('SELECT * FROM orders');
  res.json(orders);
});

app.get('/api/orders/:id', async (req, res) => {
  const order = await db.query('SELECT * FROM orders WHERE id = $1', [req.params.id]);
  res.json(order);
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

Run with:

```bash
node -r ./tracing.js app.js
```

Each HTTP request automatically generates a trace span with route, status code, and duration.

## NestJS Setup

For NestJS, load the tracing module before the application bootstraps:

```typescript
// tracing.ts
import { NodeSDK } from '@opentelemetry/sdk-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-grpc';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { Resource } from '@opentelemetry/resources';
import { ATTR_SERVICE_NAME } from '@opentelemetry/semantic-conventions';

const sdk = new NodeSDK({
  resource: new Resource({
    [ATTR_SERVICE_NAME]: 'my-nestjs-app',
  }),
  traceExporter: new OTLPTraceExporter({
    url: 'https://otlp.iapm.app',
    headers: { 'api-key': 'YOUR-API-KEY' },
  }),
  instrumentations: [getNodeAutoInstrumentations()],
});

sdk.start();
```

Update your `main.ts` or start command:

```bash
node -r ./tracing.js dist/main.js
```

Or in `package.json`:

```json
{
  "scripts": {
    "start": "node -r ./tracing.js dist/main.js",
    "start:dev": "NODE_OPTIONS='--require ./tracing.js' nest start --watch"
  }
}
```

## Manual Instrumentation

Create custom spans for your business logic:

```javascript
const { trace, SpanStatusCode } = require('@opentelemetry/api');

const tracer = trace.getTracer('myapp.orders');

async function processOrder(orderId) {
  return tracer.startActiveSpan('processOrder', async (span) => {
    span.setAttribute('order.id', orderId);

    try {
      const order = await getOrder(orderId);
      span.setAttribute('order.total', order.total);

      await chargePayment(order);
      span.addEvent('payment.completed');

      await fulfillOrder(order);

      span.setStatus({ code: SpanStatusCode.OK });
      return order;
    } catch (error) {
      span.setStatus({ code: SpanStatusCode.ERROR, message: error.message });
      span.recordException(error);
      throw error;
    } finally {
      span.end();
    }
  });
}
```

### Custom Metrics

```javascript
const { metrics } = require('@opentelemetry/api');

const meter = metrics.getMeter('myapp.orders');

const ordersCounter = meter.createCounter('orders.processed', {
  unit: 'orders',
  description: 'Number of orders processed',
});

const orderDuration = meter.createHistogram('orders.processing.duration', {
  unit: 'ms',
  description: 'Order processing time',
});

async function processOrder(order) {
  const start = Date.now();

  await doProcessing(order);

  const duration = Date.now() - start;
  ordersCounter.add(1, { 'order.type': order.type });
  orderDuration.record(duration);
}
```

## Environment Variable Configuration

The OpenTelemetry Node.js SDK reads these variables automatically:

| Variable | Value | Description |
|----------|-------|-------------|
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `https://otlp.iapm.app` | OTLP collector endpoint |
| `OTEL_EXPORTER_OTLP_HEADERS` | `api-key=YOUR-API-KEY` | Authentication header |
| `OTEL_SERVICE_NAME` | `your-service-name` | Service name shown in DeepCube |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `grpc` | Protocol (grpc or http/protobuf) |
| `OTEL_TRACES_EXPORTER` | `otlp` | Trace exporter type |
| `OTEL_METRICS_EXPORTER` | `otlp` | Metrics exporter type |
| `OTEL_LOG_LEVEL` | `info` | SDK diagnostic log level |
| `NODE_OPTIONS` | `--require ./tracing.js` | Load tracing before app |

When using environment variables, the SDK auto-configures the exporters:

```javascript
const sdk = new NodeSDK({
  instrumentations: [getNodeAutoInstrumentations()],
  // endpoint and headers come from environment variables
});
```

## Verify It's Working

1. Run your instrumented application with `node -r ./tracing.js app.js`
2. Send a few HTTP requests to generate traces
3. Open [portal.iapm.app](https://portal.iapm.app){ target="_blank" } and select your Grid
4. Click **Enter** - you should see your service and traces within a few minutes

!!! tip "Quick verification with console exporter"
    Add the console exporter to see spans in your terminal during development:

    ```bash
    npm install @opentelemetry/sdk-trace-base
    ```

    ```javascript
    const { ConsoleSpanExporter } = require('@opentelemetry/sdk-trace-base');

    const sdk = new NodeSDK({
      traceExporter: new ConsoleSpanExporter(),
      // ...
    });
    ```

## Troubleshooting

### No data appearing in DeepCube

- Verify that `tracing.js` is loaded **before** your application code. Use `node -r ./tracing.js` or `NODE_OPTIONS="--require ./tracing.js"`.
- Verify the API key by copying a fresh one from [portal.iapm.app](https://portal.iapm.app){ target="_blank" } under **Administration > Grids > Instrument**.
- Check network connectivity: `curl -v https://otlp.iapm.app`.

### gRPC connection errors

- Ensure `@grpc/grpc-js` is installed: `npm install @grpc/grpc-js`.
- If behind a corporate proxy, you may need to use the HTTP/protobuf exporter instead:

    ```bash
    npm install @opentelemetry/exporter-trace-otlp-proto
    ```

    ```javascript
    const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-proto');
    ```

### ES Modules (import/export) compatibility

- For ESM applications, use `--import` instead of `--require`:

    ```bash
    node --import ./tracing.mjs app.mjs
    ```

- Ensure your `tracing.mjs` uses `import` syntax.

### Memory leaks with auto-instrumentation

- Disable instrumentations you do not need:

    ```javascript
    getNodeAutoInstrumentations({
      '@opentelemetry/instrumentation-fs': { enabled: false },
      '@opentelemetry/instrumentation-dns': { enabled: false },
    })
    ```

## Further Reading

- [OpenTelemetry Node.js Documentation](https://opentelemetry.io/docs/languages/js/){ target="_blank" }
- [Node.js Auto-Instrumentation](https://opentelemetry.io/docs/languages/js/automatic/){ target="_blank" }
- [:octicons-arrow-left-24: Back to Instrument Overview](../index.md)
