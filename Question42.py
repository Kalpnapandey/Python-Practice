# Class: NumberCheck
# Takes a number.
# Add:
# is_even() – returns True/False
# is_prime() – returns True/False

class NumberCheck:
    def __init__(self,num):
        self.num=num
    def is_even(self):
        if self.num%2==0:
            return True
        else:
            return False
    def is_prime
check_num=int(input("Enter a number to be checked"))
check=NumberCheck(check_num)
if check.is_even is True:
    print("Even")
else:
    print("Odd")