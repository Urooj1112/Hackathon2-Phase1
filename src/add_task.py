# add_task.py

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        """
        Adds a new task to the list.

        Args:
            task_description (str): The description of the task.

        Raises:
            ValueError: If the task description is empty.
        """
        if not task_description.strip():
            raise ValueError("Task description cannot be empty.")

        self.tasks.append(task_description)

    def get_tasks(self):
        """
        Returns the list of tasks.

        Returns:
            list: The current list of tasks.
        """
        return self.tasks


def main():
    task_manager = TaskManager()

    while True:
        print("\n--- Add Task ---")
        task_description = input("Enter task description (or type 'exit' to quit): ").strip()

        if task_description.lower() == 'exit':
            print("Exiting Add Task feature.")
            break

        try:
            task_manager.add_task(task_description)
            print("Task added successfully!")
            print("Current Tasks:", task_manager.get_tasks())
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
