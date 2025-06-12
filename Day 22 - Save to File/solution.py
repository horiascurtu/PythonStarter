tasks = [
    {"name": "Exercise", "done": True},
    {"name": "Write journal", "done": False}
]

with open("tasks.txt", "w") as f:
    for task in tasks:
        line = f"{task['name']}|{task['done']}
"
        f.write(line)

print("Tasks saved.")
