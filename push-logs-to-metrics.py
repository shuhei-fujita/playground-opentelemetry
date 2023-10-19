from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# TracerProvider（トレーシングの設定や管理を行うオブジェクト）を設定
trace.set_tracer_provider(TracerProvider())

# トレーサー（トレースデータを作成するオブジェクト）を取得
tracer = trace.get_tracer(__name__)

# OTLPエクスポーター（トレースデータをOTLPプロトコルで送信するオブジェクト）を設定
otlp_exporter = OTLPSpanExporter(endpoint="localhost:4317", insecure=True)

# BatchSpanProcessor（複数のSpan（トレースの単位）をまとめて送信するオブジェクト）を設定
span_processor = BatchSpanProcessor(otlp_exporter)

# TracerProviderにSpanプロセッサ（Spanを処理するオブジェクト）を追加
trace.get_tracer_provider().add_span_processor(span_processor)

# 新しいSpan（トレースの一部を表すオブジェクト）を作成し、それをアクティブにする
with tracer.start_as_current_span("foo"):
    print("Hello, world!")
