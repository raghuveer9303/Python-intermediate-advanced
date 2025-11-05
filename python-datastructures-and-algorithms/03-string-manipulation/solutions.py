"""
Solutions to String Manipulation Exercises
"""

from collections import Counter, defaultdict

# Solution 1: Reverse String
def reverse_string(s):
    # If list (mutable)
    if isinstance(s, list):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
    # If string (immutable)
    else:
        return s[::-1]


# Solution 2: Valid Palindrome
def is_palindrome(s):
    # Clean string: lowercase, alphanumeric only
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    # Two pointers
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


# Solution 3: Longest Substring Without Repeating Characters
def longest_unique_substring(s):
    char_index = {}
    start = 0
    max_length = 0
    
    for end, char in enumerate(s):
        # If char seen and within current window, move start
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length


# Solution 4: Valid Anagram
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)

# Alternative: Sort and compare
def is_anagram_sort(s1, s2):
    return sorted(s1) == sorted(s2)


# Solution 5: Longest Palindromic Substring
def longest_palindrome(s):
    if not s:
        return ""
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    for i in range(len(s)):
        # Odd length palindrome
        palindrome1 = expand_around_center(i, i)
        # Even length palindrome
        palindrome2 = expand_around_center(i, i + 1)
        
        longest = max(longest, palindrome1, palindrome2, key=len)
    
    return longest


# Solution 6: Valid Parentheses
def valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            # Closing bracket
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            # Opening bracket
            stack.append(char)
    
    return len(stack) == 0


# Solution 7: String to Integer (atoi)
def atoi(s):
    s = s.strip()
    if not s:
        return 0
    
    # Handle sign
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    
    # Convert digits
    result = 0
    for char in s:
        if not char.isdigit():
            break
        result = result * 10 + int(char)
        
        # Check overflow
        if sign * result > 2**31 - 1:
            return 2**31 - 1
        if sign * result < -2**31:
            return -2**31
    
    return sign * result


# Solution 8: Longest Common Prefix
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Compare character by character
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    
    return strs[0]


# Solution 9: Reverse Words in String
def reverse_words(s):
    # Split and reverse
    words = s.split()
    return ' '.join(words[::-1])

# Alternative: Manual approach
def reverse_words_manual(s):
    words = []
    current_word = []
    
    for char in s:
        if char == ' ':
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    
    if current_word:
        words.append(''.join(current_word))
    
    return ' '.join(words[::-1])


# Solution 10: Minimum Window Substring
def min_window(s, t):
    if not s or not t:
        return ""
    
    # Count characters needed
    need = Counter(t)
    need_count = len(need)
    
    # Window tracking
    window = defaultdict(int)
    have_count = 0
    
    # Result tracking
    min_len = float('inf')
    result = ""
    
    left = 0
    for right in range(len(s)):
        # Expand window
        char = s[right]
        window[char] += 1
        
        # Check if we have enough of this char
        if char in need and window[char] == need[char]:
            have_count += 1
        
        # Try to contract window
        while have_count == need_count:
            # Update result
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
            
            # Remove from left
            left_char = s[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                have_count -= 1
            left += 1
    
    return result


# Test solutions
if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    assert s == ["o", "l", "l", "e", "h"]
    print("✓ Exercise 1 passed")
    
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    print("✓ Exercise 2 passed")
    
    assert longest_unique_substring("abcabcbb") == 3
    print("✓ Exercise 3 passed")
    
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
    print("✓ Exercise 4 passed")
    
    assert longest_palindrome("babad") in ["bab", "aba"]
    print("✓ Exercise 5 passed")
    
    assert valid_parentheses("()[]{}") == True
    assert valid_parentheses("([)]") == False
    print("✓ Exercise 6 passed")
    
    assert atoi("42") == 42
    assert atoi("   -42") == -42
    print("✓ Exercise 7 passed")
    
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    print("✓ Exercise 8 passed")
    
    assert reverse_words("the sky is blue") == "blue is sky the"
    print("✓ Exercise 9 passed")
    
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    print("✓ Exercise 10 passed")
    
    print("\n🎉 All tests passed!")

