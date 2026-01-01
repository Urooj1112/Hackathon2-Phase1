# Add Task Feature Specification

## Description
This feature allows users to add new tasks to their task list.

## Requirements
1. **Task Input:** User should input the task description.
2. **Validation:** Task description cannot be empty.
3. **Addition Logic:** Add the validated task to a list of tasks.
4. **Output:** Display the updated task list.

## Example Usage
```python
task_manager = TaskManager()
task_manager.add_task("Buy groceries")
task_manager.add_task("Finish project report")
print(task_manager.get_tasks())
