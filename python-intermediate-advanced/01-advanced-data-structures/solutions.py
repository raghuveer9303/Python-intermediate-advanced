"""
Module 01: Advanced Data Structures - Solutions

Compare your solutions with these after you've attempted the exercises!
"""

from collections import Counter, defaultdict, deque, namedtuple


# ============================================================================
# Exercise 1: Counter - Find the most common element
# ============================================================================
def most_common_element(items):
    """
    Given a list of items, return the most common element.
    """
    counter = Counter(items)
    return counter.most_common(1)[0][0]


# ============================================================================
# Exercise 2: defaultdict - Group students by grade
# ============================================================================
def group_by_grade(students):
    """
    Given a list of tuples (name, grade), group students by their grade.
    """
    grouped = defaultdict(list)
    for name, grade in students:
        grouped[grade].append(name)
    return dict(grouped)


# ============================================================================
# Exercise 3: deque - Implement a simple browser history
# ============================================================================
class BrowserHistory:
    """
    Implement a browser history with forward and back functionality.
    Keep only the last 5 visited pages.
    """
    
    def __init__(self):
        self.history = deque(maxlen=5)
    
    def visit(self, url):
        """Visit a new URL"""
        self.history.append(url)
    
    def get_history(self):
        """Return current history as a list"""
        return list(self.history)


# ============================================================================
# Exercise 4: namedtuple - Create a Book record
# ============================================================================
Book = namedtuple('Book', ['title', 'author', 'year', 'isbn'])

def create_book(title, author, year, isbn):
    """Create and return a Book namedtuple"""
    return Book(title, author, year, isbn)


# ============================================================================
# Exercise 5: List Comprehension - Filter and transform
# ============================================================================
def get_even_squares(numbers):
    """
    Return a list of squares of even numbers only.
    """
    return [x**2 for x in numbers if x % 2 == 0]


# ============================================================================
# Exercise 6: Dict Comprehension - Invert a dictionary
# ============================================================================
def invert_dict(d):
    """
    Invert a dictionary (swap keys and values).
    """
    return {value: key for key, value in d.items()}


# ============================================================================
# Exercise 7: Nested Comprehension - Matrix transpose
# ============================================================================
def transpose_matrix(matrix):
    """
    Transpose a matrix (swap rows and columns).
    """
    if not matrix:
        return []
    return [[matrix[j][i] for j in range(len(matrix))] 
            for i in range(len(matrix[0]))]


# ============================================================================
# Exercise 8: Unpacking - Parse CSV-like data
# ============================================================================
def parse_person_data(data_string):
    """
    Parse a string like "John,30,New York" and return a dictionary.
    """
    name, age, city = data_string.split(',')
    return {
        'name': name,
        'age': int(age),
        'city': city
    }


# ============================================================================
# Exercise 9: Complex Challenge - Word Statistics
# ============================================================================
def analyze_text(text):
    """
    Analyze a text and return comprehensive statistics.
    """
    words = text.lower().split()
    word_counter = Counter(words)
    
    return {
        'total_words': len(words),
        'unique_words': len(set(words)),
        'most_common': word_counter.most_common(1)[0],
        'word_lengths': {word: len(word) for word in set(words)}
    }


# ============================================================================
# Exercise 10: Advanced Challenge - LRU Cache (simple version)
# ============================================================================
class SimpleCache:
    """
    Implement a simple Least Recently Used (LRU) cache.
    """
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.usage_order = deque()
    
    def get(self, key):
        """Get value by key, return None if not found"""
        if key not in self.cache:
            return None
        
        # Move to end (most recently used)
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache[key]
    
    def put(self, key, value):
        """Put key-value pair in cache"""
        if key in self.cache:
            # Update existing key
            self.usage_order.remove(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used
            lru_key = self.usage_order.popleft()
            del self.cache[lru_key]
        
        # Add/update key
        self.cache[key] = value
        self.usage_order.append(key)


# ============================================================================
# DEMONSTRATION
# ============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("SOLUTIONS DEMONSTRATION")
    print("=" * 60)
    print()
    
    # Test Exercise 1
    print("Exercise 1: Most common element")
    print(f"Result: {most_common_element([1, 2, 2, 3, 3, 3])}")
    print()
    
    # Test Exercise 2
    print("Exercise 2: Group by grade")
    students = [('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A'), ('David', 'B')]
    print(f"Result: {group_by_grade(students)}")
    print()
    
    # Test Exercise 3
    print("Exercise 3: Browser history")
    browser = BrowserHistory()
    for url in ['google.com', 'github.com', 'stackoverflow.com']:
        browser.visit(url)
    print(f"History: {browser.get_history()}")
    print()
    
    # Test Exercise 4
    print("Exercise 4: Book namedtuple")
    book = create_book("Python Crash Course", "Eric Matthes", 2019, "978-1593279288")
    print(f"Book: {book.title} by {book.author}")
    print()
    
    # Test Exercise 5
    print("Exercise 5: Even squares")
    print(f"Result: {get_even_squares([1, 2, 3, 4, 5, 6])}")
    print()
    
    # Test Exercise 6
    print("Exercise 6: Invert dictionary")
    print(f"Result: {invert_dict({'a': 1, 'b': 2, 'c': 3})}")
    print()
    
    # Test Exercise 7
    print("Exercise 7: Transpose matrix")
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(f"Original: {matrix}")
    print(f"Transposed: {transpose_matrix(matrix)}")
    print()
    
    # Test Exercise 8
    print("Exercise 8: Parse person data")
    print(f"Result: {parse_person_data('John,30,New York')}")
    print()
    
    # Test Exercise 9
    print("Exercise 9: Text analysis")
    text = "the cat and the dog and the bird"
    print(f"Result: {analyze_text(text)}")
    print()
    
    # Test Exercise 10
    print("Exercise 10: Simple LRU Cache")
    cache = SimpleCache(capacity=3)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)
    print(f"Get 'a': {cache.get('a')}")
    cache.put('d', 4)  # This should evict 'b'
    print(f"Get 'b' (evicted): {cache.get('b')}")
    print(f"Get 'c': {cache.get('c')}")
    print()
    
    print("=" * 60)
    print("All solutions demonstrated successfully!")
    print("=" * 60)

