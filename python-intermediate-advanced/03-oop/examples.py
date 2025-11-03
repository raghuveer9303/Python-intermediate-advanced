"""
Module 03: Object-Oriented Programming - Examples

Type each example, run it, and experiment!
"""

# ============================================================================
# 1. BASIC CLASSES AND OBJECTS
# ============================================================================
print("=" * 60)
print("1. BASIC CLASSES AND OBJECTS")
print("=" * 60)

# Example 1: Simple class
class Dog:
    """A simple Dog class"""
    
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Constructor - initialize instance variables"""
        self.name = name  # Instance variable
        self.age = age
    
    def bark(self):
        """Instance method"""
        return f"{self.name} says Woof!"
    
    def description(self):
        return f"{self.name} is {self.age} years old"

# Create instances
buddy = Dog("Buddy", 3)
max_dog = Dog("Max", 5)

print(f"Dog 1: {buddy.description()}")
print(f"Dog 2: {max_dog.description()}")
print(f"Species: {Dog.species}")
print(f"Buddy says: {buddy.bark()}")
print()


# ============================================================================
# 2. CLASS METHODS AND STATIC METHODS
# ============================================================================
print("=" * 60)
print("2. CLASS METHODS AND STATIC METHODS")
print("=" * 60)

class Person:
    population = 0  # Class variable
    
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        Person.population += 1
    
    # Instance method
    def get_age(self, current_year):
        return current_year - self.birth_year
    
    # Class method - works with the class, not instance
    @classmethod
    def get_population(cls):
        return f"Total population: {cls.population}"
    
    # Alternative constructor using class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, birth_year)
    
    # Static method - doesn't access instance or class
    @staticmethod
    def is_adult(age):
        return age >= 18

alice = Person("Alice", 1990)
bob = Person.from_birth_year("Bob", 1995)

print(f"Alice's age in 2024: {alice.get_age(2024)}")
print(Person.get_population())
print(f"Is 20 an adult? {Person.is_adult(20)}")
print()


# ============================================================================
# 3. INHERITANCE
# ============================================================================
print("=" * 60)
print("3. INHERITANCE")
print("=" * 60)

# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"
    
    def info(self):
        return f"I am {self.name}, a {self.__class__.__name__}"

# Child classes
class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name)  # Call parent constructor
        self.can_fly = can_fly
    
    def speak(self):
        return "Chirp!"

cat = Cat("Whiskers")
bird = Bird("Tweety")

print(f"{cat.name}: {cat.speak()}")
print(f"{bird.name}: {bird.speak()}")
print(f"Bird info: {bird.info()}")
print(f"Can fly? {bird.can_fly}")
print()


# ============================================================================
# 4. MAGIC METHODS (DUNDER METHODS)
# ============================================================================
print("=" * 60)
print("4. MAGIC METHODS")
print("=" * 60)

class Vector:
    """A simple 2D vector class with magic methods"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation for users"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """String representation for developers"""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Add two vectors"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        """Multiply vector by scalar"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Check equality"""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """Magnitude of vector"""
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"len(v1): {len(v1)}")
print(f"v1 == v2: {v1 == v2}")
print()


# ============================================================================
# 5. MORE MAGIC METHODS - Container-like behavior
# ============================================================================
print("=" * 60)
print("5. CONTAINER MAGIC METHODS")
print("=" * 60)

class Playlist:
    """A music playlist that acts like a list"""
    
    def __init__(self):
        self._songs = []
    
    def add_song(self, song):
        self._songs.append(song)
    
    def __len__(self):
        """len(playlist)"""
        return len(self._songs)
    
    def __getitem__(self, index):
        """playlist[index]"""
        return self._songs[index]
    
    def __setitem__(self, index, value):
        """playlist[index] = value"""
        self._songs[index] = value
    
    def __contains__(self, song):
        """song in playlist"""
        return song in self._songs
    
    def __iter__(self):
        """for song in playlist"""
        return iter(self._songs)

playlist = Playlist()
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")

print(f"Playlist length: {len(playlist)}")
print(f"First song: {playlist[0]}")
print(f"'Song A' in playlist: {'Song A' in playlist}")
print("All songs:")
for song in playlist:
    print(f"  - {song}")
print()


