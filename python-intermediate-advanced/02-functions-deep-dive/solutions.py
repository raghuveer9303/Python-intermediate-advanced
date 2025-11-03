"""
Module 02: Functions Deep Dive - Solutions

Compare your solutions with these after you've attempted the exercises!
"""

from functools import wraps, reduce
import time


# ============================================================================
# Exercise 1: First-Class Functions - Create a calculator
# ============================================================================
def create_calculator():
    """Return a dictionary mapping operation names to functions."""
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    return {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }


# ============================================================================
# Exercise 2: Closure - Create a password validator
# ============================================================================
def create_password_validator(min_length):
    """Create a function that validates passwords based on minimum length."""
    def validate(password):
        return len(password) >= min_length
    return validate


# ============================================================================
# Exercise 3: Closure with State - Account balance
# ============================================================================
def create_account(initial_balance):
    """Create an account with deposit and withdraw functions."""
    balance = initial_balance
    
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            raise ValueError("Insufficient funds")
        balance -= amount
        return balance
    
    def get_balance():
        return balance
    
    return {
        'deposit': deposit,
        'withdraw': withdraw,
        'balance': get_balance
    }


# ============================================================================
# Exercise 4: Simple Decorator - Logging
# ============================================================================
def log_calls(func):
    """Decorator that prints when a function is called and what it returns."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper


# ============================================================================
# Exercise 5: Decorator with Arguments - Validate input
# ============================================================================
def validate_positive(func):
    """Decorator that ensures all numeric arguments are positive."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument {arg} must be positive")
        for value in kwargs.values():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"Argument {value} must be positive")
        return func(*args, **kwargs)
    return wrapper


# ============================================================================
# Exercise 6: Stacking Decorators - Combine multiple decorators
# ============================================================================
def timing(func):
    """Decorator that times function execution"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

def debug(func):
    """Decorator that prints debug info"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"DEBUG: Calling {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper


# ============================================================================
# Exercise 7: Lambda - Sort complex data
# ============================================================================
def sort_students(students):
    """Sort students by grade (descending), then by name."""
    return sorted(students, key=lambda s: (-s['grade'], s['name']))


# ============================================================================
# Exercise 8: Map, Filter, Reduce - Data processing
# ============================================================================
def process_numbers(numbers):
    """Square all numbers, keep evens, sum them."""
    # Square all numbers
    squared = map(lambda x: x ** 2, numbers)
    
    # Keep only even squares
    evens = filter(lambda x: x % 2 == 0, squared)
    
    # Sum the results
    total = reduce(lambda x, y: x + y, evens, 0)
    
    return total


# ============================================================================
# Exercise 9: Memoization - Cache expensive function
# ============================================================================
def memoize(func):
    """Create a memoization decorator that caches function results."""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrapper


# ============================================================================
# Exercise 10: Advanced - Decorator Factory
# ============================================================================
def repeat_on_exception(max_retries=3, delay=0.1):
    """Decorator that retries a function if it raises an exception."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < max_retries - 1:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator


# ============================================================================
# Exercise 11: Advanced - Function Composition
# ============================================================================
def compose(*functions):
    """Compose multiple functions into one (right to left)."""
    def composed(x):
        result = x
        for func in reversed(functions):
            result = func(result)
        return result
    return composed


# ============================================================================
# Exercise 12: Challenge - Rate Limiter Decorator
# ============================================================================
def rate_limit(max_calls, time_window):
    """Decorator that limits how often a function can be called."""
    def decorator(func):
        call_times = []
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_times
            current_time = time.time()
            
            # Remove old calls outside the time window
            call_times = [t for t in call_times if current_time - t < time_window]
            
            # Check if we've hit the limit
            if len(call_times) >= max_calls:
                raise Exception(f"Rate limit exceeded: {max_calls} calls per {time_window}s")
            
            # Record this call
            call_times.append(current_time)
            
            return func(*args, **kwargs)
        
        return wrapper
    return decorator


# ============================================================================
# DEMONSTRATION
# ============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("SOLUTIONS DEMONSTRATION")
    print("=" * 60)
    print()
    
    # Test Exercise 1
    print("Exercise 1: Calculator")
    calc = create_calculator()
    print(f"5 + 3 = {calc['add'](5, 3)}")
    print(f"10 - 4 = {calc['subtract'](10, 4)}")
    print()
    
    # Test Exercise 2
    print("Exercise 2: Password Validator")
    validate = create_password_validator(8)
    print(f"'short' is valid? {validate('short')}")
    print(f"'longenough' is valid? {validate('longenough')}")
    print()
    
    # Test Exercise 3
    print("Exercise 3: Account")
    account = create_account(100)
    print(f"Initial balance: {account['balance']()}")
    print(f"After deposit 50: {account['deposit'](50)}")
    print(f"After withdraw 30: {account['withdraw'](30)}")
    print()
    
    # Test Exercise 4
    print("Exercise 4: Log Decorator")
    @log_calls
    def add(a, b):
        return a + b
    
    result = add(5, 3)
    print()
    
    # Test Exercise 5
    print("Exercise 5: Validate Positive")
    @validate_positive
    def multiply(a, b):
        return a * b
    
    print(f"5 * 3 = {multiply(5, 3)}")
    try:
        multiply(-5, 3)
    except ValueError as e:
        print(f"Error caught: {e}")
    print()
    
    # Test Exercise 6
    print("Exercise 6: Stacking Decorators")
    @timing
    @debug
    def slow_add(a, b):
        time.sleep(0.1)
        return a + b
    
    result = slow_add(5, 3)
    print()
    
    # Test Exercise 7
    print("Exercise 7: Sort Students")
    students = [
        {'name': 'Alice', 'grade': 85.5},
        {'name': 'Bob', 'grade': 92.0},
        {'name': 'Charlie', 'grade': 85.5}
    ]
    sorted_students = sort_students(students)
    print("Sorted:")
    for s in sorted_students:
        print(f"  {s['name']}: {s['grade']}")
    print()
    
    # Test Exercise 8
    print("Exercise 8: Process Numbers")
    result = process_numbers([1, 2, 3, 4])
    print(f"Result: {result}")
    print()
    
    # Test Exercise 9
    print("Exercise 9: Memoization")
    @memoize
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    print(f"Fibonacci(30): {fibonacci(30)}")
    print()
    
    # Test Exercise 11
    print("Exercise 11: Function Composition")
    def add_one(x):
        return x + 1
    
    def double(x):
        return x * 2
    
    def square(x):
        return x ** 2
    
    f = compose(add_one, double, square)
    print(f"compose(add_one, double, square)(3) = {f(3)}")
    print()
    
    # Test Exercise 12
    print("Exercise 12: Rate Limiter")
    @rate_limit(max_calls=3, time_window=1.0)
    def api_call():
        return "Success"
    
    for i in range(3):
        print(f"Call {i + 1}: {api_call()}")
    
    try:
        api_call()  # This should fail
    except Exception as e:
        print(f"4th call failed: {e}")
    print()
    
    print("=" * 60)
    print("All solutions demonstrated successfully!")
    print("=" * 60)

