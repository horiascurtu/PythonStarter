# Day 30 - Example Solution: Countdown App

import json
import os
from datetime import datetime

DATA_FILE = "events.json"

def load_events():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_events(events):
    with open(DATA_FILE, "w") as f:
        json.dump(events, f, indent=2)

def add_event(name, date_str):
    events = load_events()
    events.append({"name": name, "date": date_str})
    save_events(events)
    print(f"Event added: {name} - {date_str}")

def show_events():
    events = load_events()
    now = datetime.now()
    for event in events:
        event_date = datetime.strptime(event["date"], "%Y-%m-%d")
        days_left = (event_date - now).days
        print(f"{event['name']} in {days_left} day(s)")

# Example usage:
# add_event("My Birthday", "2025-01-01")
# show_events()
