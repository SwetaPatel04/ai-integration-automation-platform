from agents.base_agent import BaseAgent


class DecisionAgent(BaseAgent):
    """
    A simple rule-based decision agent.
    This will later evolve into an AI-powered agent.
    """

    def process(self, payload: dict) -> dict:
        """
        Processes incoming payload and returns a decision.
        """

        trigger = payload.get("trigger", "").lower()

        if trigger == "webhook-test":
            decision = "approved"
        else:
            decision = "review"

        return {
            "agent": "DecisionAgent",
            "decision": decision,
            "input": payload
        }
