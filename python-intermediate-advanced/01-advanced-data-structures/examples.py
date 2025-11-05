"""
Module 01: Advanced Data Structures - Examples

Type each example, run it, and experiment!
"""

# ============================================================================
# 1. COUNTER - Counting made easy
# ============================================================================
print("=" * 60)
print("1. COUNTER")
print("=" * 60)

from collections import Counter
from typing import Any

# Example 1: Counting items in a list
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruit_count = Counter(fruits)
print(f"Fruit counts: {fruit_count}")
print(f"Most common: {fruit_count.most_common(2)}")  # Top 2
print()

# Example 2: Counting characters in a string
text = "hello world"
char_count = Counter(text)
print(f"Character counts: {char_count}")
print(f"Letter 'l' appears: {char_count['l']} times")
print()

# Example 3: Counter arithmetic
counter1 = Counter(['a', 'b', 'c', 'a'])
counter2 = Counter(['a', 'b', 'd'])
print(f"Counter1: {counter1}")
print(f"Counter2: {counter2}")
print(f"Addition: {counter1 + counter2}")
print(f"Subtraction: {counter1 - counter2}")
print(f"Intersection: {counter1 & counter2}")
print(f"Union: {counter1 | counter2}")
print()


# ============================================================================
# 2. DEFAULTDICT - No more KeyError
# ============================================================================
print("=" * 60)
print("2. DEFAULTDICT")
print("=" * 60)

from collections import defaultdict

# Example 1: Group items by first letter (without defaultdict)
words = ['apple', 'ant', 'banana', 'bear', 'cat', 'ant']
grouped_normal = {}
for word in words:
    first_letter = word[0]
    if first_letter not in grouped_normal:
        grouped_normal[first_letter] = []
    grouped_normal[first_letter].append(word)
print(f"Normal dict: {grouped_normal}")
print()

# Example 2: Same thing with defaultdict (cleaner!)
grouped_default = defaultdict(list)
for word in words:
    grouped_default[word[0]].append(word)
print(f"Defaultdict: {dict(grouped_default)}")
print()

# Example 3: Counting with defaultdict
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1
print(f"Word count: {dict(word_count)}")
print()


# ============================================================================
# 3. DEQUE - Fast queue operations
# ============================================================================
print("=" * 60)
print("3. DEQUE")
print("=" * 60)

from collections import deque

# Example 1: Basic queue operations
queue = deque(['a', 'b', 'c'])
print(f"Initial queue: {queue}")
queue.append('d')           # Add to right
print(f"After append: {queue}")
queue.appendleft('z')       # Add to left
print(f"After appendleft: {queue}")
print(f"Pop from right: {queue.pop()}")
print(f"Pop from left: {queue.popleft()}")
print(f"Final queue: {queue}")
print()

# Example 2: Rotating elements
dq = deque([1, 2, 3, 4, 5])
print(f"Original: {dq}")
dq.rotate(2)                # Rotate right by 2
print(f"Rotate right 2: {dq}")
dq.rotate(-1)               # Rotate left by 1
print(f"Rotate left 1: {dq}")
print()

# Example 3: Limited size deque (sliding window)
recent = deque(maxlen=3)
for i in range(5):
    recent.append(i)
    print(f"Added {i}, recent: {list(recent)}")
print()


# ============================================================================
# 4. NAMEDTUPLE - Lightweight objects
# ============================================================================
print("=" * 60)
print("4. NAMEDTUPLE")
print("=" * 60)

from collections import namedtuple

# Example 1: Creating a Point
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)
print(f"Point: {p1}")
print(f"Access by name: x={p1.x}, y={p1.y}")
print(f"Access by index: x={p1[0]}, y={p1[1]}")
print()

# Example 2: Person with more fields
Person = namedtuple('Person', ['name', 'age', 'city'])
john = Person('John', 30, 'New York')
print(f"Person: {john}")
print(f"Name: {john.name}, Age: {john.age}")
print()

# Example 3: Convert to dictionary
print(f"As dict: {john._asdict()}")
print()


# ============================================================================
# 5. LIST COMPREHENSIONS - Elegant and fast
# ============================================================================
print("=" * 60)
print("5. LIST COMPREHENSIONS")
print("=" * 60)

# Example 1: Basic comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")
print()

# Example 2: With condition
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")
print()

# Example 3: With if-else
labels = ['even' if x % 2 == 0 else 'odd' for x in numbers]
print(f"Labels: {labels}")
print()

# Example 4: Nested comprehension (matrix flattening)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened: {flattened}")
print()


# ============================================================================
# 6. DICT COMPREHENSIONS
# ============================================================================
print("=" * 60)
print("6. DICT COMPREHENSIONS")
print("=" * 60)

# Example 1: Square numbers
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dict: {squares_dict}")
print()

# Example 2: Filter dictionary
prices = {'apple': 0.50, 'banana': 0.30, 'orange': 0.80, 'grape': 1.20}
expensive = {fruit: price for fruit, price in prices.items() if price > 0.50}
print(f"Expensive fruits: {expensive}")
print()

# Example 3: Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {value: key for key, value in original.items()}
print(f"Original: {original}")
print(f"Swapped: {swapped}")
print()


# ============================================================================
# 7. SET COMPREHENSIONS
# ============================================================================
print("=" * 60)
print("7. SET COMPREHENSIONS")
print("=" * 60)

# Example 1: Unique squares
numbers_with_dups = [1, 2, 2, 3, 3, 3, 4, 5]
unique_squares = {x**2 for x in numbers_with_dups}
print(f"Unique squares: {unique_squares}")
print()


# ============================================================================
# 8. UNPACKING & DESTRUCTURING
# ============================================================================
print("=" * 60)
print("8. UNPACKING & DESTRUCTURING")
print("=" * 60)

# Example 1: Basic unpacking
a, b, c = [1, 2, 3]
print(f"a={a}, b={b}, c={c}")
print()

# Example 2: Extended unpacking with *
first, *middle, last = [1, 2, 3, 4, 5]
print(f"first={first}, middle={middle}, last={last}")
print()

# Example 3: Swapping variables
x, y = 10, 20
print(f"Before swap: x={x}, y={y}")
x, y = y, x
print(f"After swap: x={x}, y={y}")
print()

# Example 4: Ignoring values
first, _, third = [1, 2, 3]
print(f"first={first}, third={third}")
print()

# Example 5: Dictionary unpacking
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print(f"Merged dict: {merged}")
print()

# Example 6: Function arguments unpacking
def print_info(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

person_info = {'name': 'Alice', 'age': 25, 'city': 'Boston'}
print_info(**person_info)
print()


# ============================================================================
# 9. WHEN TO USE WHAT?
# ============================================================================
print("=" * 60)
print("9. PRACTICAL USE CASES")
print("=" * 60)

# Use Case 1: Word frequency analysis (Counter)
text = "the quick brown fox jumps over the lazy dog the fox"
word_freq = Counter(text.split())
print(f"Most common words: {word_freq.most_common(3)}")
print()

# Use Case 2: Graph adjacency list (defaultdict)
graph = defaultdict(list)
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D')]
for start, end in edges:
    graph[start].append(end)
print(f"Graph: {dict[Any, list](graph)}")
print()

# Use Case 3: Task queue (deque)
tasks = deque(['task1', 'task2', 'task3'])
print("Processing tasks:")
while tasks:
    task = tasks.popleft()
    print(f"  Processing {task}")
print()

print("=" * 60)
print("Great job! Now try the exercises in exercises.py")
print("=" * 60)

