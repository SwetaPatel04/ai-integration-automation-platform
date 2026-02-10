from datetime import datetime


class AuditAgent:
    def process(self, data):
        raise Exception("Simulated failure")

        status = data.get("action_taken", "unknown")

        return {
            "agent": "AuditAgent",
            "timestamp": datetime.utcnow().isoformat(),
            "status": status
        }
    
    def log(self, input_data, decision_result=None, action_result=None):
        return {
            "agent": "AuditAgent",
            "event": "Agent chain executed",
            "input": input_data,
            "decision": decision_result,
            "action": action_result
        }
