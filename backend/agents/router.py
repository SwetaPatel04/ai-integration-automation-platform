from agents.decision_agent import DecisionAgent
from agents.health_agent import HealthAgent
from agents.action_agent import ActionAgent


class AgentRouter:
    def __init__(self):
        self.decision_agent = DecisionAgent()
        self.health_agent = HealthAgent()
        self.action_agent = ActionAgent()

    def route(self, payload):
        trigger = payload.get("trigger")

        if trigger == "health-check":
            return {
                "agent": "HealthAgent",
                "result": self.health_agent.process(payload)
            }

        if trigger == "webhook-test":
            return {
                "agent": "DecisionAgent",
                "result": self.decision_agent.process(payload)
            }

        return {
            "agent": "RouterFallback",
            "result": {
                "message": "No matching agent found"
            }
        }
