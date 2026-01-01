# mark_complete.py

tasks = []

def add_task(task_description):
    """Add a new task."""
    if not task_description.strip():
        print("Error: Task description cannot be empty.")
        return
    tasks.append({
        "description": task_description,
        "completed": False
    })
    print(f"Task added: {task_description}")

def mark_complete(index):
    """Mark a task as complete by index."""
    try:
        index = int(index)
        if index < 0 or index >= len(tasks):
            print("Error: Invalid task index.")
            return

        if tasks[index]["completed"]:
            print("Task is already marked as complete.")
        else:
            tasks[index]["completed"] = True
            print(f"Task marked as complete: {tasks[index]['description']}")

    except ValueError:
        print("Error: Please enter a valid integer index.")

def list_tasks():
    """List all tasks with status."""
    if not tasks:
        print("No tasks available.")
        return

    print("\nCurrent Tasks:")
    for i, task in enumerate(tasks):
        status = "Completed ✅" if task["completed"] else "Pending ⏳"
        print(f"{i}: {task['description']} [{status}]")

# Example usage
if __name__ == "__main__":
    # Demo tasks
    add_task("Buy groceries")
    add_task("Finish project report")
    add_task("Read book")

    list_tasks()

    index = input("\nEnter task index to mark as complete: ")
    mark_complete(index)

    list_tasks()
