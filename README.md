# Task-Manager
Task Manager – How It Works
The code implements a simple command-line task manager with four functions:

**add_tasks(tasks, task_name)**:

Appends a new task name to the tasks list and prints a confirmation message.

**view_tasks(tasks)**:

Checks if the list is non-empty, then prints each task with a numbered index. If empty, it notifies the user.

**remove_task(tasks, task_index)**:

Validates that the list is non-empty and the given index is in range, then removes the matching task. Prints an error if the index is invalid.

**task_manager()** — the main driver:

Initializes an empty tasks list and displays a menu with 4 options.
Enters a while loop that keeps running until the user chooses to exit (choice 4).
On each iteration it routes to the appropriate function based on the user's input, then re-displays the menu and prompts again.
The whole thing is wrapped in a try/except ValueError to catch non-integer inputs.
