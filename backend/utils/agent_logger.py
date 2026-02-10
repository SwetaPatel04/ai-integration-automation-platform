import json
from datetime import datetime
from pathlib import Path


LOG_FILE = Path("agent_logs.json")


def log_agent_event(event_data):
    """
    Appends agent event logs into JSON file.
    Creates file if it does not exist.
    """

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event_data
    }

    # Load existing logs
    if LOG_FILE.exists():
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
    else:
        logs = []

    logs.append(log_entry)

    # Save logs
    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=2)
