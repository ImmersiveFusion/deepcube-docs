# Instrument Your Application

{!template/subscription-required.mdp!}

Send traces, metrics, and logs from your application to DeepCube using standard [OpenTelemetry](https://opentelemetry.io/){ target="_blank" }. No proprietary SDKs required - use the same open-source libraries the industry relies on.

## Quick Configuration

All you need is your **OTLP endpoint** and **API key**:

| Setting | Value |
|---------|-------|
| **Endpoint** | `https://otlp.iapm.app` |
| **Protocol** | `grpc` (default) or `http/protobuf` |
| **API Key Header** | `api-key: YOUR-API-KEY` |

Get your API key by logging in at [portal.iapm.app](https://portal.iapm.app){ target="_blank" }, then go to **Administration > Grids** and click **Instrument** on your Grid.

### Environment Variables

The fastest way to configure any OpenTelemetry SDK is with environment variables. These work across all languages:

| Variable | Value | Description |
|----------|-------|-------------|
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `https://otlp.iapm.app` | OTLP collector endpoint |
| `OTEL_EXPORTER_OTLP_HEADERS` | `api-key=YOUR-API-KEY` | Authentication header |
| `OTEL_SERVICE_NAME` | `your-service-name` | Identifies your service in DeepCube |

## Quick Start by Language

Choose your language to see the minimal configuration needed to start sending telemetry:

=== "C# / .NET"

    ```csharp
    // Program.cs
    builder.Services.AddOpenTelemetry()
        .WithTracing(tracing => tracing
            .AddAspNetCoreInstrumentation()
            .AddHttpClientInstrumentation()
            .AddOtlpExporter(options =>
            {
                options.Endpoint = new Uri("https://otlp.iapm.app");
                options.Headers = "api-key=YOUR-API-KEY";
            }))
        .WithMetrics(metrics => metrics
            .AddAspNetCoreInstrumentation()
            .AddOtlpExporter(options =>
            {
                options.Endpoint = new Uri("https://otlp.iapm.app");
                options.Headers = "api-key=YOUR-API-KEY";
            }));
    ```

    [:octicons-arrow-right-24: Full .NET Guide](dotnet/index.md)

=== "Java"

    ```bash
    # Download the OpenTelemetry Java agent
    curl -L -o opentelemetry-javaagent.jar \
      https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar

    # Run your application with auto-instrumentation
    java -javaagent:opentelemetry-javaagent.jar \
      -Dotel.exporter.otlp.endpoint=https://otlp.iapm.app \
      -Dotel.exporter.otlp.headers=api-key=YOUR-API-KEY \
      -Dotel.service.name=your-service-name \
      -jar your-app.jar
    ```

    [:octicons-arrow-right-24: Full Java Guide](java/index.md)

=== "Python"

    ```bash
    pip install opentelemetry-distro opentelemetry-exporter-otlp

    # Auto-instrument and run
    OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.iapm.app \
    OTEL_EXPORTER_OTLP_HEADERS="api-key=YOUR-API-KEY" \
    OTEL_SERVICE_NAME=your-service-name \
    opentelemetry-instrument python your_app.py
    ```

    [:octicons-arrow-right-24: Full Python Guide](python/index.md)

=== "Node.js"

    ```bash
    npm install @opentelemetry/sdk-node \
      @opentelemetry/exporter-trace-otlp-grpc \
      @opentelemetry/exporter-metrics-otlp-grpc \
      @opentelemetry/auto-instrumentations-node
    ```

    ```javascript
    // tracing.js - require this before your app
    const { NodeSDK } = require('@opentelemetry/sdk-node');
    const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-grpc');
    const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');

    const sdk = new NodeSDK({
      traceExporter: new OTLPTraceExporter({
        url: 'https://otlp.iapm.app',
        headers: { 'api-key': 'YOUR-API-KEY' },
      }),
      instrumentations: [getNodeAutoInstrumentations()],
    });

    sdk.start();
    ```

    [:octicons-arrow-right-24: Full Node.js Guide](nodejs/index.md)

=== "Go"

    ```go
    import (
        "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
        "google.golang.org/grpc/credentials"
    )

    exporter, err := otlptracegrpc.New(ctx,
        otlptracegrpc.WithEndpoint("otlp.iapm.app:443"),
        otlptracegrpc.WithHeaders(map[string]string{
            "api-key": "YOUR-API-KEY",
        }),
        otlptracegrpc.WithTLSCredentials(credentials.NewClientTLSFromCert(nil, "")),
    )
    ```

    [:octicons-arrow-right-24: Full Go Guide](go/index.md)

## What Gets Collected

Once configured, OpenTelemetry captures three types of telemetry:

| Signal | What It Captures | Examples |
|--------|-----------------|----------|
| **Traces** | Request flows across services | HTTP requests, database calls, message queue operations |
| **Metrics** | Performance measurements over time | Request latency, CPU usage, error rates, queue depth |
| **Logs** | Application log events | Errors, warnings, structured log entries |

All three signal types are sent to the same OTLP endpoint. DeepCube correlates them automatically so you can navigate from a metric spike to the traces and logs that explain it.

## Verify It's Working

After deploying your instrumented application:

1. Generate some traffic by making a few requests to your application
2. Open [portal.iapm.app](https://portal.iapm.app){ target="_blank" } and select your Grid
3. Click **Enter** to open the DeepCube experience
4. You should see your service and its telemetry data within a few minutes

!!! tip "Not seeing data?"
    - Verify your API key is correct (copy it fresh from **Administration > Grids > Instrument**)
    - Check that your application can reach `https://otlp.iapm.app` on port 443
    - Ensure the `OTEL_SERVICE_NAME` is set so your service is identifiable
    - Look for OpenTelemetry errors in your application logs
    - Try the troubleshooting section in your language-specific guide

## Language Guides

Detailed setup instructions for each language and platform:

| Guide | Coverage |
|-------|----------|
| [:octicons-arrow-right-24: **.NET**](dotnet/index.md) | ASP.NET Core, console apps, worker services, logging integration |
| [:octicons-arrow-right-24: **Java**](java/index.md) | Java agent, Spring Boot, Maven/Gradle, manual instrumentation |
| [:octicons-arrow-right-24: **Python**](python/index.md) | Django, Flask, FastAPI, auto-instrumentation |
| [:octicons-arrow-right-24: **Node.js**](nodejs/index.md) | Express.js, NestJS, auto-instrumentation |
| [:octicons-arrow-right-24: **Go**](go/index.md) | net/http, gRPC, manual spans |
| [:octicons-arrow-right-24: **Kubernetes**](kubernetes/index.md) | OTel Operator, Collector DaemonSet, Helm charts |
| [:octicons-arrow-right-24: **Collector**](collector/index.md) | OTel Collector configuration, Docker, Kubernetes deployment |

## Further Reading

- [OpenTelemetry Documentation](https://opentelemetry.io/docs/){ target="_blank" } - Official OpenTelemetry reference
- [OpenTelemetry Language SDKs](https://opentelemetry.io/docs/languages/){ target="_blank" } - SDK documentation by language
