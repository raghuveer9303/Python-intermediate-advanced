# 🔑 Dictionaries & Hash Maps - Fast Lookups

## Why This Matters (80-20)

**Hash Maps are used in 30% of DS interview problems!**
- O(1) average lookup time
- Frequency counting
- Caching and memoization
- Essential for optimization

---

## 🎯 Core Concepts

### 1. Dictionary/HashMap Basics
- Key-value pairs
- Hash function and collisions
- Time complexity: O(1) average, O(n) worst case

### 2. Common Patterns
- **Frequency Counting** - Most common pattern
- **Two Sum Variants** - Complement lookup
- **Caching** - Memoization
- **Grouping** - Group by key

### 3. Data Science Applications
- Feature counting
- Categorical encoding
- Cache frequently used computations
- Join operations simulation

---

## 📝 Key Operations

```python
# Creating dictionaries
d = {}
d = dict()
d = {'a': 1, 'b': 2}
d = dict(a=1, b=2)

# Common operations
d[key] = value          # O(1) average
d.get(key, default)     # O(1) average, safe lookup
key in d                # O(1) average
d.keys()                # O(n) - returns view
d.values()              # O(n) - returns view
d.items()               # O(n) - returns view
del d[key]              # O(1) average
len(d)                  # O(1)

# Dictionary comprehension
d = {x: x**2 for x in range(10)}
d = {k: v for k, v in d.items() if v > 5}
```

---

## 🔑 Common Patterns

### Pattern 1: Frequency Counting
```python
def count_frequency(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Using Counter
from collections import Counter
freq = Counter(arr)
```

### Pattern 2: Two Sum with Hash Map
```python
def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Pattern 3: Grouping
```python
def group_by_key(data, key_func):
    groups = {}
    for item in data:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

# Using defaultdict
from collections import defaultdict
groups = defaultdict(list)
for item in data:
    groups[key_func(item)].append(item)
```

### Pattern 4: Caching (Memoization)
```python
cache = {}
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]

# Using functools.lru_cache
from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

---

## 🎓 Interview Tips

1. **Defaultdict vs dict**: Use defaultdict when you need default values
2. **Counter**: Use for frequency counting - more Pythonic
3. **Space vs Time**: Hash maps trade space for time
4. **Edge cases**: Empty dict, single element, all same values
5. **Order matters?**: Use OrderedDict or dict (Python 3.7+ maintains insertion order)

---

## 📚 Next Steps

- Complete `exercises.py`
- Review `solutions.py`
- Practice frequency counting problems
- Move to String Manipulation

