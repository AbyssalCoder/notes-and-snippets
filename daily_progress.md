## 2026-06-08

Practiced Docker Containers with some exercises.

The hands-on practice made the theory click.


<!-- formatting -->

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


<!-- indent fix -->

## 2026-06-14

Morning study session: Lovable.

Going to revisit this topic next week for deeper understanding.

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

## 2026-07-06

Explored Array Traversal — here are my notes.

Understanding the 'why' behind this made everything clearer.

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

## Number Pyramid Pattern

```python
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + ' '.join(str(j) for j in range(1, i + 1)))
```

Output:
```
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
```

## Inheritance Example

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return f'{self.name} says Woof!'

class Cat(Animal):
    def speak(self):
        return f'{self.name} says Meow!'

for a in [Dog('Rex'), Cat('Whiskers')]:
    print(a.speak())
```
