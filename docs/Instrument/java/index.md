# Java Instrumentation

{!template/subscription-required.mdp!}

Instrument your Java applications with OpenTelemetry to send traces, metrics, and logs to DeepCube. This guide covers the Java agent for auto-instrumentation, Spring Boot setup, and manual SDK usage.

[:octicons-arrow-left-24: Back to Instrument Overview](../index.md)

## Approach 1: Java Agent (Recommended)

The OpenTelemetry Java agent provides automatic instrumentation for most popular frameworks and libraries with zero code changes.

### Download the Agent

```bash
curl -L -o opentelemetry-javaagent.jar \
  https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar
```

### Run with the Agent

```bash
java -javaagent:opentelemetry-javaagent.jar \
  -Dotel.exporter.otlp.endpoint=https://otlp.deepcube.ai \
  -Dotel.exporter.otlp.headers=api-key=YOUR-API-KEY \
  -Dotel.service.name=my-java-app \
  -jar your-application.jar
```

The agent automatically instruments:

- Spring Web MVC, WebFlux
- JAX-RS
- Servlet API
- JDBC, Hibernate
- Kafka, RabbitMQ
- gRPC
- HTTP clients (Apache HttpClient, OkHttp, java.net.HttpClient)
- And [many more](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md){ target="_blank" }

## Approach 2: Spring Boot Starter

For Spring Boot applications, you can use the OpenTelemetry Spring Boot starter instead of the Java agent:

### Maven

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.opentelemetry.instrumentation</groupId>
            <artifactId>opentelemetry-instrumentation-bom</artifactId>
            <version>2.12.0</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <dependency>
        <groupId>io.opentelemetry.instrumentation</groupId>
        <artifactId>opentelemetry-spring-boot-starter</artifactId>
    </dependency>
</dependencies>
```

### Gradle

```groovy
implementation platform("io.opentelemetry.instrumentation:opentelemetry-instrumentation-bom:2.12.0")
implementation "io.opentelemetry.instrumentation:opentelemetry-spring-boot-starter"
```

### Spring Boot Configuration

Configure in `application.yml`:

```yaml
otel:
  exporter:
    otlp:
      endpoint: https://otlp.deepcube.ai
      headers:
        api-key: YOUR-API-KEY
  service:
    name: my-spring-boot-app
```

Or in `application.properties`:

```properties
otel.exporter.otlp.endpoint=https://otlp.deepcube.ai
otel.exporter.otlp.headers.api-key=YOUR-API-KEY
otel.service.name=my-spring-boot-app
```

## Approach 3: Manual Instrumentation with SDK

For full control, configure the OpenTelemetry SDK programmatically.

### Maven Dependencies

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.opentelemetry</groupId>
            <artifactId>opentelemetry-bom</artifactId>
            <version>1.46.0</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-api</artifactId>
    </dependency>
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-sdk</artifactId>
    </dependency>
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-exporter-otlp</artifactId>
    </dependency>
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-sdk-extension-autoconfigure</artifactId>
    </dependency>
</dependencies>
```

### Gradle Dependencies

```groovy
implementation platform("io.opentelemetry:opentelemetry-bom:1.46.0")
implementation "io.opentelemetry:opentelemetry-api"
implementation "io.opentelemetry:opentelemetry-sdk"
implementation "io.opentelemetry:opentelemetry-exporter-otlp"
implementation "io.opentelemetry:opentelemetry-sdk-extension-autoconfigure"
```

### SDK Initialization

```java
import io.opentelemetry.api.OpenTelemetry;
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.exporter.otlp.trace.OtlpGrpcSpanExporter;
import io.opentelemetry.exporter.otlp.metrics.OtlpGrpcMetricExporter;
import io.opentelemetry.sdk.OpenTelemetrySdk;
import io.opentelemetry.sdk.resources.Resource;
import io.opentelemetry.sdk.trace.SdkTracerProvider;
import io.opentelemetry.sdk.trace.export.BatchSpanProcessor;
import io.opentelemetry.sdk.metrics.SdkMeterProvider;
import io.opentelemetry.sdk.metrics.export.PeriodicMetricReader;
import io.opentelemetry.semconv.ResourceAttributes;

public class OtelConfig {

    public static OpenTelemetry initialize() {
        Resource resource = Resource.getDefault()
            .merge(Resource.builder()
                .put(ResourceAttributes.SERVICE_NAME, "my-java-app")
                .put(ResourceAttributes.SERVICE_VERSION, "1.0.0")
                .build());

        // Trace exporter
        OtlpGrpcSpanExporter spanExporter = OtlpGrpcSpanExporter.builder()
            .setEndpoint("https://otlp.deepcube.ai")
            .addHeader("api-key", "YOUR-API-KEY")
            .build();

        SdkTracerProvider tracerProvider = SdkTracerProvider.builder()
            .setResource(resource)
            .addSpanProcessor(BatchSpanProcessor.builder(spanExporter).build())
            .build();

        // Metric exporter
        OtlpGrpcMetricExporter metricExporter = OtlpGrpcMetricExporter.builder()
            .setEndpoint("https://otlp.deepcube.ai")
            .addHeader("api-key", "YOUR-API-KEY")
            .build();

        SdkMeterProvider meterProvider = SdkMeterProvider.builder()
            .setResource(resource)
            .registerMetricReader(PeriodicMetricReader.builder(metricExporter).build())
            .build();

        OpenTelemetrySdk sdk = OpenTelemetrySdk.builder()
            .setTracerProvider(tracerProvider)
            .setMeterProvider(meterProvider)
            .buildAndRegisterGlobal();

        // Shut down providers on JVM exit
        Runtime.getRuntime().addShutdownHook(new Thread(sdk::close));

        return sdk;
    }
}
```

