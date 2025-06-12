tasks = []

try:
    index = int(input("Which task to delete? ")) - 1
    tasks.pop(index)
except (IndexError, ValueError):
    print("Invalid task number.")
