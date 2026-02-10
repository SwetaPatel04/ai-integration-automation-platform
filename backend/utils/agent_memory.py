import json
from pathlib import Path

MEMORY_FILE = Path("agent_memory.json")


def load_memory():
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def remember_event(event):
    memory = load_memory()
    memory.append(event)
    save_memory(memory)
