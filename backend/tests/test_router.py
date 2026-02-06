def test_router_routes_to_decision_agent():
    from agents.router import AgentRouter

    router = AgentRouter()

    result = router.route({"trigger": "webhook-test"})
    assert result["agent"] == "DecisionAgent"


def test_router_routes_to_health_agent():
    from agents.router import AgentRouter

    router = AgentRouter()

    result = router.route({"trigger": "health-check"})
    assert result["agent"] == "HealthAgent"


def test_router_fallback():
    from agents.router import AgentRouter

    router = AgentRouter()

    result = router.route({"trigger": "unknown"})
    assert result["agent"] == "RouterFallback"
