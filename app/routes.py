from flask import jsonify

def register_routes(app):
    @app.route("/")
    def index():
        return jsonify(message="Welcome to Flask Backend v3")
