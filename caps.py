# Base class
class Superhero:
    def __init__(self, name, power, city, secret_identity):
        self.name = name                # Public attribute
        self.power = power              # Public attribute
        self.city = city                # Public attribute
        self.__secret_identity = secret_identity  # Private (Encapsulation)

    def introduce(self):
        return f"I am {self.name}, protector of {self.city}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

    def reveal_identity(self):
        # Encapsulated method
        return f"My secret identity is {self.__secret_identity}"


# Subclass (Inheritance + Polymorphism)
class FlyingHero(Superhero):
    def __init__(self, name, power, city, secret_identity, flight_speed):
        # Call base class constructor
        super().__init__(name, power, city, secret_identity)
        self.flight_speed = flight_speed

    # Override method (Polymorphism)
    def use_power(self):
        return f"{self.name} soars through the sky at {self.flight_speed} km/h using {self.power}!"


# Creating objects
batman = Superhero("Batman", "Martial Arts", "Gotham", "Bruce Wayne")
superman = FlyingHero("Superman", "Heat Vision", "Metropolis", "Clark Kent", 3000)

# Testing methods
print(batman.introduce())        # I am Batman, protector of Gotham!
print(batman.use_power())        # Batman uses Martial Arts!
print(batman.reveal_identity())  # My secret identity is Bruce Wayne

print(superman.introduce())      # I am Superman, protector of Metropolis!
print(superman.use_power())      # Superman soars through the sky at 3000 km/h using Heat Vision!
print(superman.reveal_identity())# My secret identity is Clark Kent
