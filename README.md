# Task Tracker CLI

A command-line tool written in Python to manage tasks stored in a JSON file. This CLI lets you:

- **Add** new tasks
- **List** existing tasks
- **Update** task descriptions
- **Mark** tasks as in-progress or done
- **Delete** tasks by ID

---

## Table of Contents

1. [Features](#features)  
2. [Requirements](#requirements)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Project Structure](#project-structure)  
6. [Testing](#testing)  
7. [Contributing](#contributing)  
8. [License](#license)

---

## Features

- **Tasks Stored in JSON**: Uses a `tasks.json` file to persist your data.  
- **Multiple Statuses**: A task can be in one of three states: `todo`, `in-progress`, or `done`.  
- **Simple CLI Commands**: Each action (add, list, update, etc.) is a command-line argument.  
- **Logging**: Built-in logging via Python’s `logging` module, which helps debug or monitor activity.  
- **Unit Testing**: A suite of tests ensures core functionality is reliable.

---

## Requirements

- **Python 3.7+** (or higher)  
- (Optional) A **virtual environment** for isolating dependencies, though no external libraries are required beyond the standard library.  

---

## Installation

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/ivansing/task-tracker-cli.git
   cd task-tracker-cli
    ```

2. **(Optional) Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. **Make the CLI script executable (optional on Unix/Mac)**
    ```bash
    chmod +x task_cli.py
    ```

That’s it! No further dependencies are required.

## Usage

Run the following commands from inside the project directory:

    ```bash
        # Add a new task
        python task_cli.py add "Buy groceries"
        # Output: Task added successfully (ID: 1)

        # List all tasks
        python task_cli.py list

        # List tasks by status
        python task_cli.py list todo
        python task_cli.py list in-progress
        python task_cli.py list done

        # Mark a task as in-progress
        python task_cli.py mark-in-progress 1

        # Mark a task as done
        python task_cli.py mark-done 1

        # Update a task description
        python task_cli.py update 1 "Buy groceries and cook dinner"

        # Delete a task
        python task_cli.py delete 1

    ```

If you made the script executable, you can also run:

    ```bash
        ./task_cli.py add "Wash the car"
    ```

## Project Structure

    ```bash
        task-tracker-cli/
        ├── __init__.py          # Makes this a Python package (optional)
        ├── logger.py            # Handles logging configuration
        ├── task_cli.py          # Main CLI script (entry point)
        ├── task_manager.py      # Core logic (loading/saving tasks, add/delete/update)
        ├── tasks.json           # Local JSON database of tasks
        └── tests/
            ├── __init__.py
            └── test_tasks.py    # Unit tests for task_manager.py

    ```

- task_cli.py – Handles command-line argument parsing and delegates to the task manager.
- task_manager.py – Contains all functions for adding, listing, marking, updating, and deleting tasks.
- logger.py – A helper module for setting up Python’s built-in logging.
- tests/ – Contains your unit tests.

## Testing

**Run all tests via `unittest`:**

    ```bash
        python -m unittest discover

    ```
Or specify the exact test file:

    ```bash
        python -m unittest tests/test_tasks.py

    ```
You'll see a report showing which tests passed or failed.

## Contributing

1. Fork the repository or create a feature branch.
2. Make your changes, ensuring to update tests if you modify or add new functionality.
3. Submit a pull request for review.

We welcome any ideas to improve or extend the tool—like adding priorities, due dates, or more advanced logging!

## License

This project is licensed under the MIT License. See the LICENSE file for details.







