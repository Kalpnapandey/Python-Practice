# Vehicle Abstract Class
#
# Define an abstract class Vehicle with an abstract method start_engine().
# Create two child classes: Car and Motorcycle that implement start_engine() with different messages.

from abc import ABC, abstractmethod
class Vehicle(ABC):
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Runs on 4 wheels"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Runs on 2 wheels"

c=Car()
m=Motorcycle()
print(c.start_engine())
print(m.start_engine())