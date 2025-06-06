# # 1. Identify the Data Type
# # Guess the datatype of the following. Then use type() to confirm.
# a = 100
# b = 12.5
# c = "Python"
# d = True
# e = [1, 2, 3]
# f = (4, 5, 6)
# g = {7, 8, 9}
# h = {"name": "Kalpna", "age": 22}
# for i in [a,b,c,d,e,f,g,h]:
#     print(type(i))
#
# # 2. Type Conversion Practice
# # Convert the following:
# # An integer 10 to float
# # A float 9.8 to integer
# # A string "25" to integer
# # A number 44 to string
# # Write code to do all the above conversions and print the result with type.
# i=float(10)
# print(type(i))
# f=int(9.8)
# print(type(f))
# j=int('25')
# print(type(j))
# h=str(44)
# print(type(h))

# 3. Detect Type Error
# What will happen here? Try and observe:
# a = "10" b = 5 print(a + b)
# Fix the code so that it adds the values numerically.
a = "10"
b = 5
print(int(a)+b)
# 4. Real-World Scenario
# You are storing the following details about a person:
# Name (e.g., "Alex")
# Age (e.g., 30)
# Married or not (e.g., True)
# Hobbies (e.g., ["reading", "cycling"])
# Location as latitude & longitude (e.g., (26.14, 91.76))
# Create variables with proper datatypes to represent this data.
name=str("Alex")
age=int(30)
hobbies=list(["Reading","Cycling"])
latitude,longitude=26.14,91.76
for i in[name,age,hobbies,latitude,longitude]:
    print(type(i))

# 5. Mix and Match
# Guess the result and its datatype:
# x = 5 + 3.0  y = "7" * 3  z = 10 > 5
# Use type() to confirm your guesses.
x = 5 + 3.0
y = "7" * 3
z = 10 > 5
print(type(x))
print(type(y))
print(type(z))
