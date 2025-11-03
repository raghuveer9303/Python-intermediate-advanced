"""
Module 03: Object-Oriented Programming - Exercises

Complete these exercises to practice what you've learned!
"""

from abc import ABC, abstractmethod


# ============================================================================
# Exercise 1: Basic Class - Create a Book class
# ============================================================================
# TODO: Create a Book class with:
# - __init__(self, title, author, pages)
# - A method read() that prints "Reading {title}"
# - A property is_long that returns True if pages > 300


# ============================================================================
# Exercise 2: Class Variables - Track all instances
# ============================================================================
# TODO: Create a Car class that:
# - Tracks total number of cars created (class variable)
# - Has instance variables: make, model, year
# - Has a class method get_total_cars()


# ============================================================================
# Exercise 3: Inheritance - Create an animal hierarchy
# ============================================================================
# TODO: Create:
# - Animal base class with name and speak() method
# - Dog class that inherits from Animal, overrides speak() to return "Woof!"
# - Cat class that inherits from Animal, overrides speak() to return "Meow!"


# ============================================================================
# Exercise 4: Magic Methods - Create a Money class
# ============================================================================
# TODO: Create a Money class with:
# - __init__(self, amount, currency)
# - __str__ to return "X currency" (e.g., "100 USD")
# - __add__ to add two Money objects (same currency only)
# - __eq__ to compare Money objects
# - __lt__ and __gt__ for comparison


# ============================================================================
# Exercise 5: Container Magic Methods - Stack implementation
# ============================================================================
# TODO: Create a Stack class with:
# - __init__, push(item), pop()
# - __len__ to get stack size
# - __str__ to display stack
# - __bool__ to check if stack is empty


# ============================================================================
# Exercise 6: Properties - Rectangle with validation
# ============================================================================
# TODO: Create a Rectangle class with:
# - width and height as properties (must be positive)
# - area property (computed, read-only)
# - perimeter property (computed, read-only)


# ============================================================================
# Exercise 7: Private Attributes - Password Manager
# ============================================================================
# TODO: Create a PasswordManager class with:
# - __init__(self, master_password)
# - Private __passwords dict
# - add_password(service, password, master_pass)
# - get_password(service, master_pass)
# - Only allow access with correct master password


# ============================================================================
# Exercise 8: Abstract Base Class - Payment System
# ============================================================================
# TODO: Create:
# - Payment abstract base class with abstract process_payment(amount)
# - CreditCard class implementing process_payment
# - PayPal class implementing process_payment
# - Cash class implementing process_payment


# ============================================================================
# Exercise 9: Class Methods - Date Parser
# ============================================================================
# TODO: Create a Date class with:
# - __init__(self, year, month, day)
# - @classmethod from_string(cls, date_string) - parse "YYYY-MM-DD"
# - @classmethod today(cls) - create Date for today
# - __str__ to display date


# ============================================================================
# Exercise 10: Advanced - Bank Account System
# ============================================================================
# TODO: Create a banking system with:
# - Account base class (account_number, balance)
# - SavingsAccount with interest_rate and add_interest() method
# - CheckingAccount with overdraft_limit
# - Both should override withdraw() with their own rules
# - Use properties for balance (read-only from outside)


# ============================================================================
# Exercise 11: Multiple Inheritance - Smart Device
# ============================================================================
# TODO: Create:
# - NetworkEnabled mixin with connect() and disconnect()
# - BatteryPowered mixin with charge() and battery_level
# - SmartPhone class that inherits from both


# ============================================================================
# Exercise 12: Challenge - Library Management System
# ============================================================================
# TODO: Create a complete library system:
# - Item base class (title, item_id, is_available)
# - Book(Item) with author, isbn
# - DVD(Item) with duration, director
# - Library class that manages items
# - Methods: add_item, remove_item, checkout_item, return_item, search
# - Use proper OOP principles (encapsulation, inheritance, etc.)


# ============================================================================
# TEST YOUR SOLUTIONS
# ============================================================================
if __name__ == "__main__":
    print("Testing your solutions...\n")
    
    # Test Exercise 1
    try:
        book = Book("Python Mastery", "John Doe", 350)
        assert book.title == "Python Mastery"
        assert book.is_long == True
        print("✓ Exercise 1: Passed")
    except:
        print("✗ Exercise 1: Not implemented or has errors")
    
    # Test Exercise 2
    try:
        car1 = Car("Toyota", "Camry", 2020)
        car2 = Car("Honda", "Civic", 2021)
        assert Car.get_total_cars() == 2
        print("✓ Exercise 2: Passed")
    except:
        print("✗ Exercise 2: Not implemented or has errors")
    
    # Test Exercise 3
    try:
        dog = Dog("Buddy")
        assert dog.speak() == "Woof!"
        print("✓ Exercise 3: Passed")
    except:
        print("✗ Exercise 3: Not implemented or has errors")
    
    print("\n" + "="*60)
    print("Complete all exercises, then check solutions.py")
    print("="*60)


# Add your class definitions below:

