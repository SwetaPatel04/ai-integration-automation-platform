# Flask core imports
from flask import Flask, jsonify, request

# External HTTP requests
import requests

# Timestamp handling
from datetime import datetime

# Import agents
from agents.decision_agent import DecisionAgent
from agents.action_agent import ActionAgent
from agents.router import AgentRouter
from agents.audit_agent import AuditAgent
from agents.action_agent import ActionAgent
from agents.agent_chain import AgentChain
from agents.retry import AgentRetry


def create_app():
    """
    Factory function to create and configure the Flask app.
    """

    app = Flask(__name__)

    # Initialize agents (singletons)
    decision_agent = DecisionAgent()
    action_agent = ActionAgent()
    audit_agent = AuditAgent()
    router = AgentRouter()
    agent_chain = AgentChain()
    retry = AgentRetry()

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
    # WEBHOOK + AGENT CHAIN
    # -------------------------------
    @app.route("/webhook/external-trigger", methods=["POST"])
    def webhook_external_trigger():
        payload = request.get_json(silent=True) or {}

        decision_result = retry.run(decision_agent.process, payload)

        return jsonify(decision_result)


    return app


# -------------------------------
# APPLICATION ENTRY POINT
# -------------------------------
if __name__ == "__main__":
    app = create_app()
    print(app.url_map)
    app.run(debug=True)
