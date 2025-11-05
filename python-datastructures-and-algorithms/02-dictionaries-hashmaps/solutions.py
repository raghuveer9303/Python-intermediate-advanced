"""
Solutions to Dictionaries & Hash Maps Exercises
"""

from collections import Counter, defaultdict, OrderedDict

# Solution 1: Count Character Frequency
def count_chars(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Alternative with Counter
def count_chars_counter(s):
    return dict(Counter(s))


# Solution 2: Find First Unique Character
def first_unique_char(s):
    freq = {}
    # Count frequency
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Find first unique
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    return -1


# Solution 3: Group Anagrams
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        # Use sorted string as key
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())


# Solution 4: Two Sum (All Pairs)
def two_sum_all_pairs(arr, target):
    seen = {}
    result = []
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            # Add all pairs with this complement
            for j in seen[complement]:
                result.append((j, i))
        
        # Track all indices for this number
        if num not in seen:
            seen[num] = []
        seen[num].append(i)
    
    return result


# Solution 5: Longest Consecutive Sequence
def longest_consecutive(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start from beginning of sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Extend sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length


# Solution 6: Subarray Sum Equals K
def subarray_sum_k(arr, k):
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # prefix_sum -> count
    
    for num in arr:
        prefix_sum += num
        # If prefix_sum - k exists, we found a subarray
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        # Update count
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count


# Solution 7: Word Pattern
def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    pattern_to_word = {}
    word_to_pattern = {}
    
    for p, word in zip(pattern, words):
        if p in pattern_to_word:
            if pattern_to_word[p] != word:
                return False
        else:
            pattern_to_word[p] = word
        
        if word in word_to_pattern:
            if word_to_pattern[word] != p:
                return False
        else:
            word_to_pattern[word] = p
    
    return True


# Solution 8: Top K Frequent Elements
def top_k_frequent(arr, k):
    # Count frequency
    freq = Counter(arr)
    
    # Sort by frequency (descending) and get top k
    return [item[0] for item in freq.most_common(k)]

# Alternative: Using heap (more efficient for large k)
from heapq import nlargest
def top_k_frequent_heap(arr, k):
    freq = Counter(arr)
    return [item[0] for item in nlargest(k, freq.items(), key=lambda x: x[1])]


# Solution 9: LRU Cache
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key not in self.cache:
            return -1
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            # Update existing key
            self.cache.move_to_end(key)
        else:
            # Check capacity
            if len(self.cache) >= self.capacity:
                # Remove least recently used (first item)
                self.cache.popitem(last=False)
        self.cache[key] = value


# Test solutions
if __name__ == "__main__":
    assert count_chars("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print("✓ Exercise 1 passed")
    
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    print("✓ Exercise 2 passed")
    
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert len(result) == 3
    print("✓ Exercise 3 passed")
    
    pairs = two_sum_all_pairs([1, 5, 3, 3, 3], 6)
    assert len(pairs) == 4
    print("✓ Exercise 4 passed")
    
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    print("✓ Exercise 5 passed")
    
    assert subarray_sum_k([1, 1, 1], 2) == 2
    print("✓ Exercise 6 passed")
    
    assert word_pattern("abba", "dog cat cat dog") == True
    assert word_pattern("abba", "dog cat cat fish") == False
    print("✓ Exercise 7 passed")
    
    assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    print("✓ Exercise 8 passed")
    
    # Test LRU Cache
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)  # Evicts key 2
    assert lru.get(2) == -1
    assert lru.get(3) == 3
    print("✓ Exercise 9 passed")
    
    print("\n🎉 All tests passed!")

