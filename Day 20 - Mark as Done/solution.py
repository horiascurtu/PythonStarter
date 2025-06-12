tasks = [
    {"name": "Clean room", "done": False},
    {"name": "Call mom", "done": False}
]

index = int(input("Which task did you finish? (1-2): ")) - 1
tasks[index]["done"] = True
print("Task updated!")
