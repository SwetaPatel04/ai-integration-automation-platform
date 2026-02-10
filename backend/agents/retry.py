class AgentRetry:
    def __init__(self, max_retries=1):
        self.max_retries = max_retries

    def run(self, agent_func, payload):
        attempts = 0

        while attempts <= self.max_retries:
            try:
                return agent_func(payload)
            except Exception as e:
                attempts += 1

        return {
            "agent": "RetryFallback",
            "error": "Agent failed after retries"
        }
