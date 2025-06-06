# # 1. Check Type of User Input
# # Ask the user to enter any value and check its type.
# # user_input = input("Enter something: ")# Now check and print its type
# # 🧠 Tip: All inputs using input() are strings by default. Convert and verify with type().
# # user_input = int(input("Enter something: "))
# # print(type(user_input))
# from curses.ascii import isdigit
#
# # 2. Convert String to Integer Safely
# # Ask the user to enter a number. Convert it into an integer and print the square of it.
# # Hint: use int() and input()
# # n=int(input("Enter a number"))
# # print(n**2)
# # # Handle what happens if the input is decimal (like "4.5").
# # n=float(input("Enter a number"))
# # print(n**2)
#
# # 3. Fix the Type Error
# # This code throws an error. Fix it:
# age = int(input("Enter your age: "))
# print("Your age after 5 years will be: " ,(age + 5))
# # Explain what the error was, and how you fixed it.
#
#
# # 4. Type Conversion Puzzle
# a = 5
# b = "10"
# c = float(b)
# d = a + c
# print(type(d))
# # What is the final output? What type is d?
#
# # 5. User Input Checker Without try-except
# # Ask the user to enter a number. If the input is numeric, convert it to int. If not,
# # print "Invalid input".
# # 🧠 Hint: Use .isdigit() for integers, or try checking for a . in string to guess float.
value=input("Enter a value you want to be checked:")
if value.isdigit():
    print(int(value))
else:
    print("Invalid input")