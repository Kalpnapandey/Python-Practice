# Class: Student
# Create a class Student with name, math_marks, science_marks, and english_marks.
# Add:
# total_marks()
# is_passed() – pass if all 3 marks ≥ 40

class Student:
    def __init__(self,name,math_marks, science_marks,english_marks):
        self.name=name
        self.math_marks=math_marks
        self.science_marks=science_marks
        self.english_marks=english_marks
    def total_marks(self):
        total=self.math_marks+self.math_marks+self.english_marks
        return total
    def is_passed(self):
        if self.math_marks>=40 and self.science_marks>=40 and self.english_marks>=40:
            print("Pass")
        else:
            print("fail")

stu=Student("kalpna",33,33,33)
marks=stu.total_marks()
print(marks)
stu.is_passed()