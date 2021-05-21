"""
Check if any letter is repeated in the string.
"""

text = input("Enter your text here: ")

unique = True
for letter in text:
    if text.count(letter) > 1:
        unique = False
        break

if unique:
    print("Unique")
else:
    print("Deja Vu")
