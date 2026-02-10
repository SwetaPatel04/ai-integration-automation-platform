from agents.router import AgentRouter
from agents.decision_agent import DecisionAgent
from agents.action_agent import ActionAgent
from agents.audit_agent import AuditAgent


class AgentChain:
    """
    Executes a resilient agent workflow:
    Router → Decision → Action → Audit
    """

    def __init__(self):
        self.router = AgentRouter()
        self.decision_agent = DecisionAgent()
        self.action_agent = ActionAgent()
        self.audit_agent = AuditAgent()

    def execute(self, payload):
        # Decide which agent to use
        routed = self.router.route(payload)

        decision_result = None
        action_result = None

        # Only process decision/action if router matched
        if routed["agent"] == "DecisionAgent":
            decision_result = self.decision_agent.process(payload)
            action_result = self.action_agent.process(decision_result)

        # Audit ALWAYS runs
        audit_result = self.audit_agent.log(
            payload,
            decision_result,
            action_result
        )
        raise Exception("Simulated failure")


        return {
            "automation": "resilient-agent-chain",
            "routed_agent": routed["agent"],
            "decision_result": decision_result,
            "action_result": action_result,
            "audit_result": audit_result
        }

