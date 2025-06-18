class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        a=self.length*self.breadth
        print(a)
rec=Rectangle(10,10)
rec.area()
print(rec)
