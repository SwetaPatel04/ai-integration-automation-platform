from agents.decision_agent import DecisionAgent


def test_decision_agent_notify():
    agent = DecisionAgent()
    result = agent.process({"trigger": "webhook-test"})
    assert result["decision"] == "notify"


def test_decision_agent_ignore():
    agent = DecisionAgent()
    result = agent.process({"trigger": "other-event"})
    assert result["decision"] == "ignore"
