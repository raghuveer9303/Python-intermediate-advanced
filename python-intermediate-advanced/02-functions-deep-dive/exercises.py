"""
Module 02: Functions Deep Dive - Exercises

Complete these exercises to practice what you've learned!
"""

from functools import wraps
import time


# ============================================================================
# Exercise 1: First-Class Functions - Create a calculator
# ============================================================================
def create_calculator():
    """
    Return a dictionary mapping operation names to functions.
    Operations: 'add', 'subtract', 'multiply', 'divide'
    
    Example:
        calc = create_calculator()
        calc['add'](5, 3) -> 8
        calc['multiply'](4, 2) -> 8
    """
    # TODO: Define four functions and return them in a dict
    pass


# ============================================================================
# Exercise 2: Closure - Create a password validator
# ============================================================================
def create_password_validator(min_length):
    """
    Create a function that validates passwords based on minimum length.
    The returned function should check if a password meets the requirement.
    
    Example:
        validate = create_password_validator(8)
        validate("short") -> False
        validate("longenough") -> True
    """
    # TODO: Create and return a closure
    pass


# ============================================================================
# Exercise 3: Closure with State - Account balance
# ============================================================================
def create_account(initial_balance):
    """
    Create an account with deposit and withdraw functions.
    Return a dict with 'deposit', 'withdraw', and 'balance' functions.
    
    Example:
        account = create_account(100)
        account['deposit'](50) -> 150
        account['withdraw'](30) -> 120
        account['balance']() -> 120
    """
    # TODO: Use closure to maintain state
    pass


# ============================================================================
# Exercise 4: Simple Decorator - Logging
# ============================================================================
def log_calls(func):
    """
    Decorator that prints when a function is called and what it returns.
    
    Example output:
        Calling function_name with args: (1, 2) kwargs: {}
        function_name returned: 3
    """
    # TODO: Implement the decorator
    pass


# ============================================================================
# Exercise 5: Decorator with Arguments - Validate input
# ============================================================================
def validate_positive(func):
    """
    Decorator that ensures all numeric arguments are positive.
    Raise ValueError if any argument is negative.
    
    Example:
        @validate_positive
        def add(a, b):
            return a + b
        
        add(5, 3) -> 8
        add(-5, 3) -> ValueError
    """
    # TODO: Implement the decorator
    pass


# ============================================================================
# Exercise 6: Stacking Decorators - Combine multiple decorators
# ============================================================================
# TODO: Create two decorators:
# 1. @timing - measures execution time
# 2. @debug - prints function name and arguments before execution

def timing(func):
    """Decorator that times function execution"""
    # TODO: Implement
    pass

def debug(func):
    """Decorator that prints debug info"""
    # TODO: Implement
    pass

# Test function (uncomment after implementing decorators)
# @timing
# @debug
# def test_function(n):
#     time.sleep(0.1)
#     return n * 2


# ============================================================================
# Exercise 7: Lambda - Sort complex data
# ============================================================================
def sort_students(students):
    """
    Sort a list of student dictionaries by grade (descending), then by name.
    Each student: {'name': str, 'grade': float}
    
    Example:
        students = [
            {'name': 'Alice', 'grade': 85.5},
            {'name': 'Bob', 'grade': 92.0},
            {'name': 'Charlie', 'grade': 85.5}
        ]
        Result: Bob, Alice, Charlie
    """
    # TODO: Use sorted() with a lambda function
    pass


# ============================================================================
# Exercise 8: Map, Filter, Reduce - Data processing
# ============================================================================
def process_numbers(numbers):
    """
    Given a list of numbers:
    1. Square all numbers (map)
    2. Keep only even squares (filter)
    3. Sum the results (reduce)
    
    Example:
        process_numbers([1, 2, 3, 4]) -> 20
        (squares: [1, 4, 9, 16] -> evens: [4, 16] -> sum: 20)
    """
    # TODO: Use map, filter, and reduce
    from functools import reduce
    pass


# ============================================================================
# Exercise 9: Memoization - Cache expensive function
# ============================================================================
def memoize(func):
    """
    Create a memoization decorator that caches function results.
    
    Example:
        @memoize
        def expensive(n):
            # ... expensive computation ...
            return result
    """
    # TODO: Implement memoization decorator
    pass


# ============================================================================
# Exercise 10: Advanced - Decorator Factory
# ============================================================================
def repeat_on_exception(max_retries=3, delay=0.1):
    """
    Decorator that retries a function if it raises an exception.
    
    Args:
        max_retries: Maximum number of retry attempts
        delay: Seconds to wait between retries
    
    Example:
        @repeat_on_exception(max_retries=3, delay=0.5)
        def unstable_function():
            # might fail
            pass
    """
    # TODO: Implement decorator factory
    pass


# ============================================================================
# Exercise 11: Advanced - Function Composition
# ============================================================================
def compose(*functions):
    """
    Compose multiple functions into one.
    The functions are applied from right to left.
    
    Example:
        def add_one(x): return x + 1
        def double(x): return x * 2
        def square(x): return x ** 2
        
        f = compose(add_one, double, square)
        f(3) -> (3^2 * 2) + 1 = 19
    """
    # TODO: Implement function composition
    pass


# ============================================================================
# Exercise 12: Challenge - Rate Limiter Decorator
# ============================================================================
def rate_limit(max_calls, time_window):
    """
    Decorator that limits how often a function can be called.
    
    Args:
        max_calls: Maximum number of calls allowed
        time_window: Time window in seconds
    
    Example:
        @rate_limit(max_calls=3, time_window=1.0)
        def api_call():
            return "Success"
        
        # Can call 3 times within 1 second, 4th call raises exception
    """
    # TODO: Implement rate limiter
    # Hint: Use time.time() and a list to track call times
    pass


# ============================================================================
# TEST YOUR SOLUTIONS
# ============================================================================
if __name__ == "__main__":
    print("Testing your solutions...\n")
    
    # Test Exercise 1
    try:
        calc = create_calculator()
        assert calc['add'](5, 3) == 8
        print("✓ Exercise 1: Passed")
    except:
        print("✗ Exercise 1: Not implemented or has errors")
    
    # Test Exercise 2
    try:
        validate = create_password_validator(8)
        assert validate("short") == False
        assert validate("longenough") == True
        print("✓ Exercise 2: Passed")
    except:
        print("✗ Exercise 2: Not implemented or has errors")
    
    # Test Exercise 3
    try:
        account = create_account(100)
        assert account['deposit'](50) == 150
        assert account['withdraw'](30) == 120
        print("✓ Exercise 3: Passed")
    except:
        print("✗ Exercise 3: Not implemented or has errors")
    
    # Test Exercise 7
    try:
        students = [
            {'name': 'Alice', 'grade': 85.5},
            {'name': 'Bob', 'grade': 92.0},
            {'name': 'Charlie', 'grade': 85.5}
        ]
        result = sort_students(students)
        assert result[0]['name'] == 'Bob'
        print("✓ Exercise 7: Passed")
    except:
        print("✗ Exercise 7: Not implemented or has errors")
    
    print("\n" + "="*60)
    print("Complete all exercises, then check solutions.py")
    print("="*60)

