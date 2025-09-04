from flask import Flask, jsonify
import logging
from prometheus_flask_exporter import PrometheusMetrics
from .config import get_config
from .routes import register_routes
from .errors import register_error_handlers


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    # Logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    # Register routes & errors
    register_routes(app)
    register_error_handlers(app)

    # Prometheus metrics
    metrics = PrometheusMetrics(app)
    metrics.info("app_info", "Application info", version="1.0.0", environment=app.config["ENV"])

    @app.route("/health")
    def health():
        return jsonify(status="ok")

    return app


