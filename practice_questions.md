## Exception Handling

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Cannot divide by zero!')
        return None
    except TypeError as e:
        print(f'Type error: {e}')
        return None
    finally:
        print('Division attempted.')

print(safe_divide(10, 3))
print(safe_divide(10, 0))
```

`finally` always runs — useful for cleanup.


<!-- snippet correction -->

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

## Factorial

```python
# Iterative
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Recursive
def factorial_rec(n):
    return 1 if n <= 1 else n * factorial_rec(n - 1)

print(factorial_iter(5))  # 120
```
