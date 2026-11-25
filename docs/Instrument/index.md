# Instrument Your Application

Send traces, metrics, and logs from your application to DeepCube using standard [OpenTelemetry](https://opentelemetry.io/){ target="_blank" }. No proprietary SDKs required - use the same open-source libraries the industry relies on.

## Quick Configuration

All you need is your **OTLP endpoint** and **API key**:

| Setting | Value |
|---------|-------|
| **Endpoint** | `https://otlp.deepcube.ai:443` |
| **Protocol** | `grpc` |
| **API Key Header** | `api-key: YOUR-API-KEY` |

!!! warning "DeepCube accepts OTLP over gRPC only"
    Send to `https://otlp.deepcube.ai:443` over gRPC. DeepCube does not accept OTLP over HTTP (`http/protobuf`): there is no `/v1/traces` path and no port 4318. An exporter left on HTTP sends nothing that arrives, and the only sign is an export error, usually a 404, in your application's own log. Many SDKs default to HTTP, so set the protocol to gRPC as shown in [Exporter setting by SDK](#exporter-setting-by-sdk).

    Nothing arriving? See [Nothing arriving?](#nothing-arriving).

Get your API key by logging in at [portal.deepcube.ai](https://portal.deepcube.ai){ target="_blank" }, then go to **Administration > Grids** and click **Instrument** on your Grid.

### Environment Variables

The fastest way to configure any OpenTelemetry SDK is with environment variables. These work across all languages:

| Variable | Value | Description |
|----------|-------|-------------|
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `https://otlp.deepcube.ai:443` | OTLP collector endpoint |
| `OTEL_EXPORTER_OTLP_HEADERS` | `api-key=YOUR-API-KEY` | Authentication header |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `grpc` | Protocol (must be `grpc`; some SDKs default to `http/protobuf`) |
| `OTEL_SERVICE_NAME` | `your-service-name` | Identifies your service in DeepCube |

### Exporter Setting by SDK

| SDK | Set this | Not this |
|-----|----------|----------|
| .NET (`OpenTelemetry.Exporter.OpenTelemetryProtocol`) | Leave `Protocol` at `OtlpExportProtocol.Grpc` (the exporter's default) | `OtlpExportProtocol.HttpProtobuf` |
| Java agent 2.x, Spring Boot starter | `-Dotel.exporter.otlp.protocol=grpc` or `OTEL_EXPORTER_OTLP_PROTOCOL=grpc` (they default to `http/protobuf`) | The default |
| Java SDK in code | `OtlpGrpcSpanExporter`, `OtlpGrpcMetricExporter` | `OtlpHttpSpanExporter`, `OtlpHttpMetricExporter` |
| Python (`opentelemetry-instrument`) | `OTEL_EXPORTER_OTLP_PROTOCOL=grpc` | `http/protobuf` |
| Python in code | `opentelemetry.exporter.otlp.proto.grpc` exporters | `opentelemetry.exporter.otlp.proto.http` exporters |
| Node.js | `@opentelemetry/exporter-trace-otlp-grpc`, `@opentelemetry/exporter-metrics-otlp-grpc`; with environment configuration, `OTEL_EXPORTER_OTLP_PROTOCOL=grpc` | `-otlp-http` and `-otlp-proto` packages |
| Go | `otlptracegrpc`, `otlpmetricgrpc` with `WithEndpoint("otlp.deepcube.ai:443")`; with `autoexport`, `OTEL_EXPORTER_OTLP_PROTOCOL=grpc` | `otlptracehttp`, `otlpmetrichttp` |
| Kubernetes Operator | Java, Python, .NET and Go through a [Collector](kubernetes/index.md); Node.js direct, with `OTEL_EXPORTER_OTLP_PROTOCOL=grpc` in the `Instrumentation` resource's `spec.env` | Pointing those four at DeepCube directly |
| OpenTelemetry Collector | `otlp` exporter, `endpoint: otlp.deepcube.ai:443` | `otlphttp` exporter |

The defaults above were checked on November 24, 2026, against the OpenTelemetry Java agent 2.x, the .NET OTLP exporter 1.x, the Go `autoexport` package and the [Operator's auto-instrumentation documentation](https://opentelemetry.io/docs/platforms/kubernetes/operator/automatic/){ target="_blank" }. If a newer release changes a default, the setting in the **Set this** column still works.

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
                options.Endpoint = new Uri("https://otlp.deepcube.ai:443");
                options.Headers = "api-key=YOUR-API-KEY";
            }))
        .WithMetrics(metrics => metrics
            .AddAspNetCoreInstrumentation()
            .AddOtlpExporter(options =>
            {
                options.Endpoint = new Uri("https://otlp.deepcube.ai:443");
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
      -Dotel.exporter.otlp.endpoint=https://otlp.deepcube.ai:443 \
      -Dotel.exporter.otlp.protocol=grpc \
      -Dotel.exporter.otlp.headers=api-key=YOUR-API-KEY \
      -Dotel.service.name=your-service-name \
      -jar your-app.jar
    ```

    [:octicons-arrow-right-24: Full Java Guide](java/index.md)

=== "Python"

    ```bash
    pip install opentelemetry-distro opentelemetry-exporter-otlp

    # Auto-instrument and run
    OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.deepcube.ai:443 \
    OTEL_EXPORTER_OTLP_PROTOCOL=grpc \
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
        url: 'https://otlp.deepcube.ai:443',
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
        otlptracegrpc.WithEndpoint("otlp.deepcube.ai:443"),
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
2. Open [portal.deepcube.ai](https://portal.deepcube.ai){ target="_blank" } and select your Grid
3. Click **Enter** to open the DeepCube experience
4. You should see your service and its telemetry data within a few minutes

Not seeing your service? See [Nothing arriving?](#nothing-arriving).

## Nothing Arriving?

If your service does not appear in DeepCube after a few minutes, check these in order:

1. **Check the protocol.** It must be gRPC. Look through your configuration for `http/protobuf`, `/v1/traces`, port `4318`, `otlphttp`, or an exporter package or class with `http` in its name. Any of these means your exporter uses HTTP, which DeepCube does not accept. Change it as shown in [Exporter setting by SDK](#exporter-setting-by-sdk).
2. **Check the endpoint.** Use `https://otlp.deepcube.ai:443`, or `otlp.deepcube.ai:443` where the setting takes a host and port (Go, the Collector). Add no path.
3. **Check the API key.** Copy it fresh from **Administration > Grids > Instrument** for the grid you are looking at, and send it in the `api-key` header.
4. **Read the exporter's own log.** Turn on your SDK's debug or diagnostic logging if export errors are hidden. An HTTP exporter pointed at DeepCube gets `404 Not Found`. A missing or wrong key is refused as unauthenticated.
5. **Send a test trace.** Run the [Snowglobe command from Your First Trace](../Getting-Started/your-first-trace.md) with the same API key. It sends over gRPC. If its services appear, your key and network are fine, and the problem is your application's exporter: go back to step 1. If they do not appear either, the problem is the key, the grid, or the route out.
6. **Check the route out.** Your application must reach `otlp.deepcube.ai` on port 443 over HTTP/2. A proxy that allows only HTTP/1.1 blocks gRPC. A plain HTTPS request to `https://otlp.deepcube.ai:443` that gets any HTTP status back shows the host is reachable, but it does not test gRPC.
7. **Check where you are looking.** Set `OTEL_SERVICE_NAME` so your service has a name you will recognize, open the grid whose key you used, and make sure the time range covers when you sent.

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
