from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# TracerProviderを設定
trace.set_tracer_provider(TracerProvider())

# トレーサーを取得
tracer = trace.get_tracer(__name__)

# OTLPエクスポーターを設定
otlp_exporter = OTLPSpanExporter(endpoint="jaeger:4317", insecure=True)

# BatchSpanProcessorを設定
span_processor = BatchSpanProcessor(otlp_exporter)

# TracerProviderにSpanプロセッサを追加
trace.get_tracer_provider().add_span_processor(span_processor)

# トレーシング
with tracer.start_as_current_span("service2-operation"):
    print("Hello from Service 2!")
