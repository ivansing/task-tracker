import os
import json
from datetime import datetime

from logger import get_logger

log = get_logger(__name__)

DEFAULT_FILENAME = "tasks.json"

def load_tasks(filename=DEFAULT_FILENAME):
   
    if not os.path.exists(filename):
        log.debug(f"No JSON file found at {filename}. Returning empty list.")
        return []
    try:
        with open(filename, "r") as f:
            tasks = json.load(f)
            log.debug(f"Loaded {len(tasks)} tasks from {filename}.")
            return tasks
    except (json.JSONDecodeError, FileNotFoundError) as e:
        log.error(f"Error reading {filename}: {e}")
        return []

def save_tasks(tasks, filename=DEFAULT_FILENAME):
    """Save tasks to JSON file."""
    try:
        with open(filename, "w") as f:
            json.dump(tasks, f, indent=2)
        log.debug(f"Saved {len(tasks)} tasks to {filename}.")
    except Exception as e:
        log.error(f"Error writing to {filename}: {e}")
        raise

def add_task(description):
    tasks = load_tasks()
    max_id = max((task["id"] for task in tasks), default=0)
    new_id = max_id + 1

    current_time = datetime.now().isoformat()

    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": current_time,
        "updatedAt": current_time,
    }

    tasks.append(new_task)
    save_tasks(tasks)
    log.info(f"Task added successfully (ID: {new_id})")
    return new_id  

def list_tasks(status_filter=None):
    tasks = load_tasks()
    if status_filter:
        valid_statuses = ["todo", "done", "in-progress"]
        if status_filter not in valid_statuses:
            log.error("Invalid status. Use: todo, done, or in-progress.")
            return []
        tasks = [t for t in tasks if t["status"] == status_filter]
    return tasks

def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            log.info(f"Task {task_id} marked as in-progress.")
            return True
    log.warning(f"No task found with ID {task_id}")
    return False

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            log.info(f"Task {task_id} marked as done.")
            return True
    log.warning(f"No task found with ID {task_id}")
    return False

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            log.info(f"Task {task_id} updated.")
            return True
    log.warning(f"No task found with ID {task_id}")
    return False

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        log.warning(f"No task found with ID {task_id}")
        return False
    save_tasks(new_tasks)
    log.info(f"Task {task_id} deleted.")
    return True
