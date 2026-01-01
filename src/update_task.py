# update_task.py

tasks = []

def add_task(task_description):
    """Add a task to the task list."""
    if not task_description.strip():
        print("Error: Task description cannot be empty.")
        return
    tasks.append(task_description)
    print(f"Task added: {task_description}")

def update_task(index, new_description):
    """Update a task by its index."""
    try:
        index = int(index)
        if index < 0 or index >= len(tasks):
            print("Error: Invalid task index.")
            return
        if not new_description.strip():
            print("Error: New task description cannot be empty.")
            return
        old_task = tasks[index]
        tasks[index] = new_description
        print(f"Task updated: '{old_task}' → '{new_description}'")
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

    # Update a task input
    index_to_update = input("\nEnter the index of the task to update: ")
    new_task_desc = input("Enter the new description: ")
    update_task(index_to_update, new_task_desc)

    # Show updated tasks
    list_tasks()
