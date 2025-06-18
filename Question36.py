# 1. Class: Circle
# Create a class Circle with radius as input.
# Add a method area() that returns the area of the circle. (Formula: 3.14 × r²)

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=3.14*self.radius**2
        print(area)
ar=Circle(5)
print(ar.area())