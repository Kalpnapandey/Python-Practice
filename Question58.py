# Write a function that returns True if a string is a palindrome, ignoring case and spaces
def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False

print(palindrome('wow'))