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
