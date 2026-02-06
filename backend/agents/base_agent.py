class BaseAgent:
    """
    Base class for all agents.
    Every agent must implement the process() method.
    """

    def process(self, payload: dict) -> dict:
        raise NotImplementedError("Agents must implement the process method")
