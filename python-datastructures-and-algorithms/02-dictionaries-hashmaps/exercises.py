"""
Dictionaries & Hash Maps - Hands-On Exercises
"""

# Exercise 1: Count Character Frequency
# Count frequency of each character in a string
def count_chars(s):
    """
    Input: "hello"
    Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    # TODO: Your code here
    pass


# Exercise 2: Find First Unique Character
# Find first character that appears only once
def first_unique_char(s):
    """
    Input: "leetcode"
    Output: 'l' (index 0)
    
    Input: "loveleetcode"
    Output: 'v' (index 2)
    
    If no unique char, return -1
    """
    # TODO: Your code here
    pass


# Exercise 3: Group Anagrams
# Group strings that are anagrams of each other
def group_anagrams(strs):
    """
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    
    Hint: Use sorted string as key
    """
    # TODO: Your code here
    pass


# Exercise 4: Two Sum (All Pairs)
# Find all pairs that sum to target
def two_sum_all_pairs(arr, target):
    """
    Input: arr = [1, 5, 3, 3, 3], target = 6
    Output: [(0, 1), (2, 3), (2, 4), (3, 4)]
    
    Return list of tuples (index1, index2)
    """
    # TODO: Your code here
    pass


# Exercise 5: Longest Consecutive Sequence
# Find length of longest consecutive sequence
def longest_consecutive(nums):
    """
    Input: [100, 4, 200, 1, 3, 2]
    Output: 4 (sequence: 1, 2, 3, 4)
    
    Time: O(n) required
    """
    # TODO: Your code here
    pass


# Exercise 6: Subarray Sum Equals K
# Count number of subarrays with sum equals k
def subarray_sum_k(arr, k):
    """
    Input: arr = [1, 1, 1], k = 2
    Output: 2 (subarrays: [1,1] and [1,1])
    
    Hint: Use prefix sum with hash map
    """
    # TODO: Your code here
    pass


# Exercise 7: Word Pattern
# Check if string follows pattern
def word_pattern(pattern, s):
    """
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: True
    
    Input: pattern = "abba", s = "dog cat cat fish"
    Output: False
    """
    # TODO: Your code here
    pass


# Exercise 8: Top K Frequent Elements
# Find k most frequent elements
def top_k_frequent(arr, k):
    """
    Input: arr = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]
    
    Hint: Use Counter and sorting
    """
    # TODO: Your code here
    pass


# Exercise 9: Design LRU Cache
# Implement Least Recently Used cache
class LRUCache:
    """
    Operations: get(key) and put(key, value)
    Both should be O(1)
    """
    def __init__(self, capacity):
        # TODO: Initialize cache
        pass
    
    def get(self, key):
        # TODO: Return value or -1
        pass
    
    def put(self, key, value):
        # TODO: Add or update key-value pair
        pass


# Exercise 10: Find Duplicate Subtrees
# Find all duplicate subtrees in binary tree
# (Advanced - will cover in Trees section, but good hash map practice)

# Test your functions
if __name__ == "__main__":
    # Test Exercise 1
    print("Exercise 1:", count_chars("hello"))
    
    # Test Exercise 2
    print("Exercise 2:", first_unique_char("leetcode"))
    
    # Add more tests

