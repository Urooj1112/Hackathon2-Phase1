# delete_task.py

tasks = []

def add_task(task_description):
    """Add a task to the task list."""
    if not task_description.strip():
        print("Error: Task description cannot be empty.")
        return
    tasks.append(task_description)
    print(f"Task added: {task_description}")

def delete_task(index):
    """Delete a task by its index."""
    try:
        index = int(index)
        if index < 0 or index >= len(tasks):
            print("Error: Invalid task index.")
            return
        removed_task = tasks.pop(index)
        print(f"Task deleted: {removed_task}")
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
    # Adding some demo tasks
    add_task("Buy groceries")
    add_task("Finish project report")
    add_task("Read book")

    # Show tasks
    list_tasks()

    # Delete a task input
    index_to_delete = input("\nEnter the index of the task to delete: ")
    delete_task(index_to_delete)

    # Show updated tasks
    list_tasks()
