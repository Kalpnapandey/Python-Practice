# # 3. Palindrome Checker
# # Ask the user to enter a string. Check if it's a palindrome (same forward and backward).
# val=str(input("Enter a palindrome value"))
# val[0]==val[-1]and val[1]==val[-2]
# str='Kalpna Pandey'
# str.slice[]
# print(rev)
s=str(input("Enter a string")).lower()
s=s.replace(" ","")
print(s)
if s==(s[::-1]):
    print("It's a palindrome")
else:
    print("Not")

