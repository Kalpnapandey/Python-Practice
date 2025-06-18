# def fun(a):
#     a=10
#     print(a)
# fun(11)

# a=10        #global variable/scope
# def display():
#     a=202       #local variable/scope
#     print(a)
# display()

# We have one more scope that is not in other python but is available in other languages
# BLOCK SCOPE : Variables limited to a certain block of code only like if block or else
# block or for block etc.

# a=10
# def display():
#     global a
#     a=a+1
#     print(a)
# display()

def display():
    a=20
    def show():
        global a
        a=30
        print(a)
    show()
    print(a)
display()
