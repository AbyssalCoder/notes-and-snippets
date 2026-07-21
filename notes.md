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

## Armstrong Number

An Armstrong number is a number that equals the sum of its digits each raised to the power of the number of digits.

```python
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)

# Examples: 153 = 1^3 + 5^3 + 3^3
print(is_armstrong(153))  # True
print(is_armstrong(370))  # True
```

## List Comprehensions

```python
# Squares of even numbers
squares = [x**2 for x in range(20) if x % 2 == 0]
print(squares)

# Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print(flat)  # [1, 2, 3, 4, 5, 6]

# Dict comprehension
char_pos = {ch: i for i, ch in enumerate('abcde')}
print(char_pos)
```

## Docker Volumes

Volumes persist data beyond container lifecycle.

```bash
# Named volume
docker volume create mydata
docker run -v mydata:/app/data nginx

# Bind mount (host directory)
docker run -v $(pwd)/data:/app/data nginx

# List volumes
docker volume ls

# Inspect
docker volume inspect mydata
```

Prefer named volumes over bind mounts in production.

## Continue.dev — Open-Source AI Extension

VS Code / JetBrains extension for AI-assisted coding.

### Key features
- Tab autocomplete
- Chat with codebase
- Supports any LLM (OpenAI, Anthropic, Ollama, etc.)
- Fully configurable via `config.json`

### Why use it
- Open source and self-hostable
- Works with local models via Ollama
- No vendor lock-in

## Fibonacci Sequence

### Iterative approach

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

for i in range(10):
    print(fibonacci(i), end=' ')
# 0 1 1 2 3 5 8 13 21 34
```

**Key takeaway:** The iterative version runs in O(n) time and O(1) space.


<!-- fixed typo -->

## Claude Code — Observations

Anthropic's CLI coding agent.

### Strengths
- Excellent at multi-file refactoring
- Understands project context across many files
- Strong at writing tests
- Good at explaining existing code

### Setup
```bash
npm install -g @anthropic-ai/claude-code
claude
```

Works directly in the terminal. Reads your repo and makes edits in place.

## Prime Number Check

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(2, 50) if is_prime(x)]
print(primes)
```

Only need to check up to √n for divisibility.

## OSI Model — 7 Layers

| Layer | Name         | Protocol Examples    |
|-------|-------------|---------------------|
| 7     | Application  | HTTP, FTP, SMTP     |
| 6     | Presentation | SSL/TLS, JPEG       |
| 5     | Session      | NetBIOS, RPC        |
| 4     | Transport    | TCP, UDP            |
| 3     | Network      | IP, ICMP            |
| 2     | Data Link    | Ethernet, WiFi      |
| 1     | Physical     | Cables, Signals     |

**Mnemonic:** Please Do Not Throw Sausage Pizza Away (bottom-up)
