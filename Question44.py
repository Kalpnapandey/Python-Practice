# Class: Rectangle
# Takes length and width.
# Add:
# area()
# perimeter()
# is_square() – returns True if length == width

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        ar=self.length*self.width
        return ar
    def perimeter(self):
        per=2*(self.length+self.width)
        return per
    def is_square(self):
        if self.length==self.width:
            return True
        else:
            return False

side=Rectangle(40,89)
print(side.area())
print(side.perimeter())
check=side.is_square()
print(check)