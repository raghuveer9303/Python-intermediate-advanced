# 📊 Arrays & Lists - Foundation for Data Scientists

## Why This Matters (80-20)

**Arrays are used in 40% of DS interview problems!**
- Data manipulation in pandas/numpy
- Feature engineering
- Time series analysis
- Most common structure in Python

---

## 🎯 Core Concepts

### 1. Array Basics
- Indexing and slicing
- List comprehensions
- Common operations

### 2. Common Patterns
- **Prefix Sum** - Range queries
- **Suffix Sum** - Cumulative calculations
- **Two Pointers** - Pair finding
- **Kadane's Algorithm** - Maximum subarray

### 3. Data Science Applications
- Feature arrays
- Time series windows
- Data cleaning operations

---

## 📝 Key Operations

```python
# Creating arrays
arr = [1, 2, 3, 4, 5]
arr = list(range(10))
arr = [x**2 for x in range(10)]  # List comprehension

# Common operations
arr.append(6)           # O(1)
arr.insert(0, 0)        # O(n)
arr.pop()               # O(1)
arr.pop(0)              # O(n)
arr.remove(3)           # O(n)
len(arr)                # O(1)
arr.index(3)            # O(n)

# Slicing (extremely useful!)
arr[1:4]                # [2, 3, 4]
arr[::-1]               # Reverse
arr[::2]                # Every 2nd element
```

---

## 🔑 Common Patterns

### Pattern 1: Two Pointers
```python
# Find pairs that sum to target
def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### Pattern 2: Prefix Sum
```python
# Calculate sum of subarray in O(1)
def prefix_sum(arr):
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)
    return prefix

# Query: sum from i to j
def range_sum(prefix, i, j):
    return prefix[j+1] - prefix[i]
```

### Pattern 3: Sliding Window
```python
# Maximum sum of subarray of size k
def max_subarray_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

---

## 🎓 Interview Tips

1. **Always ask**: Can array be modified? Sorted?
2. **Space optimization**: Can we solve in-place?
3. **Edge cases**: Empty array, single element, all same values
4. **Time complexity**: Most array problems should be O(n) or O(n log n)

---

## 📚 Next Steps

- Complete `exercises.py`
- Review `solutions.py`
- Practice on LeetCode: Easy array problems
- Move to Dictionaries & Hash Maps

