def add_tasks(tasks, task_name):
    tasks.append(task_name)
    print("Task '" + task_name + "' added successfully!")
def view_tasks(tasks):
    if len(tasks) > 0:
        print("Tasks:")
        for n in range(len(tasks)):
            print(f"{n+1}. {tasks[n]}")
    else:
        print("No tasks available.")
def remove_task(tasks, task_index):
    if len(tasks) > 0:
        if task_index > len(tasks) or task_index < 1:
            print("Invalid task index!")
        else:
            print(f"Task '{tasks[task_index-1]}' removed successfully!")
            tasks.remove(tasks[task_index-1])
    else:
        print("No tasks to remove.")
def task_manager():
    try:
        tasks = []
        print("Task Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = int(input("Enter your choice (1-4): "))
        if choice != 4:
            cont = True
        while cont:
            if choice == 1:
                task_name = input("Enter task name: ")
                add_tasks(tasks, task_name)
                print("Task Manager Menu:")
                print("1. Add Task")
                print("2. View Tasks")
                print("3. Remove Task")
                print("4. Exit")
                choice = int(input("Enter your choice (1-4): "))
            elif choice == 2:
                view_tasks(tasks)
                print("Task Manager Menu:")
                print("1. Add Task")
                print("2. View Tasks")
                print("3. Remove Task")
                print("4. Exit")
                choice = int(input("Enter your choice (1-4): "))
            elif choice == 3:
                print("Tasks:")
                for x in range(len(tasks)):
                    print(f"{x+1}. {tasks[x]}")
                index = int(input("Enter the index of the task to remove: "))
                remove_task(tasks, index)
                print("Task Manager Menu:")
                print("1. Add Task")
                print("2. View Tasks")
                print("3. Remove Task")
                print("4. Exit")
                choice = int(input("Enter your choice (1-4): "))
            elif choice == 4:
                print("Exiting Task Manager.")
                cont = False
            else:
                print(f"Invalid choice! Please choose a number between 1 and 4")
                print("Task Manager Menu:")
                print("1. Add Task")
                print("2. View Tasks")
                print("3. Remove Task")
                print("4. Exit")
                choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter a valid integer.")
task_manager()
