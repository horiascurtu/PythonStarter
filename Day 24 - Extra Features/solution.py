tasks = [
    {"name": "Laundry", "done": False, "priority": "high"},
    {"name": "Email", "done": True, "priority": "low"}
]

for task in tasks:
    print(f"{task['name']} - {task['priority']} - {'✓' if task['done'] else '✗'}")
