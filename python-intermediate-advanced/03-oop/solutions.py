"""
Module 03: Object-Oriented Programming - Solutions

Compare your solutions with these after you've attempted the exercises!
"""

from abc import ABC, abstractmethod
from datetime import date as dt_date


# ============================================================================
# Exercise 1: Basic Class - Create a Book class
# ============================================================================
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def read(self):
        print(f"Reading {self.title}")
    
    @property
    def is_long(self):
        return self.pages > 300


# ============================================================================
# Exercise 2: Class Variables - Track all instances
# ============================================================================
class Car:
    total_cars = 0
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.total_cars += 1
    
    @classmethod
    def get_total_cars(cls):
        return cls.total_cars


# ============================================================================
# Exercise 3: Inheritance - Create an animal hierarchy
# ============================================================================
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


# ============================================================================
# Exercise 4: Magic Methods - Create a Money class
# ============================================================================
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency
    
    def __str__(self):
        return f"{self.amount} {self.currency}"
    
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"
    
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)
    
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency
    
    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies")
        return self.amount < other.amount
    
    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies")
        return self.amount > other.amount


# ============================================================================
# Exercise 5: Container Magic Methods - Stack implementation
# ============================================================================
class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        if not self._items:
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def __len__(self):
        return len(self._items)
    
    def __str__(self):
        return f"Stack({self._items})"
    
    def __bool__(self):
        return len(self._items) > 0


# ============================================================================
# Exercise 6: Properties - Rectangle with validation
# ============================================================================
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
    
    @property
    def area(self):
        return self._width * self._height
    
    @property
    def perimeter(self):
        return 2 * (self._width + self._height)


# ============================================================================
# Exercise 7: Private Attributes - Password Manager
# ============================================================================
class PasswordManager:
    def __init__(self, master_password):
        self.__master_password = master_password
        self.__passwords = {}
    
    def add_password(self, service, password, master_pass):
        if master_pass != self.__master_password:
            raise ValueError("Invalid master password")
        self.__passwords[service] = password
    
    def get_password(self, service, master_pass):
        if master_pass != self.__master_password:
            raise ValueError("Invalid master password")
        return self.__passwords.get(service, "Service not found")


# ============================================================================
# Exercise 8: Abstract Base Class - Payment System
# ============================================================================
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCard(Payment):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card ending in {self.card_number[-4:]}"

class PayPal(Payment):
    def __init__(self, email):
        self.email = email
    
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal account {self.email}"

class Cash(Payment):
    def process_payment(self, amount):
        return f"Processing ${amount} in cash"


# ============================================================================
# Exercise 9: Class Methods - Date Parser
# ============================================================================
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        today = dt_date.today()
        return cls(today.year, today.month, today.day)
    
    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"


# ============================================================================
# Exercise 10: Advanced - Bank Account System
# ============================================================================
class Account:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self._balance = initial_balance
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

class SavingsAccount(Account):
    def __init__(self, account_number, initial_balance=0, interest_rate=0.01):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest)

