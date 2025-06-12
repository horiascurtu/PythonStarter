tasks = [
    {"name": "Buy milk", "done": False},
    {"name": "Read book", "done": True}
]

for task in tasks:
    status = "✓" if task["done"] else "✗"
    print(f"{status} {task['name']}")
