# app.py

tasks = []

def add_task():
    description = input("Enter task description: ").strip()
    if not description:
        print("❌ Task description cannot be empty.")
        return
    tasks.append({
        "description": description,
        "completed": False
    })
    print("✅ Task added successfully.")

def delete_task():
    list_tasks()
    try:
        index = int(input("Enter task index to delete: "))
        if index < 0 or index >= len(tasks):
            print("❌ Invalid task index.")
            return
        removed = tasks.pop(index)
        print(f"🗑️ Task deleted: {removed['description']}")
    except ValueError:
        print("❌ Please enter a valid number.")

def update_task():
    list_tasks()
    try:
        index = int(input("Enter task index to update: "))
        if index < 0 or index >= len(tasks):
            print("❌ Invalid task index.")
            return

        new_desc = input("Enter new task description: ").strip()
        if not new_desc:
            print("❌ Description cannot be empty.")
            return

        tasks[index]["description"] = new_desc
        print("✏️ Task updated successfully.")
    except ValueError:
        print("❌ Please enter a valid number.")

def mark_complete():
    list_tasks()
    try:
        index = int(input("Enter task index to mark as complete: "))
        if index < 0 or index >= len(tasks):
            print("❌ Invalid task index.")
            return

        if tasks[index]["completed"]:
            print("ℹ️ Task already completed.")
        else:
            tasks[index]["completed"] = True
            print("✅ Task marked as complete.")
    except ValueError:
        print("❌ Please enter a valid number.")

def list_tasks():
    if not tasks:
        print("\n📭 No tasks available.")
        return

    print("\n📋 Task List:")
    for i, task in enumerate(tasks):
        status = "✅ Completed" if task["completed"] else "⏳ Pending"
        print(f"{i}. {task['description']} [{status}]")

def show_menu():
    print("""
===========================
      TASK MANAGER
===========================
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Task as Complete
6. Exit
===========================
""")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            mark_complete()
        elif choice == "6":
            print("👋 Exiting Task Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
