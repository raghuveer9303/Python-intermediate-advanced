"""
Solutions to Binary Search Exercises
"""

# Solution 1: Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


# Solution 2: Find First and Last Position
def search_range(arr, target):
    def find_first(arr, target):
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                result = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
    
    def find_last(arr, target):
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                result = mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
    
    first = find_first(arr, target)
    if first == -1:
        return [-1, -1]
    last = find_last(arr, target)
    return [first, last]


# Solution 3: Search in Rotated Sorted Array
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
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


# Solution 4: Find Peak Element
def find_peak(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[mid + 1]:
            # Peak is in left half (including mid)
            right = mid
        else:
            # Peak is in right half
            left = mid + 1
    
    return left


# Solution 5: Search Insert Position
def search_insert(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


# Solution 6: Find Minimum in Rotated Array
def find_min_rotated(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half (including mid)
            right = mid
    
    return arr[left]


# Solution 7: Sqrt(x)
def sqrt(x):
    if x < 2:
        return x
    
    left, right = 1, x // 2
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # Return floor of sqrt


# Solution 8: Find K Closest Elements
def find_closest_elements(arr, k, target):
    # Find insertion point
    left, right = 0, len(arr) - k
    
    while left < right:
        mid = left + (right - left) // 2
        # If target is closer to arr[mid+k], move left
        if target - arr[mid] > arr[mid + k] - target:
            left = mid + 1
        else:
            right = mid
    
    return arr[left:left + k]


# Test solutions
if __name__ == "__main__":
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    print("✓ Exercise 1 passed")
    
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    print("✓ Exercise 2 passed")
    
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    print("✓ Exercise 3 passed")
    
    assert find_peak([1, 2, 3, 1]) == 2
    print("✓ Exercise 4 passed")
    
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    print("✓ Exercise 5 passed")
    
    assert find_min_rotated([3, 4, 5, 1, 2]) == 1
    print("✓ Exercise 6 passed")
    
    assert sqrt(4) == 2
    assert sqrt(8) == 2
    print("✓ Exercise 7 passed")
    
    assert find_closest_elements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
    print("✓ Exercise 8 passed")
    
    print("\n🎉 All tests passed!")

