import json, os, shutil
from datetime import datetime

DATA_FILE = "data/tasks.json"
BACKUP_FOLDER = "data/backups"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)
    backup_file = os.path.join(BACKUP_FOLDER, f"tasks_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    shutil.copy(DATA_FILE, backup_file)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"task": description, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
    for i, t in enumerate(tasks, 1):
        status = "[x]" if t["done"] else "[ ]"
        print(f"{i}. {status} {t['task']}")

def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"✅ Task {index} marked as done.")
    else:
        print("⚠️ Invalid task index.")

def remove_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Removed: {removed['task']}")
    else:
        print("⚠️ Invalid task index.")
