
---

### 3️⃣ `update_task.md`
```markdown
# Update Task Feature Specification

## Description
This feature allows users to update an existing task in their task list.

## Requirements
1. **Task Index Input:** User inputs the index of the task to update.
2. **New Task Description Input:** User provides a new description.
3. **Validation:** Index must be valid; new description cannot be empty.
4. **Update Logic:** Replace old description with the new one.
5. **Output:** Display the updated task list.

## Example Usage
```python
task_manager = TaskManager()
task_manager.add_task("Buy groceries")
task_manager.update_task(0, "Buy groceries from supermarket")
print(task_manager.get_tasks())
