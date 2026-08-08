# Go Instrumentation

{!template/subscription-required.mdp!}

Instrument your Go applications with OpenTelemetry to send traces, metrics, and logs to DeepCube. This guide covers net/http, gRPC, manual span creation, and SDK configuration.

[:octicons-arrow-left-24: Back to Instrument Overview](../index.md)

## Go Modules

Add the required OpenTelemetry modules to your project:

```bash
go get go.opentelemetry.io/otel \
  go.opentelemetry.io/otel/sdk \
  go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc \
  go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc \
  go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp \
  google.golang.org/grpc
```

For gRPC instrumentation, also add:

```bash
go get go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc
```

## SDK Initialization

Create a reusable initialization function:

```go
package otel

import (
	"context"
	"log"
	"time"

	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
	"go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc"
	"go.opentelemetry.io/otel/propagation"
	"go.opentelemetry.io/otel/sdk/metric"
	"go.opentelemetry.io/otel/sdk/resource"
	sdktrace "go.opentelemetry.io/otel/sdk/trace"
	semconv "go.opentelemetry.io/otel/semconv/v1.26.0"
	"google.golang.org/grpc/credentials"
)

func InitProvider(ctx context.Context, serviceName string) (func(), error) {
	res, err := resource.New(ctx,
		resource.WithAttributes(
			semconv.ServiceName(serviceName),
			semconv.ServiceVersion("1.0.0"),
		),
	)
	if err != nil {
		return nil, err
	}

	// Trace exporter
	traceExporter, err := otlptracegrpc.New(ctx,
		otlptracegrpc.WithEndpoint("otlp.deepcube.ai:443"),
		otlptracegrpc.WithHeaders(map[string]string{
			"api-key": "YOUR-API-KEY",
		}),
		otlptracegrpc.WithTLSCredentials(credentials.NewClientTLSFromCert(nil, "")),
	)
	if err != nil {
		return nil, err
	}

	tracerProvider := sdktrace.NewTracerProvider(
		sdktrace.WithBatcher(traceExporter),
		sdktrace.WithResource(res),
	)
	otel.SetTracerProvider(tracerProvider)
	otel.SetTextMapPropagator(propagation.NewCompositeTextMapPropagator(
		propagation.TraceContext{},
		propagation.Baggage{},
	))

	// Metric exporter
	metricExporter, err := otlpmetricgrpc.New(ctx,
		otlpmetricgrpc.WithEndpoint("otlp.deepcube.ai:443"),
		otlpmetricgrpc.WithHeaders(map[string]string{
			"api-key": "YOUR-API-KEY",
		}),
		otlpmetricgrpc.WithTLSCredentials(credentials.NewClientTLSFromCert(nil, "")),
	)
	if err != nil {
		return nil, err
	}

	meterProvider := metric.NewMeterProvider(
		metric.WithReader(metric.NewPeriodicReader(metricExporter,
			metric.WithInterval(30*time.Second),
		)),
		metric.WithResource(res),
	)
	otel.SetMeterProvider(meterProvider)

	// Return a cleanup function
	cleanup := func() {
		ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
		defer cancel()
		if err := tracerProvider.Shutdown(ctx); err != nil {
			log.Printf("Error shutting down tracer provider: %v", err)
		}
		if err := meterProvider.Shutdown(ctx); err != nil {
			log.Printf("Error shutting down meter provider: %v", err)
		}
	}

	return cleanup, nil
}
```

## net/http Instrumentation

Wrap your HTTP handlers and clients with `otelhttp`:

```go
package main

import (
	"log"
	"net/http"

	myotel "myapp/otel"
	"go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"
)

func main() {
	ctx := context.Background()
	cleanup, err := myotel.InitProvider(ctx, "my-http-server")
	if err != nil {
		log.Fatal(err)
	}
	defer cleanup()

	// Wrap handlers for automatic span creation
	mux := http.NewServeMux()
	mux.Handle("/api/orders", otelhttp.NewHandler(
		http.HandlerFunc(handleOrders), "GET /api/orders"))
	mux.Handle("/api/orders/", otelhttp.NewHandler(
		http.HandlerFunc(handleOrderByID), "GET /api/orders/{id}"))

	// Use an instrumented HTTP server
	log.Println("Server starting on :8080")
	log.Fatal(http.ListenAndServe(":8080", mux))
}

func handleOrders(w http.ResponseWriter, r *http.Request) {
	// Each request automatically gets a trace span
	w.Write([]byte(`{"orders": []}`))
}

func handleOrderByID(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte(`{"order": {}}`))
}
```

### Instrumented HTTP Client

Wrap outgoing HTTP calls to propagate trace context:

```go
import "go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"

// Create an instrumented HTTP client
client := &http.Client{
	Transport: otelhttp.NewTransport(http.DefaultTransport),
}

// Outgoing requests automatically create child spans
resp, err := client.Get("https://api.example.com/data")
```

## gRPC Instrumentation

Instrument gRPC servers and clients:

