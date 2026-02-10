def test_agent_chaining_notify():
    from agents.router import AgentRouter

    router = AgentRouter()
    result = router.route({"trigger": "webhook-test"})

    assert result["decision"]["decision"] == "notify"
    assert result["action"]["action_taken"] == "Notification sent"


def test_agent_chaining_store():
    from agents.router import AgentRouter

    router = AgentRouter()
    result = router.route({"trigger": "health-check"})

    assert result["decision"]["decision"] == "store"
    assert result["action"]["action_taken"] == "Data stored"
