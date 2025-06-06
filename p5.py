# Ask the user to enter a number n, and calculate the sum of numbers from 1 to n.
# sum=n*(n+1)//2
n=int(input("Enter a number"))
if n>0:
    sum = n * (n + 1) // 2
    print(sum)
else:
    print("Invalid input, enter a number greater than zero")