```go
import (
	"google.golang.org/grpc"
	"go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc"
)

// gRPC server with instrumentation
server := grpc.NewServer(
	grpc.StatsHandler(otelgrpc.NewServerHandler()),
)

// gRPC client with instrumentation
conn, err := grpc.NewClient("localhost:50051",
	grpc.WithStatsHandler(otelgrpc.NewClientHandler()),
)
```

## Manual Span Creation

Create custom spans for your business logic:

```go
import (
	"context"

	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/codes"
	"go.opentelemetry.io/otel/trace"
)

var tracer = otel.Tracer("myapp.orders")

func processOrder(ctx context.Context, orderID int) (*Order, error) {
	ctx, span := tracer.Start(ctx, "processOrder",
		trace.WithAttributes(
			attribute.Int("order.id", orderID),
		),
	)
	defer span.End()

	order, err := getOrder(ctx, orderID)
	if err != nil {
		span.SetStatus(codes.Error, err.Error())
		span.RecordError(err)
		return nil, err
	}

	span.SetAttributes(attribute.Float64("order.total", order.Total))

	if err := chargePayment(ctx, order); err != nil {
		span.SetStatus(codes.Error, err.Error())
		span.RecordError(err)
		return nil, err
	}

	span.AddEvent("payment.completed")

	if err := fulfillOrder(ctx, order); err != nil {
		span.SetStatus(codes.Error, err.Error())
		span.RecordError(err)
		return nil, err
	}

	span.SetStatus(codes.Ok, "")
	return order, nil
}
```

### Custom Metrics

```go
import (
	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/metric"
)

var meter = otel.Meter("myapp.orders")

var (
	ordersProcessed, _ = meter.Int64Counter("orders.processed",
		metric.WithUnit("orders"),
		metric.WithDescription("Number of orders processed"),
	)
	orderDuration, _ = meter.Float64Histogram("orders.processing.duration",
		metric.WithUnit("ms"),
		metric.WithDescription("Order processing time"),
	)
)

func processOrder(ctx context.Context, order *Order) {
	start := time.Now()

	doProcessing(ctx, order)

	duration := float64(time.Since(start).Milliseconds())
	ordersProcessed.Add(ctx, 1,
		metric.WithAttributes(attribute.String("order.type", order.Type)))
	orderDuration.Record(ctx, duration)
}
```

## Environment Variable Configuration

The OpenTelemetry Go SDK reads these variables when using the autoconfigure option:

| Variable | Value | Description |
|----------|-------|-------------|
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `https://otlp.deepcube.ai` | OTLP collector endpoint |
| `OTEL_EXPORTER_OTLP_HEADERS` | `api-key=YOUR-API-KEY` | Authentication header |
| `OTEL_SERVICE_NAME` | `your-service-name` | Service name shown in DeepCube |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `grpc` | Protocol (grpc or http/protobuf) |

!!! note "Environment variables in Go"
    Unlike some other language SDKs, the Go SDK does not automatically read `OTEL_EXPORTER_OTLP_ENDPOINT` by default. You need to either configure the exporter programmatically (as shown above) or use the `autoexport` package:

    ```bash
    go get go.opentelemetry.io/contrib/exporters/autoexport
    ```

## Verify It's Working

1. Run your instrumented application
2. Send a few HTTP requests to generate traces
3. Open [portal.iapm.app](https://portal.iapm.app){ target="_blank" } and select your Grid
4. Click **Enter** - you should see your service and traces within a few minutes

!!! tip "Quick verification with stdout exporter"
    Use the stdout exporter during development to see spans in your terminal:

    ```go
    import "go.opentelemetry.io/otel/exporters/stdout/stdouttrace"

    exporter, _ := stdouttrace.New(stdouttrace.WithPrettyPrint())
    ```

## Troubleshooting

### No data appearing in DeepCube

- Verify the API key by copying a fresh one from [portal.iapm.app](https://portal.iapm.app){ target="_blank" } under **Administration > Grids > Instrument**.
- Ensure `cleanup()` (or `tracerProvider.Shutdown()`) is called before the process exits - without it, buffered spans may be lost.
- Check that TLS credentials are configured: `otlptracegrpc.WithTLSCredentials(credentials.NewClientTLSFromCert(nil, ""))`.

### TLS/connection errors

- The DeepCube endpoint uses TLS. Do not use `WithInsecure()` - it will fail.
- If you see certificate errors, ensure your Go installation has up-to-date root certificates.

### Context not propagating

- Always pass `context.Context` through your call chain. The trace context is stored in the context.
- Use `tracer.Start(ctx, ...)` and pass the returned context to downstream functions.

### Missing spans

- Ensure `defer span.End()` is called for every span you create. Spans are not exported until `End()` is called.
- Check that your `TracerProvider` has not been shut down prematurely.

## Further Reading

- [OpenTelemetry Go Documentation](https://opentelemetry.io/docs/languages/go/){ target="_blank" }
- [Go Contrib Instrumentation Libraries](https://github.com/open-telemetry/opentelemetry-go-contrib){ target="_blank" }
- [:octicons-arrow-left-24: Back to Instrument Overview](../index.md)
