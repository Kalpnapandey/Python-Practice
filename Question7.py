# Arithmetic Operations (5 Practice Questions)
# Basic Calculator
# Ask the user to enter two numbers and perform: addition, subtraction, multiplication, and division. Display results using f-strings.
# a=int(input("Enter a number"))
# b=int(input("Enter another number"))
# print(f"Addition={a+b}\nSubtraction={a-b}\nMultiplication={a*b}\nDivision={a/b}")
#
# # Area of a Circle
# # Ask the user for the radius. Calculate the area using π × r² (use 3.14 as pi). Show the result.
# r=int(input("Enter the radius of the circle"))
# area=3.14*r**2
# print(area)
# Average of Three Numbers
# Ask the user to input three numbers. Calculate and print the average.
a,b,c=map(int,input("Enter three numbers").split())
avg=a+b+c/3
print(avg)
# Simple Interest Calculator
# Formula: SI = (P × R × T)/100
# Ask for Principal, Rate, and Time, and show the Simple Interest.
p,r,t=map(float,input("Enter the values of p r and t").split())
si=(p*r*t)/100
print(f"Simple Interest = {si}")
# Speed Calculator
# Ask the user to enter distance (in km) and time (in hours). Calculate and print speed using speed = distance / time.
d=float(input("ENter the distance in kms"))
t=float(input("Enter the time in hours"))
s=d/t
print(f"Speed = {s} km/h")
