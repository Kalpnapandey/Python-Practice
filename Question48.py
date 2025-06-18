# Class: Animal → Abstraction
# Create an abstract class Animal with a method make_sound() (don’t implement it).
# Then create two child classes: Dog and Cat, and implement make_sound() in both.

from abc import ABC
class Animal(ABC):
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return"Meow"

d=Dog()
c=Cat()

print(f"Sound of dog is {d.make_sound()}")
print(f"Sound of cat is {c.make_sound()}")