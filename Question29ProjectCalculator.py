# def calculator(num1,num2):
#     num1=int(input("Enter first number"))
#     print(f"+\n-\n*\n/")
#     operation=input("Pick an operation")
#     num2=int(input("Enter the second number"))
#     if operation=='+':
#         print (num1+num2)
#     elif operation=='-':
#         print(num1-num2)
#     elif operation=='*':
#         print(num1*num2)
#     elif operation=='/':
#         print(num1/num2)
#     else:
#         print("Invalid operation")
# print(calculator(10,2))

def add(a,b):
    return a+b
def sub(a,b):
    return b-a
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
operations={
    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}