class CheckingAccount(Account):
    def __init__(self, account_number, initial_balance=0, overdraft_limit=100):
        super().__init__(account_number, initial_balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit:
            raise ValueError("Exceeds overdraft limit")
        self._balance -= amount


# ============================================================================
# Exercise 11: Multiple Inheritance - Smart Device
# ============================================================================
class NetworkEnabled:
    def connect(self):
        return "Connected to network"
    
    def disconnect(self):
        return "Disconnected from network"

class BatteryPowered:
    def __init__(self):
        self._battery_level = 100
    
    def charge(self):
        self._battery_level = 100
        return "Fully charged"
    
    @property
    def battery_level(self):
        return self._battery_level

class SmartPhone(NetworkEnabled, BatteryPowered):
    def __init__(self, brand, model):
        BatteryPowered.__init__(self)
        self.brand = brand
        self.model = model
    
    def make_call(self):
        if self._battery_level > 0:
            self._battery_level -= 5
            return "Calling..."
        return "Battery dead"


# ============================================================================
# Exercise 12: Challenge - Library Management System
# ============================================================================
class Item:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self._is_available = True
    
    @property
    def is_available(self):
        return self._is_available
    
    def checkout(self):
        if not self._is_available:
            return False
        self._is_available = False
        return True
    
    def return_item(self):
        self._is_available = True
    
    def __str__(self):
        status = "Available" if self._is_available else "Checked out"
        return f"{self.title} ({self.item_id}) - {status}"

class Book(Item):
    def __init__(self, title, item_id, author, isbn):
        super().__init__(title, item_id)
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        return f"Book: {super().__str__()} by {self.author}"

class DVD(Item):
    def __init__(self, title, item_id, duration, director):
        super().__init__(title, item_id)
        self.duration = duration
        self.director = director
    
    def __str__(self):
        return f"DVD: {super().__str__()} directed by {self.director}"

class Library:
    def __init__(self):
        self._items = {}
    
    def add_item(self, item):
        self._items[item.item_id] = item
    
    def remove_item(self, item_id):
        if item_id in self._items:
            del self._items[item_id]
            return True
        return False
    
    def checkout_item(self, item_id):
        if item_id not in self._items:
            return "Item not found"
        return self._items[item_id].checkout()
    
    def return_item(self, item_id):
        if item_id not in self._items:
            return "Item not found"
        self._items[item_id].return_item()
        return True
    
    def search(self, query):
        results = []
        query_lower = query.lower()
        for item in self._items.values():
            if query_lower in item.title.lower():
                results.append(item)
        return results
    
    def list_items(self):
        return list(self._items.values())


# ============================================================================
# DEMONSTRATION
# ============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("SOLUTIONS DEMONSTRATION")
    print("=" * 60)
    print()
    
    # Exercise 1
    print("Exercise 1: Book Class")
    book = Book("Python Mastery", "John Doe", 350)
    book.read()
    print(f"Is long book? {book.is_long}")
    print()
    
    # Exercise 2
    print("Exercise 2: Car Class")
    car1 = Car("Toyota", "Camry", 2020)
    car2 = Car("Honda", "Civic", 2021)
    print(f"Total cars: {Car.get_total_cars()}")
    print()
    
    # Exercise 3
    print("Exercise 3: Animal Hierarchy")
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    print(f"{dog.name} says: {dog.speak()}")
    print(f"{cat.name} says: {cat.speak()}")
    print()
    
    # Exercise 4
    print("Exercise 4: Money Class")
    m1 = Money(100)
    m2 = Money(50)
    print(f"m1: {m1}")
    print(f"m2: {m2}")
    print(f"m1 + m2: {m1 + m2}")
    print(f"m1 > m2: {m1 > m2}")
    print()
    
    # Exercise 5
    print("Exercise 5: Stack")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack: {stack}")
    print(f"Length: {len(stack)}")
    print(f"Pop: {stack.pop()}")
    print()
    
    # Exercise 6
    print("Exercise 6: Rectangle")
    rect = Rectangle(5, 3)
    print(f"Rectangle {rect.width}x{rect.height}")
    print(f"Area: {rect.area}")
    print(f"Perimeter: {rect.perimeter}")
    print()
    
    # Exercise 8
    print("Exercise 8: Payment System")
    cc = CreditCard("1234567890123456")
    paypal = PayPal("user@example.com")
    print(cc.process_payment(100))
    print(paypal.process_payment(50))
    print()
    
    # Exercise 10
    print("Exercise 10: Bank Accounts")
    savings = SavingsAccount("SA001", 1000, 0.05)
    savings.add_interest()
    print(f"Savings balance after interest: ${savings.balance}")
    
    checking = CheckingAccount("CA001", 100, 50)
    checking.withdraw(120)  # Uses overdraft
    print(f"Checking balance: ${checking.balance}")
    print()
    
    # Exercise 12
    print("Exercise 12: Library System")
    library = Library()
    library.add_item(Book("1984", "B001", "George Orwell", "123456"))
    library.add_item(Book("To Kill a Mockingbird", "B002", "Harper Lee", "234567"))
    library.add_item(DVD("Inception", "D001", 148, "Christopher Nolan"))
    
    print("Library items:")
    for item in library.list_items():
        print(f"  {item}")
    
    print("\nSearch for '1984':")
    for item in library.search("1984"):
        print(f"  Found: {item}")
    
    print("\nCheckout 'B001':")
    library.checkout_item("B001")
    for item in library.list_items():
        print(f"  {item}")
    print()
    
    print("=" * 60)
    print("All solutions demonstrated successfully!")
    print("=" * 60)

