from agents.decision_agent import DecisionAgent


def test_decision_agent_approved():
    agent = DecisionAgent()

    result = agent.process({"trigger": "webhook-test"})

    assert result["decision"] == "approved"


def test_decision_agent_review():
    agent = DecisionAgent()

    result = agent.process({"trigger": "other-event"})

    assert result["decision"] == "review"
