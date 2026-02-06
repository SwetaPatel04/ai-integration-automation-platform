# Import Flask utilities
from flask import Flask, jsonify, request

# External API requests
import requests

# Time logging
from datetime import datetime

# Environment variables
import os


def create_app():
    """
    Factory function to create Flask application.
    """

    app = Flask(__name__)

    # Read environment variables with defaults
    APP_NAME = os.getenv("APP_NAME", "AI Integration Automation Platform")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

    @app.route("/", methods=["GET"])
    def home():
        return f"{APP_NAME} running in {ENVIRONMENT} mode"

    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify({
            "status": "OK",
            "app": APP_NAME,
            "environment": ENVIRONMENT
        })

    @app.route("/external-post", methods=["GET"])
    def get_external_post():
        external_api_url = "https://jsonplaceholder.typicode.com/posts/1"
        response = requests.get(external_api_url, timeout=5)
        return jsonify(response.json())

    @app.route("/webhook/external-trigger", methods=["POST"])
    def webhook_external_trigger():
        payload = request.get_json(silent=True) or {}
        event_log = {
            "received_at": datetime.utcnow().isoformat(),
            "payload": payload
        }

        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1",
            timeout=5
        )

        return jsonify({
            "automation": "webhook-triggered",
            "event_log": event_log,
            "external_data": response.json()
        })

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
