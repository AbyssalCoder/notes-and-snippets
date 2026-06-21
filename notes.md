## Linear Search

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

nums = [4, 2, 7, 1, 9]
print(linear_search(nums, 7))  # 2
print(linear_search(nums, 5))  # -1
```

Time complexity: O(n). Works on unsorted arrays.

## Git Basics

```bash
git init                        # Initialize repo
git add .                       # Stage all changes
git commit -m 'Initial commit'  # Commit
git status                      # Check status
git log --oneline               # Compact log
git diff                        # Show unstaged changes
git diff --staged               # Show staged changes
```

### Three areas
Working Directory → Staging Area → Repository

## Cline — Autonomous Coding Agent for VS Code

### Features
- Creates and edits files autonomously
- Runs terminal commands
- Asks for approval before actions
- Uses browser for testing

### Observations
- Very capable but can be expensive (high token usage)
- Good at building full features end-to-end
- Works with Claude, GPT-4, and other models
- Human-in-the-loop design (approve/reject each action)


<!-- fixed typo -->
