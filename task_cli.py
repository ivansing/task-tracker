#!/usr/bin/env python3
import sys
from task_manager import (
    add_task,
    list_tasks,
    mark_in_progress,
    mark_done,
    update_task,
    delete_task
)
from logger import get_logger

log = get_logger(__name__)

def main():
    args = sys.argv[1:]  
    if not args:
        print("Usage: python task_cli.py [command] [options]")
        sys.exit(1)

    command = args[0].lower()

    if command == "add":
       
        if len(args) < 2:
            print("Please provide a task description.")
            sys.exit(1)
        description = args[1]
        add_task(description)

    elif command == "list":
        
        status_filter = args[1].lower() if len(args) == 2 else None
        results = list_tasks(status_filter)
        if not results:
            print("No tasks found.")
        else:
            for t in results:
                print(f"ID: {t['id']}")
                print(f"Description: {t['description']}")
                print(f"Status: {t['status']}")
                print(f"Created At: {t['createdAt']}")
                print(f"Updated At: {t['updatedAt']}")
                print("-" * 40)

    elif command == "mark-in-progress":
        if len(args) < 2:
            print("Please provide a task ID.")
            sys.exit(1)
        try:
            task_id = int(args[1])
        except ValueError:
            print("Invalid task ID. Must be a number.")
            sys.exit(1)
        mark_in_progress(task_id)

    elif command == "mark-done":
        if len(args) < 2:
            print("Please provide a task ID.")
            sys.exit(1)
        try:
            task_id = int(args[1])
        except ValueError:
            print("Invalid task ID. Must be a number.")
            sys.exit(1)
        mark_done(task_id)

    elif command == "update":
        
        if len(args) < 3:
            print("Usage: update [ID] [NEW_DESCRIPTION]")
            sys.exit(1)
        try:
            task_id = int(args[1])
        except ValueError:
            print("Invalid task ID. Must be a number.")
            sys.exit(1)
        new_description = args[2]
        update_task(task_id, new_description)

    elif command == "delete":
        if len(args) < 2:
            print("Please provide a task ID.")
            sys.exit(1)
        try:
            task_id = int(args[1])
        except ValueError:
            print("Invalid task ID. Must be a number.")
            sys.exit(1)
        delete_task(task_id)

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
