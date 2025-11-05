# 🔍 Binary Search - Optimization Problems

## Why This Matters (80-20)

**Binary Search appears in 15% of DS interview problems!**
- O(log n) time complexity
- Optimization problems
- Search in sorted data
- Common in data science (finding thresholds, cutoffs)

---

## 🎯 Core Concepts

### 1. Binary Search Basics
- Requires sorted array
- Divide and conquer approach
- Time: O(log n), Space: O(1)

### 2. Common Patterns
- **Standard Binary Search** - Find exact value
- **Find First/Last Occurrence** - Modified binary search
- **Search in Rotated Array** - Modified binary search
- **Binary Search on Answer** - Search space reduction

### 3. Data Science Applications
- Finding thresholds
- Cutoff values
- Optimization problems
- Search in sorted data

---

## 📝 Template

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

---

## 🔑 Common Patterns

### Pattern 1: Find First Occurrence
```python
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### Pattern 2: Search in Rotated Array
```python
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

### Pattern 3: Binary Search on Answer
```python
def binary_search_answer(arr, condition):
    left, right = min(arr), max(arr)
    
    while left < right:
        mid = (left + right) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
```

---

## 🎓 Interview Tips

1. **Always check**: Is array sorted? Can we sort it?
2. **Edge cases**: Empty array, single element, all same values
3. **Off-by-one errors**: Be careful with `<=` vs `<`
4. **Overflow**: Use `mid = left + (right - left) // 2` for large arrays

---

## 📚 Next Steps

- Complete `exercises.py`
- Review `solutions.py`
- Practice binary search variations
- Move to Sliding Window

