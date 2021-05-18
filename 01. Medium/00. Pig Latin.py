"""
Translate english sentence to pig latin.
Take the first letter of a word, move it after the word and add "ay"
"""

english_text = [x for x in input("Enter an english sentence: ").split()]

pig_latin_text = []

for word in english_text:
    pig_latin_text.append(word[1:] + word[0] + 'ay')

print(f"Pig-Latin translation: {' '.join(pig_latin_text)}")
