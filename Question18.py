# # Print numbers from 1 to 10.
# for i in range(1,11):
#     print(i)
# # Print even numbers between 1 and 20.
# for i in range(2,22,2):
#     print(i)
# # Print each character of a string on a new line.
# name='Kalpna Pandey'
# for i in name:
#     print(f"{i}\n")
# # Calculate and print the sum of the first 10 natural numbers.
# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)
# Display the multiplication table of a given number.
n=int(input("Enter the digit of which you want a table"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")