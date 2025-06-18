# Day to Weekend Checker
# Ask user to enter a day of the week.
# If it's Saturday or Sunday → "It's weekend!"
# If it's Monday to Friday → "Working day!"
# Else → "Invalid day"

# day=input("Enter a day of a week").lower()
# if day=='saturday' or day=='sunday':
#     print("Weekend")
# elif day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday':
#     print("Working day")
# else:
#     print("Invalid input")

day=input("Enter a day of a week").lower()
weekday={'monday','tuesday','wednesday','thursday','friday'}
weekend={'saturday','sunday'}
if day in weekend:
    print("It's a weekend")
elif day in weekday:
    print("Its a weekday")
else:
    print("Invalid input")