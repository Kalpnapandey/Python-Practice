# Abstract Shape Class
#
# Create an abstract class Shape with a method area().
# Create two child classes: Circle and Rectangle, and implement area() in each.
# Use appropriate formulas.

from abc import ABC, abstractmethod
class Shape(ABC):
    def area(self):
        pass

class Circle(Shape):
    def area(self,r):
        return 3.14*r**2

class Rectangle(Shape):
    def area(self,l,b):
        return l*b

c=Circle()
r=Rectangle()

print(c.area(2))
print(r.area(2,2))