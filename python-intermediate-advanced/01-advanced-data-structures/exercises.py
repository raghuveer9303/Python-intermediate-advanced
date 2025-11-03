"""
Module 01: Advanced Data Structures - Exercises

Complete these exercises to practice what you've learned!
Run this file to test your solutions.
"""

from collections import Counter, defaultdict, deque, namedtuple


# ============================================================================
# Exercise 1: Counter - Find the most common element
# ============================================================================
def most_common_element(items):
    """
    Given a list of items, return the most common element.
    If there's a tie, return any of them.
    
    Example:
        most_common_element([1, 2, 2, 3, 3, 3]) -> 3
        most_common_element(['a', 'b', 'a']) -> 'a'
    """
    # TODO: Implement this using Counter
    pass


# ============================================================================
# Exercise 2: defaultdict - Group students by grade
# ============================================================================
def group_by_grade(students):
    """
    Given a list of tuples (name, grade), group students by their grade.
    
    Example:
        students = [('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A'), ('David', 'B')]
        Result: {'A': ['Alice', 'Charlie'], 'B': ['Bob', 'David']}
    """
    # TODO: Implement this using defaultdict
    pass


# ============================================================================
# Exercise 3: deque - Implement a simple browser history
# ============================================================================
class BrowserHistory:
    """
    Implement a browser history with forward and back functionality.
    Keep only the last 5 visited pages.
    """
    
    def __init__(self):
        # TODO: Initialize a deque with maxlen=5
        pass
    
    def visit(self, url):
        """Visit a new URL"""
        # TODO: Add URL to history
        pass
    
    def get_history(self):
        """Return current history as a list"""
        # TODO: Return history
        pass


# ============================================================================
# Exercise 4: namedtuple - Create a Book record
# ============================================================================
# TODO: Create a namedtuple called 'Book' with fields: title, author, year, isbn

def create_book(title, author, year, isbn):
    """Create and return a Book namedtuple"""
    # TODO: Create and return a Book
    pass


# ============================================================================
# Exercise 5: List Comprehension - Filter and transform
# ============================================================================
def get_even_squares(numbers):
    """
    Return a list of squares of even numbers only.
    
    Example:
        get_even_squares([1, 2, 3, 4, 5]) -> [4, 16]
    """
    # TODO: Implement using list comprehension
    pass


# ============================================================================
# Exercise 6: Dict Comprehension - Invert a dictionary
# ============================================================================
def invert_dict(d):
    """
    Invert a dictionary (swap keys and values).
    Assume all values are unique.
    
    Example:
        invert_dict({'a': 1, 'b': 2}) -> {1: 'a', 2: 'b'}
    """
    # TODO: Implement using dict comprehension
    pass


# ============================================================================
# Exercise 7: Nested Comprehension - Matrix transpose
# ============================================================================
def transpose_matrix(matrix):
    """
    Transpose a matrix (swap rows and columns).
    
    Example:
        matrix = [[1, 2, 3],
                  [4, 5, 6]]
        Result: [[1, 4],
                 [2, 5],
                 [3, 6]]
    """
    # TODO: Implement using nested list comprehension
    # Hint: New matrix[i][j] = old matrix[j][i]
    pass


# ============================================================================
# Exercise 8: Unpacking - Parse CSV-like data
# ============================================================================
def parse_person_data(data_string):
    """
    Parse a string like "John,30,New York" and return a dictionary
    with keys: name, age, city
    
    Example:
        parse_person_data("John,30,New York") 
        -> {'name': 'John', 'age': 30, 'city': 'New York'}
    """
    # TODO: Use unpacking to parse the data
    # Hint: data_string.split(',')
    pass


# ============================================================================
# Exercise 9: Complex Challenge - Word Statistics
# ============================================================================
def analyze_text(text):
    """
    Analyze a text and return statistics as a dictionary:
    - total_words: total number of words
    - unique_words: number of unique words
    - most_common: the most common word and its count as a tuple (word, count)
    - word_lengths: a dict mapping each unique word to its length
    
    Example:
        text = "the cat and the dog"
        Result: {
            'total_words': 5,
            'unique_words': 4,
            'most_common': ('the', 2),
            'word_lengths': {'the': 3, 'cat': 3, 'and': 3, 'dog': 3}
        }
    """
    # TODO: Use Counter, dict comprehension, and other tools you've learned
    pass


# ============================================================================
# Exercise 10: Advanced Challenge - LRU Cache (simple version)
# ============================================================================
class SimpleCache:
    """
    Implement a simple Least Recently Used (LRU) cache.
    When the cache is full, remove the least recently used item.
    """
    
    def __init__(self, capacity):
        """Initialize cache with given capacity"""
        # TODO: Use deque to track usage order and dict to store values
        self.capacity = capacity
        self.cache = {}
        self.usage_order = deque()
    
    def get(self, key):
        """Get value by key, return None if not found"""
        # TODO: If key exists, update its position in usage_order
        pass
    
    def put(self, key, value):
        """Put key-value pair in cache"""
        # TODO: If cache is full, remove least recently used item
        # Add/update the item and track its usage
        pass


# ============================================================================
# TEST YOUR SOLUTIONS
# ============================================================================
if __name__ == "__main__":
    print("Testing your solutions...\n")
    
    # Test Exercise 1
    try:
        result = most_common_element([1, 2, 2, 3, 3, 3])
        print(f"✓ Exercise 1: {result == 3}")
    except:
        print("✗ Exercise 1: Not implemented or has errors")
    
    # Test Exercise 2
    try:
        students = [('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A')]
        result = group_by_grade(students)
        print(f"✓ Exercise 2: {result['A'] == ['Alice', 'Charlie']}")
    except:
        print("✗ Exercise 2: Not implemented or has errors")
    
    # Test Exercise 3
    try:
        browser = BrowserHistory()
        browser.visit("google.com")
        browser.visit("github.com")
        print(f"✓ Exercise 3: {len(browser.get_history()) == 2}")
    except:
        print("✗ Exercise 3: Not implemented or has errors")
    
    # Test Exercise 5
    try:
        result = get_even_squares([1, 2, 3, 4, 5])
        print(f"✓ Exercise 5: {result == [4, 16]}")
    except:
        print("✗ Exercise 5: Not implemented or has errors")
    
    # Test Exercise 6
    try:
        result = invert_dict({'a': 1, 'b': 2})
        print(f"✓ Exercise 6: {result == {1: 'a', 2: 'b'}}")
    except:
        print("✗ Exercise 6: Not implemented or has errors")
    
    print("\n" + "="*60)
    print("Complete all exercises, then check solutions.py")
    print("="*60)

