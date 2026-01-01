# view_task.py

tasks = []

def add_task(task_description):
    """Add a task to the task list."""
    if not task_description.strip():
        print("Error: Task description cannot be empty.")
        return
    tasks.append(task_description)
    print(f"Task added: {task_description}")

def view_task(index):
    """View a task by its index."""
    try:
        index = int(index)
        if index < 0 or index >= len(tasks):
            print("Error: Invalid task index.")
            return
        print(f"Task at index {index}: {tasks[index]}")
    except ValueError:
        print("Error: Please enter a valid integer index.")

def list_tasks():
    """List all tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i}: {task}")

# Example usage
if __name__ == "__main__":
    # Adding demo tasks
    add_task("Buy groceries")
    add_task("Finish project report")
    add_task("Read book")

    # Show all tasks
    list_tasks()

    # View a specific task
    task_index = input("\nEnter the index of the task to view: ")
    view_task(task_index)
