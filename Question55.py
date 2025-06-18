# Check if a list is a rotated version of another
list=[1,2,3,4]
list2=[4,3,2,1]
if list==list2[::-1]:
    print("It is a roatated version")
else:
    print("Not the rotated version")
