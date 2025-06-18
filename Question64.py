# # # list comprehensions
# # squares = [x**2 for x in range(5)]
# # print(squares)
#
# Find the product of digits in a number (e.g., 123 → 1×2×3 = 6)

# num=str(123)
# mul=1
# for i in (num):
#     mul*=int(i)
# print(mul)

# Find the GCD (Greatest Common Divisor) of two numbers
# import math
# a=32
# b=20
# print(math.gcd(a,b))


# Remove all vowels from a string
s='kalpna'
l=list(s)
print(l)
vowels='aeiou'
nl=[]
for i in l:
    if i not in vowels:
        nl.append(i)
print(nl)

