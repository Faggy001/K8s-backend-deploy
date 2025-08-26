import logging

def configure_logging(app):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    app.logger.info("Logging is configured.")
