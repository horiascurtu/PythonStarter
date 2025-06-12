tasks = [
    {"name": "Workout", "done": True},
    {"name": "Study", "done": False}
]

for task in tasks:
    status = "✅" if task["done"] else "⬜"
    print(f"{status}  {task['name'].ljust(20)}")
