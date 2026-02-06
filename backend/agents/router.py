from agents.decision_agent import DecisionAgent
from agents.health_agent import HealthAgent


class AgentRouter:
    def __init__(self):
        self.decision_agent = DecisionAgent()
        self.health_agent = HealthAgent()

    def route(self, payload):
        trigger = payload.get("trigger")

        if trigger == "webhook-test":
            return self.decision_agent.process(payload)

        if trigger == "health-check":
            return self.health_agent.process(payload)

        return {
            "agent": "RouterFallback",
            "message": "No matching agent found",
            "payload": payload
        }
