"""
Solutions to Arrays & Lists Exercises
Study these after attempting exercises yourself
"""

# Solution 1: Find Maximum Element
def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val

# Alternative: return max(arr) - but interviewers want manual implementation


# Solution 2: Reverse Array In-Place
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


# Solution 3: Two Sum
def two_sum(arr, target):
    """
    Time: O(n), Space: O(n)
    Use hash map for O(1) lookups
    """
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Solution 4: Move Zeros to End
def move_zeros(arr):
    """
    Time: O(n), Space: O(1)
    Two pointers: one for current position, one for last non-zero
    """
    last_non_zero = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[last_non_zero], arr[i] = arr[i], arr[last_non_zero]
            last_non_zero += 1
    return arr


# Solution 5: Maximum Subarray Sum (Kadane's Algorithm)
def max_subarray_sum(arr):
    """
    Time: O(n), Space: O(1)
    Key insight: Either extend previous subarray or start new one
    """
    if not arr:
        return 0
    
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        # Either extend previous subarray or start fresh
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# Solution 6: Product of Array Except Self
def product_except_self(arr):
    """
    Time: O(n), Space: O(1) excluding output array
    Two passes: left products, then right products
    """
    n = len(arr)
    result = [1] * n
    
    # Left pass: result[i] = product of all left elements
    for i in range(1, n):
        result[i] = result[i-1] * arr[i-1]
    
    # Right pass: multiply by right products
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= arr[i]
    
    return result


# Solution 7: Find Missing Number
def find_missing_number(arr):
    """
    Time: O(n), Space: O(1)
    Sum approach: expected sum - actual sum
    """
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Alternative: XOR approach (more elegant)
def find_missing_number_xor(arr):
    n = len(arr)
    missing = n
    for i, num in enumerate(arr):
        missing ^= i ^ num
    return missing


# Solution 8: Rotate Array
def rotate_array(arr, k):
    """
    Time: O(n), Space: O(1)
    Reverse trick: reverse all, then reverse first k, then reverse rest
    """
    n = len(arr)
    k = k % n  # Handle k > n
    
    # Reverse entire array
    arr.reverse()
    
    # Reverse first k elements
    arr[:k] = arr[:k][::-1]
    
    # Reverse remaining elements
    arr[k:] = arr[k:][::-1]
    
    return arr


# Solution 9: Find Duplicate (Floyd's Cycle Detection)
def find_duplicate(arr):
    """
    Time: O(n), Space: O(1)
    Treat array as linked list with cycles
    """
    # Phase 1: Find intersection point in cycle
    slow = fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    # Phase 2: Find entrance to cycle
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow


# Solution 10: Merge Sorted Arrays
def merge_sorted_arrays(arr1, arr2):
    """
    Time: O(n + m), Space: O(n + m)
    Two pointers approach
    """
    result = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result


# Test all solutions
if __name__ == "__main__":
    print("Testing Solutions:")
    
    assert find_max([3, 7, 2, 9, 1]) == 9
    print("✓ Exercise 1 passed")
    
    arr = [1, 2, 3, 4, 5]
    reverse_array(arr)
    assert arr == [5, 4, 3, 2, 1]
    print("✓ Exercise 2 passed")
    
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    print("✓ Exercise 3 passed")
    
    arr = [0, 1, 0, 3, 12]
    move_zeros(arr)
    assert arr == [1, 3, 12, 0, 0]
    print("✓ Exercise 4 passed")
    
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    print("✓ Exercise 5 passed")
    
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    print("✓ Exercise 6 passed")
    
    assert find_missing_number([3, 0, 1]) == 2
    print("✓ Exercise 7 passed")
    
    arr = [1, 2, 3, 4, 5]
    rotate_array(arr, 2)
    assert arr == [4, 5, 1, 2, 3]
    print("✓ Exercise 8 passed")
    
    assert find_duplicate([1, 3, 4, 2, 2]) == 2
    print("✓ Exercise 9 passed")
    
    assert merge_sorted_arrays([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    print("✓ Exercise 10 passed")
    
    print("\n🎉 All tests passed!")

