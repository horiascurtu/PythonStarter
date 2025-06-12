def display_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        print(f"{i+1}. {task['name']} [{status}]")

def add_task(tasks, name):
    tasks.append({"name": name, "done": False})

tasks = []
add_task(tasks, "Finish homework")
display_tasks(tasks)
