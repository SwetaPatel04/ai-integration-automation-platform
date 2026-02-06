from agents.base_agent import BaseAgent
import pytest


def test_base_agent_requires_process():
    agent = BaseAgent()

    with pytest.raises(NotImplementedError):
        agent.process({})
