from agents.decision_agent import DecisionAgent


class AgentRouter:
    """
    Routes incoming payloads to the appropriate agent.
    """

    def __init__(self):
        # Register agents here
        self.decision_agent = DecisionAgent()

    def route(self, payload: dict) -> dict:
        """
        Decide which agent should process the payload.
        """

        trigger = payload.get("trigger", "").lower()

        # Simple routing rule
        if trigger:
            return self.decision_agent.process(payload)

        # Default fallback
        return {
            "agent": "None",
            "decision": "no-agent-selected",
            "input": payload
        }
