class ActionAgent:
    def process(self, decision_result):
        action = decision_result.get("decision", "none")

        retries = 2

        for attempt in range(retries + 1):
            try:
                if action == "notify":
                    return {
                        "agent": "ActionAgent",
                        "action_taken": "Notification sent"
                    }

                if action == "store":
                    return {
                        "agent": "ActionAgent",
                        "action_taken": "Data stored"
                    }

                raise ValueError("Unknown action")

            except Exception as e:
                if attempt == retries:
                    return {
                        "agent": "ActionAgent",
                        "action_taken": "failed",
                        "error": str(e)
                    }
