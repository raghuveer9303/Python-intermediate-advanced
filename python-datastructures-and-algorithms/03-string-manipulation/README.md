# 📝 String Manipulation - Text Processing

## Why This Matters (80-20)

**Strings are fundamental in data science!**
- Text preprocessing for NLP
- Data cleaning and validation
- Pattern matching
- Common in DS interviews (15% of problems)

---

## 🎯 Core Concepts

### 1. String Basics
- Immutability in Python
- String methods
- String slicing and indexing

### 2. Common Patterns
- **Two Pointers** - Palindrome checking
- **Sliding Window** - Longest substring
- **Character Counting** - Frequency analysis
- **Pattern Matching** - String matching

### 3. Data Science Applications
- Text cleaning
- Feature extraction
- Regex matching
- Data validation

---

## 📝 Key Operations

```python
# String creation
s = "hello"
s = 'hello'
s = """multiline
string"""

# Common operations
s[i]                    # Character at index i
s[i:j]                  # Slice
s[::-1]                 # Reverse
len(s)                  # Length
s.lower()               # Lowercase
s.upper()               # Uppercase
s.strip()               # Remove whitespace
s.split(sep)            # Split into list
','.join(list)          # Join list into string
s.replace(old, new)     # Replace
s.find(substring)        # Find index
s.count(substring)       # Count occurrences
s.startswith(prefix)     # Check prefix
s.endswith(suffix)       # Check suffix

# String formatting
f"Value: {x}"           # f-string (Python 3.6+)
"Value: {}".format(x)    # format method
"Value: %s" % x          # Old style
```

---

## 🔑 Common Patterns

### Pattern 1: Two Pointers for Palindrome
```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

### Pattern 2: Sliding Window for Substring
```python
def longest_substring_no_repeat(s):
    char_index = {}
    start = 0
    max_length = 0
    
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length
```

### Pattern 3: Character Frequency
```python
from collections import Counter
freq = Counter(s)
most_common = freq.most_common(1)
```

---

## 🎓 Interview Tips

1. **Immutability**: Strings are immutable in Python - operations create new strings
2. **Space optimization**: Use two pointers instead of creating new strings
3. **Edge cases**: Empty string, single character, all same characters
4. **Regex**: Know basics but avoid overuse in interviews
5. **Unicode**: Be aware of encoding issues in real-world scenarios

---

## 📚 Next Steps

- Complete `exercises.py`
- Review `solutions.py`
- Practice string manipulation problems
- Move to Two Pointers technique

