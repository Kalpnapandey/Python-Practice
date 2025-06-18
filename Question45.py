# Class: Grader
# Takes marks out of 100.
# Method grade() returns:
# A for marks ≥ 90
# B for 75–89
# C for 60–74
# D for 40–59
# F for < 40

class Grader:
    def __init__(self,marks):
        self.marks=marks
    def grade(self):
        if self.marks>=90:
            print('A')
        elif 75<=self.marks <89:
            print('B')
        elif 60<=self.marks <74:
            print('C')
        elif 40<=self.marks <59:
            print("D")
        else:
            print('F')

grad=Grader(76)
grad.grade()