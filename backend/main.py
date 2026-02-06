# Import Flask class to create the web application
# jsonify is used to return JSON responses
# request is used to receive data from tools/webhooks
from flask import Flask, jsonify, request

# Import requests library to call external APIs manually
import requests

# Import datetime to log webhook trigger time
from datetime import datetime

# Import os to read environment variables (CI/CD, secrets, etc.)
import os


def create_app():
    """
    Factory function to create and configure the Flask app.
    This pattern is used in real-world scalable applications.
    """

    # Create the Flask application instance
    app = Flask(__name__)

    # Load environment name (development / ci / production)
    app.config["ENVIRONMENT"] = os.getenv("ENVIRONMENT", "development")

    # Load secret securely from environment variables
    app.config["EXTERNAL_API_KEY"] = os.getenv("EXTERNAL_API_KEY", "not-set")

    # -------------------------------
    # HOME ENDPOINT
    # -------------------------------
    @app.route("/", methods=["GET"])
    def home():
        return "Backend is running"

    # -------------------------------
    # HEALTH CHECK ENDPOINT
    # -------------------------------
    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify({
            "status": "OK",
            "message": "AI Integration Automation Platform is running"
        })

    # -------------------------------
    # ENVIRONMENT CHECK ENDPOINT
    # -------------------------------
    @app.route("/env", methods=["GET"])
    def show_environment():
        return jsonify({
            "environment": app.config["ENVIRONMENT"]
        })

    # -------------------------------
    # SECURE CONFIG CHECK (NO SECRET LEAK)
    # -------------------------------
    @app.route("/secure-info", methods=["GET"])
    def secure_info():
        """
        Confirms secret is loaded without exposing it.
        """
        secret_loaded = app.config["EXTERNAL_API_KEY"] != "not-set"

        return jsonify({
            "secret_loaded": secret_loaded
        })

    # -------------------------------
    # MANUAL EXTERNAL API INTEGRATION
    # -------------------------------
    @app.route("/external-post", methods=["GET"])
    def get_external_post():
        external_api_url = "https://jsonplaceholder.typicode.com/posts/1"

        try:
            response = requests.get(external_api_url, timeout=5)
            response.raise_for_status()
            data = response.json()

            return jsonify({
                "source": "jsonplaceholder",
                "success": True,
                "data": data
            })

        except requests.exceptions.RequestException as e:
            return jsonify({
                "success": False,
                "error": str(e)
            }), 500

    # -------------------------------
    # WEBHOOK / TOOL-BASED AUTOMATION
    # -------------------------------
    @app.route("/webhook/external-trigger", methods=["POST"])
    def webhook_external_trigger():
        payload = request.get_json(silent=True) or {}

        event_log = {
            "received_at": datetime.utcnow().isoformat(),
            "payload": payload
        }

        external_api_url = "https://jsonplaceholder.typicode.com/posts/1"
        response = requests.get(external_api_url, timeout=5)
        data = response.json()

        return jsonify({
            "automation": "webhook-triggered",
            "event_log": event_log,
            "external_data": data
        })

    return app


if __name__ == "__main__":
    app = create_app()
    print(app.url_map)
    app.run(debug=True)
