# Character Analyzer
# Ask the user to enter a single character.
# If it’s a vowel → print "Vowel"
# If it's a consonant → print "Consonant"
# If it’s a digit → print "Digit"
# If it’s a special character → print "Special Character"
# (Hint: you’ll need multiple if because more than one category can match invalid inputs)
# alphabet check
# vowel else consonant
# digit
# else of all it is a special symbol
char=input("Enter a single character")
if char.isalpha():
    if char.lower()in'aeiou':
        print("Provided character is a Vowel")
    else:
        print("It's a consonant")
elif char.isdigit():
    print("Given character is a numeric value")
else:
    print("It's a Special character")