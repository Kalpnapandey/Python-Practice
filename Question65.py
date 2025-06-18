# Check if two
# strings
# are
# anagrams(e.g., "listen" and "silent")

s1=input("Enter first string")
s2=input("Enter second string")
if sorted(s1)==sorted(s2):
    print("It is an anagram")
else:
    print("Not an anagram")


from collections import Counter
s1=input("Enter first string")
s2=input("Enter second string")
if Counter(s1)==Counter(s2):
    print("It's an anagram")
else:
    print("Not an anagram")