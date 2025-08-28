# Base class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        # Generic version (to be overridden by subclasses)
        print(f"{self.name} is moving...")

# Subclasses with different behaviors
class Car(Vehicle):
    def move(self):
        print(f"{self.name} is Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is Sailing ⛵")

class Bike(Vehicle):
    def move(self):
        print(f"{self.name} is Pedaling 🚴")

# Create objects
vehicles = [
    Car("Toyota"),
    Plane("Boeing 747"),
    Boat("Sailfish"),
    Bike("Mountain Bike")
]

# Demonstrate polymorphism
for v in vehicles:
    v.move()
