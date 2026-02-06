from agents.router import AgentRouter


def test_router_routes_to_decision_agent():
    router = AgentRouter()

    payload = {"trigger": "webhook-test"}

    result = router.route(payload)

    assert result["agent"] == "DecisionAgent"
    assert result["decision"] == "approved"


def test_router_fallback():
    router = AgentRouter()

    payload = {}

    result = router.route(payload)

    assert result["decision"] == "no-agent-selected"
