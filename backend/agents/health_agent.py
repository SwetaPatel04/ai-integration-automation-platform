class HealthAgent:
    def process(self, payload):
        return {
            "agent": "HealthAgent",
            "status": "healthy",
            "received": payload
        }