# ============================================================================
# 6. PROPERTIES - Computed attributes
# ============================================================================
print("=" * 60)
print("6. PROPERTIES")
print("=" * 60)

class Temperature:
    """Temperature class with Celsius and Fahrenheit"""
    
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set Celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get Fahrenheit (computed)"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set Fahrenheit"""
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")

temp.celsius = 0
print(f"After setting to 0°C: {temp.fahrenheit}°F")

temp.fahrenheit = 212
print(f"After setting to 212°F: {temp.celsius}°C")
print()


# ============================================================================
# 7. ENCAPSULATION - Private and protected attributes
# ============================================================================
print("=" * 60)
print("7. ENCAPSULATION")
print("=" * 60)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self._balance = balance     # Protected (convention)
        self.__pin = "1234"         # Private (name mangling)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount, pin):
        if pin != self.__pin:
            return "Invalid PIN"
        if amount <= self._balance:
            self._balance -= amount
            return "Success"
        return "Insufficient funds"
    
    def get_balance(self):
        return self._balance

account = BankAccount("Alice", 1000)
account.deposit(500)
print(f"Balance: ${account.get_balance()}")
print(f"Withdraw: {account.withdraw(200, '1234')}")
print(f"New balance: ${account.get_balance()}")

# Can access _balance (but shouldn't)
print(f"Protected _balance: ${account._balance}")

# Cannot access __pin directly (name mangling)
# print(account.__pin)  # This would raise AttributeError
print()


# ============================================================================
# 8. ABSTRACT BASE CLASSES
# ============================================================================
print("=" * 60)
print("8. ABSTRACT BASE CLASSES")
print("=" * 60)

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclasses"""
        pass
    
    def description(self):
        """Concrete method - can be inherited as-is"""
        return f"I am a {self.__class__.__name__}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Cannot instantiate abstract class
# shape = Shape()  # This would raise TypeError

rect = Rectangle(5, 3)
circle = Circle(4)

print(f"Rectangle: {rect.description()}")
print(f"  Area: {rect.area()}, Perimeter: {rect.perimeter()}")
print(f"Circle: {circle.description()}")
print(f"  Area: {circle.area():.2f}, Circumference: {circle.perimeter():.2f}")
print()


# ============================================================================
# 9. MULTIPLE INHERITANCE AND MRO
# ============================================================================
print("=" * 60)
print("9. MULTIPLE INHERITANCE")
print("=" * 60)

class Flyer:
    def fly(self):
        return "Flying in the air"

class Swimmer:
    def swim(self):
        return "Swimming in water"

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

duck = Duck()
print(f"Duck can: {duck.fly()}")
print(f"Duck can: {duck.swim()}")
print(f"Duck says: {duck.quack()}")
print(f"MRO: {[cls.__name__ for cls in Duck.__mro__]}")
print()


# ============================================================================
# 10. PRACTICAL EXAMPLE - Shopping Cart
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLE - SHOPPING CART")
print("=" * 60)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

class ShoppingCart:
    def __init__(self):
        self._items = []
    
    def add_item(self, product, quantity=1):
        self._items.append({'product': product, 'quantity': quantity})
    
    def remove_item(self, product_name):
        self._items = [
            item for item in self._items 
            if item['product'].name != product_name
        ]
    
    @property
    def total(self):
        return sum(
            item['product'].price * item['quantity'] 
            for item in self._items
        )
    
    def __len__(self):
        return sum(item['quantity'] for item in self._items)
    
    def __str__(self):
        if not self._items:
            return "Cart is empty"
        
        lines = ["Shopping Cart:"]
        for item in self._items:
            product = item['product']
            quantity = item['quantity']
            subtotal = product.price * quantity
            lines.append(f"  {product.name} x{quantity}: ${subtotal:.2f}")
        lines.append(f"Total: ${self.total:.2f}")
        return "\n".join(lines)

# Use the shopping cart
cart = ShoppingCart()
cart.add_item(Product("Apple", 0.50), quantity=5)
cart.add_item(Product("Banana", 0.30), quantity=3)
cart.add_item(Product("Orange", 0.80), quantity=2)

print(cart)
print(f"\nTotal items: {len(cart)}")
print()

print("=" * 60)
print("Great job! Now try the exercises in exercises.py")
print("=" * 60)

