# # Assignment and Comparison Operators (5 Practice Questions)
# # Compare Two Numbers
# # Ask the user to enter two numbers. Use comparison operators (==, !=, <, >, <=, >=) to compare them and print appropriate messages.
# a,b=map(int,input("Enter two numbers").split())
# if a==b:
#     print("Both numbers are equal")
# elif a!=b:
#     print("Both numbers are equal")
# elif a<b:
#     print(f"{a} is less than {b}")
# elif a>b:
#     print(f"{a} is graeter than {b}")
# elif a<=b:
#     print(f"{a} is less than or equal to{b}")
# elif a>=b:
#     print(f"{a}i greater than or equal to {b}")
# # Check if User is Eligible to Vote
# # Ask for the user's age. If age is greater than or equal to 18, print "Eligible to vote", else print "Not eligible".
# age=int(input("Enter your age"))
# if age>=18:
#     print("You can vote")
# else:
#     print("Not eligible for voting")
# Check for Same Values and Same Type
# Ask for two inputs. Compare both value and type (use == and is).
# a=input("Enter the first value")
# b=input("Enter the second value")
# if a==b:
#     print("Both values are equal")
# elif a is b:
#     print("Both values are of the same type")
# else:
#     print("Values are not equal or of different types")

# Guess the Number Game (Comparison Check)
# Set a secret number (e.g., 7). Ask the user to guess it. Use <, >, and == to guide them:
# If guess > 7: "Too high"
# If guess < 7: "Too low"
# Else: "Correct!"
secret_number=7
guess=int(input("Enter your guess number between 1 to 10:"))
if secret_number <guess:
    print("Too high")
elif secret_number >guess:
    print("Too low")
else:
    print("Correct!")