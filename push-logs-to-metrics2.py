# 必要なライブラリをインポート
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# TracerProviderを設定（トレーシングの設定や管理を行うオブジェクト）
trace.set_tracer_provider(TracerProvider())

# トレーサーを取得（トレースデータを作成するオブジェクト）
tracer = trace.get_tracer(__name__)

# OTLPエクスポーターを設定（トレースデータをOTLPプロトコルで送信するオブジェクト）
otlp_exporter = OTLPSpanExporter(endpoint="localhost:4317", insecure=True)

# BatchSpanProcessorを設定（複数のSpanをまとめて送信するオブジェクト）
span_processor = BatchSpanProcessor(otlp_exporter)

# TracerProviderにSpanプロセッサを追加（Spanを処理するオブジェクト）
trace.get_tracer_provider().add_span_processor(span_processor)

# メインのSpanを作成
with tracer.start_as_current_span("main-operation") as main_span:
    main_span.set_attribute("component", "main")

    # サブ操作1
    with tracer.start_as_current_span("sub-operation-1", parent=main_span) as sub_span1:
        sub_span1.set_attribute("component", "sub1")
        print("Doing sub operation 1")

    # サブ操作2
    with tracer.start_as_current_span("sub-operation-2", parent=main_span) as sub_span2:
        sub_span2.set_attribute("component", "sub2")
        print("Doing sub operation 2")

    print("Doing main operation")
