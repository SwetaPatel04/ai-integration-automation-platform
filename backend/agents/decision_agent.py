from utils.agent_memory import load_memory, remember_event


class DecisionAgent:
    def process(self, payload):
        # 🧪 TEMPORARY TEST - REMOVE AFTER TESTING RETRY LOGIC
        # raise Exception("Simulated failure")
        
        trigger = payload.get("trigger")
        
        # 🧠 CHECK MEMORY: Have I seen this trigger before?
        memory = load_memory()
        previous_triggers = [m.get("trigger") for m in memory if "trigger" in m]
        
        # 🚦 SMART DECISION LOGIC
        if trigger in previous_triggers:
            # Already handled this before → ignore duplicate
            decision = "ignore"
        elif trigger == "webhook-test":
            decision = "notify"
        elif trigger == "health-check":
            decision = "store"
        else:
            decision = "ignore"

        
        # 💾 REMEMBER THIS EVENT
        remember_event(payload)
        
        return {
            "agent": "DecisionAgent",
            "decision": decision,
            "input": payload
        }