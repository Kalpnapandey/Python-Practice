# Sum of Digits Until Single Digit
# Write a program to reduce a number to a single-digit sum.
# Input: 987 → 9+8+7=24 → 2+4=6
# Output: 6

value=12345998765890
sum=0
sum1=0
for i in str(value):
    sum+=int(i)
print(sum)
for j in str(sum):
    sum1+=int(j)
print(sum1)





