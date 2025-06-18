#Inheritance:Allows one class(Child) to use the properties and methods of another
#   class(Parent)

#Parent class
class Student:
    def __init__(self,name,grade,percentage,):      #method
        self.name=name
        self.grade=grade
        self.percentage=percentage

    def student_details(self):
        print(self.name,self.grade,self.percentage,)

# Object:Instance of class
student2=Student('Kalpna','A',98,)
student3=Student('Gaurav','A',90,)

#Child class
class GraduateStudent(Student):                         #Child class inherits
    # properties and methods of parent class student
    def __init__(self,name,grade,percentage,stream):    #old parameters from parent
        # class and new from child
        super().__init__(name,grade,stream)             #call parent class init
        self.stream=stream                              #New attribute in child class

    #Method inheritance
    def student_details(self):
        super().student_details()
        print(f"Stream is {self.stream}")

#Object
grad=GraduateStudent("Saksham",'A',99,'PCM')
print(grad.stream)
GraduateStudent.student_details
