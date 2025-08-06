from flask import Flask, jsonify
import logging
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    # Configure logging
    configure_logging(app)

    # Register routes
    register_routes(app)

    # Register error handlers
    register_error_handlers(app)

    return app

def get_config():
    class Config:
        ENV = os.environ.get("FLASK_ENV", "production")
        DEBUG = ENV == "development"
        APP_NAME = os.environ.get("APP_NAME", "FlaskBackendApp")
        VERSION = "1.0.0"
        PORT = int(os.environ.get("PORT", 5000))
    return Config

def configure_logging(app):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )
    app.logger.setLevel(logging.INFO)

def register_routes(app):
    @app.route("/")
    def index():
        app.logger.info("Root route accessed")
        return jsonify(
            message="Welcome to the backend API",
            app=app.config["APP_NAME"],
            version=app.config["VERSION"]
        )

    @app.route("/health")
    def health():
        return jsonify(status="healthy")

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return jsonify(error="Not Found"), 404

    @app.errorhandler(500)
    def server_error(error):
        app.logger.error(f"Internal Server Error: {error}")
        return jsonify(error="Internal Server Error"), 500

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=app.config["PORT"])
