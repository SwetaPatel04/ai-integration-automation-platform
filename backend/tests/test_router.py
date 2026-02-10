def test_router_routes_to_decision_agent():
    from agents.router import AgentRouter

    router = AgentRouter()
    result = router.route({"trigger": "webhook-test"})

    # Router should start with DecisionAgent
    assert "chain" in result
    assert result["chain"][0] == "DecisionAgent"
    assert result["decision"]["decision"] == "notify"


def test_router_routes_to_health_agent():
    from agents.router import AgentRouter

    router = AgentRouter()
    result = router.route({"trigger": "health-check"})

    assert "chain" in result
    assert result["chain"][0] == "DecisionAgent"
    assert result["decision"]["decision"] == "store"


def test_router_fallback():
    from agents.router import AgentRouter

    router = AgentRouter()
    result = router.route({"trigger": "unknown"})

    assert "chain" in result
    assert result["decision"]["decision"] == "ignore"
