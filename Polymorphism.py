#Allows methods in different classes to have same name but different behaviour
#Parent class
from zipfile import stringEndArchive


class Student:
    def __init__(self,name,grade,percentage,):      #method
        self.name=name
        self.grade=grade
        self.percentage=percentage

    def student_details(self):
        print(self.name,self.grade,self.percentage,)

# # Object:Instance of class
# student2=Student('Kalpna','A',98,)
# student3=Student('Gaurav','A',90,)

#Child class
class GraduateStudent(Student):
    def __init__(self,name,grade,percentage,stream):
        # class and new from child
        super().__init__(name,grade,stream)
        self.stream=stream

    def student_details(self):
        print(f"Stream is {self.stream}")

#Object
student2=Student('Kalpna','A',98,)
grad=GraduateStudent("Saksham",'A',99,'PCM')
student2.student_details()
grad.student_details()