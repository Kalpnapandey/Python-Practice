#Triangle Type Checker
# Take lengths of 3 sides of a triangle.
# Check if it's valid (sum of any 2 > third).
# If valid, check:
# All sides equal → Equilateral
# Two sides equal → Isosceles
# All sides different → Scalene
a,b,c=map(int,input("Enter the sides of a triangle:").split())
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Equilateral triangle")
    elif a==b or b==c or a==c:
        print("Isosceles traiangle")
    else:
        print("Scalene triangle")