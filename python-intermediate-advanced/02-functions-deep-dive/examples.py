"""
Module 02: Functions Deep Dive - Examples

Type each example, run it, and experiment!
"""

# ============================================================================
# 1. FIRST-CLASS FUNCTIONS - Functions are objects!
# ============================================================================
print("=" * 60)
print("1. FIRST-CLASS FUNCTIONS")
print("=" * 60)

# Example 1: Assign function to a variable
def greet(name):
    return f"Hello, {name}!"

say_hello = greet  # Assign function to variable
print(f"Direct call: {greet('Alice')}")
print(f"Variable call: {say_hello('Bob')}")
print(f"Function type: {type(greet)}")
print()

# Example 2: Pass function as argument
def execute_twice(func, arg):
    """Execute a function twice with the same argument"""
    print(func(arg))
    print(func(arg))

execute_twice(greet, "Charlie")
print()

# Example 3: Return function from function
def create_multiplier(n):
    """Create a function that multiplies by n"""
    def multiplier(x):
        return x * n
    return multiplier

times_3 = create_multiplier(3)
times_5 = create_multiplier(5)
print(f"3 * 10 = {times_3(10)}")
print(f"5 * 10 = {times_5(10)}")
print()

# Example 4: Store functions in data structures
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

operations = {
    'add': add,
    'sub': subtract,
    'mul': multiply
}

print(f"5 + 3 = {operations['add'](5, 3)}")
print(f"5 - 3 = {operations['sub'](5, 3)}")
print(f"5 * 3 = {operations['mul'](5, 3)}")
print()


# ============================================================================
# 2. CLOSURES - Functions that remember their environment
# ============================================================================
print("=" * 60)
print("2. CLOSURES")
print("=" * 60)

# Example 1: Basic closure
def outer(x):
    def inner(y):
        return x + y  # 'x' is captured from outer scope
    return inner

add_5 = outer(5)
add_10 = outer(10)
print(f"add_5(3) = {add_5(3)}")
print(f"add_10(3) = {add_10(3)}")
print()

# Example 2: Closure with state
def make_counter():
    count = 0  # This variable is enclosed
    
    def increment():
        nonlocal count  # Modify the enclosed variable
        count += 1
        return count
    
    return increment

counter1 = make_counter()
counter2 = make_counter()
print(f"Counter1: {counter1()}, {counter1()}, {counter1()}")
print(f"Counter2: {counter2()}, {counter2()}")
print()

# Example 3: Practical use - Configuration
def create_logger(prefix):
    def log(message):
        print(f"[{prefix}] {message}")
    return log

error_log = create_logger("ERROR")
info_log = create_logger("INFO")
error_log("Something went wrong!")
info_log("Application started")
print()

# Example 4: LEGB Rule (Local, Enclosing, Global, Built-in)
x = "global"

def outer_func():
    x = "enclosing"
    
    def inner_func():
        x = "local"
        print(f"Local x: {x}")
    
    inner_func()
    print(f"Enclosing x: {x}")

outer_func()
print(f"Global x: {x}")
print()


# ============================================================================
# 3. DECORATORS - Modify function behavior
# ============================================================================
print("=" * 60)
print("3. DECORATORS")
print("=" * 60)

# Example 1: Simple decorator
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet_person(name):
    return f"hello, {name}"

print(f"Decorated: {greet_person('alice')}")
print()

# Example 2: Timing decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "Done!"

result = slow_function()
print()

# Example 3: Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")
    return "done"

say_hello("Bob")
print()

# Example 4: Multiple decorators (stacking)
def bold(func):
    def wrapper(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return "<i>" + func(*args, **kwargs) + "</i>"
    return wrapper

@bold
@italic
def styled_text():
    return "Hello World"

print(f"Styled: {styled_text()}")
print()

# Example 5: Preserving metadata with functools.wraps
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def important_function():
    """This is an important function"""
    return "Result"

print(f"Name: {important_function.__name__}")
print(f"Doc: {important_function.__doc__}")
print()


# ============================================================================
# 4. LAMBDA FUNCTIONS - Anonymous functions
# ============================================================================
print("=" * 60)
print("4. LAMBDA FUNCTIONS")
print("=" * 60)

# Example 1: Basic lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")
print()

# Example 2: Lambda with multiple arguments
add_nums = lambda a, b: a + b
print(f"3 + 7 = {add_nums(3, 7)}")
print()

# Example 3: Lambda with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {squared}")
print()

# Example 4: Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")
print()

# Example 5: Lambda in sorting
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]
sorted_by_age = sorted(people, key=lambda person: person['age'])
print("Sorted by age:")
for person in sorted_by_age:
    print(f"  {person['name']}: {person['age']}")
print()

# Example 6: Lambda with reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of {numbers}: {product}")
print()


# ============================================================================
# 5. *ARGS and **KWARGS - Variable arguments
# ============================================================================
print("=" * 60)
print("5. *ARGS and **KWARGS")
print("=" * 60)

# Example 1: *args - Variable positional arguments
def sum_all(*args):
    """Sum any number of arguments"""
    return sum(args)

print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")
print()

# Example 2: **kwargs - Variable keyword arguments
def print_info(**kwargs):
    """Print all keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
print()

# Example 3: Combining positional, *args, and **kwargs
def complex_function(required, *args, default=10, **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

complex_function("must have", 1, 2, 3, default=20, extra1="hello", extra2="world")
print()


# ============================================================================
# 6. PARTIAL FUNCTIONS - Pre-fill arguments
# ============================================================================
print("=" * 60)
print("6. PARTIAL FUNCTIONS")
print("=" * 60)

from functools import partial

# Example 1: Create specialized functions
def power(base, exponent):
    return base ** exponent

square_func = partial(power, exponent=2)
cube_func = partial(power, exponent=3)

print(f"5 squared: {square_func(5)}")
print(f"5 cubed: {cube_func(5)}")
print()


# ============================================================================
# 7. RECURSION - Functions calling themselves
# ============================================================================
print("=" * 60)
print("7. RECURSION")
print("=" * 60)

# Example 1: Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")
print()

# Example 2: Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"First 10 Fibonacci: {[fibonacci(i) for i in range(10)]}")
print()


# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("8. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Memoization decorator
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def slow_fibonacci(n):
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

print(f"Fibonacci(30) with memoization: {slow_fibonacci(30)}")
print()

# Example 2: Retry decorator
def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt == max_attempts - 1:
                        raise
        return wrapper
    return decorator

@retry(max_attempts=3)
def unreliable_function(should_fail=False):
    if should_fail:
        raise ValueError("Something went wrong")
    return "Success!"

print(f"Result: {unreliable_function(should_fail=False)}")
print()

# Example 3: Function factory
def create_validator(min_val, max_val):
    def validate(value):
        return min_val <= value <= max_val
    return validate

age_validator = create_validator(0, 120)
temperature_validator = create_validator(-50, 50)

print(f"Age 25 valid? {age_validator(25)}")
print(f"Age 150 valid? {age_validator(150)}")
print(f"Temp -10 valid? {temperature_validator(-10)}")
print()

print("=" * 60)
print("Great job! Now try the exercises in exercises.py")
print("=" * 60)

