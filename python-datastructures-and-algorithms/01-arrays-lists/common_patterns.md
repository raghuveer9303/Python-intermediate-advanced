# Common Patterns for Arrays & Lists

## Quick Reference Templates

---

## 1. Two Pointers Pattern

**Use when**: Finding pairs, palindromes, merging sorted arrays

```python
def two_pointers_template(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Do something with arr[left] and arr[right]
        if condition:
            left += 1
        else:
            right -= 1
    return result
```

**Examples**:
- Two Sum (sorted array)
- Valid Palindrome
- Container With Most Water
- Merge Sorted Arrays

---

## 2. Sliding Window Pattern

**Use when**: Finding subarrays/substrings with specific properties

```python
def sliding_window_template(arr, k):
    # Initialize window
    window_sum = sum(arr[:k])
    result = window_sum
    
    # Slide window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        result = max(result, window_sum)  # or min, or other operation
    
    return result
```

**Examples**:
- Maximum/Minimum sum of subarray of size k
- Longest substring with k distinct characters
- Minimum window substring

---

## 3. Kadane's Algorithm (Maximum Subarray)

**Use when**: Finding maximum sum of contiguous subarray

```python
def kadane_template(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```

**Variations**:
- Maximum product subarray
- Maximum subarray with at least k elements

---

## 4. Prefix Sum Pattern

**Use when**: Multiple range sum queries

```python
def prefix_sum_template(arr):
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)
    return prefix

# Query range [i, j]
def query(prefix, i, j):
    return prefix[j+1] - prefix[i]
```

**Examples**:
- Range sum queries
- Subarray sum equals k
- Maximum size subarray sum equals k

---

## 5. Dutch National Flag (Three-way Partition)

**Use when**: Partitioning array into 3 groups

```python
def three_way_partition(arr, pivot):
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == pivot:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr
```

**Examples**:
- Sort colors (0s, 1s, 2s)
- Partition around pivot

---

## 6. Fast and Slow Pointers

**Use when**: Finding cycles, middle element, nth from end

```python
def fast_slow_pointers(arr):
    slow = fast = 0
    while fast < len(arr) and fast + 1 < len(arr):
        slow += 1
        fast += 2
    return slow  # Middle or meeting point
```

**Examples**:
- Find middle of linked list
- Detect cycle
- Find duplicate in array (with constraints)

---

## 7. In-place Array Modification

**Use when**: Space optimization is required

```python
def inplace_modification(arr):
    write_idx = 0
    for read_idx in range(len(arr)):
        if should_keep(arr[read_idx]):
            arr[write_idx] = arr[read_idx]
            write_idx += 1
    return arr[:write_idx]  # Return valid portion
```

**Examples**:
- Remove duplicates
- Remove element
- Move zeros

---

## 8. Array Rotation

**Use when**: Rotating array by k positions

```python
def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    arr.reverse()
    arr[:k] = arr[:k][::-1]
    arr[k:] = arr[k:][::-1]
    return arr
```

---

## 🎯 Pattern Recognition Tips

1. **Two Pointers**: Look for "find pairs", "palindrome", "sorted array"
2. **Sliding Window**: Look for "subarray", "substring", "window of size k"
3. **Prefix Sum**: Look for "range queries", "cumulative"
4. **Kadane**: Look for "maximum sum", "contiguous subarray"
5. **Fast/Slow**: Look for "cycle", "middle", "nth element"

---

## 💡 Pro Tips

- Always consider **edge cases**: empty array, single element, all same values
- Ask about **modification**: Can we modify input? Do we need in-place?
- Consider **sorting**: Sometimes sorting first simplifies problem
- **Space optimization**: Can we use O(1) extra space?
- **Time complexity**: Most array problems should be O(n) or O(n log n)

