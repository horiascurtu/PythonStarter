tasks = [
    {"name": "Cook dinner", "done": False},
    {"name": "Walk dog", "done": True}
]

index = int(input("Which task to delete? (1-2): ")) - 1
tasks.pop(index)
print("Task removed.")
