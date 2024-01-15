import json
from datetime import datetime, timedelta

# File to store tasks
tasks_file = "tasks.json"


def load_tasks():
    """Load tasks from a JSON file."""
    try:
        with open(tasks_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(tasks_file, "w") as file:
        json.dump(tasks, file, indent=2)


def display_tasks(tasks):
    """Display tasks in a list with details."""
    print("\nTask List:")
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(
                f"{index}. {task['description']} - Priority: {task['priority']} - Due Date: {task['due_date']} - {'(completed)' if task['completed'] else ''}")
    else:
        print("No tasks found.")


def add_task(tasks, description, priority, due_date):
    """Add a new task."""
    task = {"description": description, "priority": priority, "due_date": due_date, "completed": False}
    tasks.append(task)
    print(f'Task "{description}" added successfully.')


def remove_task(tasks, task_index):
    """Remove a task."""
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f'Task "{removed_task["description"]}" removed successfully.')
    else:
        print("Invalid task index.")


def mark_completed(tasks, task_index):
    """Mark a task as completed."""
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print(f'Task marked as completed: "{tasks[task_index - 1]["description"]}"')
    else:
        print("Invalid task index.")


def main():
    # Load existing tasks or initialize an empty list
    tasks = load_tasks()

    while True:
        # Display menu
        print("\nMenu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        # Get user input
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            description = input("Enter task description: ")
            priority = input("Enter task priority (high/medium/low): ").lower()
            due_date_str = input("Enter due date (YYYY-MM-DD): ")

            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue

            add_task(tasks, description, priority, due_date.strftime("%Y-%m-%d"))
        elif choice == "3":
            display_tasks(tasks)
            task_index = int(input("Enter the task index to remove: "))
            remove_task(tasks, task_index)
        elif choice == "4":
            display_tasks(tasks)
            task_index = int(input("Enter the task index to mark as completed: "))
            mark_completed(tasks, task_index)
        elif choice == "5":
            # Save tasks and exit
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
