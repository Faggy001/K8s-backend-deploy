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
    logging.basicConfig(level=logging.INFO)

    # Register routes & errors
    register_routes(app)
    register_error_handlers(app)

    # Prometheus metrics
    PrometheusMetrics(app)

    @app.route("/health")
    def health():
        return jsonify(status="ok")

    return app

