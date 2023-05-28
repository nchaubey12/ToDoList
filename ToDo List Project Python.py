# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(title, description):
    tasks.append({"title": title, "description": description, "completed": False})

# Function to view all tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Incomplete"
            print(f"{index}. {task['title']} - {task['description']} [{status}]")

# Function to mark a task as completed
def mark_completed(task_index):
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task index.")
    else:
        tasks[task_index - 1]["completed"] = True
        print("Task marked as completed.")

# Function to delete a task
def delete_task(task_index):
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task index.")
    else:
        del tasks[task_index - 1]
        print("Task deleted.")

# Main program loop
while True:
    print("===== To-Do List Manager =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        add_task(title, description)
        print("Task added successfully.")
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task index to mark as completed: "))
        mark_completed(task_index)
    elif choice == "4":
        task_index = int(input("Enter the task index to delete: "))
        delete_task(task_index)
    elif choice == "5":
        print("Thank you for using the To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
