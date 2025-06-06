height=input("Enter multiple heights seperated by commas")
print(height)
heights=height.split(',')
print(heights)
count=0
for i in heights:
    count=count+1
print(count)
for i in range(5):
    avg=sum(heights)/heights.count()
    print(round(avg))
