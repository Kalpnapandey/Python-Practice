
# class Student:
#     name="kalpna"
#     age=22
# stu1=Student()
# print(stu1.name,stu1.age)
#__init__ method - constructor
# Self parameter

class Student:                          # class
    def __init__(self,name,grade,percentage,team):      #method
        self.name=name                  #Attribute
        self.grade=grade                #Attribute
        self.percentage=percentage
        self.team=team

    def student_details(self):                      #Abstraction method
        print(self.name,self.grade,self.percentage+2,self.team) # hidden grace marks logic
team1='A'
team2='B'
# Object1:Instance of the class
student2=Student('Kalpna','A',98,team1)
# print(student2.name,student2.grade)
#
# #Object2
student3=Student('Gaurav','A',90,team2)
# print(student3.name,student3.grade)

student2.student_details()
print(student2.team)

# student2.percentage=100
# print(student2.percentage)
#
# del (student2.percentage)
# print(student2.__dict__)
#
# del student2
# print(student2.__dict__)

