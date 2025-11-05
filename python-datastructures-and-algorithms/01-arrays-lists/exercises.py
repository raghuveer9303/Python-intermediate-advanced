"""
Arrays & Lists - Hands-On Exercises
Complete these exercises to master array manipulation
"""

# Exercise 1: Find Maximum Element
# Write a function to find the maximum element in an array
def find_max(arr):
    """
    Input: [3, 7, 2, 9, 1]
    Output: 9
    """
    # TODO: Your code here
    pass


# Exercise 2: Reverse Array
# Reverse an array in-place (modify the original array)
def reverse_array(arr):
    """
    Input: [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1] (modify in-place)
    """
    # TODO: Your code here
    pass


# Exercise 3: Two Sum
# Find two numbers that add up to target, return their indices
def two_sum(arr, target):
    """
    Input: arr = [2, 7, 11, 15], target = 9
    Output: [0, 1] (because arr[0] + arr[1] = 2 + 7 = 9)
    
    Assumption: Exactly one solution exists
    """
    # TODO: Your code here
    pass


# Exercise 4: Move Zeros to End
# Move all zeros to the end while maintaining relative order
def move_zeros(arr):
    """
    Input: [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0] (modify in-place)
    """
    # TODO: Your code here
    pass


# Exercise 5: Maximum Subarray Sum (Kadane's Algorithm)
# Find the maximum sum of contiguous subarray
def max_subarray_sum(arr):
    """
    Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6 (subarray [4, -1, 2, 1])
    
    Hint: Use dynamic programming approach
    """
    # TODO: Your code here
    pass


# Exercise 6: Product of Array Except Self
# Return array where each element is product of all others
def product_except_self(arr):
    """
    Input: [1, 2, 3, 4]
    Output: [24, 12, 8, 6]
    
    Constraint: Cannot use division, O(n) time, O(1) extra space (excluding output)
    """
    # TODO: Your code here
    pass


# Exercise 7: Find Missing Number
# Array contains n distinct numbers from 0 to n, find missing one
def find_missing_number(arr):
    """
    Input: [3, 0, 1]
    Output: 2
    
    Input: [9, 6, 4, 2, 3, 5, 7, 0, 1]
    Output: 8
    """
    # TODO: Your code here
    pass


# Exercise 8: Rotate Array
# Rotate array to right by k steps
def rotate_array(arr, k):
    """
    Input: arr = [1, 2, 3, 4, 5], k = 2
    Output: [4, 5, 1, 2, 3] (modify in-place)
    
    Hint: Reverse array, then reverse first k, then reverse rest
    """
    # TODO: Your code here
    pass


# Exercise 9: Find Duplicate
# Array contains n+1 integers in range [1, n], find duplicate
def find_duplicate(arr):
    """
    Input: [1, 3, 4, 2, 2]
    Output: 2
    
    Constraint: O(1) extra space, cannot modify array
    Hint: Use Floyd's cycle detection
    """
    # TODO: Your code here
    pass


# Exercise 10: Merge Sorted Arrays
# Merge two sorted arrays into one sorted array
def merge_sorted_arrays(arr1, arr2):
    """
    Input: arr1 = [1, 3, 5], arr2 = [2, 4, 6]
    Output: [1, 2, 3, 4, 5, 6]
    """
    # TODO: Your code here
    pass


# Test your functions
if __name__ == "__main__":
    # Test Exercise 1
    print("Exercise 1:", find_max([3, 7, 2, 9, 1]))  # Expected: 9
    
    # Test Exercise 2
    arr = [1, 2, 3, 4, 5]
    reverse_array(arr)
    print("Exercise 2:", arr)  # Expected: [5, 4, 3, 2, 1]
    
    # Test Exercise 3
    print("Exercise 3:", two_sum([2, 7, 11, 15], 9))  # Expected: [0, 1]
    
    # Add more tests as you complete exercises

