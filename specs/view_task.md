
---

### 4️⃣ `view_task.md`
```markdown
# View Task Feature Specification

## Description
This feature allows users to view a specific task by index.

## Requirements
1. **Task Index Input:** User inputs the index of the task to view.
2. **Validation:** Index must be valid.
3. **Output:** Display the task description.

## Example Usage
```python
task_manager = TaskManager()
task_manager.add_task("Buy groceries")
print(task_manager.view_task(0))