### Creating Custom Spans

```java
import io.opentelemetry.api.GlobalOpenTelemetry;
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.api.trace.StatusCode;
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.context.Scope;

public class OrderService {

    private static final Tracer tracer =
        GlobalOpenTelemetry.getTracer("com.myapp.orders");

    public Order processOrder(int orderId) {
        Span span = tracer.spanBuilder("processOrder")
            .setAttribute("order.id", orderId)
            .startSpan();

        try (Scope scope = span.makeCurrent()) {
            Order order = repository.findById(orderId);
            span.setAttribute("order.total", order.getTotal());

            paymentService.charge(order);
            span.addEvent("payment.completed");

            fulfillmentService.fulfill(order);

            span.setStatus(StatusCode.OK);
            return order;
        } catch (Exception e) {
            span.setStatus(StatusCode.ERROR, e.getMessage());
            span.recordException(e);
            throw e;
        } finally {
            span.end();
        }
    }
}
```

## Environment Variable Configuration

The Java agent and SDK autoconfigure module read these variables:

| Variable | Value | Description |
|----------|-------|-------------|
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `https://otlp.deepcube.ai` | OTLP collector endpoint |
| `OTEL_EXPORTER_OTLP_HEADERS` | `api-key=YOUR-API-KEY` | Authentication header |
| `OTEL_SERVICE_NAME` | `your-service-name` | Service name shown in DeepCube |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `grpc` | Protocol (grpc or http/protobuf) |
| `OTEL_TRACES_EXPORTER` | `otlp` | Trace exporter type |
| `OTEL_METRICS_EXPORTER` | `otlp` | Metrics exporter type |
| `OTEL_LOGS_EXPORTER` | `otlp` | Logs exporter type |

You can also use JVM system properties (prefix with `-D` and replace underscores with dots in lowercase):

```bash
java -javaagent:opentelemetry-javaagent.jar \
  -Dotel.exporter.otlp.endpoint=https://otlp.deepcube.ai \
  -Dotel.exporter.otlp.headers=api-key=YOUR-API-KEY \
  -Dotel.service.name=my-java-app \
  -jar your-app.jar
```

## Verify It's Working

1. Run your instrumented application
2. Send a few HTTP requests to generate traces
3. Open [portal.iapm.app](https://portal.iapm.app){ target="_blank" } and select your Grid
4. Click **Enter** - you should see your service and traces within a few minutes

!!! tip "Quick verification with logging exporter"
    Add `-Dotel.traces.exporter=otlp,logging` to see spans in your console output during development.

## Troubleshooting

### Java agent not loading

- Ensure `-javaagent:` appears **before** `-jar` in the command line.
- Verify the `opentelemetry-javaagent.jar` file exists at the specified path.
- Check that the JAR file is not corrupted (re-download it).

### No data appearing in DeepCube

- Verify the API key by copying a fresh one from [portal.iapm.app](https://portal.iapm.app){ target="_blank" } under **Administration > Grids > Instrument**.
- Check network connectivity: `curl -v https://otlp.deepcube.ai`.
- Look for OpenTelemetry warnings in your application logs.

### Spring Boot starter conflicts

- Ensure you are not using both the Java agent and the Spring Boot starter at the same time - pick one approach.
- Check for dependency version conflicts using `mvn dependency:tree` or `gradle dependencies`.

### High overhead with the Java agent

- Use the `otel.instrumentation.[name].enabled=false` property to disable instrumentation for libraries you do not need.
- Example: `-Dotel.instrumentation.jdbc.enabled=false`

## Further Reading

- [OpenTelemetry Java Documentation](https://opentelemetry.io/docs/languages/java/){ target="_blank" }
- [Java Agent Supported Libraries](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md){ target="_blank" }
- [:octicons-arrow-left-24: Back to Instrument Overview](../index.md)
