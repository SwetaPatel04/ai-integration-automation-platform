# Flask core imports
from flask import Flask, jsonify, request

# External HTTP requests
import requests

# Timestamp handling
from datetime import datetime

# Import agent
from agents.decision_agent import DecisionAgent


def create_app():
    """
    Factory function to create and configure the Flask app.
    """

    app = Flask(__name__)

    # Initialize agent once (singleton pattern)
    decision_agent = DecisionAgent()

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
            "app": "AI Integration Automation Platform",
            "environment": "development"
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

            return jsonify({
                "source": "jsonplaceholder",
                "success": True,
                "data": response.json()
            })

        except requests.exceptions.RequestException as e:
            return jsonify({
                "success": False,
                "error": str(e)
            }), 500

    # -------------------------------
    # WEBHOOK + AGENT INTEGRATION
    # -------------------------------
    @app.route("/webhook/external-trigger", methods=["POST"])
    def webhook_external_trigger():
        """
        Webhook endpoint that:
        - Receives payload
        - Sends payload to agent
        - Returns agent decision + metadata
        """

        payload = request.get_json(silent=True) or {}

        # Agent processes the payload
        agent_result = decision_agent.process(payload)

        event_log = {
            "received_at": datetime.utcnow().isoformat(),
            "payload": payload
        }

        return jsonify({
            "automation": "agent-driven-webhook",
            "event_log": event_log,
            "agent_result": agent_result
        })

    return app


# -------------------------------
# APPLICATION ENTRY POINT
# -------------------------------
if __name__ == "__main__":
    app = create_app()
    print(app.url_map)
    app.run(debug=True)
