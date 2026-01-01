
---

### 5️⃣ `mark_complete.md`
```markdown
# Mark Complete Task Feature Specification

## Description
This feature allows users to mark a task as complete.

## Requirements
1. **Task Index Input:** User inputs the index of the task to mark complete.
2. **Validation:** Index must be valid.
3. **Completion Logic:** Append "[Completed]" to the task description.
4. **Output:** Display the updated task list.

## Example Usage
```python
task_manager = TaskManager()
task_manager.add_task("Buy groceries")
task_manager.mark_complete(0)
print(task_manager.get_tasks())
