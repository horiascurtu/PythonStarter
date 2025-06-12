def display_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        print(f"{i+1}. {task['name']} [{status}]")

# Example usage:
tasks = [{"name": "Email client", "done": False}]
display_tasks(tasks)
