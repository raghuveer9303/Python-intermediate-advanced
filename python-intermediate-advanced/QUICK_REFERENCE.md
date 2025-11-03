# 📚 Python Intermediate/Advanced Quick Reference

A quick lookup guide for concepts covered in this course.

## Module 01: Advanced Data Structures

### Counter
```python
from collections import Counter
counter = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
# Counter({'a': 3, 'b': 2, 'c': 1})

counter.most_common(2)  # [('a', 3), ('b', 2)]
counter['a']  # 3
```

### defaultdict
```python
from collections import defaultdict
d = defaultdict(list)
d['key'].append('value')  # No KeyError!
```

### deque
```python
from collections import deque
dq = deque([1, 2, 3])
dq.append(4)         # [1, 2, 3, 4]
dq.appendleft(0)     # [0, 1, 2, 3, 4]
dq.pop()             # [0, 1, 2, 3]
dq.popleft()         # [1, 2, 3]
```

### namedtuple
```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # 10 20
```

### Comprehensions
```python
# List
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]

# Dict
squares_dict = {x: x**2 for x in range(5)}

# Set
unique = {x % 3 for x in range(10)}
```

## Module 02: Functions Deep Dive

### First-Class Functions
```python
def greet(name):
    return f"Hello, {name}"

say_hi = greet  # Assign to variable
functions = [greet, say_hi]  # Store in list
```

### Closures
```python
def outer(x):
    def inner(y):
        return x + y  # x is captured
    return inner

add_5 = outer(5)
add_5(10)  # 15
```

### Decorators
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

### Decorator with Arguments
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi!")
```

### Lambda Functions
```python
square = lambda x: x**2
add = lambda a, b: a + b

# With map, filter, reduce
list(map(lambda x: x**2, [1, 2, 3]))  # [1, 4, 9]
list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))  # [2, 4]
```

## Module 03: Object-Oriented Programming

### Basic Class
```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy")
```

### Class Methods and Static Methods
```python
class MyClass:
    @classmethod
    def class_method(cls):
        return "I work with the class"
    
    @staticmethod
    def static_method():
        return "I'm independent"
```

### Inheritance
```python
class Animal:
    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
```

### Magic Methods
```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)
    
    def __getitem__(self, index):
        return [self.x, self.y][index]
```

### Properties
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Too cold!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
```

### Abstract Base Classes
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    
    def area(self):
        return self.w * self.h
```

## Common Patterns

### Singleton Pattern
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Context Manager
```python
class MyContext:
    def __enter__(self):
        print("Entering")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")

with MyContext() as ctx:
    print("Inside")
```

### Memoization
```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
```

## Useful Built-ins

### map, filter, reduce
```python
from functools import reduce

list(map(lambda x: x**2, [1, 2, 3]))  # [1, 4, 9]
list(filter(lambda x: x > 5, [3, 6, 8, 4, 9]))  # [6, 8, 9]
reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 10
```

### any, all
```python
any([False, False, True])  # True
all([True, True, True])    # True
```

### enumerate, zip
```python
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)  # 0 a, 1 b, 2 c

for x, y in zip([1, 2, 3], ['a', 'b', 'c']):
    print(x, y)  # 1 a, 2 b, 3 c
```

### sorted with key
```python
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
sorted(people, key=lambda p: p['age'])
```

## Common Idioms

### Unpacking
```python
a, b, c = [1, 2, 3]
first, *middle, last = [1, 2, 3, 4, 5]
x, y = y, x  # Swap
```

### Dictionary Merge
```python
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
merged = {**d1, **d2}
```

### List Flattening
```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
```

### Conditional Expression
```python
result = "even" if x % 2 == 0 else "odd"
```

## Debugging Tips

### Print Debugging
```python
print(f"{variable=}")  # Python 3.8+
```

### Using pdb
```python
import pdb; pdb.set_trace()
# n - next line
# s - step into
# c - continue
# p variable - print variable
```

### Assert for Testing
```python
assert len(result) == 5, "Result should have 5 items"
```

---

**Keep this handy as you work through the modules!**

