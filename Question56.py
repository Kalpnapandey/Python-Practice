# Without using max() or min(), find the second largest number in a list
list=[2,3,4,5]
largest=list[0]
for i in list:
    if i > largest:
        largest=i
print(largest)

