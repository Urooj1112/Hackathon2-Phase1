# task_manager.py

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description: str):
        if not task_description.strip():
            raise ValueError("Task description cannot be empty.")
        self.tasks.append(task_description)

    def delete_task(self, index: int):
        if not isinstance(index, int) or index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index.")
        del self.tasks[index]

    def update_task(self, index: int, new_task_description: str):
        if not isinstance(index, int) or index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index.")
        if not new_task_description.strip():
            raise ValueError("New task description cannot be empty.")
        self.tasks[index] = new_task_description

    def view_task(self, index: int) -> str:
        if not isinstance(index, int) or index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index.")
        return self.tasks[index]

    def mark_complete(self, index: int):
        if not isinstance(index, int) or index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index.")
        if "[Completed]" not in self.tasks[index]:
            self.tasks[index] += " [Completed]"

    def get_tasks(self):
        return self.tasks
